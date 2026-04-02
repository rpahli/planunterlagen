# Decision Sign-off Template

Use this template to formally approve architecture decisions and governance changes.

## Decision Information

**Decision ID**: [e.g., ADR-001]  
**Decision Title**: [Brief title]  
**Decision Document**: [Link to decision record]  
**Date Proposed**: [YYYY-MM-DD]

## Summary

[Brief 2-3 sentence summary of what is being decided]

## Impact Assessment

**Affected Systems/Components**:
- [List impacted areas]

**Affected Roles**:
- [List roles impacted by this decision]

**Required Changes**:
- [List implementation changes needed]

**Timeline**:
- Proposed implementation date: [YYYY-MM-DD]
- Review period end: [YYYY-MM-DD]

## Prerequisites Verification

Have all prerequisites been met?

- [ ] Technical prerequisites verified
- [ ] Organizational prerequisites in place
- [ ] Required skills/training available
- [ ] Budget approved (if applicable)
- [ ] Infrastructure ready
- [ ] Stakeholders informed

See [Publishing Prerequisites](../maintenance/publishing-prerequisites.md) for details.

## Risk Assessment

**Identified Risks**:

1. **Risk**: [Description]
   - **Likelihood**: [Low/Medium/High]
   - **Impact**: [Low/Medium/High]
   - **Mitigation**: [Mitigation strategy]

2. **Risk**: [Description]
   - **Likelihood**: [Low/Medium/High]
   - **Impact**: [Low/Medium/High]
   - **Mitigation**: [Mitigation strategy]

**Overall Risk Level**: [Low/Medium/High]

## Approval Authority

This decision requires approval from:

- [ ] Technical Owner
- [ ] Documentation Maintainer
- [ ] Project Lead
- [ ] [Other stakeholder if applicable]

## Sign-off

### Technical Owner

- **Name**: _______________________
- **Date**: _______________________
- **Signature/Approval**: _______________________

**Comments**:


---

### Documentation Maintainer

- **Name**: _______________________
- **Date**: _______________________
- **Signature/Approval**: _______________________

**Comments**:


---

### Project Lead

- **Name**: _______________________
- **Date**: _______________________
- **Signature/Approval**: _______________________

**Comments**:


---

### [Additional Approver]

- **Name**: _______________________
- **Role**: _______________________
- **Date**: _______________________
- **Signature/Approval**: _______________________

**Comments**:


---

## Decision Status

Once all required approvals are received:

- **Final Status**: [ ] Approved / [ ] Rejected / [ ] Deferred
- **Approval Date**: _______________________
- **Effective Date**: _______________________

## Implementation Tracker

After approval, track implementation progress:

| Task | Owner | Target Date | Status | Notes |
|------|-------|-------------|--------|-------|
|      |       |             |        |       |

## Review Schedule

This decision should be reviewed:

- **Next review date**: _______________________
- **Review frequency**: [Annually/Quarterly/As needed]
- **Review owner**: _______________________

## Document History

| Date | Version | Change | Author |
|------|---------|--------|--------|
| YYYY-MM-DD | 1.0 | Initial sign-off request | [Name] |

---

## Instructions for Use

### 1. Preparation

- Create a copy of this template
- Name it: `signoff-[decision-id]-[short-title].md`
- Complete all sections above

### 2. Distribution

- Share with all required approvers
- Set a reasonable review deadline (minimum 5 business days)
- Provide access to full decision document

### 3. Review Period

- Approvers review decision document and prerequisites
- Approvers may request clarifications or changes
- Address feedback and update decision document if needed

### 4. Approval Collection

- Collect approvals via:
  - Digital signature (DocuSign, etc.)
  - Email confirmation (attach to this document)
  - GitHub PR approval (for code-related decisions)
  - In-person sign-off meeting (document in comments)

### 5. Finalization

- Once all approvals received, update status to "Approved"
- Set effective date
- Archive this document with decision record
- Communicate approval to stakeholders
- Begin implementation tracking

### 6. Rejection Handling

If decision is rejected:
- Document reasons in Comments section
- Update status to "Rejected"
- Communicate to stakeholders
- Revisit decision or explore alternatives

### 7. Deferral Handling

If decision is deferred:
- Document reasons and conditions for revisiting
- Set review date for reconsideration
- Communicate deferral to stakeholders

## Example: Abbreviated Sign-off

For minor decisions or when using GitHub PR workflow:

```markdown
## Quick Sign-off (Minor Decision)

**Decision**: [Brief description]
**Approver**: [Name]
**Date**: YYYY-MM-DD
**Method**: GitHub PR #[number] approval

Approved via PR review process. Full decision documented in [link].
```

## Storage and Retention

- Store completed sign-off documents in `docs/decisions/signoffs/`
- Keep for minimum 2 years after decision implementation
- Archive old sign-offs but maintain decision records indefinitely

## Related Documents

- [ADR 001: Publishing Approach](001-publishing-approach.md)
- [Publishing Prerequisites](../maintenance/publishing-prerequisites.md)
- [Publishing Runbook](../maintenance/publishing-runbook.md)
