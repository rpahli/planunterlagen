# URL Lifecycle and Depublication Policy

## Purpose

Ensure stable URLs and graceful handling of content moves, renames, and deletions.

## URL Stability Principles

1. **URLs are public contracts**: Once published, URLs should remain accessible
2. **Redirects over breaking**: Moving content requires redirect rules
3. **Deprecation before removal**: Mark content as deprecated before removing
4. **Communication**: Document all URL changes in release notes

## Content Lifecycle States

### Published

- Content is live and accessible
- URL is stable and indexed
- Regular maintenance and updates

### Moved/Renamed

- Original URL redirects to new location
- Redirect rule documented in `mkdocs.yml`
- Old URL remains accessible (301 redirect)

### Deprecated

- Content marked with deprecation notice
- Warning banner added to page
- Redirect rule planned for future
- Minimum 90 days before removal

### Removed

- Content deleted from repository
- 404 page with helpful context
- Search engines notified (sitemap update)
- Documented in deprecation log

## URL Change Procedures

### Moving a Page

1. Move the Markdown file to new location
2. Add redirect rule in `mkdocs.yml` (using redirects plugin)
3. Update all internal links to use new URL
4. Test with `mkdocs build --strict`
5. Document change in release notes

Example redirect configuration:
```yaml
plugins:
  - redirects:
      redirect_maps:
        'old/path.md': 'new/path.md'
```

### Renaming a Page

1. Rename the Markdown file
2. Add redirect rule from old name to new name
3. Update navigation in `mkdocs.yml`
4. Update internal references
5. Verify with link checker

### Removing a Page

1. Add deprecation notice to page (minimum 90 days)
2. Update navigation to mark as deprecated
3. After deprecation period:
   - Remove file
   - Add custom 404 handler if needed
   - Update sitemap
   - Document removal in deprecation log

## Redirect Rules Management

### Redirect Plugin Configuration

```yaml
plugins:
  - redirects:
      redirect_maps:
        # Format: 'old-path.md': 'new-path.md'
        # Add new redirects here
```

### Redirect Testing

Before deploying redirects:

1. Test locally with `mkdocs serve`
2. Verify old URL shows redirect
3. Verify new URL loads correctly
4. Check that internal links update

### Redirect Maintenance

- Review redirect rules quarterly
- Remove redirects older than 2 years if traffic is negligible
- Document redirect removal decisions

## Depublication Checklist

Before removing any published content:

- [ ] Deprecation notice added (90 days minimum)
- [ ] Maintainer approval obtained
- [ ] Alternative content identified (if applicable)
- [ ] Redirect rule planned and tested
- [ ] Internal references updated
- [ ] Release notes drafted
- [ ] Analytics reviewed for traffic impact

## URL Lifecycle Log

Maintain a log of significant URL changes:

| Date | Old URL | New URL | Type | Reason | Approver |
|------|---------|---------|------|--------|----------|
| TBD  | -       | -       | -    | -      | -        |

## External References

If the documentation is referenced externally:

1. Maintain redirects for at least 2 years
2. Notify known external sites of URL changes
3. Monitor inbound traffic to detect broken references
4. Provide canonical URL guidance in documentation

## Monitoring

- Track 404 errors in deployment logs
- Review redirect usage in analytics
- Monitor search engine indexing changes
- Alert on unexpected URL access patterns
