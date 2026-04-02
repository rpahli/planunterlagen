# Publishing Overview

This page explains how the Planunterlagen documentation site is built, published, and maintained.

## Overview

The documentation site is automatically generated from Markdown files in the repository and published to GitHub Pages. The publishing system is designed to be simple for non-technical maintainers while ensuring quality through automated validation.

## How It Works

### 1. Source Content

Documentation is written in **Markdown** files stored in the `docs/` directory of the repository. Markdown is a simple, human-readable format that's easy to write and maintain.

Example:
```markdown
# Page Title

This is a paragraph with **bold** and *italic* text.

- List item 1
- List item 2
```

### 2. Static Site Generation

The site is built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. MkDocs converts Markdown files into a complete website with:

- Navigation menus
- Search functionality
- Responsive design
- Code highlighting
- And more...

### 3. Automated Publishing

When changes are pushed to the main branch, GitHub Actions automatically:

1. Checks out the repository
2. Installs dependencies
3. Builds the documentation with strict validation
4. Runs link checks
5. Deploys to GitHub Pages

The entire process typically completes in under 10 minutes.

## Publishing Workflow

### For Content Authors

1. **Edit Markdown files** in the `docs/` directory
2. **Test locally** with `mkdocs serve`
3. **Validate** with `mkdocs build --strict`
4. **Submit pull request** with your changes
5. **Wait for CI checks** to pass
6. **Merge** after review

### For Maintainers

1. **Review pull request** for content accuracy and style
2. **Check CI status** (build and link validation must pass)
3. **Approve and merge** when ready
4. **Monitor deployment** to ensure successful publication

## Quality Gates

Before deployment, the documentation must pass:

### Build Validation

- **Strict mode**: All warnings are treated as errors
- **Internal links**: Must resolve to existing pages
- **Anchors**: Must reference valid headings
- **Navigation**: Must reference existing files

### Link Validation

- **Internal links**: 100% must be valid (zero tolerance)
- **External links**: <5% failure threshold
- **Anchor references**: Must exist in target documents

### Content Policies

- **Publishing scope**: Only approved paths are published
- **URL stability**: Redirects required for moved/renamed content
- **Deprecation**: 90-day notice before removing published content

## Publishing Architecture

### Directory Structure

```
repository/
├── docs/                    # Documentation source
│   ├── index.md            # Home page
│   ├── guide/              # User guides
│   ├── maintenance/        # Maintainer docs
│   └── stylesheets/        # Custom CSS
├── mkdocs.yml              # Site configuration
├── requirements-docs.txt   # Python dependencies
└── .github/workflows/      # CI/CD workflows
    ├── docs-pages.yml      # Build and deploy
    └── docs-link-check.yml # Link validation
```

### Configuration

The site is configured in `mkdocs.yml`, which defines:

- Site metadata (name, URL, repository)
- Theme and features
- Navigation structure
- Validation rules
- Plugins and extensions

### Deployment

Deployment uses the official GitHub Actions workflow:

1. **Build job**: Builds static HTML from Markdown
2. **Deploy job**: Publishes to GitHub Pages

The deployment is fully automated with no manual steps required.

## URL Structure

Published URLs follow this pattern:

```
https://rpahli.github.io/planunterlagen/{page-path}
```

Examples:
- Home page: `https://rpahli.github.io/planunterlagen/`
- This page: `https://rpahli.github.io/planunterlagen/guide/publishing-overview/`

### URL Stability

Once published, URLs should remain stable. When moving or renaming content:

1. Add redirect rule in `mkdocs.yml`
2. Update internal references
3. Test with link checker
4. Document in URL lifecycle log

See the [URL Lifecycle Policy](../maintenance/url-lifecycle.md) for details.

## Theming and Customization

### Current Theme

The site uses **Material for MkDocs**, which provides:

- Modern, responsive design
- Built-in search
- Mobile-friendly navigation
- Accessibility features
- Customizable color palette

### Customization Options

Theming is managed through:

1. **Configuration** (`mkdocs.yml`): Features, colors, fonts
2. **Custom CSS** (`docs/stylesheets/extra.css`): Additional styling
3. **Template overrides** (if needed): Advanced customization

Custom styles can be added without modifying core theme files, making updates easier.

## Performance

### Build Performance

- **Local builds**: ~5-10 seconds
- **CI builds**: ~3-5 minutes (includes dependency installation)
- **Deployment**: ~5 minutes total from merge to live

### Site Performance

- **Static HTML**: Fast loading with no server processing
- **Search index**: Generated at build time
- **Assets**: Optimized CSS and JavaScript
- **CDN**: GitHub Pages serves content via CDN

## Monitoring and Maintenance

### Automated Checks

- **Build status**: Every push and pull request
- **Link validation**: On PRs and weekly scheduled runs
- **Deployment status**: Visible in GitHub Actions

### Manual Checks

Maintainers should periodically:

- Review external link health
- Monitor 404 errors
- Audit content structure
- Update dependencies
- Review theming and branding

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Authoring | Markdown | Content creation |
| Generator | MkDocs 1.6+ | Static site generation |
| Theme | Material for MkDocs 9+ | UI and features |
| CI/CD | GitHub Actions | Automated build/deploy |
| Hosting | GitHub Pages | Static site hosting |
| Link Check | Lychee | Link validation |

## Next Steps

- **Authors**: See [Getting Started](getting-started.md) for writing documentation
- **Maintainers**: Review the [Publishing Runbook](../maintenance/publishing-runbook.md)
- **Technical Owners**: Check the [Publishing Scope Policy](../maintenance/publishing-scope.md)

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)
