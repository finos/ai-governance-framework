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
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# SSSOM sets of citations

`linkml/scripts/build_sssom_mappings.py` writes each set from the catalogue. Every predicate is `skos:relatedMatch`, every justification is `semapv:ManualMappingCuration`, and FINOS is the mapping provider.[^build_sssom_mappings.py]

An object keeps the key FINOS's file gives it, under a namespace this project binds for that file. The set for `iso-42001` leaves labels out, because that file's titles may be ISO's headings.[^build_sssom_mappings.py]

`linkml/tests/test_mappings.py` holds each set to the front matter both ways.[^test_mappings.py]

[^build_sssom_mappings.py]: linkml/scripts/build_sssom_mappings.py, the docstring
[^test_mappings.py]: linkml/tests/test_mappings.py
