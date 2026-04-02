# Link Check Policy and Thresholds

## Purpose

Define validation rules and acceptable thresholds for internal and external links in the documentation.

## Link Validation Rules

### Internal Links

**Requirement**: All internal links MUST resolve successfully.

- Internal relative links (e.g., `[guide](../guide/index.md)`)
- Internal anchor links (e.g., `[section](#overview)`)
- Navigation references in `mkdocs.yml`

**Threshold**: 0 broken internal links allowed (strict enforcement)

### External Links

**Requirement**: External links SHOULD be valid and accessible.

- HTTP/HTTPS links to external resources
- Repository links (GitHub, GitLab, etc.)
- Documentation references

**Thresholds**:
- **Error threshold**: < 5% broken external links
- **Warning threshold**: < 10% slow-response external links (>5s)

### Anchor Links

**Requirement**: All anchor references MUST exist in target documents.

**Threshold**: 0 broken anchor links allowed

## Validation Tools

- **MkDocs built-in**: Validates internal links and anchors during `mkdocs build --strict`
- **Lychee**: Validates both internal and external links in CI

## Link Check Execution

### On Every Build

- Internal link validation (strict)
- Anchor validation (strict)

### On Pull Requests

- Full link validation including external links
- Performance check for external link response times

### Scheduled Checks

- Weekly full external link validation
- Report broken external links for maintainer review

## Exemptions

### Allowed Failures

External links may be exempted if:

1. The external site is temporarily unavailable but known to be reliable
2. The link requires authentication
3. The link is behind a firewall or VPN

Exemptions must be documented with:
- URL pattern
- Reason for exemption
- Date of exemption
- Reviewer approval

## Link Policy Violations

### Critical (Block Deployment)

- Broken internal links
- Broken anchor references
- Navigation pointing to non-existent pages

### Warning (Allow Deployment, Require Fix)

- Broken external links (under threshold)
- Slow external links
- Redirected links (should update to final URL)

## Maintenance

This policy should be reviewed:

- After any major documentation restructuring
- Quarterly for threshold adjustments
- When link check tool versions are upgraded
