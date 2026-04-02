# Documentation Smoke Check Plan

This document defines smoke tests to verify that the documentation site is functioning correctly after deployment.

## Purpose

Smoke tests provide quick validation that:
- The site is accessible
- Core navigation works
- Critical pages load
- Search functions
- Links resolve correctly

## When to Run Smoke Checks

### Required

- **After every deployment** to GitHub Pages
- **After major configuration changes** (theme, plugins, navigation)
- **After dependency updates** (MkDocs, Material, plugins)

### Recommended

- **Weekly scheduled check** (automated or manual)
- **Before announcing documentation to stakeholders**
- **After large content additions or reorganizations**

## Manual Smoke Check Procedure

### 1. Site Accessibility (Critical)

**Test**: Can the site be accessed?

**Steps**:
1. Open browser
2. Navigate to: `https://rpahli.github.io/planunterlagen/`
3. Verify page loads without errors

**Expected**: Home page loads successfully (200 OK)

**Failure**: If site doesn't load, check:
- GitHub Pages deployment status
- DNS configuration (if custom domain)
- Repository Pages settings

### 2. Home Page Content (Critical)

**Test**: Does the home page display expected content?

**Steps**:
1. Verify page title: "Planunterlagen Documentation"
2. Check main sections appear:
   - What is Planunterlagen?
   - Quick Links
   - Documentation Structure
3. Verify no rendering errors

**Expected**: All content renders correctly with proper formatting

**Failure**: If content missing or broken:
- Check `docs/index.md` in repository
- Rebuild site locally to reproduce
- Review build logs for errors

### 3. Navigation (Critical)

**Test**: Does the navigation menu work?

**Steps**:
1. Verify top-level navigation tabs appear:
   - Home
   - Guide
   - Maintenance
   - Decisions
2. Click each tab and verify it expands/navigates
3. Click on subsection items (e.g., "Getting Started")
4. Verify page loads correctly

**Expected**: All navigation items are clickable and load correct pages

**Failure**: If navigation broken:
- Check `mkdocs.yml` navigation structure
- Verify all referenced files exist
- Run navigation sync checker

### 4. Search Functionality (Critical)

**Test**: Does search work?

**Steps**:
1. Click search icon or press `/` key
2. Type a search term (e.g., "publishing")
3. Verify results appear
4. Click on a result
5. Verify it navigates to correct page with highlighting

**Expected**: Search returns relevant results and navigates correctly

**Failure**: If search broken:
- Check search plugin enabled in `mkdocs.yml`
- Clear browser cache and retry
- Rebuild search index

### 5. Internal Links (Critical)

**Test**: Do internal links resolve?

**Steps**:
1. Navigate to "Getting Started" page
2. Click on internal links (e.g., "Publishing Overview")
3. Verify links navigate to correct pages
4. Test anchor links (links to headings on same page)
5. Verify anchor links scroll to correct section

**Expected**: All internal links work and navigate correctly

**Failure**: If links broken:
- Review link check CI results
- Run `mkdocs build --strict` locally
- Check for recent file moves without redirects

### 6. Code Blocks (High)

**Test**: Do code blocks render with syntax highlighting?

**Steps**:
1. Navigate to page with code examples (e.g., "Publishing Overview")
2. Verify code blocks have syntax highlighting
3. Check copy button appears on hover
4. Click copy button and verify it works

**Expected**: Code blocks render with highlighting and copy button works

**Failure**: If highlighting broken:
- Check markdown_extensions in `mkdocs.yml`
- Verify theme version supports features
- Test in different browser

### 7. Theme and Styling (Medium)

**Test**: Does the site look correct?

**Steps**:
1. Verify color scheme loads (check primary/accent colors)
2. Test dark/light mode toggle (if enabled)
3. Check custom CSS applies (`docs/stylesheets/extra.css`)
4. Verify responsive design on mobile (resize browser)
5. Check footer content displays

**Expected**: Theme renders correctly with all customizations

**Failure**: If styling broken:
- Check `extra.css` syntax
- Verify CSS file path in `mkdocs.yml`
- Clear browser cache
- Review theme configuration

### 8. External Links (Low)

**Test**: Do external links work? (Sample check)

**Steps**:
1. Find page with external links
2. Click 2-3 external links
3. Verify they open and work

**Expected**: External links open to valid destinations

**Failure**: If external links broken:
- Check link check CI logs for failures
- Update broken links
- Consider adding to exemptions if temporary

## Automated Smoke Check (Optional)

For automated smoke testing, consider using Playwright:

### Example Playwright Test

```javascript
// tests/smoke.spec.js
const { test, expect } = require('@playwright/test');

test('home page loads', async ({ page }) => {
  await page.goto('https://rpahli.github.io/planunterlagen/');
  await expect(page).toHaveTitle(/Planunterlagen Documentation/);
});

test('navigation works', async ({ page }) => {
  await page.goto('https://rpahli.github.io/planunterlagen/');
  await page.click('text=Getting Started');
  await expect(page).toHaveURL(/.*guide\/getting-started/);
});

test('search works', async ({ page }) => {
  await page.goto('https://rpahli.github.io/planunterlagen/');
  await page.press('body', '/');
  await page.fill('input[type="search"]', 'publishing');
  await page.waitForSelector('.md-search-result');
  const results = await page.locator('.md-search-result__item').count();
  expect(results).toBeGreaterThan(0);
});
```

### Running Automated Tests

```bash
npm install -D @playwright/test
npx playwright install
npx playwright test tests/smoke.spec.js
```

## Smoke Check Checklist

Use this checklist after each deployment:

- [ ] Site accessible at published URL
- [ ] Home page loads with correct content
- [ ] All navigation tabs and sections work
- [ ] Search functionality works
- [ ] Internal links navigate correctly
- [ ] Anchor links scroll to correct sections
- [ ] Code blocks render with syntax highlighting
- [ ] Theme and styling appear correct
- [ ] Dark/light mode toggle works (if enabled)
- [ ] Mobile responsive design works
- [ ] External links work (sample check)

## Critical Path Pages

These pages must always be accessible:

1. **Home** (`/`)
2. **Getting Started** (`/guide/getting-started/`)
3. **Publishing Overview** (`/guide/publishing-overview/`)
4. **Publishing Runbook** (`/maintenance/publishing-runbook/`)
5. **ADR 001** (`/decisions/001-publishing-approach/`)

Verify these pages specifically after every deployment.

## Smoke Check Results

Document results for tracking:

| Date | Result | Failures | Notes |
|------|--------|----------|-------|
| YYYY-MM-DD | PASS/FAIL | List any failures | Additional context |

## Failure Response

If smoke check fails:

1. **Document failure**: Record what failed and how
2. **Assess severity**:
   - **Critical**: Site down, navigation broken, security issue → Fix immediately
   - **High**: Core features broken → Fix within 24 hours
   - **Medium**: Minor issues → Fix in next update
   - **Low**: Cosmetic issues → Add to backlog
3. **Rollback if needed**: Revert to last known good deployment
4. **Fix and redeploy**: Address issue and redeploy
5. **Re-run smoke check**: Verify fix works
6. **Post-mortem**: Document cause and prevention for future

## Integration with CI/CD

Consider adding automated smoke checks to deployment workflow:

```yaml
# In .github/workflows/docs-pages.yml
- name: Smoke Check (Optional)
  run: |
    # Wait for Pages deployment
    sleep 60
    # Run basic checks
    curl -f https://rpahli.github.io/planunterlagen/ || exit 1
```

## Monitoring and Alerts

For production documentation sites, consider:

- **Uptime monitoring**: Pingdom, UptimeRobot, StatusCake
- **Broken link monitoring**: Weekly link check CI runs
- **Analytics**: Google Analytics or similar for traffic monitoring
- **Error tracking**: GitHub Pages deployment logs

## Review and Updates

This smoke check plan should be reviewed:

- **After adding major features**: Update checks to cover new functionality
- **Quarterly**: Ensure checks remain relevant and comprehensive
- **After incidents**: Add checks to prevent recurrence

## Resources

- [Playwright Testing](https://playwright.dev/)
- [GitHub Pages Status](https://www.githubstatus.com/)
- [MkDocs Deployment](https://www.mkdocs.org/user-guide/deploying-your-docs/)
- [Publishing Runbook](../../docs/maintenance/publishing-runbook.md)
