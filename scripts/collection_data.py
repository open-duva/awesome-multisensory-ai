"""Public catalog schema shared by the generators and validation.
SPDX-License-Identifier: MIT
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_FIELDS = {
    'schema_version', 'reviewed_at', 'title', 'date_note', 'papers', 'evaluations',
}
PAPER_FIELDS = {
    'id', 'short_name', 'title', 'authors', 'authors_complete', 'year',
    'citation_year', 'arxiv_id', 'paper_url', 'code_url', 'code_label',
    'status', 'status_source', 'timeline_date', 'date_precision', 'date_basis',
    'date_source', 'modalities', 'domains', 'category', 'decision', 'summary',
    'method', 'input_level', 'supervision', 'demonstrated', 'ground_truth',
    'generalization', 'baselines', 'limitation', 'availability',
    'encoder_profile', 'featured', 'evidence_sources',
}
PRIVATE_DIRECTORIES = {
    '.git', '.research', 'guides', 'reviews', 'research', 'notes', 'drafts',
    'reports', 'backups', '.local', '.cache', 'tmp', 'temp', 'logs',
    'downloads', 'screenshots', 'playwright-report', 'test-results',
    '__pycache__', '.venv', 'venv', 'node_modules', '.pytest_cache',
}
PRIVATE_FILES = {
    'data/search-log.json', 'data/verification.json',
    'data/resource-audits.json', 'resources/screening-ledger.md',
}
ENCODER_FIELDS = {
    'channel_handling', 'embedding_granularity', 'family', 'limitations',
    'normalization', 'pretraining_scope', 'reusable_artifact', 'strengths',
    'transfer_protocol',
}
EVALUATION_FIELDS = {
    'benchmark', 'evidence_section', 'evidence_url', 'model', 'note', 'relation',
}
RELATION_FIELDS = {
    'evidence_section', 'evidence_url', 'explanation', 'label', 'relation',
    'source', 'target', 'type', 'variant_scope',
}


def is_private(path):
    relative = path.resolve().relative_to(ROOT)
    return (
        bool(PRIVATE_DIRECTORIES.intersection(relative.parts))
        or relative.as_posix() in PRIVATE_FILES
        or relative.name == '.env'
        or (relative.name.startswith('.env.') and relative.name != '.env.example')
        or relative.name.endswith('.log')
    )


def public_schema_errors(catalog):
    errors = []
    extra = set(catalog) - CATALOG_FIELDS
    if extra:
        errors.append('Unpublished catalog fields: ' + ', '.join(sorted(extra)))
    for paper in catalog.get('papers', []):
        extra = set(paper) - PAPER_FIELDS
        if extra:
            errors.append(f"{paper.get('id', '?')}: unpublished fields: " + ', '.join(sorted(extra)))
        if paper.get('decision') not in {'selected', 'background', 'watch'}:
            errors.append(f"{paper.get('id', '?')}: not a public collection entry")
        for source in paper.get('evidence_sources', []):
            if set(source) - {'url', 'section'}:
                errors.append(f"{paper.get('id', '?')}: source contains non-public fields")
        if set(paper.get('encoder_profile', {})) - ENCODER_FIELDS:
            errors.append(f"{paper.get('id', '?')}: encoding profile contains non-public fields")
    for evaluation in catalog.get('evaluations', []):
        if set(evaluation) - EVALUATION_FIELDS:
            errors.append('Evaluation contains non-public fields')
    return errors


def public_relation_errors(relations):
    errors = []
    if set(relations) - {'schema_version', 'note', 'edges'}:
        errors.append('Relationships contain non-public fields')
    for edge in relations.get('edges', []):
        if set(edge) - RELATION_FIELDS:
            errors.append('Relationship contains non-public fields')
    return errors


def load_catalog():
    catalog = json.loads((ROOT / 'data/catalog.json').read_text())
    errors = public_schema_errors(catalog)
    if errors:
        raise ValueError('\n'.join(errors))
    return catalog
