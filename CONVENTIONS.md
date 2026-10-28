# Conventions for the Jekyll Project

## YAML Front Matter
- Each file includes a YAML front matter block with attributes such as `sequence`, `title`, `layout`, `doc-status`, and `type`.
  - The `type` attribute is scalar and specifies the Risk or Mitigation classification.
  - The `domain` attribute is scalar and places the item in one of the domains listed in `risk_domain_labels` or `mitigation_domain_labels` in `_config.yml` ([#398](https://github.com/finos/ai-governance-framework/issues/398)). Use the lower-case key, for example `domain: inputs`.

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

Mitigations are associated with Risks via the `mitigates` list in `mi-*.md` files. For example:
```
mitigates:
  - ri-1
```
The author of the link does not have to worry about the title appended to the filename
through the magic of brute-force looping through all the document objects and inspecting
the sequence numbers for a match.

Note: Risk files (`ri-*.md`) do NOT have a `mitigations:` section - the relationship is 
one-way from mitigations to risks.

In `ri-*.md` files, other risks may be referenced:
```
related_risks:
- ri-4
```

In `mi-*.md` files, other mitigations may be referenced:
```
related_mitigations:
- mi-8
```

## Numbering Convention
- The `risk-id.html` and `mitigation-id.html` templates enforce a numbering convention where risks and mitigations are prefixed with `AIR-*`.
  - For risks, the numbering follows the format `AIR-<risk_type>-<number>`.
  - For mitigations, the numbering follows the format `AIR-<mitigation_type>-<number>`.

Risk and Mitigation types are defined in `_config.yml`.

Order in which the Risk and Mitigation types are presented are defined
in `index.md`.

# External References

Risk files (`ri-*.md`) can include several types of external references.

## NIST References
The `nist-sp-800-53r5_references:` section references keys from `_data/nist-sp-800-53r5.yml`.
The `nist-ai-600-1_references:` section references keys from `_data/nist-ai-600-1.yml`.
Each reference links to the corresponding NIST control or section with deep PDF links.

## FFIEC References  
The `ffiec-itbooklets_references:` section references keys from `_data/ffiec-itbooklets.yml`.
Each reference links to the corresponding FFIEC IT Handbook booklet.

## OWASP ML Top 10 References
The `owasp-ml_references:` section references keys from `_data/owasp-ml.yml`.
Each reference links to the corresponding OWASP Machine Learning Security Top 10 risk.

## OWASP LLM Top 10 References
The `owasp-llm_references:` section references keys from `_data/owasp-llm.yml`.
Each reference links to the corresponding OWASP LLM Security Top 10 risk.

## OWASP Agentic Applications Top 10 References
The `owasp-asi_references:` section references keys from `_data/references/owasp-asi.yml`.
Each reference links to the corresponding OWASP Top 10 for Agentic Applications risk.

## EU AI Act References
The `eu-ai-act_references:` section references keys from `_data/eu-ai-act.yml`.
Each reference links to the corresponding EU AI Act article.

All reference types are displayed as separate cards in the risk layout sidebar.

## Sorting and Grouping

- Risks and mitigations are grouped by their `type` attribute and
  sorted by their `sequence` attribute in the index pages.
- The front page has a "Group by" switch. "Domain" regroups both catalogues by the `domain` attribute, in the order of `risk_domain_labels` and `mitigation_domain_labels`, with icons from `risk_domain_icons` and `mitigation_domain_icons` in `_config.yml`. `?groupby=domain` in the URL opens the page in that view.

## Tags

- Each risk and mitigation page shows its tags in a "Tags" card at the top of the right-hand column, one row per field.
- `risk_tags` and `mitigation_tags` in `_config.yml` list which front matter fields are shown, for example `risk_tags: [type]`.
- Display names come from a map in `_config.yml` named `<risk|mitigation>_<field>_labels`, for example `risk_type_labels`. A value with no display name is shown as it is.
- A field can hold one value or a list of values.
- `type` and `domain` are shown today. To show another tag, add the field to the front matter, add the field name to the list, and add a `_labels` map if the values need display names. The templates do not need to change.

## Templates
- The `_includes/risk-id.html` and `_includes/mitigation-id.html` templates dynamically generate the `AIR-*` identifiers based on the file's metadata.
- The `_layouts/risk.html` and `_layouts/mitigation.html` templates format the `_risks/ri-*.md`  and `_mitigations/mi-*.md` as HTML, including backlinks.
- The `_includes/item-tags.html` template shows the tags listed in `risk_tags` and `mitigation_tags`.

## Local Development

For instructions on setting up and running the Jekyll site locally, see [DEVELOPMENT.md](DEVELOPMENT.md).