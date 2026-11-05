---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/sssom-sets
genre: reference
title: SSSOM sets of citations
description: "`linkml/src/ai_governance_framework/mappings/`: one SSSOM set per reference file, 13 sets and 793 rows. Each row says that a page cites an entry, as FINOS's front matter states; it is a citation, not an equivalence."
resource: linkml/src/ai_governance_framework/mappings
derivedFrom:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/finos-tree
isPartOf:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/catalogue
sources:
  - id: build_sssom_mappings.py
    resource: linkml/scripts/build_sssom_mappings.py
    title: the docstring
  - id: test_mappings.py
    resource: linkml/tests/test_mappings.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T15:45:24Z"
status: draft
---

# SSSOM sets of citations

`linkml/scripts/build_sssom_mappings.py` writes each set from the catalogue. Every predicate is `skos:relatedMatch`, every justification is `semapv:ManualMappingCuration`, and FINOS is the mapping provider.[^build_sssom_mappings.py]

An object keeps the key FINOS's file gives it, under a namespace this project binds for that file, and `object_source` names the address the file was generated from. A row carries the entry's title only where `LABEL_POSITIONS` in the builder records that the cited work's terms allow it: the sets for `iso-42001`, whose titles may be ISO's headings, and `iosco-supervisory-toolkit`, whose terms could not be read, name each entry by key alone.[^build_sssom_mappings.py]

`linkml/tests/test_mappings.py` holds each set to the front matter both ways.[^test_mappings.py]

[^build_sssom_mappings.py]: linkml/scripts/build_sssom_mappings.py, the docstring
[^test_mappings.py]: linkml/tests/test_mappings.py
