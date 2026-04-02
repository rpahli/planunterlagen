# Getting Started

Welcome to the Planunterlagen documentation! This guide will help you navigate and make the most of this documentation site.

## Navigating the Documentation

The documentation is organized into logical sections accessible from the top navigation bar:

- **Home**: Overview and quick links
- **Guide**: User guides and tutorials
- **Maintenance**: Operational documentation for maintainers

### Using the Search Function

Use the search bar at the top of the page to quickly find specific topics, keywords, or pages. The search supports:

- Full-text search across all documentation pages
- Keyword highlighting in results
- Instant suggestions as you type

### Navigation Menu

The left sidebar provides hierarchical navigation through all documentation sections. Click on section headers to expand or collapse subsections.

## Reading Documentation

### Page Structure

Each documentation page includes:

- **Title**: Clear page heading
- **Table of Contents**: Right sidebar for quick navigation within the page
- **Content**: Main documentation content with headings, lists, code blocks, and diagrams
- **Permalinks**: Hover over headings to get permanent links to specific sections

### Code Blocks

Code examples include a copy button in the top-right corner for easy copying:

```bash
# Example command
mkdocs serve
```

### Admonitions and Callouts

Important information is highlighted with colored callouts:

!!! note
    This is a note with additional information.

!!! warning
    This is a warning about potential issues.

!!! tip
    This is a helpful tip or best practice.

## For Content Authors

If you're contributing to the documentation:

1. Review the [Publishing Overview](publishing-overview.md) to understand the publishing workflow
2. Check the [Publishing Runbook](../maintenance/publishing-runbook.md) for roles and procedures
3. Set up your local development environment (see below)

### Local Development Setup

To preview documentation locally, first set up your environment:

#### Step 1: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # Linux/Mac
# OR
.venv\Scripts\activate  # Windows
```

!!! tip "Why use a virtual environment?"
    Virtual environments isolate documentation dependencies from your system Python, preventing conflicts and ensuring reproducible builds.

#### Step 2: Install Dependencies

```bash
# Install all required packages
pip install -r requirements-docs.txt
```

This installs:
- MkDocs (static site generator)
- Material for MkDocs (theme)
- mkdocs-redirects (URL management)
- PyYAML (configuration parsing)

#### Step 3: Start Local Server

```bash
# Start development server
mkdocs serve
```

Visit `http://127.0.0.1:8000` to preview your changes.

The server will automatically reload when you save Markdown files.

#### Step 4: Validate Changes

Before submitting a pull request:

```bash
# Run strict build (catches all warnings)
mkdocs build --strict

# Check navigation sync
python scripts/docs/check_nav_sync.py
```

#### Deactivate Virtual Environment

When finished:

```bash
deactivate
```

#### Troubleshooting

**"Command not found" errors**:
- Ensure virtual environment is activated
- Or use full path: `.venv/bin/mkdocs serve`

**"Externally managed environment" error**:
- You must use a virtual environment (your system requires it)
- Follow Step 1 above

**Port 8000 already in use**:
- Stop other mkdocs instance: `pkill -f mkdocs`
- Or use different port: `mkdocs serve -a 127.0.0.1:8001`

## Getting Help

### Documentation Issues

If you find errors, broken links, or unclear content:

1. Check if the issue is already reported in the repository issues
2. Create a new issue with details about the problem
3. Tag it with the `documentation` label

### Feature Requests

To suggest improvements or new documentation:

1. Open a GitHub issue describing the proposed documentation
2. Tag it with `documentation` and `enhancement`
3. Discuss with maintainers before creating large documentation additions

## Next Steps

- Explore the [Publishing Overview](publishing-overview.md) to understand how this site is built and maintained
- Review operational guides in the [Maintenance](../maintenance/publishing-runbook.md) section
- Check out decision records to understand architectural choices
