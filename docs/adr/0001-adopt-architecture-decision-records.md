# ADR-0001: Adopt Architecture Decision Records

**Status:** Proposed
**Date:** 2026-10-28
**Deciders:** AIGF maintainers
**Related:** [#405](https://github.com/finos/ai-governance-framework/issues/405), [#402](https://github.com/finos/ai-governance-framework/issues/402), [#406](https://github.com/finos/ai-governance-framework/issues/406), [#426](https://github.com/finos/ai-governance-framework/issues/426), [#398](https://github.com/finos/ai-governance-framework/issues/398), [#417](https://github.com/finos/ai-governance-framework/pull/417)

## Context

[#405](https://github.com/finos/ai-governance-framework/issues/405) proposes an `AGENTS.md` file, so that AI agents follow the same rules as human contributors. Those rules are in [CONTRIBUTING.md](https://github.com/finos/ai-governance-framework/blob/main/CONTRIBUTING.md), [CONVENTIONS.md](https://github.com/finos/ai-governance-framework/blob/main/CONVENTIONS.md) and [GOVERNANCE.md](https://github.com/finos/ai-governance-framework/blob/main/GOVERNANCE.md).

Those files say *what* the rules are. They do not say *why*. The reasons are spread across issues, PR reviews and meeting minutes. Several open proposals have the same problem:

- [#402](https://github.com/finos/ai-governance-framework/issues/402): writing style for risks and mitigations
- [#406](https://github.com/finos/ai-governance-framework/issues/406): conventions for reviewability
- [#426](https://github.com/finos/ai-governance-framework/issues/426): floor, cap and ranking rules for references
- [#398](https://github.com/finos/ai-governance-framework/issues/398): ID scheme and groupings for risks and mitigations
- [#417](https://github.com/finos/ai-governance-framework/pull/417): a design for a reference drift monitor

When these are decided, the decision and its reasons need a home. New contributors need it, and so do AI agents, which cannot read meeting discussions.

In #405, it was suggested to put this guidance under `docs/adr/`, as other FINOS repositories do:

- [finos/technical-oversight-committee](https://github.com/finos/technical-oversight-committee/tree/main/adrs), which adopted ADRs in its own [ADR-0001](https://github.com/finos/technical-oversight-committee/blob/main/adrs/0001-adopt-architecture-decision-records.md)
- [finos/aigf-mcp-server](https://github.com/finos/aigf-mcp-server/tree/main/docs/adr)
- [finos/traderX](https://github.com/finos/traderX/tree/main/docs/adr)

The issue author agreed, and suggested starting with ADRs so that agents get better context.

## Decision Drivers

- **Easy to find.** A person or an agent asking "why does AIGF do X?" should find the answer in one place.
- **Same structure each time.** A fixed structure makes proposals easier to write, compare and review.
- **Fits the current process.** [GOVERNANCE.md](https://github.com/finos/ai-governance-framework/blob/main/GOVERNANCE.md) still decides how changes are approved. ADRs record decisions; they do not add a new way to make them.
- **Readable by agents.** The record must be plain files in the repository, not only in issue threads, meetings or a wiki.
- **Consistent with FINOS.** Use a pattern that other FINOS projects already use.

## Considered Options

### Option A: Keep using issues only

Discuss and decide in issues, as now.

- Advantages: no new process.
- Disadvantages: the reasons stay spread across threads. Agents and new contributors cannot find them easily. Each proposal has a different structure.

### Option B: Add the reasons to CONTRIBUTING.md and CONVENTIONS.md

Write each rule's reason next to the rule.

- Advantages: one less place to look.
- Disadvantages: the files get long, and the reasons hide the rules. Options that were rejected have no home. When a rule changes, the old reasoning is lost.

### Option C: Use the GitHub wiki

- Advantages: easy to edit.
- Disadvantages: the wiki is turned off. Wiki pages do not go through PR review, and agents working in a clone cannot see them.

### Option D: Adopt ADRs in `docs/adr/` (chosen)

Record each decision with a lasting effect as a numbered Markdown file in `docs/adr/`, using the [FINOS TOC template](https://github.com/finos/technical-oversight-committee/blob/main/adrs/README.md).

- Advantages: decisions are reviewed in PRs, kept in version control, and readable by people and agents. The site publishes them, because GitHub Pages renders Markdown in `docs/` without front matter. Old decisions stay on record when a new ADR supersedes them.
- Disadvantages: a small amount of extra process. Someone must write the ADR and keep its status up to date.

`docs/adr/` follows aigf-mcp-server and traderX. The TOC uses a top-level `adrs/` folder, but here `docs/` is the published site, so `docs/adr/` makes the ADRs visible to readers of the framework too.

## Decision Outcome

**Option D.** The project records decisions with a lasting effect as ADRs in `docs/adr/`. [docs/adr/README.md](README.md) describes when to write one, the process and the template.

## Consequences

- A proposal with real trade-offs still starts as an issue, and is still approved under GOVERNANCE.md. After the decision, the result is recorded as an ADR.
- The `AGENTS.md` file from #405 can be short. It can point agents to CONTRIBUTING.md, CONVENTIONS.md and `docs/adr/`, so the rules and the reasons are not copied into it.
- CONTRIBUTING.md should mention `docs/adr/` in a later PR.
- Earlier decisions are not converted. A past decision that is still useful can be recorded later.
- First candidates:
  - AI-assisted maintenance tools ([#362](https://github.com/finos/ai-governance-framework/pull/362), [#417](https://github.com/finos/ai-governance-framework/pull/417), [#413](https://github.com/finos/ai-governance-framework/issues/413))
  - the data model for the catalogue: IDs and groupings (#398), lenses (#426), reference status fields (#417), and jurisdiction and binding level ([#255](https://github.com/finos/ai-governance-framework/issues/255))
  - the writing style (#402) and conventions for reviewability (#406)
