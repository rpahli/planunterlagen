# Research: Static Site for Markdown Files on GitHub Pages

## Decision 1: Static Site Framework

- Decision: Use MkDocs + Material for MkDocs as the primary framework.
- Rationale: It is the strongest fit for non-technical maintainers (Markdown-first workflow, simple YAML navigation, low day-2 ops burden), while still offering robust navigation and good theming without React-level complexity.
- Alternatives considered:
  - Docusaurus: excellent flexibility and UX, but higher maintenance and customization complexity.
  - Astro Starlight: modern and strong docs UX, but slightly higher setup complexity than MkDocs for this repo's immediate needs.
  - Jekyll: native GitHub Pages support, but weaker default docs navigation and less ergonomic modern theming.

## Decision 2: GitHub Pages Deployment Strategy

- Decision: Deploy via GitHub Actions using `actions/configure-pages@v5`, `actions/upload-pages-artifact@v4`, and `actions/deploy-pages@v4`.
- Rationale: This is the current recommended GitHub Pages workflow for custom static generators and gives explicit, auditable build/deploy steps.
- Alternatives considered:
  - `mkdocs gh-deploy`: simpler for manual use, but less controlled and less reviewable than CI-based deployment.
  - Jekyll-native branch publishing: not chosen because framework selection is MkDocs.

## Decision 3: TDD and Verification Approach for Docs

- Decision: Treat docs publishing as testable software delivery with strict pre-deploy checks.
- Rationale: The feature requires reliable sync and link correctness; strict checks prevent regressions before site publication.
- Alternatives considered:
  - Build-only checks: insufficient for broken external/internal links and navigation drift.
  - Manual review only: too error-prone and not scalable.

### Selected test gates

- `mkdocs build --strict` as mandatory build gate.
- MkDocs validation rules enabled for omitted files, absolute links, unrecognized links, and anchors.
- Lychee-based link validation in CI for internal and external links.
- Optional route smoke tests (Playwright) from sitemap for high-risk navigation paths.

## Decision 4: Theming Strategy

- Decision: Start with Material palette/typography/config-level customization and allow incremental extension via `docs/stylesheets/extra.css`; reserve template overrides for explicit needs.
- Rationale: Meets current branding/theming needs with low complexity, while still enabling deeper customization later.
- Alternatives considered:
  - Full template override from day one: unnecessary complexity and higher maintenance.
  - Docusaurus swizzling-heavy customization: powerful but not aligned with non-technical maintainer goal.

## Decision 5: Content Scope and URL Stability

- Decision: Define explicit include/exclude path rules and maintain stable URL mapping with redirect rules when files are moved or renamed.
- Rationale: This directly addresses FR-005, FR-009, and FR-010 and reduces broken links after reorganizations.
- Alternatives considered:
  - Implicit filesystem-only discovery without policy: easier initially but fragile over time.

## Framework Recommendation Matrix (Condensed)

| Option | Non-technical ease | Setup/Maintenance | GH Pages fit | Theming | Docs nav | Overall fit |
|---|---:|---:|---:|---:|---:|---:|
| MkDocs + Material | 5 | 4 | 5 | 4 | 5 | 5 |
| Astro Starlight | 4 | 4 | 4 | 4 | 5 | 4 |
| Docusaurus | 3 | 2 | 4 | 5 | 5 | 4 |
| Jekyll | 3 | 3 | 5 | 3 | 2 | 3 |

## Sources

- MkDocs deployment and config docs
- Material for MkDocs theming/customization docs
- GitHub Pages custom workflow docs
- Docusaurus deployment/config docs
- Astro/Starlight deployment and theming docs
- Lychee action docs

Detailed source extracts are stored in `.tmp/external-context/ssg-testing-github-pages/`.
