# Data Model: Markdown Static Site Publishing

## Entity: MarkdownSourceFile

- Purpose: Source document intended for publication.
- Fields:
  - `id` (string, derived from repository-relative path, unique)
  - `path` (string, repository-relative path)
  - `title` (string, inferred from first heading or frontmatter)
  - `frontmatter` (map, optional metadata)
  - `inScope` (boolean, based on include/exclude rules)
  - `lastModifiedAt` (datetime)
  - `contentHash` (string, for change detection)
- Validation rules:
  - `path` must be unique among in-scope files.
  - `title` must be non-empty; duplicates allowed but must be disambiguated in nav label.
  - Markdown links should resolve or be explicitly allowed as external.

## Entity: PublishedPage

- Purpose: Generated HTML page corresponding to a source document.
- Fields:
  - `urlPath` (string, stable route)
  - `sourceFileId` (string, FK to `MarkdownSourceFile.id`)
  - `publishedAt` (datetime)
  - `buildId` (string, CI run reference)
  - `status` (enum: `generated`, `redirected`, `removed`)
- Validation rules:
  - `urlPath` must be unique.
  - `status=generated` requires existing source file.
  - `status=redirected` requires redirect target route.

## Entity: NavigationNode

- Purpose: Navigation item visible to site visitors.
- Fields:
  - `id` (string)
  - `label` (string)
  - `targetUrlPath` (string, optional for grouping nodes)
  - `order` (integer)
  - `parentId` (string, nullable)
- Validation rules:
  - Sibling nodes cannot share the same `order`.
  - Leaf nodes require `targetUrlPath` mapped to a `PublishedPage`.

## Entity: PublishingConfiguration

- Purpose: Rules and settings controlling what and how content is published.
- Fields:
  - `siteName` (string)
  - `siteUrl` (string)
  - `baseUrl` (string)
  - `includePaths` (list<string>)
  - `excludePaths` (list<string>)
  - `navDefinition` (list<NavigationNode refs>)
  - `themeConfig` (map: palette, typography, logo, custom CSS)
  - `validationConfig` (map: link/anchor/nav strictness)
- Validation rules:
  - Include/exclude rules cannot conflict for same final path without explicit precedence.
  - `siteUrl` must match configured GitHub Pages URL.

## Entity: SolutionDecisionRecord

- Purpose: Persisted rationale for framework and workflow choices.
- Fields:
  - `decisionId` (string)
  - `decision` (string)
  - `rationale` (string)
  - `alternatives` (list<string>)
  - `approvedBy` (string/list)
  - `approvedAt` (datetime)

## Relationships

- `MarkdownSourceFile` 1 -> 0..1 `PublishedPage` (a source usually maps to one page).
- `PublishedPage` many -> 1 `PublishingConfiguration` (single active config per deployment).
- `NavigationNode` many -> 0..1 `PublishedPage` (group nodes may not target pages).
- `SolutionDecisionRecord` 1 -> many `PublishingConfiguration` revisions.

## State Transitions

### MarkdownSourceFile lifecycle

- `draft` -> `in_scope` (matches include/exclude policy)
- `in_scope` -> `published` (successful strict build + deploy)
- `published` -> `moved_or_renamed` (path change detected)
- `moved_or_renamed` -> `redirected` (old route redirected) or `removed` (intentional depublication)

### PublishedPage lifecycle

- `generated` -> `redirected` (source moved/renamed with route preservation)
- `generated` -> `removed` (source deleted and policy removes page)
