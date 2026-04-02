# Contract: Markdown Publishing Workflow

## Purpose

Define the operational contract for converting repository Markdown into a stable GitHub Pages website.

## Producer/Consumer

- Producer: Repository maintainers and CI pipeline
- Consumer: Public site visitors and project stakeholders

## Input Contract

### Source content

- In-scope Markdown files must be under agreed include paths.
- Excluded paths must be explicitly listed.
- Every in-scope page must have a resolvable title.

### Configuration

- `mkdocs.yml` is the authoritative publishing configuration.
- Navigation order is explicit in `nav` to avoid accidental IA drift.
- Theme configuration changes must not break readability or navigation.

## Build Contract

Build is valid only if all are true:

1. `mkdocs build --strict` exits successfully.
2. No unresolved internal links/anchors remain.
3. Link checker passes policy thresholds.
4. Output artifact (`site/`) is produced.

If any condition fails, deployment is blocked.

## Deployment Contract

- Deployment must run through GitHub Pages actions-based workflow.
- Deploy job runs only after successful build job.
- Site URL remains stable once configured.
- Deployment output URL is captured in workflow summary.

## URL and Lifecycle Contract

- New source file -> new published page route.
- Updated source file -> same route updated content.
- Renamed/moved source file -> old route redirected or documented as removed.
- Deleted source file -> route removed only per explicit policy.

## Theming Contract

- Baseline theming via Material config and CSS variables.
- Custom CSS is allowed in `docs/stylesheets/extra.css`.
- Template overrides require maintainer review and justification.

## Verification Contract (TDD-aligned)

- Any content or config change must add/update at least one verification expectation:
  - strict build pass
  - link integrity pass
  - nav reachability pass for affected pages
- CI is the final gate before publication.
