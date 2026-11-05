# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Added

- **A schema of FINOS's own files**, with `Aigf` classes for the risks, mitigations and use cases, the reference files and the other data files, at FINOS's v3 of 2026-10-26. A reference file validates unchanged, and a page validates once the keys the schema's `aliases` list are renamed.
- **The catalogue**, `src/ai_governance_framework/data/aigf-v3.yaml`, which `scripts/build_catalogue.py` writes from FINOS's files, and tests that hold FINOS's cross references and each list to the schema.
- **`tests/departures.yaml`**, which lists where FINOS's files break a statement of FINOS's own.
- **A weekly watch** of FINOS's main and tags, against a list of every file of the pinned commit.
- **`.lokf/ai-governance-framework.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-ai-governance-framework.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, NOTICE and the CONTRIBUTING checklist.

### Changed

- **The SSSOM sets now hold FINOS's citations.** There is one set per reference file, written from the front matter at the pinned commit, with `semapv:ManualMappingCuration` and FINOS as the provider. A row is a citation, not an equivalence. The sets named v2's `AIR-*` identifiers and called the rows LLM-based.
- **Pin linkml and linkml-runtime at 1.12.1.** PyPI publishing and the docs preview stay off.
- **A set carries an entry's title only where the cited work's terms allow it.** `LABEL_POSITIONS` in `scripts/build_sssom_mappings.py` records the position for each reference file, `iosco-supervisory-toolkit` joins `iso-42001` in naming each entry by key alone, every row names the file's address as `object_source`, and NOTICE lists the positions.
- **The upstream watch follows a redirect only to another https address of the GitHub API**, and refuses a manifest path that leaves FINOS's tree.

### Removed

- **The copy of IBM's ai-atlas-nexus 0.5.0, the data dumps built on it and the two empty SSSOM sets.** The schema declared nothing of its own, and the dumps named v2's identifiers. `git show e10791f` holds what went.

## [0.0.0] - 2026-11-05

### Added

- **The baseline**: this fork's merge of FINOS's v3 tree, which the `v0.0.0` tag marks.
