# Glossary

* [Lens](lens.md) - A lens: what a reference file tells a reader about a risk or mitigation, one of `threat`, `obligation` or `control`, each answering one question, set by `lens` in the file and configured in `docs/_config.yml`.
* [Reference file](reference-file.md) - A reference file: a YAML file under `docs/_data/references/` that lists the citable entries of one regulation, framework or standard, each under a stable key a page cites it by.
* [Citation](citation.md) - A citation: an entry of a reference file named by key in a page's `<file>_references` front matter. It says a page cites the entry, and claims no equivalence between the two.
* [Adapt copy](adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.
* [Document status](doc-status.md) - A page's `doc-status`: how far FINOS has approved it, one of `Pre-Draft`, `Draft`, `Working-Group-Approved` or `Approved-Specification`, as `docs/_config.yml` lists them.
