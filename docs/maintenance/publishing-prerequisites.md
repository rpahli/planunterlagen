# Publishing Prerequisites and Responsibilities

This document outlines the technical, organizational, and skill prerequisites required to operate the documentation publishing system successfully.

## Technical Prerequisites

### Infrastructure Requirements

#### GitHub Repository Configuration

- [X] Repository created with appropriate name and description
- [X] GitHub Pages enabled in repository settings
- [X] Pages source set to GitHub Actions
- [X] Branch protection rules configured for main branch
- [ ] Required status checks enabled (build, link-check)

#### CI/CD Pipeline

- [X] GitHub Actions workflows configured
  - [X] Build and deploy workflow (`.github/workflows/docs-pages.yml`)
  - [X] Link validation workflow (`.github/workflows/docs-link-check.yml`)
- [ ] Workflow permissions verified (pages: write, id-token: write)
- [ ] Deployment environment configured in repository settings

#### Local Development Environment

For all contributors:

- **Python 3.11+**: Required for MkDocs
- **Git**: Version control operations
- **Text editor**: Markdown editing (VS Code, Sublime, Vim, etc.)
- **Web browser**: Preview and testing

Installation verification:

```bash
python --version  # Should be 3.11+
git --version     # Any recent version
```

### Software Dependencies

#### Required Python Packages

Installed via `requirements-docs.txt`:

- **MkDocs** >= 1.6.0
- **mkdocs-material** >= 9.0.0
- **mkdocs-redirects** >= 1.2.0
- **PyYAML** >= 6.0

Installation (recommended approach with virtual environment):

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # Linux/Mac
# OR .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements-docs.txt
```

!!! note "Why Virtual Environments?"
    Virtual environments are **strongly recommended** to:
    
    - Isolate documentation dependencies from system Python
    - Prevent version conflicts with other projects
    - Ensure reproducible builds across different machines
    - Comply with PEP 668 on modern Linux distributions
    
    The `.venv/` directory is already excluded in `.gitignore`.

Alternative (system-wide, not recommended):

```bash
# Only if virtual environment is not an option
pip install -r requirements-docs.txt
```

#### Optional Tools

- **Lychee**: Link validation (runs in CI, optional locally)
- **Playwright**: Optional smoke testing (not required for MVP)

## Organizational Prerequisites

### Role Assignments

At minimum, the following roles must be assigned:

#### 1. Technical Owner (Required)

**Responsibilities**:
- Maintain MkDocs configuration and dependencies
- Manage CI/CD workflows
- Troubleshoot build failures
- Implement theming customizations
- Handle infrastructure issues

**Prerequisites**:
- Python package management experience
- GitHub Actions workflow knowledge
- CSS for theming (basic)
- MkDocs configuration understanding

**Time Commitment**: 2-4 hours/month (steady state)

#### 2. Documentation Maintainer (Required)

**Responsibilities**:
- Review and approve content pull requests
- Maintain navigation structure in `mkdocs.yml`
- Enforce publishing scope and quality policies
- Monitor link validation
- Coordinate with content authors

**Prerequisites**:
- Strong Markdown knowledge
- Git workflow proficiency
- YAML syntax familiarity
- Documentation best practices understanding

**Time Commitment**: 4-8 hours/month (varies with content volume)

#### 3. Content Authors (Multiple)

**Responsibilities**:
- Create and update documentation
- Test changes locally
- Submit pull requests
- Respond to review feedback
- Follow content guidelines

**Prerequisites**:
- Markdown authoring
- Basic Git operations (fork, branch, commit, PR)
- Local MkDocs setup for testing

**Time Commitment**: As needed per project

### Approval Authority

Define who can approve:

- **Content changes**: Documentation Maintainer
- **Structural changes** (navigation, scope): Technical Owner + Documentation Maintainer
- **Configuration changes** (mkdocs.yml, workflows): Technical Owner
- **Dependency updates**: Technical Owner
- **Publishing decisions**: Project Lead + Technical Owner

## Skill Prerequisites by Role

### Content Author Skills

**Required**:
- ✅ Markdown syntax (headings, lists, links, code blocks)
- ✅ Git basics (clone, branch, commit, push, PR)
- ✅ Local command-line usage (cd, pip, mkdocs serve)

**Recommended**:
- YAML syntax (for frontmatter)
- Basic HTML (for advanced formatting)
- Documentation writing best practices

**Training Resources**:
- [Markdown Guide](https://www.markdownguide.org/)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [MkDocs Getting Started](https://www.mkdocs.org/getting-started/)

### Documentation Maintainer Skills

**Required**:
- ✅ All Content Author skills (above)
- ✅ YAML configuration (mkdocs.yml structure)
- ✅ Git workflow (branches, merges, conflict resolution)
- ✅ Pull request review process
- ✅ Link validation interpretation

**Recommended**:
- GitHub Actions basics (reading workflow logs)
- Information architecture principles
- Content governance

**Training Resources**:
- [MkDocs Configuration](https://www.mkdocs.org/user-guide/configuration/)
- [Material for MkDocs Setup](https://squidfunk.github.io/mkdocs-material/setup/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

### Technical Owner Skills

**Required**:
- ✅ All Maintainer skills (above)
- ✅ Python package management (pip, requirements files)
- ✅ GitHub Actions workflow authoring
- ✅ CSS for theming customization
- ✅ MkDocs plugin ecosystem knowledge

**Recommended**:
- Python scripting (for custom checks/tools)
- Web performance optimization
- DevOps best practices

**Training Resources**:
- [MkDocs Plugins](https://www.mkdocs.org/dev-guide/plugins/)
- [Material for MkDocs Customization](https://squidfunk.github.io/mkdocs-material/customization/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Process Prerequisites

### Content Workflow

A documented content workflow must be established covering:

1. **Content Planning**: How topics are identified and prioritized
2. **Authoring Process**: Draft → Review → Publish cycle
3. **Review Standards**: What maintainers check during review
4. **Approval Requirements**: When sign-off is required
5. **Publication Timeline**: Expected turnaround times

See [Content Update Checklist](content-update-checklist.md) for operational guidance.

### Quality Gates

Define and document:

- **Pre-merge requirements**: CI checks, review approval, etc.
- **Link validation policy**: Acceptable thresholds for broken links
- **Style guide**: Formatting and writing standards
- **Deprecation policy**: Notice period before content removal

See Link Policy (repository `/tests/docs/link-policy.md`) and [URL Lifecycle](url-lifecycle.md).

### Communication Channels

Establish:

- **Primary channel**: Where documentation discussions happen (GitHub Issues, Discussions, Slack, etc.)
- **Review notifications**: How reviewers are alerted to PRs
- **Incident escalation**: Who to contact for urgent issues
- **Stakeholder updates**: How to communicate major documentation changes

## Access Control Prerequisites

### Repository Permissions

Define permission levels:

| Role | Repository Access | Needed Permissions |
|------|------------------|-------------------|
| Content Author | Read (fork workflow) | Fork, create PR |
| Content Author (team member) | Write | Create branches, create PR |
| Documentation Maintainer | Write | Review PRs, merge, manage labels |
| Technical Owner | Admin | All above + manage settings, workflows |

### GitHub Pages Permissions

Ensure deployment account/workflow has:

- [X] `pages: write` permission
- [X] `id-token: write` permission (for attestation)
- [X] `contents: read` permission

Configured in `.github/workflows/docs-pages.yml`.

## Knowledge Prerequisites

### Documentation Available

The following documentation must be accessible to all roles:

- [X] [Publishing Runbook](publishing-runbook.md) - Operational procedures
- [X] [Content Update Checklist](content-update-checklist.md) - Step-by-step guide
- [X] [URL Lifecycle Policy](url-lifecycle.md) - Content change management
- [X] [Publishing Scope](publishing-scope.md) - What gets published
- [X] Link Policy (repository `/tests/docs/link-policy.md`) - Link validation rules
- [X] README.md - Quick start and local setup

### Onboarding Process

New team members should complete:

1. **Content Authors**:
   - [ ] Read Getting Started guide
   - [ ] Set up local environment
   - [ ] Clone repository
   - [ ] Run `mkdocs serve` successfully
   - [ ] Review style guide and content checklist
   - [ ] Submit test PR (small documentation fix)

2. **Documentation Maintainers**:
   - [ ] Complete Content Author onboarding
   - [ ] Review all publishing policies
   - [ ] Shadow experienced maintainer for 2-3 PR reviews
   - [ ] Understand CI/CD workflow logs
   - [ ] Practice local testing and validation

3. **Technical Owners**:
   - [ ] Complete Maintainer onboarding
   - [ ] Review all workflow configurations
   - [ ] Understand dependency management
   - [ ] Practice troubleshooting build failures
   - [ ] Test configuration changes in feature branch

## Monitoring and Maintenance Prerequisites

### Regular Monitoring Required

#### Weekly

- Review CI/CD execution logs
- Check link validation results
- Monitor deployment success rate

#### Monthly

- Review dependency versions for updates
- Check for MkDocs/Material plugin updates
- Audit published content scope
- Review redirect rules

#### Quarterly

- Reassess roles and responsibilities
- Review and update policies
- Evaluate workflow efficiency
- Plan major improvements or migrations

### Incident Response Readiness

Technical Owner must be prepared to:

- Debug build failures within 4 hours
- Restore deployment within 24 hours
- Escalate infrastructure issues to GitHub Support
- Communicate status during outages

See [Publishing Runbook](publishing-runbook.md) for incident response procedures.

## Financial Prerequisites

### Costs

This publishing approach is **free** for public repositories:

- ✅ GitHub Pages hosting: $0
- ✅ GitHub Actions (2,000 minutes/month free): $0 for typical doc builds
- ✅ MkDocs and plugins: Open source, $0
- ✅ Domain (if using github.io): $0

**Optional costs**:

- Custom domain: ~$10-15/year (if desired)
- Additional GitHub Actions minutes: If exceeding free tier (~$0.008/minute)

### Budget Approval

No budget required for basic implementation. Custom domain requires minimal approval.

## Risk Mitigation Prerequisites

### Backup and Recovery

- **Source control**: All content in Git (primary backup)
- **Deployment history**: GitHub Pages keeps deployment history
- **Rollback capability**: Revert commits and re-deploy

No additional backup infrastructure needed.

### Disaster Recovery Plan

In case of:

- **Repository loss**: Restore from local clones
- **GitHub Pages outage**: Wait for restoration (typically minutes to hours)
- **Corrupted build**: Revert to last known good commit
- **Lost local environment**: Reinstall from `requirements-docs.txt`

## Checklist: Ready to Publish?

Before going live, verify:

**Technical**:
- [ ] Python 3.11+ installed
- [ ] Dependencies installed (`requirements-docs.txt`)
- [ ] Local build succeeds: `mkdocs build --strict`
- [ ] GitHub Pages enabled
- [ ] CI/CD workflows configured and tested

**Organizational**:
- [ ] Technical Owner assigned
- [ ] Documentation Maintainer assigned
- [ ] Roles and responsibilities documented
- [ ] Onboarding materials available

**Process**:
- [ ] Content workflow defined
- [ ] Review standards established
- [ ] Quality gates configured
- [ ] Communication channels established

**Content**:
- [ ] Initial documentation written
- [ ] Navigation structure defined
- [ ] Style guide available (or adopted)
- [ ] First content review completed

**Approval**:
- [ ] Publishing decision approved (see [ADR 001](../decisions/001-publishing-approach.md))
- [ ] Stakeholders informed
- [ ] Go-live date set

## Next Steps

Once prerequisites are met:

1. **Initial Deployment**: Merge to main and verify GitHub Pages deployment
2. **Validation**: Test navigation, links, and search on live site
3. **Communication**: Announce documentation site to stakeholders
4. **Iteration**: Gather feedback and improve content

## Support and Resources

- **MkDocs Issues**: [github.com/mkdocs/mkdocs/issues](https://github.com/mkdocs/mkdocs/issues)
- **Material Theme Issues**: [github.com/squidfunk/mkdocs-material/issues](https://github.com/squidfunk/mkdocs-material/issues)
- **GitHub Pages Support**: [docs.github.com/en/pages](https://docs.github.com/en/pages)
- **Project Maintainers**: See [Publishing Runbook](publishing-runbook.md) for contact info
