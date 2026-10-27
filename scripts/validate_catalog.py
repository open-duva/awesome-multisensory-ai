#!/usr/bin/env python3
"""Check evidence-catalog integrity without network access or dependencies.
SPDX-License-Identifier: MIT
"""
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit
from collection_data import public_schema_errors, public_relation_errors

ROOT = Path(__file__).resolve().parents[1]


def validate(catalog, relations):
    errors=public_schema_errors(catalog) + public_relation_errors(relations)
    papers=catalog.get('papers',[])
    ids=[p.get('id') for p in papers]
    if len(ids)!=len(set(ids)):errors.append('Duplicate paper id')
    by_id={p.get('id'):p for p in papers}
    cutoff=date.fromisoformat(catalog['reviewed_at'])
    for p in papers:
        key=p.get('id','?')
        if not re.fullmatch(r'[a-z0-9-]+',key):errors.append(f'{key}: invalid stable id')
        if not p.get('title'):errors.append(f'{key}: missing title')
        if not isinstance(p.get('authors'),list):errors.append(f'{key}: authors must be an array')
        milestone=p.get('timeline_date')
        if milestone:
            try:
                if not re.fullmatch(r'\d{4}(?:-\d{2}){0,2}',milestone):raise ValueError()
                year,month,day=(list(map(int,milestone.split('-')))+[1,1])[:3]
                if date(year,month,day)>cutoff:errors.append(f'{key}: date after cutoff')
                expected={4:'year',7:'month',10:'day'}[len(milestone)]
                if p.get('date_precision')!=expected:errors.append(f'{key}: date precision mismatch')
            except (ValueError,KeyError):errors.append(f'{key}: invalid milestone date')
        for field in ['paper_url','date_source','status_source']:
            url=p.get(field)
            if not url or urlsplit(url).scheme not in {'http','https'} or not urlsplit(url).hostname:errors.append(f'{key}: invalid {field}')
        if not p.get('evidence_sources'):errors.append(f'{key}: no source evidence')
        if p.get('encoder_profile'):
            for field in ['family','reusable_artifact','embedding_granularity','pretraining_scope','transfer_protocol','channel_handling','normalization','strengths','limitations']:
                if not isinstance(p['encoder_profile'].get(field),str) or not p['encoder_profile'][field].strip():errors.append(f'{key}: encoding profile missing {field}')
            if any(x in json.dumps(p).lower() for x in ['not deeply inspected','screening only']):errors.append(f'{key}: shallow placeholder in reviewed encoder')
        if p.get('decision')=='selected':
            for field in ['method','input_level','demonstrated','ground_truth','generalization','baselines','limitation','summary']:
                if not p.get(field):errors.append(f'{key}: core record missing {field}')
            if not milestone:errors.append(f'{key}: core record has no sourced milestone')
            if not p.get('authors_complete'):errors.append(f'{key}: core authors incomplete')
            if any(x in json.dumps(p).lower() for x in ['not yet audited','pending detailed curation','not deeply inspected','screening only']):errors.append(f'{key}: unreviewed placeholder in core')
    seen=set();adj={key:[] for key in ids}
    for e in relations.get('edges',[]):
        source,target=e.get('source'),e.get('target')
        if source not in by_id or target not in by_id:errors.append('Missing dependency endpoint');continue
        identity=(source,target,e.get('relation'))
        if identity in seen:errors.append('Duplicate dependency')
        seen.add(identity)
        if source==target:errors.append('Self dependency')
        if e.get('type') not in {'method','data'}:errors.append('Invalid dependency type')
        for field in ['explanation','evidence_url','evidence_section']:
            if not e.get(field):errors.append(f'{source}->{target}: missing {field}')
        if e.get('relation')=='evaluates_checkpoint':errors.append('Evaluation mislabeled as dependency')
        adj[source].append(target)
    visited=set();visiting=set()
    def visit(key):
        if key in visiting:errors.append('Dependency cycle');return
        if key in visited:return
        visiting.add(key)
        for child in adj[key]:visit(child)
        visiting.remove(key);visited.add(key)
    for key in ids:visit(key)
    for e in catalog.get('evaluations',[]):
        if e.get('benchmark') not in by_id or e.get('model') not in by_id:errors.append('Missing independent-evaluation endpoint')
        if not e.get('evidence_url') or not e.get('evidence_section'):errors.append('Evaluation missing provenance')
    return errors


def main():
    catalog=json.loads((ROOT/'data/catalog.json').read_text())
    relations=json.loads((ROOT/'data/relationships.json').read_text())
    errors=validate(catalog,relations)
    if errors:
        for error in errors:print('ERROR:',error)
        return 1
    print('Catalog valid:',dict(Counter(p['decision'] for p in catalog['papers'])),f"; {len(relations['edges'])} sourced dependencies.")
    return 0


if __name__=='__main__':sys.exit(main())
