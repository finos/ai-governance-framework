<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# ai-governance-framework

FINOS AI Governance Framework v3 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/ai-governance-framework](https://lmodel.github.io/ai-governance-framework)

## What it models

The schema models the [AI Governance Framework](https://air-governance-framework.finos.org/) that FINOS publishes for financial services, at v3 of 26 October 2026: its risks, mitigations and use cases, the reference files they cite, and the data files beside them. [src/ai_governance_framework/data/aigf-v3.yaml](src/ai_governance_framework/data/aigf-v3.yaml) holds the framework's facts as records.

This repository is a fork of [finos/ai-governance-framework](https://github.com/finos/ai-governance-framework). FINOS's tree sits unchanged at the repository's root, and this project sits beside it, in this folder, `.lokf/` and `website/`. FINOS has tagged no v3, so [tests/upstream_tree.tsv](tests/upstream_tree.tsv) pins every file of the commit that merged it, and a weekly workflow opens an issue when FINOS's main changes a file the schema reads or FINOS adds a tag.

A reference file validates unchanged. A page's front matter validates once its keys are renamed, because JSON Schema generation turns a hyphen into an underscore and a key named `type` would project as a false `rdf:type`. Each slot lists FINOS's key under `aliases`, [scripts/build_catalogue.py](scripts/build_catalogue.py) renames by that list, and [tests/test_upstream_tree.py](tests/test_upstream_tree.py) shows that the renaming is one to one.

## Mappings

* **FINOS's citations**: [src/ai_governance_framework/mappings/](src/ai_governance_framework/mappings) holds one SSSOM set per reference file, with `skos:relatedMatch`. A row says that a page of the framework cites an entry, as the page's front matter states: a citation, not an equivalence. A row carries the entry's title only where the cited work's terms allow it, as [NOTICE](NOTICE) lists. `tests/test_mappings.py` holds each set to the front matter both ways.
* **[lmodel/nist-sp-800-53](https://github.com/lmodel/nist-sp-800-53)**: `related_mappings` on `nist_sp_800_53r5_references`. `tests/test_schema_rules.py` checks it against the released copy.
* **[lmodel/nist-ai-600-1](https://github.com/lmodel/nist-ai-600-1)**: `related_mappings` on `nist_ai_600_1_references`. `tests/test_schema_rules.py` checks it against the released copy.
* **[AIRO](https://w3id.org/airo) and [AI Atlas Nexus](https://github.com/IBM/ai-atlas-nexus)**: `close_mappings` on the risk and the mitigation, and `related_mappings` on the mitigation.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the builders of the catalogue and the SSSOM sets, and the upstream watch
* [src/ai_governance_framework/schema/](src/ai_governance_framework/schema): the LinkML schema (edit it)
* [src/ai_governance_framework/data/](src/ai_governance_framework/data): the catalogue, which the builder writes
* [src/ai_governance_framework/mappings/](src/ai_governance_framework/mappings): the SSSOM sets, which the builder writes
* [src/ai_governance_framework/datamodel/](src/ai_governance_framework/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)

The knowledge bundle is in `.lokf/` and the website in `website/`, at the repository's root.

## Developer Tools

Run `just` from this folder to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) sidecar. Its domain schema, `.lokf/ai-governance-framework.yaml`, is the copy `just lokf-adapt` writes from `src/ai_governance_framework/schema/ai_governance_framework.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-ai-governance-framework.yaml`.

In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
AigfDataClassification, AigfMitigation, AigfRisk, AigfUseCase
```

The copy drops `item_id` for LOKF's `id`, folds `title` and `description` into LOKF's, and renames `version`, `name`, `url`, `source` and `references` with an `aigf_` prefix, keeping their IRIs. A concept keeps FINOS's identifier in its own path, and names a risk or mitigation by the concept's `id`. Every class and enum carries the `Aigf` prefix, so none is a neighbour's. FINOS's keys are ordinary words, so the copy shares a few with attack, d3fend, gist, nist-nvd, ocsf, oscal, stix, uco and void, which `tests/test_schema_rules.py` lists.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier) published under [10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).

## License

The schema project is under the [Apache License 2.0](LICENSE), and the bundle under CC BY 4.0.

FINOS's files are under [CC-BY-4.0](../LICENSE), and this project's catalogue and SSSOM sets adapt them under the same terms. [NOTICE](NOTICE) says which applies where. This project is not a FINOS project, and FINOS does not endorse it.
