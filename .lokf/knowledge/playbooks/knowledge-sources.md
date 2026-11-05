---
type: Playbook
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons."
resource: .
references:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/datasets/ai-governance-framework-linkml-schema
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/references/finos-ai-governance-framework
sources:
  - resource: linkml/src/ai_governance_framework/schema/ai_governance_framework.yaml
  - resource: linkml/src/ai_governance_framework/data
  - resource: linkml/src/ai_governance_framework/mappings
  - resource: linkml/src/ai_governance_framework/datamodel
  - resource: linkml/scripts
  - resource: linkml/tests
  - resource: linkml/docs
  - resource: linkml/project
  - resource: website
  - resource: .github/workflows
  - resource: .github/scripts
  - resource: .github/release
  - resource: .github/SECURITY.md
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: .lokf/ai-governance-framework.yaml
  - resource: .lokf/lokf.yaml
  - resource: linkml/.linkml
  - resource: linkml/.linkmllint.yaml
  - resource: linkml/config.public.mk
  - resource: linkml/justfile
  - resource: linkml/project.justfile
  - resource: linkml/README.md
  - resource: linkml/CHANGELOG.md
  - resource: linkml/CONTRIBUTING.md
  - resource: linkml/AI_COVENANT.md
  - resource: linkml/NOTICE
  - resource: .releaserc.json
  - resource: docs
  - resource: scripts
  - resource: README.md
exclusions:
  - resource: .github/dependabot.yml
    reason: "Tooling: when Dependabot opens version bumps."
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sync pull request text, from the KTL template, states nothing about the schema.
  - resource: .lokf/README.md
    reason: The sidecar README, from the KTL template, states nothing about this project.
  - resource: .lokf/queries.http
    reason: Sample queries from the KTL template.
  - resource: .lokf/ingest.yaml.sample
    reason: The ingest example from the KTL template, unused here.
  - resource: .lokf/uv.lock
    reason: The sidecar lock file, tooling that pins versions.
  - resource: .lokf/.gitignore
    reason: "Tooling: what git ignores in the sidecar."
  - resource: .lokf/.gitattributes
    reason: "Tooling: the line endings of the bundle."
  - resource: .lokf/scripts
    reason: The sidecar scripts, copies of the KTL templates that the weekly sync replaces.
  - resource: .lokf/m365
    reason: The Copilot skill builder, copies of the KTL templates that the weekly sync replaces.
  - resource: knowledge_bundle
    reason: A link to the bundle under an ordinary name.
  - resource: llms.txt
    reason: The pointer for agents, from the KTL template.
  - resource: linkml/.copier-answers.yml
    reason: The answers copier records, tooling with no fact about the framework.
  - resource: linkml/.editorconfig
    reason: "Tooling: editor settings."
  - resource: linkml/.gitignore
    reason: "Tooling: what git ignores in the project."
  - resource: linkml/.markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown lint settings."
  - resource: linkml/.pre-commit-config.yaml
    reason: "Tooling: the pre-commit hooks."
  - resource: linkml/.yamllint.yaml
    reason: "Tooling: the YAML lint settings."
  - resource: linkml/lychee.toml
    reason: "Tooling: the link check settings."
  - resource: linkml/CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: linkml/LICENSE
    reason: The Apache-2.0 text, which NOTICE names.
  - resource: linkml/uv.lock
    reason: The package lock file, tooling that pins versions.
  - resource: linkml/pyproject.toml
    reason: Package metadata and the spell checkers' settings.
  - resource: linkml/examples
    reason: The template's note on example output, which the examples run writes beside it.
  - resource: linkml/docs/templates-linkml
    reason: The template's note on gen-doc templates; this project has none.
  - resource: linkml/docs/elements
    reason: A placeholder for pages `just gen-doc` writes and git ignores.
  - resource: linkml/src/README.md
    reason: The template's note on the source folder.
  - resource: linkml/src/ai_governance_framework/__init__.py
    reason: The package marker and its version lookup.
  - resource: linkml/src/ai_governance_framework/_version.py
    reason: The package's version lookup.
  - resource: linkml/tests/__init__.py
    reason: The test package marker.
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Knowledge sources map

Each source below yields the concepts that name it. Re-check a source with `bash .lokf/scripts/knowledge-report.sh worklist`, which lists the concepts whose sources moved.

- **FINOS's tree** yields `datasets/finos-tree` and the typed concepts under `framework/`. Read it only through the pinned commit, and report a fault in it rather than editing it.
- **`linkml/`** yields the schema, the catalogue, the mappings, the examples and the playbooks.
- **`.github/`** yields the workflows and the security policy.
- **`website/`** yields the documentation site.

`bash .lokf/scripts/knowledge-report.sh coverage` counts the tracked files under no listed path.
