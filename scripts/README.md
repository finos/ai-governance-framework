# Scripts

This directory contains scripts for downloading external references, processing governance framework files, and maintaining project consistency.

## dl-owasp-llm-md
  - Downloads Markdown files from the OWASP repository into the `_refs-markdown/owasp-llm_<year>` directory.
  - Defaults to 2025 by default. Pass `2024` if you want a copy of that instead.
  - Usage: `./dl-owasp-llm-md [year]`

## dl_nist-ai-600-1-md
   - Downloads the (presumably-latest) `NIST.AI.600-1.md` file from the (unofficial) Cloud Security Alliance GitHub repository.
   - Saves the file to the `_refs-markdown/nist-ai-600_<year>` directory.
   - Usage: `./dl_nist-ai-600-1-md`

## dl_ffiec-itbooklets.py
   - Downloads and converts FFIEC IT Handbook booklets to Markdown format.
   - Generates YAML mappings, downloads HTML files (with navigation filtering), and converts to Markdown using pandoc.
   - Requires: `pip install requests beautifulsoup4 pyyaml` and `pandoc`
   - Usage: `python dl_ffiec-itbooklets.py --all` (or `--yml`, `--html`, `--md` individually)

## dl_eu-ai-act.py
   - Downloads EU AI Act Explorer content and extracts table of contents and annexes into structured Markdown and YAML files.
   - Generates `eu-ai-act-toc.md` (human-readable) and `eu-ai-act.yml` (machine-readable) with hierarchical document structure.
   - Requires: `pip install requests beautifulsoup4 pyyaml roman`
   - Usage: `python dl_eu-ai-act.py` (add `--download` to force fresh download)

## annotate_yaml_front_matter.py
   - Adds title comments to YAML front matter in risk and mitigation files for better readability.
   - Processes external risks, risks, and mitigations to create cross-referenced annotations.
   - Requires: `pip install PyYAML`
   - Usage: `python annotate_yaml_front_matter.py`

## rename-with-titles
   - Renames risk and mitigation files to include their titles in the filename.
   - Supports dry-run mode for preview and separate processing of risks vs mitigations.
   - Usage: `./rename-with-titles --ri --dryrun` or `./rename-with-titles --mi`

## lint-check
   - Validates filename conventions and project structure consistency.
   - Checks that files follow expected naming patterns.
   - Usage: `./lint-check`


