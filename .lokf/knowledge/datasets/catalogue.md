---
type: Dataset
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/catalogue
genre: reference
title: The catalogue
description: "`linkml/src/ai_governance_framework/data/aigf-v3.yaml`, FINOS's v3 as one `AigfCatalogue` record: 24 risks, 25 mitigations, 4 use cases, the keys of 13 reference files, 11 classes of data and the two taxonomies."
resource: linkml/src/ai_governance_framework/data/aigf-v3.yaml
derivedFrom:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/finos-tree
dependsOn:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
sources:
  - id: build_catalogue.py
    resource: linkml/scripts/build_catalogue.py
    title: the docstring
  - id: test_catalogue.py
    resource: linkml/tests/test_catalogue.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# The catalogue

`linkml/scripts/build_catalogue.py` writes the file from FINOS's files, and renames each key by the schema's `aliases`. It adds `item_id` and `source_file` from a page's file name.[^build_catalogue.py]

The file holds what the front matter states and leaves the page bodies in FINOS's files. It names each reference file's entries by key and leaves their titles there.[^build_catalogue.py]

`linkml/tests/test_catalogue.py` holds the file to the builder's output and to the counts, validates it with the committed JSON Schema, and loads it into both generated models.[^test_catalogue.py]

[^build_catalogue.py]: linkml/scripts/build_catalogue.py, the docstring
[^test_catalogue.py]: linkml/tests/test_catalogue.py
