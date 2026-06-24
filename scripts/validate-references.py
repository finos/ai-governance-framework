#!/usr/bin/env python3
"""
Validates YAML files in docs/_data/references/ against the standard schema.

Schema rules (see docs/_data/references/README.md):

  Top-level (required):
    title       — non-empty string
    description — non-empty string

  Top-level (optional):
    source_url  — string

  entries (required):
    A non-empty mapping. Each value must contain:
      title — non-empty string
      url   — non-empty string beginning with http

    Optional entry fields (must be strings if present):
      description
      issuer

Files that do not conform cause the script to exit with a non-zero status,
making it suitable for use as a pre-commit hook or CI step.

Usage:
    python scripts/validate-references.py
    python scripts/validate-references.py docs/_data/references/eu-ai-act.yml
"""

import glob
import os
import sys

import yaml

REFERENCES_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "_data", "references",
)

REQUIRED_TOP_LEVEL = ["title", "description"]
OPTIONAL_TOP_LEVEL = ["source_url"]
KNOWN_TOP_LEVEL = set(REQUIRED_TOP_LEVEL + OPTIONAL_TOP_LEVEL + ["entries"])

REQUIRED_ENTRY_FIELDS = ["title", "url"]
OPTIONAL_ENTRY_FIELDS = ["description", "issuer", "booklet_abbrev"]


def validate_file(path):
    errors = []

    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        return [f"YAML parse error: {exc}"]

    if not isinstance(data, dict):
        return ["File must be a YAML mapping at the top level"]

    # --- Top-level required fields ---
    for field in REQUIRED_TOP_LEVEL:
        value = data.get(field)
        if not value:
            errors.append(f"Missing or empty required top-level field: '{field}'")
        elif not isinstance(value, str):
            errors.append(f"Top-level field '{field}' must be a string")

    # --- Top-level optional fields ---
    for field in OPTIONAL_TOP_LEVEL:
        value = data.get(field)
        if value is not None and not isinstance(value, str):
            errors.append(f"Optional top-level field '{field}' must be a string")

    # --- entries ---
    entries = data.get("entries")
    if entries is None:
        errors.append("Missing required top-level field: 'entries'")
    elif not isinstance(entries, dict):
        errors.append("'entries' must be a mapping")
    elif len(entries) == 0:
        errors.append("'entries' must not be empty")
    else:
        for key, entry in entries.items():
            prefix = f"entries.{key}"

            if not isinstance(entry, dict):
                errors.append(f"{prefix}: entry must be a mapping")
                continue

            # Required entry fields
            for field in REQUIRED_ENTRY_FIELDS:
                value = entry.get(field)
                if not value:
                    errors.append(f"{prefix}: missing or empty required field '{field}'")
                elif not isinstance(value, str):
                    errors.append(f"{prefix}: field '{field}' must be a string")

            # url format
            url = entry.get("url", "")
            if isinstance(url, str) and url and not url.startswith("http"):
                errors.append(f"{prefix}: 'url' must begin with http")

            # Optional entry fields must be strings if present
            for field in OPTIONAL_ENTRY_FIELDS:
                value = entry.get(field)
                if value is not None and not isinstance(value, str):
                    errors.append(f"{prefix}: optional field '{field}' must be a string")

    return errors


def main(paths=None):
    if paths:
        files = [p for p in paths if p.endswith(".yml")]
    else:
        files = sorted(glob.glob(os.path.join(REFERENCES_DIR, "*.yml")))

    if not files:
        print("No YAML files found.")
        sys.exit(0)

    total_errors = 0
    for path in files:
        errors = validate_file(path)
        if errors:
            print(f"\n{path}")
            for error in errors:
                print(f"  ERROR: {error}")
            total_errors += len(errors)
        else:
            print(f"  OK  {path}")

    if total_errors:
        print(f"\n{total_errors} error(s) found.")
        sys.exit(1)
    else:
        print(f"\n{len(files)} file(s) valid.")


if __name__ == "__main__":
    main(sys.argv[1:] or None)
