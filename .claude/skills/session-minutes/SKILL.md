---
name: session-minutes
description: Turn an AI Governance Framework working session transcript and live notes into minutes for the meeting agenda issue, plus the per-pull-request follow-up comments that fall out of them. Use after an AIGF working session when someone has a transcript, recording notes, or scribbled notes and needs to write up what was decided.
---

# Minuting an AIGF working session

Minutes are a governance record. Someone will act on them, and a decision
written down that nobody made is worse than a gap. The whole discipline of
this skill is refusing to fill gaps.

## Inputs

- The transcript. Usually machine-generated, so treat it as noisy evidence
  rather than as a record.
- Any live notes taken during the call. These are sparse but were written by
  a human who was present, so they outrank the transcript on intent.
- The agenda issue, which fixes what was *meant* to be covered.
- The prep brief, if there was one, which fixes what the state was going in.

## 1. Establish what actually moved

Before reading the transcript, get the current state, because contributors
push and comment after calls:

```bash
python scripts/review-pr.py --agenda <issue>
gh pr view <n> --repo finos/ai-governance-framework --json updatedAt,additions,comments
```

A pull request that changed after the meeting may already have actioned what
the room asked for. Minute the meeting, then note the follow-up separately —
do not merge the two into one claim.

## 2. Read the transcript against the catalogue

Machine transcripts mangle exactly the vocabulary this project runs on.
Expect and correct:

- Control ids: "MI-24" becomes "am I 24", "MI 24", "my 24"; "ri-9" becomes
  "R I nine", "RI9", "arion". Resolve against the actual catalogue
  (`docs/_risks/`, `docs/_mitigations/`) — never invent an id that does not
  exist.
- Acronyms: STR/SAR, MLRO, CALM, MCP, ASI, ATR, OSCAL, DCO.
- Names. Speaker labels in auto-transcripts are frequently wrong or absent.

**Attribute only when the transcript names the speaker or context makes it
unambiguous.** Otherwise write the point unattributed. Misattributing a
position to a named maintainer in a public governance record is a real harm
and is not recoverable by an edit.

## 3. Separate three different things

For every agenda item, keep these apart:

- **Discussed** — the substance raised. Goes into the minutes as context.
- **Decided** — a conclusion the room actually reached. Goes in as a decision
  only if you can point at the moment it was made.
- **Action** — who does what. Needs a named owner. An action without an owner
  is a wish and should be written as one, or dropped.

If an agenda item was reached but nothing was concluded, write **"no decision
recorded"**. If it was not reached at all, write **"not covered"**. Both are
correct, expected outputs. Neither is a failure of the minutes.

## 4. Verify before recording

Any claimed outcome that is checkable, check:

```bash
gh pr view <n> --repo finos/ai-governance-framework --json state,mergedAt,mergedBy
gh issue view <n> --repo finos/ai-governance-framework --json state
```

If the minutes would say "merged", confirm it merged. If it did not, the
minute is "agreed to merge" with an owner, which is a different fact.

## 5. Reconcile notes against transcript

Where the live notes and the transcript disagree, **surface the discrepancy
to the user rather than choosing**. The notes may record a hallway
conclusion the transcript missed; the transcript may show the room moved on
after the note was written. Only the person who was there can say.

## 6. Write the outputs

**Minutes comment for the agenda issue**, matching the established house
style — a bullet per agenda link, sub-bullets beneath it:

```markdown
- https://github.com/finos/ai-governance-framework/pull/335
  - Reviewed. Agreed to merge; @chamindra review not treated as a gate.
  - Regulatory citations to be verified separately by @handle.
```

Keep the ordering of the agenda. Include items that were not reached, marked
as such, so the next agenda can carry them.

**Follow-up comments per pull request**, drafted for the user to post, each
covering only what that contributor needs: what was asked of them, by when,
and anything the room settled that changes their work. Address the author
directly and do not restate the whole meeting.

**Actions list** with owners and dates, which the user can reuse as the
opening of the next agenda.

Offer each as a draft to review. Do not post to GitHub without being asked —
these are public records under the user's name.

## Rules

- Never write a decision you cannot locate in the transcript or the notes.
- Never attribute a position to a named person on ambiguous evidence.
- "No decision recorded" and "not covered" are valid minutes.
- Verify checkable claims against GitHub before writing them down.
- Surface contradictions; do not resolve them silently.
- Keep discussion, decision and action distinct.
