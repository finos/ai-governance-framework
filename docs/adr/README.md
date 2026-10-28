# Architecture Decision Records

This folder holds the Architecture Decision Records (ADRs) for the AI Governance Framework.

An ADR is a short document that records one decision: the problem, the options, the choice and the reasons. It is for decisions with a lasting effect, which people would otherwise have to reconstruct later from issue threads and meeting minutes. [ADR-0001](0001-adopt-architecture-decision-records.md) says why the project uses them.

ADRs are also written for AI agents. An agent that helps with this repository should read the relevant ADRs before it proposes a change. The ADRs give it the reasons behind the rules in [CONTRIBUTING.md](https://github.com/finos/ai-governance-framework/blob/main/CONTRIBUTING.md) and [CONVENTIONS.md](https://github.com/finos/ai-governance-framework/blob/main/CONVENTIONS.md).

## When to write one

Write an ADR when a decision:

- changes the structure of the catalogue, for example IDs, front matter fields or reference files
- changes how contributions are written, reviewed or merged
- changes how tools or AI agents work on the repository
- had real trade-offs, so the reasons are as useful as the result

You do not need an ADR for a single risk, mitigation or use case, or for a routine fix. [GOVERNANCE.md](https://github.com/finos/ai-governance-framework/blob/main/GOVERNANCE.md) still decides how a change is approved.

## Process

1. Open an issue that proposes the decision. The discussion happens on the issue and in the working group meetings.
2. Open a PR that adds the ADR with status `Proposed`, and link it to the issue. The PR can start before the decision, so people can comment on the wording.
3. When the maintainers agree, set the status to `Accepted` or `Rejected` and merge.
4. Do not delete or rewrite an ADR after it merges. To change a decision, write a new ADR that supersedes the old one, and set the old one's status to `Superseded by ADR-NNNN`.

## Numbering and format

Name each file `NNNN-short-title.md`. Use the next free number, starting at `0001`.

Use this structure. It is the same as the [FINOS TOC template](https://github.com/finos/technical-oversight-committee/blob/main/adrs/README.md).

```markdown
# ADR-NNNN: Title

**Status:** Proposed | Accepted | Rejected | Superseded by ADR-NNNN
**Date:** YYYY-MM-DD
**Deciders:** who decided
**Related:** links to issues and PRs

## Context

What caused this decision, and what limits or earlier discussion shaped it.

## Decision Drivers

The things that matter most when choosing between the options.

## Considered Options

Each option, with its advantages and disadvantages.

## Decision Outcome

The chosen option, and why.

## Consequences

What becomes easier, what becomes harder, and what follow-up work is needed.
```

## Index

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-adopt-architecture-decision-records.md) | Adopt Architecture Decision Records | Proposed |
