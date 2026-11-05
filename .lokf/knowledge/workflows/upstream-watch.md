---
type: Service
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `linkml/scripts/check_upstream_release.py` runs: a drifted copy, a changed file the schema reads, a changed licence or a new FINOS tag fails the run and opens or updates an issue."
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: check_upstream_release.py
    resource: linkml/scripts/check_upstream_release.py
    title: the docstring
  - id: test_watch.py
    resource: linkml/tests/test_watch.py
    title: the docstring
  - resource: .github/scripts/report-issue.sh
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/references/finos-ai-governance-framework
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/upstream-tree-list
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday, and a failing check opens an issue or comments on the one already open.[^upstream-watch.yaml] The script asks the GitHub API about finos/ai-governance-framework, sending its token there alone.[^check_upstream_release.py] `linkml/tests/test_watch.py` runs it against stubbed answers.[^test_watch.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^check_upstream_release.py]: linkml/scripts/check_upstream_release.py, the docstring
[^test_watch.py]: linkml/tests/test_watch.py, the docstring
