# Contributing to ai-governance-framework

*This file is a checklist, not a design log. Each rule is a line or two that links to where its reasoning lives. `lint-and-docs.yaml` holds it to a word budget.*

## What this project is

A LinkML schema of the AI Governance Framework that FINOS publishes, in a fork of FINOS's repository. FINOS's tree sits unchanged at the repository's root, and this project sits beside it.

| Path | Holds |
| --- | --- |
| `linkml/src/ai_governance_framework/schema/` | The LinkML schema. Edit it. |
| `linkml/src/ai_governance_framework/datamodel/`, `linkml/project/`, `linkml/docs/schema/` | Artefacts generated from the schema. |
| `linkml/src/ai_governance_framework/data/` | The catalogue, which `linkml/scripts/build_catalogue.py` writes from FINOS's files. |
| `linkml/src/ai_governance_framework/mappings/` | One SSSOM set of FINOS's citations per reference file, which `linkml/scripts/build_sssom_mappings.py` writes. |
| `linkml/scripts/check_upstream_release.py` | The weekly comparison with FINOS's main. |
| `linkml/docs/` | The website's own pages. |
| `linkml/tests/` | Python tests and example data. |
| `.lokf/knowledge/` | This repository's knowledge bundle. |

Everything else is FINOS's.

## Development setup

You need Python 3.10+, [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

```bash
git clone https://github.com/lmodel/ai-governance-framework.git
cd ai-governance-framework/linkml
uv sync --group dev
just --list
```

### Agent skills (optional, only for this repo's `.lokf/` bundle)

The bundle is maintained with the Knowledge Trust Ladder (KTL) skills, **installed, never committed**. Continuous integration (CI) installs the librarian skill at run time, pinned to a release. [The install page](https://w3id.org/ktl/docs/install/) lists every route. With npm:

```bash
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-librarian --yes   # derive concepts
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-curator --yes     # confirm them as a person
```

## Before opening a pull request

- **Leave FINOS's files alone.** A change to one goes to [FINOS](https://github.com/finos/ai-governance-framework). `linkml/tests/test_upstream_tree.py` holds every file `linkml/tests/upstream_tree.tsv` lists to its hash.
- **Edit the schema, then regenerate.** From `linkml/`, run `just gen-project`, `just gen-doc`, `just build-catalogue`, `just build-mappings` and `just lokf-adapt`, and commit the output.
- **Follow FINOS's keys and lists.** A key FINOS writes differently goes under the slot's `aliases`, and `linkml/tests/test_upstream_tree.py` holds the renaming one to one and each enum to `docs/_config.yml`. Add no rule of your own.
- **A departure is reported, not hidden.** `linkml/tests/departures.yaml` lists where FINOS's files break a statement of FINOS's own. Add to it only with a report to FINOS.
- **A row of an SSSOM set is a citation FINOS wrote.** It is not an equivalence, and no row is written by hand.
- **A class mapping is read at its source.** `linkml/tests/test_schema_rules.py` holds each one to a released neighbour copy. A term with no sure match stays unmapped.
- **Keep names apart.** A host imports this adapt copy beside the Linked Open Knowledge Format (LOKF) schema and the released copies in `linkml/tests/neighbours/`. `linkml/tests/test_schema_rules.py` checks this.
- **Run the tests**: `just test` from `linkml/`. Example data goes in `tests/data/valid/` and `tests/data/invalid/`, named `ClassName-suffix.yaml`; an invalid example's first line, `# Fails at: <pointer>`, names where it fails.
- **Follow the schema's conventions**: PascalCase classes and enums with the `Aigf` prefix, snake_case slots from FINOS's keys, FINOS's spelling for values, and a short description on every element.
- **Run the pre-commit hooks** on what you staged, from the root (`uvx pre-commit run -c linkml/.pre-commit-config.yaml`).
- **Lock files are part of the change.** CI installs with `uv sync --locked`, so an edit without its `linkml/uv.lock` (or `.lokf/uv.lock`) fails.
- **Knowledge-bundle changes**: `cd .lokf && just lokf-validate` must pass, and `knowledge-registrar.yaml` runs on any `.lokf/**` change.
- **`lint-and-docs.yaml`** runs ShellCheck, actionlint, markdownlint, lychee and codespell over this project's files, never FINOS's.
- **Actions are pinned to commit hashes**; Dependabot bumps them.
- **The skills pin moves with the sidecar copies.** When moving `TRUST_LADDER_SKILLS_REF` in `.github/workflows/knowledge-librarian.yaml`, copy the other `knowledge-*.yaml` workflows and `.lokf/scripts/` and `.lokf/m365/` from that release's `skills/ktl-sidecar/templates/` in the same pull request.
- **If your change alters behaviour**, add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).

## Taking a new edition from FINOS

The weekly watch opens an issue when FINOS's main changes a file the schema reads. On a branch, merge `upstream/main`, rewrite `linkml/tests/upstream_tree.tsv` from `git ls-tree -r`, move the pin in `linkml/scripts/check_upstream_release.py` and the schema's header, follow the changes, and regenerate. Merge with a merge commit: a squash loses FINOS's history, and the next merge conflicts on every file.

## Code of conduct

Participation here is covered by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Using AI tools

Artificial intelligence (AI) assistance is welcome; [AI_COVENANT.md](AI_COVENANT.md) sets the rules, for people and the scheduled `knowledge-librarian` agent alike.

## Reporting issues

Use the [issue tracker](https://github.com/lmodel/ai-governance-framework/issues) for the schema. A problem in the framework belongs with [FINOS](https://github.com/finos/ai-governance-framework/issues).

## Releasing (maintainers)

- Write `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you go. The release job refuses an empty one (`.github/scripts/changelog-release.mjs check`).
- Type the commit ([Conventional Commits](https://www.conventionalcommits.org/)) for what the change *is*. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release, and FINOS's commits in a merge count too. A pull request that would release must carry a releasing type in its title.
- On merge, [`semantic-release.yml`](../.github/workflows/semantic-release.yml) retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `linkml/CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `.github/workflows/knowledge-release.yaml`, which attaches the schema copy and the bundle when either changed.
- That step runs behind the `release` GitHub Environment. Configure required reviewers on it in Settings → Environments, or every qualifying merge is released unattended.
- Below 1.0.0: the `v0.0.0` baseline tag sits on the merge of FINOS's tree, so FINOS's older commits do not count. `.releaserc.json` maps `breaking: true` to `minor`.
- A branch rule requiring pull requests, status checks or signed commits would reject the release job's own push to `main`, so leave them off. [SECURITY.md](../.github/SECURITY.md) says what holds `main` instead.

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE). FINOS's files are under CC-BY-4.0; [NOTICE](NOTICE) says what applies where. Update it when you add something from elsewhere.
