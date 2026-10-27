#!/usr/bin/env python3
"""Check the Git index and optional history contain only public collection files.
SPDX-License-Identifier: MIT
"""
import argparse
import json
from pathlib import PurePosixPath
import re
import subprocess

from collection_data import ROOT, is_private, public_schema_errors, public_relation_errors

ROOT_FILES = {
    '.gitignore', '.env.example', 'README.md', 'CONTRIBUTING.md',
    'MAINTAINING.md', 'LICENSE', 'LICENSE-CODE', 'references.bib',
}
DATA_FILES = {'data/catalog.json', 'data/relationships.json'}
ATLAS_FILES = {'atlas/template.html', 'atlas/dist/index.html', 'atlas/assets/research-map.png'}
RESOURCE_FILES = {
    'resources/papers.md', 'resources/datasets.md', 'resources/benchmarks.md',
    'resources/tools.md', 'resources/watchlist.md', 'resources/encoder-comparison.md',
}


def allowed(name):
    path = PurePosixPath(name)
    if is_private(ROOT / name):
        return False
    if name in ROOT_FILES | DATA_FILES | ATLAS_FILES | RESOURCE_FILES:
        return True
    if len(path.parts) == 2 and path.parts[0] == 'topics' and path.suffix == '.md':
        return True
    if len(path.parts) == 2 and path.parts[0] == 'scripts' and path.suffix == '.py':
        return True
    return path.parts[0] == '.github' and path.suffix in {'.md', '.yml', '.yaml'}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def check_content(name, blob):
    if name == 'data/catalog.json':
        return public_schema_errors(json.loads(blob))
    if name == 'data/relationships.json':
        return public_relation_errors(json.loads(blob))
    if name == 'atlas/dist/index.html':
        match = re.search(rb'<script id="atlas-data" type="application/json">(.*?)</script>', blob, re.S)
        if not match:
            return ['Missing public website data']
        payload = json.loads(match[1])
        edges = payload.pop('edges', [])
        return public_schema_errors(payload) + public_relation_errors({'edges': edges})
    return []


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--history', action='store_true', help='also inspect every reachable commit')
    args = parser.parse_args()
    entries = set()
    errors = []
    for row in git('ls-files', '--stage', '-z').split(b'\0'):
        if not row:
            continue
        metadata, name = row.decode().split('\t', 1)
        mode, oid, stage = metadata.split()
        if stage != '0':
            errors.append(f'{name}: unresolved index entry')
        entries.add((mode, oid, name))
    commits = git('rev-list', '--all').decode().splitlines() if args.history else []
    for commit in commits:
        for row in git('ls-tree', '-r', '-z', commit).split(b'\0'):
            if not row:
                continue
            metadata, name = row.decode().split('\t', 1)
            mode, kind, oid = metadata.split()
            entries.add((mode, oid, name))
    for mode, oid, name in sorted(entries):
        if mode not in {'100644', '100755'} or not allowed(name):
            errors.append(f'{name}: not an approved public file')
            continue
        if name not in DATA_FILES | {'atlas/dist/index.html'}:
            continue
        try:
            errors.extend(f'{name}: {error}' for error in check_content(name, git('cat-file', 'blob', oid)))
        except (ValueError, TypeError, KeyError) as error:
            errors.append(f'{name}: malformed public data ({type(error).__name__})')
    if errors:
        for error in sorted(set(errors)):
            print('ERROR:', error)
        return 1
    print(f'Public-file check passed: {len(entries)} file versions, {len(commits)} historical commits.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
