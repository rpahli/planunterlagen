# Quickstart: Markdown Site on GitHub Pages (MkDocs + Material)

## 1) Prerequisites

- Python 3.11+
- GitHub repository with Pages enabled
- Write access to repository settings/workflows

## 2) Install dependencies

```bash
python -m pip install mkdocs mkdocs-material
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
site_name: Project Docs
site_url: https://<org>.github.io/<repo>/
theme:
  name: material
  features:
    - navigation.sections
    - navigation.top
nav:
  - Home: index.md
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

Use a two-job workflow: build then deploy.

- Build job:
  - checkout
  - configure pages
  - install dependencies
  - run `mkdocs build --strict`
  - upload `site/` as Pages artifact
- Deploy job:
  - needs build
  - permissions: `pages: write`, `id-token: write`
  - deploy with `actions/deploy-pages@v4`

## 7) Link and regression checks

- Add Lychee action for internal/external link checking.
- Optionally add route smoke tests from sitemap for critical docs paths.

## 8) Theming for non-technical maintainers

- Start with Material palette/feature toggles in `mkdocs.yml`.
- Put custom styles in `docs/stylesheets/extra.css`.
- Avoid template overrides unless a specific UI need cannot be solved via config/CSS.

## 9) Ownership and maintenance

- Maintainers own `mkdocs.yml` navigation and scope include/exclude policy.
- CI must pass strict build and link checks before deploy.
- File moves/renames require redirect/update policy review to preserve stable URLs.
