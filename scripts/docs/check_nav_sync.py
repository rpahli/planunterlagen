#!/usr/bin/env python3
"""
Navigation Sync Checker

Validates that navigation entries in mkdocs.yml point to existing files
and that no markdown files are orphaned (not reachable via navigation).

Usage:
    python scripts/docs/check_nav_sync.py

Exit codes:
    0: All checks passed
    1: Validation errors found
"""

import os
import sys
from pathlib import Path
from typing import List, Set, Tuple
import yaml


def load_mkdocs_config(config_path: Path) -> dict:
    """Load and parse mkdocs.yml configuration."""
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"ERROR: Configuration file not found: {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"ERROR: Failed to parse mkdocs.yml: {e}")
        sys.exit(1)


def extract_nav_files(nav_section, files: Set[str]):
    """Recursively extract all file references from navigation structure."""
    if nav_section is None:
        return

    if isinstance(nav_section, str):
        # Direct file reference
        files.add(nav_section)
    elif isinstance(nav_section, list):
        # List of items
        for item in nav_section:
            extract_nav_files(item, files)
    elif isinstance(nav_section, dict):
        # Dictionary of section -> file/subsection
        for value in nav_section.values():
            extract_nav_files(value, files)


def find_markdown_files(docs_dir: Path) -> Set[str]:
    """Find all Markdown files in docs directory (relative paths)."""
    markdown_files = set()

    for md_file in docs_dir.rglob("*.md"):
        # Get path relative to docs directory
        relative_path = md_file.relative_to(docs_dir)
        markdown_files.add(str(relative_path))

    return markdown_files


def check_nav_file_exists(nav_file: str, docs_dir: Path) -> bool:
    """Check if a navigation-referenced file exists."""
    file_path = docs_dir / nav_file
    return file_path.exists()


def validate_navigation(config: dict, docs_dir: Path) -> Tuple[List[str], List[str]]:
    """
    Validate navigation configuration.

    Returns:
        (broken_nav_refs, orphaned_files)
    """
    # Extract all navigation file references
    nav_files = set()
    if "nav" in config:
        extract_nav_files(config["nav"], nav_files)

    # Find all markdown files in docs directory
    all_md_files = find_markdown_files(docs_dir)

    # Check for broken navigation references
    broken_refs = []
    for nav_file in nav_files:
        if not check_nav_file_exists(nav_file, docs_dir):
            broken_refs.append(nav_file)

    # Check for orphaned files (exist but not in navigation)
    # Note: Some files are intentionally not in nav (e.g., included files)
    orphaned = list(all_md_files - nav_files)

    return broken_refs, orphaned


def main():
    """Main validation entry point."""
    # Determine repository root (assume script is in scripts/docs/)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent

    config_path = repo_root / "mkdocs.yml"
    docs_dir = repo_root / "docs"

    print("Navigation Sync Checker")
    print("=" * 50)
    print(f"Config: {config_path}")
    print(f"Docs:   {docs_dir}")
    print()

    # Load configuration
    config = load_mkdocs_config(config_path)

    # Validate
    broken_refs, orphaned = validate_navigation(config, docs_dir)

    # Report results
    errors_found = False

    if broken_refs:
        errors_found = True
        print("ERROR: Broken navigation references found:")
        for ref in sorted(broken_refs):
            print(f"  - {ref} (referenced in mkdocs.yml but file not found)")
        print()

    if orphaned:
        # Orphaned files are warnings, not errors (some may be intentional)
        print("WARNING: Orphaned files found (not in navigation):")
        for orphan in sorted(orphaned):
            print(f"  - {orphan}")
        print()
        print("Note: If these files are intentionally excluded from navigation,")
        print("      this warning can be ignored.")
        print()

    if not broken_refs and not orphaned:
        print("✓ All navigation checks passed!")
        print(f"  - All navigation entries point to existing files")
        print(f"  - All Markdown files are included in navigation")
        return 0

    if not broken_refs:
        print("✓ Navigation integrity verified (no broken references)")
        return 0

    print("✗ Navigation validation failed!")
    return 1


if __name__ == "__main__":
    sys.exit(main())
