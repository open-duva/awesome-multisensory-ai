# Maintaining the list

The public sources are `data/catalog.json` and `data/relationships.json`. The catalog contains resource descriptions and source links; it does not contain search logs, rejected candidates, or editorial decision histories.

Keep research notes, backups, downloaded inputs, run logs, and preview outputs outside this repository. The ignore file only covers macOS metadata and Python caches. The public-file check limits what can enter the published collection.

## Update and check

After editing the public catalog or page template:

~~~sh
python3 scripts/build_collection.py
python3 scripts/build_atlas.py
python3 scripts/validate_catalog.py
python3 scripts/check_links.py
python3 scripts/build_collection.py --check
python3 scripts/build_atlas.py --check
python3 scripts/check_public_files.py --history
~~~

Generated topic pages, indexes, bibliography, and `atlas/dist/index.html` are tracked. Edit their sources rather than the generated output. Public-schema validation rejects editorial fields before they can be embedded in the website. The public-file check inspects the Git index and all reachable commits; CI runs it before validation and deployment. Add intentional new public file locations to its approved paths.

External URL checking is optional:

~~~sh
python3 scripts/check_links.py --external --report /tmp/multisensory-links.json
~~~

## Website

For a local preview, serve the repository with `python3 -m http.server 8765 --bind 127.0.0.1` and open `/atlas/dist/index.html`.

The Pages workflow publishes `atlas/dist/` when its contents change on `main`. Set GitHub Pages to use GitHub Actions. Document links on the site point to the repository, since only the built website directory is deployed.

Refresh `atlas/assets/research-map.png` after visible layout changes. Keep the content and code licenses separate, and publish only when authorized.
