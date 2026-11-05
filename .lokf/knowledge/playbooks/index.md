# Playbooks

* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
* [Regenerate and test the schema](regenerate-and-test.md) - How to change the schema: edit it, run `just gen-project`, `just gen-doc`, the two builders and `just lokf-adapt` from `linkml/`, then `just lint` and `just test`, and commit the output.
* [Rebuild the catalogue and the SSSOM sets](rebuild-the-catalogue.md) - How to rewrite the catalogue and the SSSOM sets from FINOS's files, with `just build-catalogue` and `just build-mappings`, and how to check them with `just check-catalogue` and `just check-mappings`.
* [Take a new edition from FINOS](take-a-new-finos-edition.md) - How to follow FINOS's main when the watch opens an issue: merge `upstream/main` on a branch, rewrite the list of files, move the pins, follow the changes, regenerate, and merge with a merge commit.
* [Release the schema](release.md) - How a release is cut: a typed commit reaches `main`, `semantic-release.yml` promotes `linkml/CHANGELOG.md` and tags it, and `knowledge-release.yaml` attaches the schema's adapt copy, the bundle zip and a docent bundle.
