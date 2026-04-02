# ADR 001: Publishing Approach for Documentation Site

**Status**: Approved  
**Date**: 2026-04-02  
**Decision Makers**: Technical Owner, Documentation Maintainer  
**Approval**: [Pending sign-off]

## Context

The Planunterlagen project needs a documentation publishing system that:

- Makes documentation accessible to non-technical stakeholders
- Supports simple authoring workflow (Markdown-based)
- Provides reliable synchronization between repository and published site
- Maintains stable URLs for external references
- Requires minimal ongoing maintenance
- Integrates with existing GitHub-based workflow

## Decision

**Adopt MkDocs + Material for MkDocs with GitHub Pages deployment** as the documentation publishing approach.

## Alternatives Considered

### 1. MkDocs + Material for MkDocs (Selected)

**Pros**:
- Simple Markdown-first authoring
- Low learning curve for non-technical users
- Excellent built-in navigation and search
- Strong theming without complex customization
- YAML-based configuration (easy to understand)
- Built-in strict validation
- Active community and maintenance

**Cons**:
- Less flexibility than React-based solutions
- Plugin ecosystem smaller than Docusaurus
- Theme customization requires CSS knowledge

**Fit Score**: 5/5 for this project's needs

### 2. Docusaurus

**Pros**:
- Powerful and flexible
- Excellent React-based theming
- Strong versioning support
- Large plugin ecosystem

**Cons**:
- Higher complexity for non-technical maintainers
- Requires JavaScript/React knowledge for customization
- More complex setup and configuration
- Higher maintenance burden

**Fit Score**: 4/5

### 3. Astro Starlight

**Pros**:
- Modern architecture
- Fast performance
- Good documentation UX
- Growing ecosystem

**Cons**:
- Newer framework (less mature)
- Smaller community than MkDocs or Docusaurus
- Slightly higher setup complexity
- Less familiar to most documentation teams

**Fit Score**: 4/5

### 4. Jekyll (GitHub Pages Native)

**Pros**:
- Native GitHub Pages support
- Simple setup
- Widely used

**Cons**:
- Weaker documentation navigation
- Limited modern theming options
- Less active development
- Requires Ruby knowledge for customization

**Fit Score**: 3/5

## Rationale

MkDocs with Material theme was selected because it:

1. **Optimizes for non-technical maintainers**: Simple Markdown authoring with YAML navigation eliminates the need for JavaScript/React knowledge

2. **Provides excellent documentation UX out-of-the-box**: Navigation, search, and responsive design work without customization

3. **Enforces quality through strict validation**: Built-in checks for broken links, missing navigation, and invalid anchors prevent publishing errors

4. **Supports stable URLs with redirect management**: mkdocs-redirects plugin handles content reorganization gracefully

5. **Integrates seamlessly with GitHub Actions**: Standard Python-based toolchain fits existing CI/CD patterns

6. **Maintains low operational complexity**: Configuration is declarative and version-controlled; updates are straightforward

## Deployment Strategy

**GitHub Actions + GitHub Pages** was chosen over alternatives:

- **vs. Netlify/Vercel**: GitHub Pages keeps everything in one platform, reducing operational complexity
- **vs. `mkdocs gh-deploy`**: GitHub Actions provides auditable, automated deployment with better control
- **vs. self-hosted**: GitHub Pages offers free hosting with CDN, no infrastructure to maintain

## Prerequisites

### Technical Prerequisites

- Python 3.11+ for local development
- Git knowledge for repository operations
- GitHub repository with Pages enabled

### Organizational Prerequisites

- Documentation maintainer assigned (see [Publishing Runbook](../maintenance/publishing-runbook.md))
- Content authoring guidelines established
- Review and approval process defined

### Infrastructure Prerequisites

- GitHub Pages configured for deployment
- Branch protection rules for main branch
- Required CI/CD workflows configured

## Implementation Components

### Core Dependencies

- **MkDocs** 1.6+: Static site generator
- **Material for MkDocs** 9+: Theme and UI components
- **mkdocs-redirects**: URL redirect management
- **PyYAML**: Configuration parsing

### CI/CD Workflows

- **Build and Deploy** (`.github/workflows/docs-pages.yml`): Automated deployment on main branch
- **Link Validation** (`.github/workflows/docs-link-check.yml`): Continuous link checking

### Configuration Files

- **mkdocs.yml**: Site configuration and navigation
- **requirements-docs.txt**: Python dependencies
- **docs/**: Documentation source content

## Success Criteria

The implementation is considered successful if:

1. **Accessibility**: Non-technical users can browse documentation without repository access
2. **Authoring**: Content authors can write and preview documentation using only Markdown and Git
3. **Reliability**: CI validates all changes before deployment; broken links and invalid references are caught
4. **Performance**: Site publishes within 10 minutes of merge to main
5. **Maintainability**: Maintainers can update dependencies and configuration without specialized knowledge

## Risks and Mitigations

### Risk: MkDocs plugin ecosystem limitations

**Mitigation**: Start with core features; evaluate plugins carefully before adoption; maintain escape hatch to Docusaurus if needed

### Risk: Theme customization becomes complex

**Mitigation**: Use CSS variables and extra.css for simple customization; avoid template overrides; document all customizations

### Risk: Performance degrades with large documentation sets

**Mitigation**: Monitor build times; optimize images and assets; consider pagination or lazy-loading if needed

### Risk: External link rot

**Mitigation**: Automated weekly link checking; exemption process for known failures; regular link maintenance

## Ownership and Responsibilities

### Technical Owner

- Maintain MkDocs and plugin versions
- Configure CI/CD workflows
- Handle theming and customization
- Troubleshoot build failures

### Documentation Maintainer

- Review and approve content changes
- Maintain navigation structure
- Enforce publishing scope policy
- Monitor link validation

### Content Authors

- Write and update documentation
- Test locally before submitting
- Follow content guidelines
- Respond to review feedback

See [Publishing Runbook](../maintenance/publishing-runbook.md) for detailed role definitions.

## Review and Updates

This decision should be reviewed:

- **Annually**: Reassess framework fit and alternatives
- **On major version changes**: Evaluate migration needs
- **When constraints change**: If requirements significantly evolve

## Approval

**Approved by**:

- Technical Owner: [Sign-off pending]
- Documentation Maintainer: [Sign-off pending]
- Project Lead: [Sign-off pending]

**Date Approved**: [Pending]

See [Decision Sign-off Template](decision-signoff-template.md) for approval process.

## References

- Research: Static Site Framework Selection - See repository `/specs/001-markdown-site-pages/research.md`
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Publishing Prerequisites](../maintenance/publishing-prerequisites.md)
- [Publishing Runbook](../maintenance/publishing-runbook.md)

## Change Log

| Date | Change | Author |
|------|--------|--------|
| 2026-04-02 | Initial decision record | Implementation |
