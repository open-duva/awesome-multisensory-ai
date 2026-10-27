#!/usr/bin/env python3
"""Build a fully local, dependency-free research map from curated source data.
SPDX-License-Identifier: MIT
"""
import argparse
import json
from pathlib import Path
from collection_data import load_catalog

ROOT = Path(__file__).resolve().parents[1]


def build():
    catalog = load_catalog()
    relationships = json.loads((ROOT / 'data/relationships.json').read_text())
    data = {**catalog, 'edges': relationships['edges']}
    encoded = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    template = (ROOT / 'atlas/template.html').read_text()
    assert template.count('@@ATLAS_DATA@@') == 1, 'Expected one data slot'
    return template.replace('@@ATLAS_DATA@@', encoded)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='verify the committed page matches its sources')
    args = parser.parse_args()
    target = ROOT / 'atlas/dist/index.html'
    content = build()
    if args.check:
        if not target.exists() or target.read_text() != content:
            raise SystemExit('Research Map is stale. Run python3 scripts/build_atlas.py')
        print('Research Map matches its curated sources.')
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
        print(f'Built {target.relative_to(ROOT)} ({len(content.encode()):,} bytes)')


if __name__ == '__main__':
    main()
