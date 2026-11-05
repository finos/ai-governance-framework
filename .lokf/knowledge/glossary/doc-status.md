---
type: GlossaryTerm
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/glossary/doc-status
title: Document status
description: "A page's `doc-status`: how far FINOS has approved it, one of `Pre-Draft`, `Draft`, `Working-Group-Approved` or `Approved-Specification`, as `docs/_config.yml` lists them."
relatedTo:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/references/finos-ai-governance-framework
sources:
  - id: config.yml
    resource: docs/_config.yml
    title: document_status
  - id: test_upstream_tree.py
    resource: linkml/tests/test_upstream_tree.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Document status

`docs/_config.yml` lists the four statuses with a description of each.[^config.yml] The schema's `AigfDocumentStatus` holds them, and a test holds the enum to the file.[^test_upstream_tree.py]

[^config.yml]: docs/_config.yml, document_status
[^test_upstream_tree.py]: linkml/tests/test_upstream_tree.py
