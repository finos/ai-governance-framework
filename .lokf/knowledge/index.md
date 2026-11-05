---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/ai-governance-framework/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: ai-governance-framework Knowledge Bundle
description: FINOS AI Governance Framework v3 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/ai-governance-framework/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# ai-governance-framework Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for ai-governance-framework. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow builds. It shows `linkml/README.md`, `linkml/docs/`, the changelog, the schema's pages and the bundle, and leaves FINOS's own site alone.

# References

* [FINOS AI Governance Framework](references/finos-ai-governance-framework.md) - The framework this repository models and forks: what FINOS publishes for financial services, its v3 of 2026-10-26, the commit it is pinned to, and its CC-BY-4.0 licence.

# Datasets

* [FINOS's tree](datasets/finos-tree.md) - Every file FINOS's commit holds, unchanged at the repository's root: the pages under `docs/_risks/`, `docs/_mitigations/` and `docs/_usecases/`, the data under `docs/_data/`, the Jekyll site, and FINOS's scripts and governance files.
* [ai-governance-framework LinkML schema](datasets/ai-governance-framework-linkml-schema.md) - The LinkML model of FINOS's framework, `linkml/src/ai_governance_framework/schema/ai_governance_framework.yaml`: `Aigf` classes for the risks, mitigations and use cases, the reference files and the other data files, at FINOS's v3.
* [The catalogue](datasets/catalogue.md) - `linkml/src/ai_governance_framework/data/aigf-v3.yaml`, FINOS's v3 as one `AigfCatalogue` record: 24 risks, 25 mitigations, 4 use cases, the keys of 13 reference files, 11 classes of data and the two taxonomies.
* [SSSOM sets of citations](datasets/sssom-sets.md) - `linkml/src/ai_governance_framework/mappings/`: one SSSOM set per reference file, 13 sets and 793 rows. Each row says that a page cites an entry, as FINOS's front matter states; it is a citation, not an equivalence.
* [The adapt copy](datasets/adapt-copy.md) - `.lokf/ai-governance-framework.yaml`, the copy `lokf adapt` writes from the schema: it re-roots `AigfItem` and `AigfDataClassification` on `Concept`, and renames `version`, `name`, `url`, `source` and `references` with an `aigf_` prefix.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - `linkml/tests/neighbours/`: the adapt copies of 27 released lmodel repositories, each the schema asset of a release and pinned by its checksum, so that tests can hold this schema's names and mappings to them.
* [Example data](datasets/example-data.md) - `linkml/tests/data/`: a valid example of each class that is not abstract, and a counter-example of each constraint, each naming the place it fails on its first line, which `linkml/tests/test_data.py` checks.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the schema: the projections in `linkml/project/`, the Python models in `linkml/src/ai_governance_framework/datamodel/` and the schema's copy in `linkml/docs/schema/`.
* [List of FINOS's files](datasets/upstream-tree-list.md) - `linkml/tests/upstream_tree.tsv`: each of the 153 files of FINOS's pinned commit, with its git object hash, which the tests and the weekly watch compare.
* [Departures from FINOS's own statements](datasets/departures.md) - `linkml/tests/departures.yaml`: where FINOS's files break a statement of FINOS's own: a use case category `docs/_config.yml` does not list, and a citation of a superseded entry. A new departure fails a test.

# Explanations

* [Why FINOS's tree stays at the root](explanations/fork-layout.md) - This repository is a fork: FINOS's tree sits unchanged at the root, and the schema project, the bundle and the website sit beside it. What keeps them apart, and why a merge from FINOS must stay a merge commit.
* [Where each part comes from](explanations/where-each-part-comes-from.md) - Which of FINOS's files gives each part of the schema and the catalogue: the pages' front matter, `docs/_config.yml`, the reference files and the other data files.
* [Modelling choices](explanations/modelling-choices.md) - The choices behind the schema: its own classes rather than IBM AI Atlas Nexus, an identifier taken from a page's file name, a category FINOS's config does not list, and an SSSOM row that is a citation.
* [What the model leaves out](explanations/what-is-left-out.md) - What the schema and the catalogue do not hold: the pages' prose, the display settings of `docs/_config.yml` other than the lenses, reference entries' titles, and a mapping to lmodel/iso42001, which has no release yet.
* [Mappings](explanations/mappings.md) - What this schema crosses to: FINOS's own citations as SSSOM sets, lmodel/nist-sp-800-53 and lmodel/nist-ai-600-1 through related mappings on two citation slots, and AIRO and AI Atlas Nexus at class level.
* [What no validator checks](explanations/what-no-validator-checks.md) - The rules the generated JSON Schema cannot state, such as a citation resolving in its reference file, which `linkml/tests/aigf_rules.py` holds, and why validation uses the JSON Schema rather than the generated Python models.

# Glossary

* [Lens](glossary/lens.md) - A lens: what a reference file tells a reader about a risk or mitigation, one of `threat`, `obligation` or `control`, each answering one question, set by `lens` in the file and configured in `docs/_config.yml`.
* [Reference file](glossary/reference-file.md) - A reference file: a YAML file under `docs/_data/references/` that lists the citable entries of one regulation, framework or standard, each under a stable key a page cites it by.
* [Citation](glossary/citation.md) - A citation: an entry of a reference file named by key in a page's `<file>_references` front matter. It says a page cites the entry, and claims no equivalence between the two.
* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.
* [Document status](glossary/doc-status.md) - A page's `doc-status`: how far FINOS has approved it, one of `Pre-Draft`, `Draft`, `Working-Group-Approved` or `Approved-Specification`, as `docs/_config.yml` lists them.

# Playbooks

* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
* [Regenerate and test the schema](playbooks/regenerate-and-test.md) - How to change the schema: edit it, run `just gen-project`, `just gen-doc`, the two builders and `just lokf-adapt` from `linkml/`, then `just lint` and `just test`, and commit the output.
* [Rebuild the catalogue and the SSSOM sets](playbooks/rebuild-the-catalogue.md) - How to rewrite the catalogue and the SSSOM sets from FINOS's files, with `just build-catalogue` and `just build-mappings`, and how to check them with `just check-catalogue` and `just check-mappings`.
* [Take a new edition from FINOS](playbooks/take-a-new-finos-edition.md) - How to follow FINOS's main when the watch opens an issue: merge `upstream/main` on a branch, rewrite the list of files, move the pins, follow the changes, regenerate, and merge with a merge commit.
* [Release the schema](playbooks/release.md) - How a release is cut: a typed commit reaches `main`, `semantic-release.yml` promotes `linkml/CHANGELOG.md` and tags it, and `knowledge-release.yaml` attaches the schema's adapt copy, the bundle zip and a docent bundle.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for using AI here: the person who submits a change owns it, FINOS's files stay FINOS's, an element says what FINOS's files say, and agents do not post in issues or discussions.
* [Security policy](policies/security-policy.md) - How to report a vulnerability, what this repository releases, what executes here and what holds each surface, in `.github/SECURITY.md`.
* [Licence and attribution](policies/license-and-attribution.md) - Whose work each part is: the schema project under Apache-2.0, FINOS's files under CC-BY-4.0, and the catalogue and the SSSOM sets as adaptations under CC-BY-4.0. No endorsement by FINOS is implied.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The test workflow on each pull request and on `main`: on five Python versions in `linkml/`, it runs `just test`, and on one it runs the lint and the adapt check.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, word budgets, markdownlint, lychee and codespell, over this project's files and never FINOS's.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The release workflow: it previews each pull request, and on `main` it promotes `linkml/CHANGELOG.md`, tags the commit, publishes the release and dispatches the knowledge release.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `linkml/scripts/check_upstream_release.py` runs: a drifted copy, a changed file the schema reads, a changed licence or a new FINOS tag fails the run and opens or updates an issue.
* [Validate references (validate-references.yml)](workflows/validate-references.md) - FINOS's own workflow, which stays as FINOS writes it: it runs `scripts/validate-references.py` when a reference file changes.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with its sources and opens a pull request. It stays inert until the repository variable `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle and runs the conventions script on each pull request that touches `.lokf/`, and checks the provenance of a person's confirmation.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the schema's adapt copy, the bundle zip and a Copilot skill zip to a release, each with a checksum and an attestation, when the bundle or the schema has changed.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of the KTL skills repository, and opens one pull request when the pin is behind.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs and weekly, and deploys to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

# Framework

* [Prompt Injection](framework/ri-10.md) - Risk `ri-10` of FINOS's framework, a security risk in its inputs domain, and a typed concept of this bundle: an `AigfRisk` that shows the adapt copy validating FINOS's values.
* [Agent Action Authorization Bypass](framework/ri-24.md) - Risk `ri-24` of FINOS's framework, an `AigfRisk` concept, one of the risks that `mi-19` lists.
* [Tool Chain Manipulation and Injection](framework/ri-25.md) - Risk `ri-25` of FINOS's framework, an `AigfRisk` concept, one of the risks that `mi-19` lists.
* [Tool Chain Validation and Sanitization](framework/mi-19.md) - Mitigation `mi-19` of FINOS's framework, a preventative mitigation in its filtering domain, and a typed concept of this bundle: an `AigfMitigation` that names its three risks.
* [Credit Risk Analysis](framework/uc-1.md) - Use case `uc-1` of FINOS's framework, an agent that analyses credit risk for small business loan applications, and a typed concept of this bundle: an `AigfUseCase`.
* [Customer PII data](framework/customer-pii-data.md) - The class `Customer_PII_Data` of FINOS's financial data classification, which uc-1 handles, and a typed concept of this bundle: an `AigfDataClassification` of high sensitivity.
