# FineNav developer documentation

This public repository is the single build and deployment center for
<https://finenav.github.io/>. Each code repository maintains its own `docs/`
Markdown and `mkdocs.yml`; it does not deploy a separate site.

## Sources

| Module | Branch | Source | Status |
| --- | --- | --- | --- |
| FineNav-Engine | `dev` | `FineNav/FineNav-Engine/docs/` | Imported |
| finenav_map | To be confirmed | Repository-owned `docs/` | Not yet imported |
| finenav_planner | To be confirmed | Repository-owned `docs/` | Not yet imported |
| FineNav-SlamBox | — | Aggregator placeholder | Reserved |
| FineNav (ICRA version) | — | Aggregator placeholder | Reserved |

English uses `.md`. Chinese uses the same path with a `.zh.md` suffix.
Missing Chinese translations fall back to English. The ecosystem homepage and
all active Engine guides and the SlamBox / ICRA placeholders have Chinese translations.

## Deployment

1. Set **Settings → Pages → Source** to **GitHub Actions**.
2. Set the repository secret **DOCS_READ_TOKEN** to a FineNav-approved token with
   Contents read permission for the imported private repositories. A fine-grained
   token must use FineNav as resource owner and be approved if the organization
   requires it. Never commit the token.
3. Run **Deploy FineNav documentation** from the Actions page.

The workflow also runs daily at **06:00 UTC / 14:00 Asia/Shanghai**.
Module pushes become visible at the next successful aggregate build.
This workflow has no push trigger and does not use a `gh-pages` branch.

## Local build

Install Python, Git and Bash, then:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
python scripts/validate_site.py
python -m mkdocs serve
```

Private module imports require an existing working Git login or a temporary
`GithubAccessToken` environment variable. On Windows, Git Bash must be available
in PATH; use `.venv/Scripts/python.exe` as the Python interpreter.
Use UTF-8 (`PYTHONUTF8=1`) for the plugin's progress output on Windows.

`scripts/multirepo_i18n.py` adapts multirepo 0.8.3 to static-i18n 1.3.1:
it temporarily places imported files inside `docs/` for both language builds,
then removes the generated files. These temporary module directories are ignored
by Git; they are not maintained copies of module documentation.

Add future modules with a quoted `!import` URL and an explicit branch in
`mkdocs.yml`. Keep the import section identifier stable: it becomes the module
URL prefix. Translate displayed titles using `nav_translations` instead of
changing the import identifier.
