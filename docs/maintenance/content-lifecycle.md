# Content Lifecycle Management

This guide explains how to handle content changes throughout its lifecycle, including creation, updates, moves, renames, and deletion.

## Content Lifecycle States

```
Draft → Published → Updated → (Moved/Renamed) → Deprecated → Removed
                      ↓
                   Archived (optional)
```

## Creating New Content

### 1. Plan the Content

- Identify target audience and purpose
- Determine appropriate location in docs structure
- Check for existing similar content to avoid duplication
- Review publishing scope policy

### 2. Create the File

```bash
# Create new Markdown file
touch docs/section/new-page.md
```

### 3. Add Basic Structure

```markdown
# Page Title

Brief introduction paragraph.

## Section 1

Content here.

## Section 2

More content.
```

### 4. Add to Navigation

Edit `mkdocs.yml`:

```yaml
nav:
  - Section:
      - New Page: section/new-page.md
```

### 5. Link from Related Pages

Update existing pages that should reference the new content.

### 6. Test and Validate

```bash
mkdocs serve        # Preview locally
mkdocs build --strict  # Validate
```

## Updating Existing Content

### Minor Updates (Typos, Clarifications)

1. Edit the file directly
2. Maintain existing heading structure (to preserve anchor links)
3. Test locally
4. Submit PR with clear commit message

### Major Updates (Restructuring, Significant Additions)

1. Review impact on linked content
2. Update or preserve important anchor links
3. Consider adding a "Last Updated" note if significant
4. Update related pages that reference this content
5. Test thoroughly before submitting

### Preserving Anchor Links

If you must change a heading that's linked externally:

**Option 1**: Keep the heading but rephrase content

**Option 2**: Add an HTML anchor to preserve the old link:

```markdown
## New Heading {#old-heading-slug}

Content here.
```

## Moving Content

Moving a file to a different location requires careful handling to preserve URLs.

### Procedure

1. **Before Moving**: Document the current URL and new target URL

2. **Move the file**:
   ```bash
   git mv docs/old/path.md docs/new/path.md
   ```

3. **Update navigation** in `mkdocs.yml`:
   ```yaml
   nav:
     - New Section:
         - Page: new/path.md  # Update path
   ```

4. **Add redirect rule**:

   First, ensure the redirects plugin is installed (see T022).

   Then, add to `mkdocs.yml`:
   ```yaml
   plugins:
     - redirects:
         redirect_maps:
           'old/path.md': 'new/path.md'
   ```

5. **Update internal links**:
   - Search for all references to `old/path.md`
   - Update them to `new/path.md`

6. **Test the redirect**:
   ```bash
   mkdocs serve
   # Visit http://127.0.0.1:8000/old/path/
   # Should redirect to new location
   ```

7. **Document the change** in URL lifecycle log

8. **Test with strict build**:
   ```bash
   mkdocs build --strict
   ```

## Renaming Content

Renaming a page (changing the filename) follows the same process as moving.

### Example

Renaming `getting-started.md` to `quick-start.md`:

1. Move: `git mv docs/guide/getting-started.md docs/guide/quick-start.md`
2. Update nav in `mkdocs.yml`
3. Add redirect: `'guide/getting-started.md': 'guide/quick-start.md'`
4. Update all internal references
5. Test and validate

## Deprecating Content

Before removing content, follow the deprecation process.

### 1. Add Deprecation Notice

Add a prominent notice at the top of the page:

```markdown
!!! warning "Deprecated"
    This documentation is deprecated and will be removed on YYYY-MM-DD.
    Please see [New Page](../new/page.md) for updated information.
```

### 2. Update Navigation

Optionally mark as deprecated in navigation:

```yaml
nav:
  - Old Section:
      - '[DEPRECATED] Old Page': old/page.md
```

### 3. Set Removal Date

**Minimum deprecation period**: 90 days from deprecation notice

### 4. Monitor Usage

If analytics are available, monitor page views to assess impact.

### 5. Communicate

Notify stakeholders of the deprecation through:
- Release notes
- Project updates
- Direct communication if heavily used

## Removing Content

After the deprecation period, content can be removed.

### Pre-Removal Checklist

- [ ] Deprecation period (90 days minimum) has passed
- [ ] Maintainer approval obtained
- [ ] Alternative content is available (if applicable)
- [ ] All internal links updated or removed
- [ ] Redirect rule planned (if preserving URL)
- [ ] Stakeholders notified

### Removal Procedure

1. **Remove from navigation** in `mkdocs.yml`

2. **Delete the file**:
   ```bash
   git rm docs/path/to/page.md
   ```

3. **Handle the URL**:

   **Option A**: Redirect to replacement content:
   ```yaml
   plugins:
     - redirects:
         redirect_maps:
           'old/page.md': 'replacement/page.md'
   ```

   **Option B**: Let it 404 (use MkDocs default 404 page)

4. **Update internal references**:
   - Search for all links to the removed page
   - Remove or update to point to replacement

5. **Document removal** in URL lifecycle log

6. **Test**:
   ```bash
   mkdocs build --strict
   # Should pass with no broken internal links
   ```

7. **Commit with clear message**:
   ```
   Remove deprecated page: old/page.md
   
   - Deprecated on YYYY-MM-DD
   - Redirect to replacement/page.md
   - All internal references updated
   ```

## Archiving Content (Optional)

For historical content that shouldn't be removed but is no longer actively maintained:

### Option 1: Archive Section

Create an "Archive" section in navigation:

```yaml
nav:
  - Archive:
      - Old Version Docs: archive/old-version.md
```

### Option 2: Version Indicator

Add a banner indicating archived status:

```markdown
!!! info "Archived Documentation"
    This documentation is for version X.X and is no longer actively maintained.
    See [Current Documentation](../current/page.md) for the latest information.
```

## Handling Redirects

### Adding a Redirect

In `mkdocs.yml`:

```yaml
plugins:
  - redirects:
      redirect_maps:
        'old-path.md': 'new-path.md'
        'another/old.md': 'another/new.md'
```

### Testing Redirects Locally

```bash
mkdocs serve
# Visit old URL - should redirect to new URL
```

### Redirect Maintenance

- Review redirects quarterly
- Remove redirects after 2 years if traffic is negligible
- Document redirect removal decisions

## URL Lifecycle Log

Maintain a log of significant URL changes in `docs/maintenance/url-lifecycle.md`:

| Date | Old URL | New URL | Type | Reason | Approver |
|------|---------|---------|------|--------|----------|
| 2026-04-02 | guide/start.md | guide/getting-started.md | Rename | Clarity | Maintainer |

## Content Update Workflow Diagram

```
[Author edits content]
         ↓
[Test locally: mkdocs serve]
         ↓
[Validate: mkdocs build --strict]
         ↓
[Create PR]
         ↓
[CI runs build + link check] ─→ [Fails] ─→ [Fix issues]
         ↓                                        ↓
      [Passes]                                    ↑
         ↓                                        │
[Maintainer reviews] ─→ [Request changes] ───────┘
         ↓
[Approve and merge]
         ↓
[Auto-deploy to GitHub Pages]
         ↓
[Verify on live site]
```

## Common Scenarios

### Scenario 1: Fix a Typo

1. Edit file
2. Run `mkdocs build --strict`
3. Submit PR
4. Merge after CI passes

### Scenario 2: Add a New Guide

1. Create `docs/guide/new-guide.md`
2. Add to navigation in `mkdocs.yml`
3. Link from `docs/index.md` or related pages
4. Test with `mkdocs serve`
5. Validate with `mkdocs build --strict`
6. Submit PR

### Scenario 3: Reorganize a Section

1. Plan new structure
2. Move files with `git mv`
3. Update navigation in `mkdocs.yml`
4. Add redirect rules for all moved files
5. Update all internal references
6. Test redirects locally
7. Validate with strict build
8. Submit PR with detailed description
9. Document in URL lifecycle log

### Scenario 4: Remove Outdated Content

1. Add deprecation notice (90 days before removal)
2. Update navigation to mark deprecated
3. Wait 90 days
4. Remove file and navigation entry
5. Add redirect or let it 404
6. Update internal references
7. Document in URL lifecycle log
8. Submit PR

## Resources

- [Content Update Checklist](content-update-checklist.md)
- [URL Lifecycle Policy](url-lifecycle.md)
- [Publishing Runbook](publishing-runbook.md)
- [MkDocs Documentation](https://www.mkdocs.org/)
