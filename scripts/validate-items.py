#!/usr/bin/env python3
"""
Validates the classification fields of risks and mitigations against
docs/_config.yml.

Each front matter field listed in risk_tags or mitigation_tags is checked
against its labels map, <risk|mitigation>_<field>_labels, if there is one:

  type   — required, and must be a key in the labels map
  domain — optional until the domains in #398 are agreed, but if present it
           must be a key in the labels map. A missing domain is a warning:
           the item is left out of the front page's "Group by: Domain" view.

A value that isn't a key in the labels map drops the item out of its group
on the front page, and shows the raw key in the Tags card.

Each <risk|mitigation>_<field>_icons map is also checked against its labels
map: an icon for an unknown key is an error, and a key without an icon is a
warning.

Errors cause the script to exit with a non-zero status, making it suitable
for use as a pre-commit hook or CI step. In GitHub Actions, errors and
warnings are also shown as annotations on the pull request.

Usage:
    python scripts/validate-items.py
    python scripts/validate-items.py docs/_risks/ri-4_hallucination-and-inaccurate-outputs.md
"""

import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, "docs", "_config.yml")
FOLDERS = {
    "risk": os.path.join(ROOT, "docs", "_risks"),
    "mitigation": os.path.join(ROOT, "docs", "_mitigations"),
}

# Fields that every item must have. Add "domain" once the domains are agreed.
REQUIRED_FIELDS = ["type"]

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(\n|\Z)", re.DOTALL)
IN_ACTIONS = os.environ.get("GITHUB_ACTIONS") == "true"


def annotate(level, path, message):
    if IN_ACTIONS:
        print(f"::{level} file={os.path.relpath(path, ROOT)}::{message}")


def front_matter(path):
    with open(path, encoding="utf-8") as f:
        match = FRONT_MATTER.match(f.read())
    if not match:
        raise ValueError("No YAML front matter found")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("Front matter must be a YAML mapping")
    return data


def validate_config(config):
    """Check each icons map against its labels map."""
    errors, warnings = [], []
    for key, icons in config.items():
        match = re.fullmatch(r"(risk|mitigation)_(\w+)_icons", key)
        if not match:
            continue
        labels_key = f"{match.group(1)}_{match.group(2)}_labels"
        labels = config.get(labels_key)
        if not isinstance(labels, dict):
            errors.append(f"'{key}' has no matching '{labels_key}' map")
            continue
        for name in icons:
            if name not in labels:
                errors.append(f"'{key}' has an icon for '{name}', which is not in '{labels_key}'")
        for name in labels:
            if name not in icons:
                warnings.append(f"'{name}' in '{labels_key}' has no icon in '{key}'")
    return errors, warnings


def validate_item(path, kind, config):
    errors, warnings = [], []
    try:
        data = front_matter(path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [f"Cannot read front matter: {exc}"], []

    for field in config.get(f"{kind}_tags") or []:
        labels = config.get(f"{kind}_{field}_labels")
        value = data.get(field)

        if value is None:
            if field in REQUIRED_FIELDS:
                errors.append(f"Missing required field '{field}'")
            elif isinstance(labels, dict):
                warnings.append(
                    f"No '{field}', so the item is left out of the front page's {field} view"
                )
            continue

        if not isinstance(labels, dict):
            continue
        if not isinstance(value, str) or value not in labels:
            errors.append(
                f"'{field}: {value}' is not one of: {', '.join(labels)} "
                f"(from {kind}_{field}_labels in docs/_config.yml)"
            )

    return errors, warnings


def kind_of(path):
    folder = os.path.dirname(os.path.abspath(path))
    for kind, kind_folder in FOLDERS.items():
        if folder == kind_folder:
            return kind
    return None


def main(paths=None):
    with open(CONFIG, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if paths:
        files = [(p, kind_of(p)) for p in paths if p.endswith(".md")]
        files = [(p, k) for p, k in files if k]
    else:
        files = [
            (p, kind)
            for kind, folder in FOLDERS.items()
            for p in sorted(glob.glob(os.path.join(folder, "*.md")))
        ]

    total_errors = total_warnings = 0

    errors, warnings = validate_config(config)
    if errors or warnings:
        print(f"\n{CONFIG}")
        for error in errors:
            print(f"  ERROR: {error}")
            annotate("error", CONFIG, error)
        for warning in warnings:
            print(f"  WARNING: {warning}")
            annotate("warning", CONFIG, warning)
    total_errors += len(errors)
    total_warnings += len(warnings)

    for path, kind in files:
        errors, warnings = validate_item(path, kind, config)
        if errors or warnings:
            print(f"\n{path}")
            for error in errors:
                print(f"  ERROR: {error}")
                annotate("error", path, error)
            for warning in warnings:
                print(f"  WARNING: {warning}")
                annotate("warning", path, warning)
        else:
            print(f"  OK  {path}")
        total_errors += len(errors)
        total_warnings += len(warnings)

    summary = f"{len(files)} file(s) checked, {total_errors} error(s), {total_warnings} warning(s)."
    print(f"\n{summary}")
    if total_errors:
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:] or None)
