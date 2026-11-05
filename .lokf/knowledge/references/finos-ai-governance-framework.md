---
type: Reference
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/references/finos-ai-governance-framework
genre: reference
title: FINOS AI Governance Framework
description: "The framework this repository models and forks: what FINOS publishes for financial services, its v3 of 2026-10-26, the commit it is pinned to, and its CC-BY-4.0 licence."
resource: https://github.com/finos/ai-governance-framework
sources:
  - id: readme.md
    resource: README.md
  - id: config.yml
    resource: docs/_config.yml
    title: the version and release-date keys
  - id: check_upstream_release.py
    resource: linkml/scripts/check_upstream_release.py
    title: the docstring and the pins
  - id: license.spdx
    resource: LICENSE.spdx
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# FINOS AI Governance Framework

FINOS publishes the AI Governance Framework as a Jekyll site, built from the Markdown and YAML files of its repository.[^readme.md] `docs/_config.yml` names the edition `v3` and its release date 2026-10-26.[^config.yml]

FINOS has no `v3` tag, so this project pins the commit that merged it, `67b8c3257695d5ede09d262798bf28a0e58d4740`.[^check_upstream_release.py] FINOS's tags are `v1` and `v2`.[^check_upstream_release.py]

FINOS declares CC-BY-4.0.[^license.spdx]

[^readme.md]: README.md
[^config.yml]: docs/_config.yml, the version and release-date keys
[^check_upstream_release.py]: linkml/scripts/check_upstream_release.py, the docstring and the pins
[^license.spdx]: LICENSE.spdx
