---
type: Explanation
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/explanations/mappings
genre: explanation
title: Mappings
description: "What this schema crosses to: FINOS's own citations as SSSOM sets, lmodel/nist-sp-800-53 and lmodel/nist-ai-600-1 through related mappings on two citation slots, and AIRO and AI Atlas Nexus at class level."
resource: linkml/README.md
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/sssom-sets
sources:
  - id: linkml-readme.md
    resource: linkml/README.md
    title: Mappings
  - id: test_schema_rules.py
    resource: linkml/tests/test_schema_rules.py
  - id: ai_governance_framework.yaml
    resource: linkml/src/ai_governance_framework/schema/ai_governance_framework.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Mappings

A row of an SSSOM set is a citation FINOS wrote.[^linkml-readme.md] `related_mappings` on `nist_sp_800_53r5_references` and `nist_ai_600_1_references` name a class of the released copy, and `linkml/tests/test_schema_rules.py` checks both.[^test_schema_rules.py]

`AigfRisk` has a close mapping to `airo:Risk`. `AigfMitigation` has a close mapping to `airo:RiskControl` and a related mapping to `nexus:Action`.[^ai_governance_framework.yaml]

[^linkml-readme.md]: linkml/README.md, Mappings
[^test_schema_rules.py]: linkml/tests/test_schema_rules.py
[^ai_governance_framework.yaml]: linkml/src/ai_governance_framework/schema/ai_governance_framework.yaml
