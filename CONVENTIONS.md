# Conventions for the Jekyll Project

## YAML Front Matter
- Each file includes a YAML front matter block with attributes such as `sequence`, `title`, `layout`, `doc-status`, and `type`.
  - The `type` attribute is scalar and specifies the Risk or Mitigation classification.

## File Naming Conventions
- Risk files are named using the prefix `ri-*` (e.g., `ri-1.md`, `ri-2.md`).
- Mitigation files are named using the prefix `mi-*` (e.g., `mi-1.md`, `mi-2.md`).
- The title may be appended by converting to lower case and converting
  runs of nonalphanumeric characters to a single hyphen.
- The `scripts/rename-with-titles.sh` script can rename the
  `_risks/ri-*.md` or `_mitigations/mi-*.md` files based on the
  sequence number and title in the YAML header.
- The cross-linking between the Risk and Mitigation pages works 

# Cross-Linking

Mitigations are associated with Risks via the `mitigates` list. For example:
```
mitigates:
  - ri-1
```
The author of the link does not have to worry about the title appended to the filename
through the magic of brute-force looping through all the document objects and inspecting
the sequence numbers for a match.

## Numbering Convention
- The `risk-id.html` and `mitigation-id.html` templates enforce a numbering convention where risks and mitigations are prefixed with `AIR-*`.
  - For risks, the numbering follows the format `AIR-<risk_type>-<number>`.
  - For mitigations, the numbering follows the format `AIR-<mitigation_type>-<number>`.

Risk and Mitigation types are defined in `_config.yml`.

Order in which the Risk and Mitigation types are presented are defined in `index.md`.

## Sorting and Grouping
- Risks and mitigations are grouped by their `type` attribute and sorted by their `sequence` attribute in the index pages.

## Templates
- The `_includes/risk-id.html` and `_includes/mitigation-id.html` templates dynamically generate the `AIR-*` identifiers based on the file's metadata.
- The `_layouts/risk.html` and `_layouts/mitigation.html` templates format the `_risks/ri-*.md`  and `_mitigations/mi-*.md` as HTML, including backlinks.
  
## Running Jekyll Locally

It's faster to preview formatting changes by running Jekyll locally.

Remember to `cd(1)` into the `docs/` directory before running `jekyll` commands. The main ones are:
- `jekyll clean`
- `jekyll build`
- `jekyll serve`

By default, the server comes up on http://localhost:4000 .