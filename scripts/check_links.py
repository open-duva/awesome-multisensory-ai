#!/usr/bin/env python3
"""Validate this Markdown collection using only the Python standard library.

Network checks are opt-in and never run in the default pull-request workflow.
An accessible URL is not a scientific, licensing, or reproducibility validation.
SPDX-License-Identifier: MIT
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collection_data import is_private


INLINE_LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)")
REFERENCE_LINK = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
PAPER_MARKER = re.compile(r"<!--\s*paper:([a-z0-9-]+)\s*-->")


def prose(text: str) -> str:
    """Exclude fenced code, which may contain illustrative Markdown URLs."""
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            lines.append("")
        else:
            lines.append("" if fence else line)
    return "\n".join(lines)


def anchors(text: str) -> set[str]:
    result = set(re.findall(r'(?:id|name)=["\']([^"\']+)["\']', text))
    used: Counter[str] = Counter()
    for line in prose(text).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if not match:
            continue
        heading = re.sub(r"!?\[([^]]+)\]\([^)]+\)", r"\1", match.group(1))
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = html.unescape(heading).lower().strip()
        slug = re.sub(r"[^\w\s-]", "", heading).replace(" ", "-")
        count = used[slug]
        used[slug] += 1
        result.add(slug + (f"-{count}" if count else ""))
    return result


def links(text: str) -> set[str]:
    clean = prose(text)
    return {html.unescape(m.group(1).strip("<>")) for m in INLINE_LINK.finditer(clean)} | {
        html.unescape(m.group(1).strip("<>")) for m in REFERENCE_LINK.finditer(clean)
    }


def local_check(root: Path) -> tuple[list[str], set[str], dict]:
    root = root.resolve()
    files = sorted(p for p in root.rglob("*.md") if not is_private(p))
    contents = {p.resolve(): p.read_text(encoding="utf-8") for p in files}
    errors = []
    external = set()
    local_count = 0
    for path, text in contents.items():
        for url in sorted(links(text)):
            parsed = urllib.parse.urlsplit(url)
            if parsed.scheme in {"https", "http"}:
                external.add(urllib.parse.urlunsplit(parsed._replace(fragment="")))
                continue
            if parsed.scheme:
                errors.append(f"{path.relative_to(root)}: unsupported link scheme: {url}")
                continue
            local_count += 1
            target = (path.parent / urllib.parse.unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: link escapes repository: {url}")
            elif is_private(target):
                errors.append(f"{path.relative_to(root)}: link points to local-only material: {url}")
            elif not target.exists():
                errors.append(f"{path.relative_to(root)}: missing target: {url}")
            elif parsed.fragment and target.suffix == ".md":
                fragment = urllib.parse.unquote(parsed.fragment)
                target_text = contents.get(target, "")
                if fragment not in anchors(target_text):
                    errors.append(f"{path.relative_to(root)}: missing anchor: {url}")
    markers = [key for path, text in contents.items() if path.parent.name == "topics" for key in PAPER_MARKER.findall(text)]
    bib = (root / "references.bib").read_text(encoding="utf-8")
    keys = re.findall(r"^@\w+\{([^,]+),", bib, re.MULTILINE)
    for label, values in [("canonical paper", markers), ("BibTeX key", keys)]:
        for key, count in Counter(values).items():
            if count != 1:
                errors.append(f"Duplicate {label}: {key} ({count})")
    if set(markers) != set(keys):
        errors.append(f"Paper/BibTeX mismatch: notes only={sorted(set(markers)-set(keys))}, bibliography only={sorted(set(keys)-set(markers))}")
    ids = re.findall(r"eprint\s*=\s*\{(\d{4}\.\d{4,5})(?:v\d+)?\}", bib)
    if len(set(ids)) != len(ids):
        errors.append("Duplicate arXiv paper in the curated bibliography.")
    entries = re.split(r"(?m)^@\w+\{", bib)[1:]
    for entry in entries:
        key = entry.split(',', 1)[0]
        for field in ["title", "author", "year", "url"]:
            if not re.search(r"\b" + field + r"\s*=\s*\{.+?\}", entry):
                errors.append(f"BibTeX {key}: missing {field}")
    external.update(re.findall(r"url\s*=\s*\{(https?://[^}]+)\}", bib))

    class PageLinks(HTMLParser):
        def __init__(self):
            super().__init__()
            self.targets, self.ids = [], set()
        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if attrs.get('id'):
                self.ids.add(attrs['id'])
            if tag in {'a', 'link'} and attrs.get('href'):
                self.targets.append(attrs['href'])
            if tag in {'script', 'img'} and attrs.get('src'):
                self.targets.append(attrs['src'])
    page_path = root / 'atlas/dist/index.html'
    if page_path.exists():
        page = PageLinks()
        page.feed(page_path.read_text())
        for url in set(page.targets):
            parsed = urllib.parse.urlsplit(url)
            if parsed.scheme in {'http', 'https'}:
                external.add(urllib.parse.urlunsplit(parsed._replace(fragment='')))
            elif not parsed.scheme:
                target = (page_path.parent / urllib.parse.unquote(parsed.path)).resolve() if parsed.path else page_path
                if not target.is_relative_to(root) or is_private(target) or not target.exists():
                    errors.append(f"atlas/dist/index.html: missing/escaping local target: {url}")
                elif not parsed.path and parsed.fragment and parsed.fragment not in page.ids:
                    errors.append(f"atlas/dist/index.html: missing anchor: {url}")
            else:
                errors.append(f"atlas/dist/index.html: unsupported target: {url}")

    def data_urls(value):
        if isinstance(value, dict):
            for child in value.values():
                data_urls(child)
        elif isinstance(value, list):
            for child in value:
                data_urls(child)
        elif isinstance(value, str) and re.fullmatch(r'https?://[^\s]+', value):
            parsed = urllib.parse.urlsplit(value)
            external.add(urllib.parse.urlunsplit(parsed._replace(fragment='')))
    for path in (root / 'data').glob('*.json'):
        if is_private(path):
            continue
        data_urls(json.loads(path.read_text()))
    return errors, external, {"markdown_files": len(files), "local_links": local_count, "papers": len(markers), "external_urls": len(external)}


def external_check(url: str, timeout: float) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "AwesomeMultisensoryAI-LinkCheck/1.0"})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
                sample = response.read(32768).decode("utf-8", errors="ignore")
                challenge = any(term in sample.lower() for term in ["verifying your browser", "<title>just a moment", "<title>access denied"])
                return {"url": url, "final_url": response.url, "http_status": response.status,
                        "result": "access_check" if challenge else "ok"}
        except urllib.error.HTTPError as error:
            if error.code in {429, 500, 502, 503, 504} and attempt == 0:
                time.sleep(1)
                continue
            result = "missing" if error.code in {404, 410} else "access_check" if error.code in {401, 403, 429} else "network_check"
            return {"url": url, "http_status": error.code, "result": result}
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            if attempt == 0:
                time.sleep(1)
                continue
            return {"url": url, "result": "network_check", "detail": str(error)}
    raise AssertionError("unreachable")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external", action="store_true", help="also request external URL targets (not their fragments)")
    parser.add_argument("--report", type=Path, help="write a JSON audit report outside the repository")
    parser.add_argument("--timeout", type=float, default=15)
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    if args.timeout <= 0 or not 1 <= args.workers <= 8:
        parser.error("timeout must be positive and workers must be between 1 and 8")
    root = Path(__file__).resolve().parents[1]
    errors, urls, counts = local_check(root)
    print(f"Checked {counts['markdown_files']} Markdown files, {counts['local_links']} local links, and {counts['papers']} canonical papers.")
    for error in errors:
        print("ERROR:", error)
    results = []
    if args.external:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            results = list(pool.map(lambda url: external_check(url, args.timeout), sorted(urls)))
        summary = Counter(row["result"] for row in results)
        print("External targets:", json.dumps(dict(summary), sort_keys=True))
        for row in results:
            if row["result"] != "ok":
                print(f"REVIEW ({row['result']}): {row['url']} [{row.get('http_status', row.get('detail', 'challenge page'))}]")
    report = {"counts": counts, "local_errors": errors, "external_results": results}
    if args.report:
        if args.report.resolve().is_relative_to(root):
            parser.error("save transient reports outside the repository")
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    if errors:
        return 1
    if any(row["result"] != "ok" for row in results):
        return 2
    print("Validation passed" + (" (external requests included)." if args.external else " (local checks only)."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
