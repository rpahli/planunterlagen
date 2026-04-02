# Publishing Runbook: Roles and Ownership

## Purpose

Define maintainer roles, responsibilities, and operational procedures for the documentation publishing system.

## Roles and Responsibilities

### Documentation Maintainer

**Primary Responsibilities**:
- Review and approve content changes
- Maintain navigation structure in `mkdocs.yml`
- Enforce publishing scope policy
- Monitor CI/CD pipeline health
- Handle URL lifecycle events

**Required Skills**:
- Markdown authoring
- Basic YAML configuration
- Git workflow knowledge
- Understanding of documentation structure

**Access Requirements**:
- Write access to repository
- Ability to merge pull requests
- GitHub Pages management permissions

### Content Author

**Primary Responsibilities**:
- Create and update documentation content
- Follow Markdown style guide
- Ensure internal links are valid
- Test locally before submitting

**Required Skills**:
- Markdown authoring
- Basic Git operations
- Local MkDocs setup

**Access Requirements**:
- Read/fork access to repository
- Ability to create pull requests

### Technical Owner

**Primary Responsibilities**:
- Maintain MkDocs and plugin versions
- Configure CI/CD workflows
- Troubleshoot build failures
- Implement theming and customization
- Manage GitHub Pages settings

**Required Skills**:
- Python package management
- GitHub Actions workflow configuration
- MkDocs plugin ecosystem knowledge
- CSS customization (for theming)

**Access Requirements**:
- Repository admin access
- Ability to modify GitHub Actions workflows
- GitHub Pages configuration access

## Operational Procedures

### Daily Operations

**Content Updates** (by Authors):
1. Fork or branch from main
2. Edit Markdown files
3. Test locally: `mkdocs serve`
4. Run strict build: `mkdocs build --strict`
5. Submit pull request
6. Address reviewer feedback

**Pull Request Review** (by Maintainers):
1. Check that CI passes (build + link check)
2. Review content for accuracy and style
3. Verify navigation updates if files added/moved
4. Approve and merge
5. Monitor deployment

### Weekly Operations

**Health Checks** (by Maintainers):
- Review CI/CD execution logs
- Check for failed link validations
- Monitor external link health
- Review any 404 errors
- Verify site accessibility

### Monthly Operations

**Maintenance Tasks** (by Technical Owner):
- Review and update dependencies in `requirements-docs.txt`
- Check for MkDocs and plugin updates
- Review and clean up redirect rules
- Audit published content scope
- Performance review (build times, site load times)

### Quarterly Operations

**Strategic Reviews** (by All Roles):
- Review documentation structure and navigation
- Evaluate user feedback
- Plan major content additions/reorganizations
- Review and update policies (publishing scope, link policy, URL lifecycle)
- Assess theming and branding needs

## Incident Response

### Build Failures

**Severity**: High (blocks deployment)

**Response Procedure**:
1. Check GitHub Actions logs for error details
2. Identify failing step (dependency install, build, link check)
3. Reproduce locally with `mkdocs build --strict`
4. Fix issue in feature branch
5. Verify fix locally
6. Submit emergency PR with fix
7. Fast-track review and merge

**Common Causes**:
- Broken internal links
- Invalid YAML in `mkdocs.yml`
- Missing navigation references
- Dependency version conflicts

### Link Check Failures

**Severity**: Medium (may allow deployment with warnings)

**Response Procedure**:
1. Review link check report in CI logs
2. Categorize failures (internal vs. external)
3. For internal links: fix immediately
4. For external links: verify if temporary or permanent
5. Update or exempt broken external links
6. Document exemptions in link policy

### Deployment Failures

**Severity**: Critical (site unavailable)

**Response Procedure**:
1. Check GitHub Pages deployment status
2. Verify GitHub Pages settings and permissions
3. Review deployment job logs
4. Check for repository or Pages quota issues
5. Rollback to last known good deployment if needed
6. Contact GitHub Support if infrastructure issue

### Performance Degradation

**Severity**: Low to Medium

**Response Procedure**:
1. Measure build time and site load time
2. Identify large files or excessive plugins
3. Optimize images and assets
4. Review and prune unused plugins
5. Consider static asset optimization

## Ownership Assignment

| Area | Primary Owner | Backup Owner |
|------|---------------|--------------|
| Content Quality | Documentation Maintainer | Content Author |
| Navigation Structure | Documentation Maintainer | Technical Owner |
| Build Pipeline | Technical Owner | - |
| Theme/Styling | Technical Owner | - |
| Link Validation | Documentation Maintainer | Technical Owner |
| URL Lifecycle | Documentation Maintainer | Technical Owner |

## Escalation Path

1. **Content Issues**: Author → Maintainer → Technical Owner
2. **Build Issues**: Maintainer → Technical Owner → Repository Admin
3. **Infrastructure Issues**: Technical Owner → GitHub Support

## Communication Channels

- **Pull Requests**: Primary channel for content changes
- **Issues**: Bug reports and feature requests
- **Discussions**: Q&A and general documentation topics
- **Workflow Notifications**: GitHub Actions status updates

## Onboarding Checklist

### New Content Author
- [ ] Repository access granted (read/fork)
- [ ] Local development environment setup
- [ ] Markdown style guide reviewed
- [ ] Test pull request submitted and merged
- [ ] Publishing workflow understood

### New Documentation Maintainer
- [ ] Write access granted
- [ ] Merge permissions configured
- [ ] Publishing policies reviewed
- [ ] CI/CD pipeline walkthrough completed
- [ ] Shadow experienced maintainer for one cycle

### New Technical Owner
- [ ] Admin access granted
- [ ] GitHub Pages configuration reviewed
- [ ] Workflow files and dependencies documented
- [ ] Incident response procedures reviewed
- [ ] Emergency contact information shared

## Metrics and KPIs

**Tracked Metrics**:
- Build success rate
- Average build time
- Link check pass rate
- Time from merge to deployment
- Number of 404 errors
- Content update frequency

**Target KPIs**:
- Build success rate: >95%
- Build time: <5 minutes
- Link check pass rate: >98% (internal links 100%)
- Merge to deploy time: <10 minutes
- Monthly 404 rate: <1% of total page views

## Implementation Verification Notes

**Initial Implementation Date**: 2026-04-02

### Verification Results

**Build Validation** ✓ PASS
- Strict build completed successfully: `mkdocs build --strict`
- Build time: 0.61 seconds
- No errors or warnings

**Navigation Validation** ✓ PASS
- Navigation sync check: All files referenced in navigation exist
- All Markdown files included in navigation
- No orphaned documentation pages

**File Structure** ✓ PASS
- All required directories created:
  - `docs/` with subdirectories (guide, maintenance, decisions)
  - `.github/workflows/` with CI/CD workflows
  - `scripts/docs/` with validation scripts
  - `tests/docs/` with test plans
- All documentation files in place

**Configuration** ✓ PASS
- `mkdocs.yml`: Valid YAML, all settings configured
- `requirements-docs.txt`: All dependencies specified
- `.gitignore`: Python/MkDocs patterns configured
- Workflow files: Valid GitHub Actions syntax

**Quality Gates** ✓ PASS
- Strict validation enabled in `mkdocs.yml`
- Link check workflow configured
- Navigation sync integrated into build pipeline
- Redirect plugin configured and ready

**Documentation Completeness** ✓ PASS
- User guides: Getting Started, Publishing Overview
- Maintenance guides: Runbook, Prerequisites, Scope, Lifecycle, Checklist, Troubleshooting
- Governance: ADR 001, Sign-off Template
- Testing: Link Policy, Smoke Check Plan

**Ready for Deployment**: ✓ YES

The documentation publishing system is fully implemented and validated. All quality gates pass. Ready for initial deployment to GitHub Pages.
