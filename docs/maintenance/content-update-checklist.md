# Content Update Checklist

This checklist ensures that documentation updates are complete, tested, and properly integrated.

## Before Making Changes

- [ ] **Understand the scope**: Identify which pages need updates
- [ ] **Check for dependencies**: Identify pages that link to the content you're updating
- [ ] **Create a branch**: Work in a feature branch, not directly on main
- [ ] **Review existing content**: Understand the current structure and style

## During Content Creation

### For New Pages

- [ ] **Create Markdown file** in appropriate `docs/` subdirectory
- [ ] **Add frontmatter** if needed (title, description, etc.)
- [ ] **Write clear heading structure** (H1 for title, H2 for sections, etc.)
- [ ] **Add to navigation** in `mkdocs.yml` if page should appear in menu
- [ ] **Link from related pages** to improve discoverability
- [ ] **Follow style guide** for consistent formatting

### For Updated Pages

- [ ] **Preserve existing headings** if possible (to avoid breaking anchor links)
- [ ] **Update related content** that references the changed information
- [ ] **Maintain consistent style** with existing documentation
- [ ] **Document significant changes** in commit message

### For Moved/Renamed Pages

- [ ] **Add redirect rule** in `mkdocs.yml` (see [URL Lifecycle](url-lifecycle.md))
- [ ] **Update navigation** to reflect new location/name
- [ ] **Update all internal links** that reference this page
- [ ] **Test redirect** works correctly
- [ ] **Document change** in URL lifecycle log

### For Deleted Pages

- [ ] **Review deprecation policy** (90-day minimum notice period)
- [ ] **Add deprecation notice** to page before removal
- [ ] **Identify replacement content** if applicable
- [ ] **Update or remove links** to the deleted page
- [ ] **Plan redirect** or custom 404 page
- [ ] **Get maintainer approval** before deletion

## Content Quality Checks

- [ ] **Spell check**: Review for typos and spelling errors
- [ ] **Grammar check**: Ensure clear, professional writing
- [ ] **Link validation**: All links point to valid targets
- [ ] **Code examples**: Test all code snippets if applicable
- [ ] **Images and assets**: Verify all images load and are optimized
- [ ] **Formatting**: Check tables, lists, and code blocks render correctly

## Local Testing

- [ ] **Set up virtual environment** (first time only):
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate  # Linux/Mac
  # OR .venv\Scripts\activate on Windows
  ```
- [ ] **Install dependencies**: `pip install -r requirements-docs.txt`
- [ ] **Start local server**: `mkdocs serve`
- [ ] **Review in browser**: `http://127.0.0.1:8000`
- [ ] **Check navigation**: Verify page appears in correct menu location
- [ ] **Test all links**: Click through internal and external links
- [ ] **Check mobile view**: Ensure responsive design works
- [ ] **Run strict build**: `mkdocs build --strict` (must pass with no warnings)

## Validation

### Required Validations

- [ ] **Strict build passes**: No errors or warnings
- [ ] **Internal links valid**: All internal links resolve
- [ ] **Anchor links valid**: All anchor references exist
- [ ] **Navigation sync**: All nav entries point to existing files
- [ ] **No orphaned pages**: All in-scope pages are reachable

### Recommended Validations

- [ ] **External links valid**: No broken external references
- [ ] **Search works**: New content appears in search results
- [ ] **Table of contents**: Right sidebar TOC is correct
- [ ] **Code highlighting**: Syntax highlighting works for code blocks

## Before Submitting Pull Request

- [ ] **Commit with clear message**: Describe what and why
- [ ] **Push to feature branch**: Not directly to main
- [ ] **Create pull request**: Include description of changes
- [ ] **Add labels**: Tag with `documentation` label
- [ ] **Request review**: Assign to documentation maintainer
- [ ] **Check CI status**: Wait for automated checks to complete

## Pull Request Review

Maintainers should verify:

- [ ] **CI checks pass**: Build and link validation successful
- [ ] **Content accuracy**: Information is correct and current
- [ ] **Style consistency**: Matches existing documentation style
- [ ] **Navigation logic**: New pages in appropriate location
- [ ] **Link quality**: Links are relevant and valid
- [ ] **No scope violations**: Changes respect publishing scope policy

## After Merge

- [ ] **Monitor deployment**: Verify GitHub Actions workflow completes
- [ ] **Check live site**: Confirm changes appear on published site
- [ ] **Test live links**: Verify links work on published site
- [ ] **Update related issues**: Close any related GitHub issues
- [ ] **Announce if significant**: Notify stakeholders of major updates

## Common Issues and Solutions

### Build Fails with "unrecognized link"

**Cause**: Link points to a file not in the navigation or excluded from publishing.

**Solution**: Either add the file to navigation in `mkdocs.yml` or update the link to point to an included page.

### Build Fails with "anchor not found"

**Cause**: Anchor link references a heading that doesn't exist.

**Solution**: Verify the heading exists in the target file and the anchor matches exactly (lowercase, hyphens for spaces).

### Page Not in Navigation

**Cause**: File exists but not added to `mkdocs.yml` nav section.

**Solution**: Add the page to the appropriate section in `mkdocs.yml` navigation.

### Redirect Not Working

**Cause**: Redirect rule syntax error or plugin not configured.

**Solution**: Verify redirect syntax in `mkdocs.yml` and ensure `mkdocs-redirects` plugin is installed.

### Link Check Fails

**Cause**: External link is broken or temporarily unavailable.

**Solution**: Fix the link or add to link policy exemptions if legitimate.

## Quick Reference Commands

```bash
# First time setup: Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# OR .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements-docs.txt

# Start local preview (with venv active)
mkdocs serve

# Build with strict validation
mkdocs build --strict

# Check navigation sync
python scripts/docs/check_nav_sync.py

# Clean build directory
rm -rf site/

# Deactivate virtual environment when done
deactivate

# Check Python version
python --version  # Should be 3.11+
```

**Without activating venv** (alternative):
```bash
# Use full path to executables
.venv/bin/mkdocs serve
.venv/bin/mkdocs build --strict
.venv/bin/python scripts/docs/check_nav_sync.py
```

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Publishing Runbook](publishing-runbook.md)
- [URL Lifecycle Policy](url-lifecycle.md)
