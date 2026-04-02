# Publishing Scope Policy

## Purpose

Define which files are included in or excluded from the published documentation site.

## Include Rules

By default, all Markdown files under `docs/` are considered for publication.

### Explicitly Included Paths

- `docs/*.md` - Top-level documentation pages
- `docs/guide/` - User guides and getting started content
- `docs/maintenance/` - Maintenance and operational guides
- `docs/decisions/` - Decision records and governance

## Exclude Rules

### Explicitly Excluded Paths

- `.tmp/` - Temporary working files
- `*.draft.md` - Draft files not ready for publication
- `.specify/` - Specification and planning artifacts
- `specs/` - Feature specifications and design docs

### Excluded File Patterns

- Files starting with `_` (underscore) are treated as private/unpublished
- Files in `.gitignore` are automatically excluded

## Scope Changes

Any changes to the include/exclude policy must:

1. Be documented in this file with rationale
2. Be reviewed by documentation maintainers
3. Be tested with `mkdocs build --strict` before merge
4. Consider impact on existing published URLs

## Validation

The CI pipeline validates that:

- All included files are valid Markdown
- All internal links resolve within the included scope
- Navigation references only exist in included files
