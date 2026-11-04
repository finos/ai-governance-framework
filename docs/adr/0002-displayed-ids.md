# ADR-0002: Displayed IDs for risks and mitigations

**Status:** Proposed
**Date:** 2026-10-28
**Deciders:** AIGF maintainers
**Related:** [ADR-0001](0001-adopt-architecture-decision-records.md), [#398](https://github.com/finos/ai-governance-framework/issues/398), [#430](https://github.com/finos/ai-governance-framework/pull/430), [#431](https://github.com/finos/ai-governance-framework/pull/431)

## Context

Each risk and mitigation has an ID. The file names and the links between items use it in the form `ri-4` and `mi-10`, built from the `sequence` field in the front matter.

The site showed a different ID: `AIR-<type>-<NNN>`, for example `AIR-OP-004` for `ri-4`. The type (Operational, Security, Regulatory and Compliance; Preventative, Detective) was part of the displayed ID ([#398](https://github.com/finos/ai-governance-framework/issues/398)).

This caused three problems:

- Readers saw two IDs for one item, and had to work out that `AIR-OP-004` and `ri-4` were the same.
- If an item's type changed, its displayed ID changed too, which breaks references in other documents.
- New ways to classify items, such as the domains in #398, could not be added to the ID without making it longer and changing it again.

## Decision Drivers

- **One ID.** The site, the files and other documents should use the same ID.
- **Stable.** People outside the project cite these IDs. An ID must not change when an item is reclassified or retitled.
- **No meaning in the ID.** Classifications change; the ID should not depend on them.
- **Easy to read in lists.** IDs appear in catalogues, sidebars and tables.

## Considered Options

### Option A: Keep `AIR-<type>-<NNN>`

- Advantages: the ID shows the type.
- Disadvantages: two IDs per item. The ID changes when the type changes.

### Option B: Show the file ID as it is (`ri-4`)

- Advantages: exactly the same text everywhere.
- Disadvantages: lower case and unpadded IDs look untidy in lists, and sort as `ri-1, ri-10, ri-14, ri-2`.

### Option C: Show `RI-<NN>` and `MI-<NN>` (chosen)

The displayed ID is the file ID in upper case, with the number padded to two digits: `ri-4` is shown as `RI-04`, and `mi-10` as `MI-10`.

- Advantages: one ID with a simple, fixed rule between its two forms. It lines up in lists and sorts in order. It never changes.
- Disadvantages: the display form and the file form differ in case and padding. The ID alone no longer shows the type.

## Decision Outcome

**Option C.** The site shows `RI-<NN>` and `MI-<NN>`, built from `sequence` (#430). Files and front matter links keep `ri-N` and `mi-N`. The two forms always refer to the same item, and `RI-04` ⇔ `ri-4` is the only rule a reader needs.

## Consequences

- Anyone who quoted an `AIR-` ID outside this repository needs the new form. The displayed ID will not change again.
- The type is no longer visible in the ID. Each page shows it as a tag instead ([#431](https://github.com/finos/ai-governance-framework/pull/431)).
- Two digits allow up to 99 risks and 99 mitigations. The template in #430 keeps the last two digits, so it would show `ri-100` as `RI-00`. Before either catalogue reaches 100, the template must change, and a new ADR should decide whether to widen all IDs to three digits.
