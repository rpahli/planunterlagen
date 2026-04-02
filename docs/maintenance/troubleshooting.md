# Documentation Troubleshooting Guide

This guide helps diagnose and resolve common issues with the documentation publishing system.

## Build Failures

### Error: "strict mode: 'FILE.md' not found in navigation"

**Symptom**: Build fails with message about files not in navigation.

**Cause**: MkDocs strict mode requires all files to be referenced in `mkdocs.yml` navigation.

**Solutions**:

1. **Add to navigation**:
   ```yaml
   nav:
     - Section:
         - Page Title: path/to/FILE.md
   ```

2. **Move file out of docs/** if not intended for publication

3. **Exclude from validation** (not recommended):
   ```yaml
   validation:
     omitted_files: ignore  # Change from 'warn'
   ```

### Error: "unrecognized link"

**Symptom**: Build fails with "WARNING: Unrecognized link: FILE.md"

**Cause**: Link points to a file that's not included in the documentation or doesn't exist.

**Solutions**:

1. **Fix the link** to point to an existing, included file
2. **Add the target file** to navigation if it should be included
3. **Use absolute URL** if linking to external resource

### Error: "anchor not found"

**Symptom**: Build fails with "WARNING: Anchor '#heading' not found"

**Cause**: Link references a heading/anchor that doesn't exist in the target file.

**Solutions**:

1. **Check heading exists** in target file
2. **Verify anchor format**: Use lowercase, hyphens for spaces
   - Heading: `## My Section Title`
   - Anchor: `#my-section-title`
3. **Check for special characters**: Some characters are stripped from anchors

**Example**:
```markdown
# Correct
[Link to section](page.md#my-heading)

# Incorrect (uppercase, spaces)
[Link to section](page.md#My Heading)
```

### Error: "Config file 'mkdocs.yml' is invalid"

**Symptom**: Build fails immediately with YAML syntax error.

**Cause**: Invalid YAML syntax in `mkdocs.yml`.

**Solutions**:

1. **Check indentation**: YAML requires consistent spacing (use 2 spaces)
2. **Validate YAML syntax** with online validator or `python -m yaml`
3. **Check for unquoted special characters**: `:`, `#`, `-`, etc.
4. **Ensure proper list formatting**

**Example**:
```yaml
# Correct
nav:
  - Home: index.md
  - Guide:
      - Getting Started: guide/start.md

# Incorrect (inconsistent indentation)
nav:
  - Home: index.md
  - Guide:
    - Getting Started: guide/start.md
```

### Error: "Could not import extension"

**Symptom**: Build fails with "ModuleNotFoundError" or "Could not import extension"

**Cause**: Missing Python dependency or plugin.

**Solutions**:

1. **Reinstall dependencies**:
   ```bash
   pip install -r requirements-docs.txt
   ```

2. **Check plugin is listed** in `requirements-docs.txt`

3. **Verify Python version**:
   ```bash
   python --version  # Should be 3.11+
   ```

## Link Check Failures

### External Links Failing

**Symptom**: Link checker reports broken external links.

**Diagnosis**:

1. **Test link manually** in browser
2. **Check if site is temporarily down**
3. **Verify URL is still valid** (site may have moved)

**Solutions**:

1. **Update link** to correct URL if site moved
2. **Add to exemptions** in link policy if site is known reliable but temporarily down
3. **Replace with archive.org link** if site is permanently gone
4. **Remove link** if no longer relevant

### Internal Links Failing

**Symptom**: Link checker or build reports broken internal links.

**Cause**: File moved, renamed, or deleted without updating references.

**Solutions**:

1. **Find all references** to the broken link:
   ```bash
   grep -r "old-file.md" docs/
   ```

2. **Update all references** to new file path

3. **Add redirect** if file was moved:
   ```yaml
   plugins:
     - redirects:
         redirect_maps:
           'old/path.md': 'new/path.md'
   ```

## Local Development Issues

### "mkdocs: command not found"

**Symptom**: Cannot run `mkdocs` commands.

**Cause**: MkDocs not installed or not in PATH.

**Solutions**:

1. **Create and activate virtual environment** (if not already done):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # OR .venv\Scripts\activate on Windows
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements-docs.txt
   ```

3. **Verify installation**:
   ```bash
   mkdocs --version
   # Should show: mkdocs, version 1.6.x
   ```

4. **Alternative: Use full path** (without activating venv):
   ```bash
   .venv/bin/mkdocs --version  # Linux/Mac
   .venv\Scripts\mkdocs --version  # Windows
   ```

### "externally-managed-environment" error

**Symptom**: `pip install` fails with "error: externally-managed-environment".

**Cause**: System Python is protected (PEP 668) and doesn't allow global package installation.

**Solution**: **Must use virtual environment**:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # Linux/Mac
# OR .venv\Scripts\activate on Windows

# Now install works
pip install -r requirements-docs.txt
```

!!! warning "Do NOT use --break-system-packages"
    Never use `pip install --break-system-packages`. This can damage your system Python installation. Always use a virtual environment instead.

### "Port 8000 already in use"

**Symptom**: `mkdocs serve` fails with "Address already in use".

**Cause**: Another process is using port 8000.

**Solutions**:

1. **Stop other mkdocs instance**:
   ```bash
   pkill -f mkdocs
   ```

2. **Use different port**:
   ```bash
   mkdocs serve -a 127.0.0.1:8001
   ```

3. **Find process using port**:
   ```bash
   lsof -i :8000  # Linux/Mac
   netstat -ano | findstr :8000  # Windows
   ```

### Changes Not Reflecting in Browser

**Symptom**: Edit files but changes don't appear in `mkdocs serve`.

**Solutions**:

1. **Hard refresh browser**: Ctrl+Shift+R (or Cmd+Shift+R on Mac)
2. **Check file is saved**
3. **Restart mkdocs serve**
4. **Clear browser cache**
5. **Check correct URL**: Should be `http://127.0.0.1:8000`

### Virtual Environment Issues

#### Virtual Environment Not Activating

**Symptom**: `source .venv/bin/activate` doesn't work or shows errors.

**Solutions**:

1. **Check venv was created**:
   ```bash
   ls -la .venv/  # Should show bin/, lib/, etc.
   ```

2. **Recreate if corrupted**:
   ```bash
   rm -rf .venv/
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-docs.txt
   ```

3. **Windows activation** (different command):
   ```bash
   .venv\Scripts\activate
   ```

#### Wrong Python Version in Virtual Environment

**Symptom**: `python --version` shows wrong version inside venv.

**Solution**: Create venv with specific Python version:

```bash
# Use python3.11 specifically
python3.11 -m venv .venv

# Or specify full path
/usr/bin/python3.11 -m venv .venv
```

#### Packages Not Found After Installation

**Symptom**: Installed packages but still get "ModuleNotFoundError".

**Cause**: Installing in wrong environment or venv not activated.

**Solutions**:

1. **Verify venv is active** (prompt should show `(.venv)`):
   ```bash
   which python  # Should show .venv/bin/python
   ```

2. **Reinstall in correct venv**:
   ```bash
   source .venv/bin/activate
   pip install -r requirements-docs.txt
   ```

3. **Check installation location**:
   ```bash
   pip show mkdocs
   # Location should be inside .venv/
   ```

## GitHub Actions / CI Failures

### Workflow: "Build documentation" step fails

**Symptom**: CI pipeline fails at build step.

**Diagnosis**: Check workflow logs for specific error.

**Solutions**:

1. **Reproduce locally**:
   ```bash
   mkdocs build --strict
   ```

2. **Fix build errors** (see Build Failures section above)

3. **Test fix locally** before pushing

### Workflow: "Check navigation sync" step fails

**Symptom**: Navigation sync check fails in CI.

**Cause**: Navigation references don't match actual files.

**Solutions**:

1. **Run locally**:
   ```bash
   python scripts/docs/check_nav_sync.py
   ```

2. **Fix reported issues**:
   - Add missing files to navigation
   - Remove broken navigation references
   - Update navigation paths after file moves

### Workflow: "Link Checker" step fails

**Symptom**: Link validation fails in CI.

**Solutions**:

1. **Review link check logs** for specific broken links

2. **Fix broken links** (see Link Check Failures above)

3. **Exempt known issues** in link policy if appropriate

### Workflow: "Deploy to GitHub Pages" step fails

**Symptom**: Deployment fails after successful build.

**Diagnosis**:

1. **Check GitHub Pages settings** in repository
2. **Verify workflow permissions**: needs `pages: write`, `id-token: write`
3. **Check repository quota**: Pages builds have size/time limits

**Solutions**:

1. **Enable GitHub Pages** in repository settings
2. **Set source to GitHub Actions** in Pages settings
3. **Verify deployment permissions** in workflow file
4. **Contact GitHub Support** if infrastructure issue

## Performance Issues

### Slow Build Times

**Symptom**: `mkdocs build` takes longer than expected.

**Diagnosis**:

1. **Measure build time**:
   ```bash
   time mkdocs build
   ```

2. **Check number of files**:
   ```bash
   find docs/ -name "*.md" | wc -l
   ```

**Solutions**:

1. **Optimize images**: Compress large images
2. **Review plugins**: Disable unused plugins
3. **Clean build directory**:
   ```bash
   rm -rf site/
   mkdocs build
   ```

### Slow Page Load Times

**Symptom**: Published site loads slowly.

**Diagnosis**: Use browser DevTools Network tab to identify slow resources.

**Solutions**:

1. **Optimize images**: Use appropriate formats and sizes
2. **Minimize custom CSS**: Review `docs/stylesheets/extra.css`
3. **Check for large files**: Move large downloads out of site assets
4. **Use GitHub Pages CDN**: Already enabled by default

## Navigation Issues

### Page Not Appearing in Menu

**Symptom**: Page exists but doesn't show in navigation.

**Cause**: Not added to `mkdocs.yml` navigation.

**Solution**: Add to navigation:

```yaml
nav:
  - Section:
      - Page Title: path/to/page.md
```

### Navigation Order Wrong

**Symptom**: Pages appear in unexpected order.

**Cause**: MkDocs uses order defined in `mkdocs.yml`, not filesystem.

**Solution**: Reorder entries in `mkdocs.yml`:

```yaml
nav:
  - First Page: first.md
  - Second Page: second.md
  - Third Page: third.md
```

### Nested Navigation Not Expanding

**Symptom**: Subsections don't expand in navigation.

**Solutions**:

1. **Enable navigation expand**:
   ```yaml
   theme:
     features:
       - navigation.expand
   ```

2. **Check navigation structure**: Ensure proper nesting

## Search Issues

### Search Not Finding Content

**Symptom**: Search doesn't return expected results.

**Cause**: Search index may not include all content.

**Solutions**:

1. **Rebuild site**:
   ```bash
   rm -rf site/
   mkdocs build --strict
   ```

2. **Check search plugin enabled**:
   ```yaml
   plugins:
     - search
   ```

3. **Clear browser cache** and retry

### Search Not Working at All

**Symptom**: Search box present but non-functional.

**Solutions**:

1. **Check browser console** for JavaScript errors
2. **Verify search plugin** in `mkdocs.yml`
3. **Test in different browser**
4. **Rebuild site**

## Theme and Styling Issues

### Custom CSS Not Applied

**Symptom**: Changes to `docs/stylesheets/extra.css` not visible.

**Solutions**:

1. **Verify CSS file referenced**:
   ```yaml
   extra_css:
     - stylesheets/extra.css
   ```

2. **Check file path** is correct (relative to `docs/`)

3. **Hard refresh browser**: Ctrl+Shift+R

4. **Rebuild site**:
   ```bash
   mkdocs build --strict
   ```

### Theme Features Not Working

**Symptom**: Enabled theme features don't appear.

**Solutions**:

1. **Check feature name** in Material docs
2. **Verify Material version**:
   ```bash
   pip show mkdocs-material
   ```
3. **Update Material** if needed:
   ```bash
   pip install --upgrade mkdocs-material
   ```

## Getting Help

### When to Escalate

Escalate to Technical Owner if:

- Issue persists after troubleshooting
- Infrastructure problem suspected
- Dependency update needed
- Security concern identified

### How to Report Issues

When reporting problems:

1. **Include exact error message**
2. **Provide steps to reproduce**
3. **Share relevant logs** (build output, workflow logs)
4. **Note what you've already tried**
5. **Specify environment** (Python version, OS, etc.)

### Useful Debug Commands

```bash
# Check Python version
python --version

# Check MkDocs version
mkdocs --version

# Check installed packages
pip list | grep mkdocs

# Validate mkdocs.yml syntax
python -c "import yaml; yaml.safe_load(open('mkdocs.yml'))"

# Test navigation sync
python scripts/docs/check_nav_sync.py

# Build with verbose output
mkdocs build --strict --verbose

# Check for broken links (requires lychee)
lychee docs/**/*.md
```

## Common Workflows

### After Moving a File

```bash
# 1. Update all references
grep -r "old-name.md" docs/

# 2. Update navigation in mkdocs.yml
# Edit mkdocs.yml

# 3. Add redirect
# Edit mkdocs.yml plugins.redirects section

# 4. Test
mkdocs build --strict
mkdocs serve
```

### After Dependency Update

```bash
# 1. Update requirements-docs.txt
# Edit file with new versions

# 2. Install updates
pip install -r requirements-docs.txt --upgrade

# 3. Test build
mkdocs build --strict

# 4. Check for deprecation warnings
mkdocs build --strict --verbose

# 5. Update docs if breaking changes
```

### Quick Reset (Nuclear Option)

```bash
# Clean everything and start fresh
rm -rf site/ .cache/
pip uninstall -y mkdocs mkdocs-material mkdocs-redirects
pip install -r requirements-docs.txt
mkdocs build --strict
```

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs GitHub Issues](https://github.com/mkdocs/mkdocs/issues)
- [Material GitHub Issues](https://github.com/squidfunk/mkdocs-material/issues)
- [Publishing Runbook](publishing-runbook.md)
