# Quickstart: Markdown Site on GitHub Pages (MkDocs + Material)

## 1) Prerequisites

- Python 3.11+
- GitHub repository with Pages enabled
- Write access to repository settings/workflows

## 2) Install dependencies

```bash
pip install -r requirements-docs.txt
```

Contents of `requirements-docs.txt`:
```
mkdocs>=1.6.0
mkdocs-material>=9.0.0
mkdocs-redirects>=1.2.0
pyyaml>=6.0
```

## 3) Create baseline structure

```text
docs/
  index.md
mkdocs.yml
.github/workflows/docs-pages.yml
```

## 4) Minimal `mkdocs.yml`

```yaml
site_name: Planunterlagen Documentation
site_url: https://rpahli.github.io/planunterlagen/
repo_url: https://github.com/rpahli/planunterlagen

theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.sections
    - navigation.top
    - navigation.tabs
    - navigation.expand
    - search.suggest
    - search.highlight
    - content.code.copy

plugins:
  - search
  - redirects:
      redirect_maps:
        # Add redirects here when moving files

nav:
  - Home: index.md
  - Guide:
      - Getting Started: guide/getting-started.md
      - Publishing Overview: guide/publishing-overview.md
  - Maintenance:
      - Publishing Runbook: maintenance/publishing-runbook.md
      - Publishing Scope: maintenance/publishing-scope.md

validation:
  omitted_files: warn
  absolute_links: warn
  unrecognized_links: warn
  anchors: warn

extra_css:
  - stylesheets/extra.css
```

## 5) Local verification (TDD loop)

```bash
mkdocs build --strict
mkdocs serve
```

- Add or edit Markdown.
- Re-run `mkdocs build --strict` until clean.
- Verify navigation and target links in browser.

## 6) GitHub Actions deployment workflow

Implemented in `.github/workflows/docs-pages.yml`:

**Build job**:
- checkout repository
- configure GitHub Pages
- set up Python 3.11
- install dependencies from `requirements-docs.txt`
- run navigation sync check: `python scripts/docs/check_nav_sync.py`
- run strict build: `mkdocs build --strict`
- upload `site/` as Pages artifact

**Deploy job**:
- needs: build
- permissions: `pages: write`, `id-token: write`
- deploy with `actions/deploy-pages@v4`
- outputs page URL

## 7) Link and regression checks

Implemented in `.github/workflows/docs-link-check.yml`:

- Runs on pull requests affecting docs
- Runs weekly via cron schedule
- Runs on manual trigger
- Uses Lychee action for internal/external link validation
- Creates GitHub issue on scheduled check failures
- Smoke check plan documented in `tests/docs/smoke-check-plan.md`

## 8) Theming for non-technical maintainers

- Start with Material palette/feature toggles in `mkdocs.yml`.
- Put custom styles in `docs/stylesheets/extra.css`.
- Avoid template overrides unless a specific UI need cannot be solved via config/CSS.

## 9) Ownership and maintenance

- Maintainers own `mkdocs.yml` navigation and scope include/exclude policy.
- CI must pass strict build and link checks before deploy.
- File moves/renames require redirect/update policy review to preserve stable URLs.
