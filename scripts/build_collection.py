#!/usr/bin/env python3
"""Generate Markdown research entries and citations from the reviewed catalog.
SPDX-License-Identifier: MIT
"""
import argparse
import json
import re
from pathlib import Path
from collections import Counter
from collection_data import load_catalog

ROOT = Path(__file__).resolve().parents[1]
TOPICS = {
    'representation': ('sensor-representations', 'Sensor representation and pretraining', 'Reusable encoders, calibrated input assumptions, and the boundary between within-family transfer and universal sensor representations.'),
    'alignment': ('multimodal-integration', 'Multimodal alignment and integration', 'Ways to connect physical measurements to language and other modalities. Shared embeddings and fluent output do not by themselves establish physical-state accuracy.'),
    'understanding': ('physical-understanding', 'Physical state understanding and reasoning', 'Calibrated estimation, explicit sensor querying, and tool-based analysis. The reference measurement and the information available to the model matter as much as answer fluency.'),
    'action': ('dynamics-and-action', 'Dynamics, world models and action', 'Executed control, open-loop planning, and prediction remain distinct claims. The selected notes identify the actual measured outcome and sensor ablations. See also [LingBot-Touch](sensor-representations.md#lingbot-touch) in representations for frozen-encoder policy evaluations with staged task scoring.'),
    'resources': ('datasets-and-benchmarks', 'Datasets and evaluation contributions', 'Reusable data and independent evaluations earn a place alongside models. Oracle labels, noisy reference instruments, and inferred states are different evidence levels.'),
    'background': ('background', 'Background and technical context', 'Methodological controls, general time-series encoders, and documented ancestors. These are not counted as core multisensory contributions. See the [encoder comparison](../resources/encoder-comparison.md) for reusable methods and shared checkpoints.')}
DECISION = {'selected': 'Selected core', 'background': 'Background', 'watch': 'Watchlist'}


def clean(value):
    if value is None:
        return ''
    if isinstance(value, list):
        return '; '.join(map(str, value))
    return str(value)


def table(value):
    return clean(value).replace('|', '\\|').replace('\n', ' ')


def anchor(p):
    return re.sub(r'[^\w\s-]', '', p['short_name'].lower()).replace(' ', '-')


def note_link(p, prefix='../'):
    if p['decision'] in {'selected', 'background'}:
        return f"{prefix}topics/{TOPICS[p['category']][0]}.md#{anchor(p)}"
    return f"{prefix}resources/watchlist.md#{anchor(p)}" if p['decision']=='watch' else p['paper_url']


def author_line(p):
    authors=p.get('authors', [])
    if not authors:
        return 'Author metadata not independently established'
    return authors[0] + (' et al.' if len(authors)>1 else '')


def sources(p):
    return ' · '.join(f"[{table(s.get('section') or 'Primary source')}]({s['url']})" for s in p.get('evidence_sources', []))


def card(p, canonical=True):
    out=(f"<!-- paper:{p['id']} -->\n\n" if canonical else '')
    out+=f"### {p['short_name']}\n\n**[{p['title']}]({p['paper_url']})**\n\n{author_line(p)} · {p['status']}. [Status source]({p['status_source']})"
    if p.get('code_url'):
        out+=f" · [{p.get('code_label','Official implementation')}]({p['code_url']})"
    out+=f"\n\n- **Contribution:** {p.get('summary') or p['title']}\n"
    if canonical and p['decision']=='selected':
        fields=[('Measurements and method',f"{clean(p.get('input_level'))}. {clean(p.get('method'))}"),('Supervision',p.get('supervision')),('Demonstrated capability',p.get('demonstrated')),('Reference / ground truth',p.get('ground_truth')),('Generalization tested',p.get('generalization')),('Baselines',p.get('baselines'))]
        for label,value in fields:
            if value:out+=f"- **{label}:** {clean(value)}\n"
    else:
        out+=f"- **Scope and evidence:** {clean(p.get('method'))} {clean(p.get('demonstrated'))}\n"
    out+=f"- **Boundary:** {clean(p.get('limitation'))}\n"
    if p.get('availability'):out+=f"- **Access:** {p['availability']}\n"
    out+=f"\n**Evidence locations:** {sources(p)}\n\n"
    return out


def generated():
    catalog=load_catalog()
    papers=catalog['papers'];retained=[p for p in papers if p['decision'] in {'selected','background'}]
    counts=Counter(p['decision'] for p in papers)
    files={}
    for category,(filename,title,description) in TOPICS.items():
        entries=[p for p in retained if p['category']==category]
        text=f"# {title}\n\n[Home](../README.md) · [Research Map](../atlas/dist/index.html) · [Paper index](../resources/papers.md)\n\n{description}\n\n{len(entries)} curated entries. Generated from the reviewed catalog; edit the source record and rebuild rather than changing this page alone.\n\n"
        text+=''.join(card(p) for p in entries)
        files[f'topics/{filename}.md']=text.rstrip()+'\n'
    index=f"""# Curated paper index

[Home](../README.md) · [Research Map](../atlas/dist/index.html) · [BibTeX](../references.bib)

**{counts['selected']} core papers and {counts['background']} background references.** Additional references are listed separately in the [watchlist](watchlist.md).

Publication status is separate from the source milestone used in the timeline. Claims are tied to the primary methods/evaluation locations in each entry. BibTeX cites the reviewed record; use a publisher citation when required. A public code link is not a guarantee of complete training-data or weight availability.

| Work | Role | Research problem | Publication status | Verified public milestone |
| --- | --- | --- | --- | --- |
"""
    for p in retained:
        index+=f"| [{p['short_name']}]({note_link(p)}) | {DECISION[p['decision']]} | {TOPICS[p['category']][1]} | [{table(p['status'])}]({p['status_source']}) | [{p.get('timeline_date') or 'Unresolved'}]({p['date_source']}) |\n"
    files['resources/papers.md']=index
    watch=f"""# Further reading

[Home](../README.md) · [Research Map](../atlas/dist/index.html) · [Paper index](papers.md)

{counts['watch']} additional references, listed separately from the core collection. Publication status and primary sources are provided for further reading; these entries do not carry the detailed technical summaries of the core papers.

| Work | Signals | Publication status | Code / project |
| --- | --- | --- | --- |
"""
    for p in papers:
        if p['decision']=='watch':
            access=f"[Official resource]({p['code_url']})" if p.get('code_url') else '—'
            watch+=f"| <a id=\"{anchor(p)}\"></a>[{table(p['short_name'])}]({p['paper_url']}) | {table(p.get('modalities',[]))} | [{table(p['status'])}]({p['status_source']}) | {access} |\n"
    files['resources/watchlist.md']=watch
    encoders=[p for p in papers if p.get('encoder_profile')]
    comparison=f'''# General time-series encoding: evidence matrix

[Home](../README.md) · [Research Map](../atlas/dist/index.html)

{len(encoders)} reviewed encoding methods, shared backbones, and evaluation references. This is a comparison set, not a ranking. A frozen encoder with a fitted target classifier is not label-free classification. Background status denotes this collection's physical-sensing scope, not a judgment that these methods are unimportant.

Generated from `encoder_profile` and the evidence fields in the [catalog](../data/catalog.json). Inspect the linked methods before treating variable channel count, cross-dataset adaptation, and held-out-domain transfer as equivalent.

| Work | Reusable artifact | Embedding granularity | Transfer protocol | Pretraining scope |
| --- | --- | --- | --- | --- |
'''
    for p in encoders:
        e=p['encoder_profile']
        comparison+=f"| [{p['short_name']}]({note_link(p)}) | {table(e['reusable_artifact'])} | {table(e['embedding_granularity'])} | {table(e['transfer_protocol'])} | {table(e['pretraining_scope'])} |\n"
    for p in encoders:
        e=p['encoder_profile']
        comparison+=f"\n## {p['short_name']}\n\n[{p['title']}]({p['paper_url']}) · {DECISION[p['decision']]} · {table(e['family'])}\n\n"
        for label, value in [('Channel interface',e['channel_handling']),('Normalization / physical scale',e['normalization']),('Useful property',e['strengths']),('Encoding boundary',e['limitations']),('Generalization tested',p.get('generalization')),('Baselines / protocol',p.get('baselines')),('Availability',p.get('availability'))]:
            if clean(value):
                comparison+=f"- **{label}:** {clean(value)}\n"
        comparison+=f"\n**Evidence:** {sources(p)}\n"
    files['resources/encoder-comparison.md']=comparison
    bib=['% Core and background records; additional references are listed separately.','% Publication status and exact evidence versions appear in the Markdown notes.','']
    esc=lambda x:clean(x).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
    for p in retained:
        authors=p.get('authors',[])
        if not p.get('authors_complete',False) and 'others' not in authors:
            authors=authors+['others']
        authors=['{'+a+'}' if 'CTRL-labs' in a else a for a in authors]
        bib += [f"@misc{{{p['id']},",'  title = {{'+esc(p['title'])+'}},','  author = {'+' and '.join(esc(a) for a in authors)+'},',f"  year = {{{p.get('citation_year',p['year'])}}},",f"  url = {{{p['paper_url']}}},"]
        if p.get('arxiv_id'):
            version=re.search(re.escape(p['arxiv_id'])+r'(v\d+)',p['paper_url'])
            bib += [f"  eprint = {{{p['arxiv_id']}{version.group(1) if version else ''}}},",'  archivePrefix = {arXiv},']
        bib += ['  note = {'+esc(p['status'])+'; collection snapshot '+catalog['reviewed_at']+'}', '}','']
    files['references.bib']='\n'.join(bib)
    return files


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args();files=generated();stale=[]
    for name,body in files.items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text()!=body:stale.append(name)
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body)
    if stale:raise SystemExit('Stale generated files: '+', '.join(stale))
    print(('Verified' if args.check else 'Built')+f' {len(files)} research documents/citation files.')


if __name__=='__main__':main()
