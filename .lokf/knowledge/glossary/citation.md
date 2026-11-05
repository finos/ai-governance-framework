---
type: GlossaryTerm
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/glossary/citation
title: Citation
description: "A citation: an entry of a reference file named by key in a page's `<file>_references` front matter. It says a page cites the entry, and claims no equivalence between the two."
relatedTo:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/sssom-sets
sources:
  - id: conventions.md
    resource: CONVENTIONS.md
    title: External References
  - id: build_sssom_mappings.py
    resource: linkml/scripts/build_sssom_mappings.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Citation

A page's `owasp-llm_references` list names keys of `docs/_data/references/owasp-llm.yml`, and so on for each file.[^conventions.md] This project writes each citation as a row of an SSSOM set, with `skos:relatedMatch`.[^build_sssom_mappings.py]

[^conventions.md]: CONVENTIONS.md, External References
[^build_sssom_mappings.py]: linkml/scripts/build_sssom_mappings.py, the docstring
