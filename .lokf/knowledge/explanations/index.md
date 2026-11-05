# Explanations

* [Why FINOS's tree stays at the root](fork-layout.md) - This repository is a fork: FINOS's tree sits unchanged at the root, and the schema project, the bundle and the website sit beside it. What keeps them apart, and why a merge from FINOS must stay a merge commit.
* [Where each part comes from](where-each-part-comes-from.md) - Which of FINOS's files gives each part of the schema and the catalogue: the pages' front matter, `docs/_config.yml`, the reference files and the other data files.
* [Modelling choices](modelling-choices.md) - The choices behind the schema: its own classes rather than IBM AI Atlas Nexus, an identifier taken from a page's file name, a category FINOS's config does not list, and an SSSOM row that is a citation.
* [What the model leaves out](what-is-left-out.md) - What the schema and the catalogue do not hold: the pages' prose, the display settings of `docs/_config.yml` other than the lenses, reference entries' titles, and a mapping to lmodel/iso42001, which has no release yet.
* [Mappings](mappings.md) - What this schema crosses to: FINOS's own citations as SSSOM sets, lmodel/nist-sp-800-53 and lmodel/nist-ai-600-1 through related mappings on two citation slots, and AIRO and AI Atlas Nexus at class level.
* [What no validator checks](what-no-validator-checks.md) - The rules the generated JSON Schema cannot state, such as a citation resolving in its reference file, which `linkml/tests/aigf_rules.py` holds, and why validation uses the JSON Schema rather than the generated Python models.
