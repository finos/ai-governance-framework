---
type: Playbook
id: https://w3id.org/lmodel/ai-governance-framework/knowledge/playbooks/release
genre: how-to
title: Release the schema
description: "How a release is cut: a typed commit reaches `main`, `semantic-release.yml` promotes `linkml/CHANGELOG.md` and tags it, and `knowledge-release.yaml` attaches the schema's adapt copy, the bundle zip and a docent bundle."
resource: linkml/CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/semantic-release
  - https://w3id.org/lmodel/ai-governance-framework/knowledge/workflows/knowledge-release
sources:
  - id: contributing.md
    resource: linkml/CONTRIBUTING.md
    title: Releasing (maintainers)
  - resource: .releaserc.json
  - resource: .github/scripts
  - resource: .github/release
  - resource: linkml/CHANGELOG.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:34:20Z"
  revision: b30eac9ec59ac9014a65797446cf255b647e647c
status: draft
---

# Release the schema

Write `## [Unreleased]` in `linkml/CHANGELOG.md` as you go, since the release job refuses an empty one.[^contributing.md]

On merge, `semantic-release.yml` retitles the section, commits the changelog, tags `vX.Y.Z` and publishes the release. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `knowledge-release.yaml`.[^contributing.md]

The `v0.0.0` baseline tag sits on the merge of FINOS's tree, so FINOS's older commits do not count.[^contributing.md]

[^contributing.md]: linkml/CONTRIBUTING.md, Releasing (maintainers)
