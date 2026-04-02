# Planunterlagen

Documentation and analysis for planning documents, focusing on transparent review and stakeholder engagement processes.

## Documentation Site

The project documentation is published to GitHub Pages: [https://rpahli.github.io/planunterlagen/](https://rpahli.github.io/planunterlagen/)

## Local Documentation Preview

To preview the documentation site locally:

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Setup

#### Option 1: Using Virtual Environment (Recommended)

Create and activate a virtual environment to isolate documentation dependencies:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On Linux/Mac:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements-docs.txt
```

When finished, deactivate the virtual environment:

```bash
deactivate
```

#### Option 2: System-wide Installation

If you prefer system-wide installation (not recommended on managed systems):

```bash
pip install -r requirements-docs.txt
```

**Note**: On some Linux distributions (e.g., Debian, Ubuntu), you may need to use a virtual environment due to PEP 668 externally-managed environment restrictions.

### Local Server

Start the local development server:

**With virtual environment active**:
```bash
mkdocs serve
```

**Or directly**:
```bash
.venv/bin/mkdocs serve  # Linux/Mac
.venv\Scripts\mkdocs serve  # Windows
```

The documentation will be available at `http://127.0.0.1:8000`

Changes to Markdown files will automatically reload in the browser.

### Build Validation

Before submitting changes, validate the documentation build:

**With virtual environment active**:
```bash
mkdocs build --strict
```

**Or directly**:
```bash
.venv/bin/mkdocs build --strict  # Linux/Mac
.venv\Scripts\mkdocs build --strict  # Windows
```

This command will:
- Build the static site to `site/` directory
- Validate all internal links
- Check for broken references
- Fail if any warnings or errors are found

### Navigation Sync Check

Verify navigation references match actual files:

```bash
python scripts/docs/check_nav_sync.py
# Or with venv: .venv/bin/python scripts/docs/check_nav_sync.py
```

## Contributing to Documentation

1. Fork or create a branch
2. Edit Markdown files in the `docs/` directory
3. Test locally with `mkdocs serve`
4. Validate with `mkdocs build --strict`
5. Submit a pull request

For more details, see the [Publishing Runbook](docs/maintenance/publishing-runbook.md).

## Project Structure

```
planunterlagen/
├── docs/                       # Documentation source (Markdown)
│   ├── index.md               # Home page
│   ├── guide/                 # User guides
│   ├── maintenance/           # Maintainer documentation
│   └── stylesheets/           # Custom CSS
├── mkdocs.yml                 # MkDocs configuration
├── requirements-docs.txt      # Documentation dependencies
├── .github/workflows/         # CI/CD workflows
│   ├── docs-pages.yml        # Build and deploy to GitHub Pages
│   └── docs-link-check.yml   # Automated link validation
├── specs/                     # Feature specifications
└── analyse_stellungnahmen_solarpark/  # Analysis artifacts
```

## CI/CD

Documentation is automatically built and deployed to GitHub Pages when changes are pushed to the `main` branch.

- **Build and Deploy**: `.github/workflows/docs-pages.yml`
- **Link Validation**: `.github/workflows/docs-link-check.yml` (runs on PRs and weekly)

## Technology Stack

- **Static Site Generator**: [MkDocs](https://www.mkdocs.org/) 1.6+
- **Theme**: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 9+
- **Hosting**: GitHub Pages
- **CI/CD**: GitHub Actions

## License

[Add license information here]
