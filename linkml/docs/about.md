# About ai-governance-framework

This page is for anyone reading the [LinkML](https://linkml.io) schema's elements: it says how they fit together, where each part comes from and what the model leaves out.

## How the classes fit together

`AigfCatalogue` holds one edition of the framework. Three kinds of page sit under it: `AigfRisk`, `AigfMitigation` and `AigfUseCase`, each a subclass of `AigfItem`. A mitigation lists the risks it mitigates, and a risk does not list its mitigations, as FINOS's `CONVENTIONS.md` says.

`AigfReferenceCitations` is a mixin of thirteen lists, one for each file under `docs/_data/references/`. A page's value in one of those lists is a key of that file, which `AigfReferenceFile` and `AigfReferenceEntry` model. The catalogue holds each file's keys in `AigfReferenceIndex`, so its citations resolve within it.

`AigfDataClassification`, `AigfUseCaseDomain` and `AigfDeploymentAxis` hold what FINOS's other three data files list, and `AigfReferenceLens` the lens settings of `docs/_config.yml`.

## Where each part comes from

Everything comes from FINOS's tree at the pinned commit, which sits at the repository's root.

- **The pages' front matter** gives each risk, mitigation and use case. The pages' bodies stay in FINOS's files, which `source_file` names.
- **`docs/_config.yml`** gives the edition, the document statuses, the type and domain labels, the use case categories and the lens settings. Each enum's values and titles are held to it.
- **`docs/_data/references/`** gives the reference files. The catalogue keeps their keys and leaves their titles there, because the titles in `iso-42001.yml` may be ISO's headings. No ISO text is read or carried here.
- **`docs/_data/`** gives the other three data files. `data_classification.yml` keeps its shape. `ai_use_cases.yml` and `ai_deployment_model.yml` nest one-key mappings, which the catalogue writes as lists of named records, and a test gives the nesting back.

## Choices worth knowing

- **The schema declares its own classes.** An earlier schema of this fork imported a patched copy of IBM's AI Atlas Nexus and held FINOS's v2 as data under it. FINOS's v3 changed the identifiers and added the lenses, and FINOS's own keys are what a reader checks. Nexus is now a mapping target.
- **A page keeps its identifier in its file name.** FINOS's front matter holds `sequence` and no identifier, and other pages cite `ri-10`. The catalogue adds `item_id` and `source_file` from the file's name, and a test holds `sequence` equal to the number.
- **A use case's category has one value `docs/_config.yml` does not list.** uc-3 and uc-4 write `Risk_and_Compliance`. The enum holds it, its description says so, and `tests/departures.yaml` lists every such place, so a new one fails.
- **An SSSOM row is a citation.** Each set's objects keep FINOS's keys under a namespace this project binds for the file, since FINOS's keys are not IRIs and most targets have no lmodel schema, and `object_source` names the address the file was generated from. `skos:relatedMatch` claims no more than the citation does. A row carries the entry's title only where the cited work's terms allow a copy of its name: `LABEL_POSITIONS` in the builder records the position for each file, and the sets for `iso-42001` and `iosco-supervisory-toolkit` name each entry by key alone.

## What is left out

- **The pages' prose**, which FINOS's site renders.
- **The display settings of `docs/_config.yml`** other than the lenses: the domain icons, the tags shown, the use case order and the FFIEC abbreviations, though a test holds each `booklet_abbrev` to the last.
- **A mapping to lmodel/iso42001**, which has no release yet. The row in `finos_to_iso_42001.sssom.tsv` names FINOS's key.
