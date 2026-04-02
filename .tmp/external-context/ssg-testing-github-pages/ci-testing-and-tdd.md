---
source: Context7 API + official docs
library: GitHub Pages / MkDocs / Docusaurus / Astro Starlight
package: ssg-testing-github-pages
topic: testing-build-output-link-validity-navigation-regressions-content-sync-ci
fetched: 2026-04-02T12:00:00Z
official_docs: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
---

## CI baseline for GitHub Pages deployments

- Use `actions/configure-pages@v5` in build jobs.
- Upload static output with `actions/upload-pages-artifact@v4`.
- Deploy with `actions/deploy-pages@v4` in a separate job.
- Ensure deploy job has `pages: write` and `id-token: write` permissions and `needs: build`.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: actions/configure-pages@v5
      - run: <your-build-command>
      - uses: actions/upload-pages-artifact@v4
        with:
          path: <build-output-dir>

  deploy:
    needs: build
    permissions:
      contents: read
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

## Testing build output (TDD-friendly)

### MkDocs Material

- Run `mkdocs build --strict` to fail on warnings.
- Configure `validation` to escalate missing pages/anchors/links to warnings (which become errors with `--strict`).
- Recommended strict config:

```yaml
validation:
  omitted_files: warn
  absolute_links: warn
  unrecognized_links: warn
  anchors: warn
```

### Docusaurus

- Broken-link checks run on production build (`docusaurus build`).
- Keep strict behavior in `docusaurus.config.*`:

```ts
export default {
  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'throw',
      onBrokenMarkdownImages: 'throw',
    },
  },
};
```

### Astro Starlight

- Validate Starlight content collections via `docsLoader()` + `docsSchema()` in `src/content.config.ts`.
- Run `pnpm astro sync` and `pnpm astro check` to catch schema/type drift.

## Link validity in CI

- Starlight project itself uses `pnpm linkcheck` for internal links.
- For repo-wide external/internal checks (Markdown/HTML/text), use `lycheeverse/lychee-action@v2`.
- Cache `.lycheecache` in CI to reduce flaky/rate-limited failures.

```yaml
- uses: lycheeverse/lychee-action@v2
  with:
    args: --root-dir "$(pwd)" --cache --max-cache-age 1d .
```

## Navigation regression checks

- **MkDocs:** keep explicit `nav:` in `mkdocs.yml` and rely on `validation.nav.not_found` + `--strict` to catch menu/file drift.
- **Docusaurus:** detect sidebar/route drift with `onDuplicateRoutes` and build-time broken-link checks; for UI regressions use Playwright screenshots from `build/sitemap.xml` (official Docusaurus visual-regression approach shown with Argos).
- **Starlight:** sidebar can be autogen from filesystem; guard regressions by checking generated pages/links (`pnpm linkcheck`) and by testing frontmatter/sidebar ordering rules.

## Content sync checks in CI (practical pattern)

1. Run strict build (`mkdocs build --strict` or `docusaurus build` or `astro build`).
2. Run link checks (`pnpm linkcheck` and/or `lychee-action`).
3. Run route-level smoke tests from sitemap (Playwright).
4. Fail on any broken anchors/links or missing nav targets.

This gives a TDD loop where doc edits are considered complete only when generated output, links, and navigation all pass.
