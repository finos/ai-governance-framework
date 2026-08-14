---
name: session-prep
description: Prepare a chair's briefing for an AI Governance Framework working session. Reads the meeting agenda issue, pulls every pull request and issue on it, runs the deterministic catalogue checks, and builds a navigable HTML run sheet with a call script. Use when someone is chairing or attending an AIGF working session and needs to be caught up, or asks what is on the agenda for a call.
---

# Preparing an AIGF working session

The job is to walk into the call knowing more about each contribution than
anyone else on it, and to know which question unblocks each item. A summary
that only restates the pull request titles is worthless; the value is in what
is *stuck*, and why.

## 1. Read the agenda

```bash
gh issue view <issue> --repo finos/ai-governance-framework
```

Meeting agendas carry the label `📆 meeting`. Find the current one with:

```bash
gh issue list --repo finos/ai-governance-framework --label "📆 meeting" --limit 5
```

The agenda lists pull requests and issues, sometimes with the contributor
handle. It may also point at a session in another repository
(`finos/ai-reference-architecture-library` is the usual one) — those sessions
are sometimes combined, and the linked issue there may be nothing but an
invite list, so check before assuming it carries content.

Read the *previous* meeting's agenda issue too. Minutes are added to it as
the body or as comments, and they carry the commitments the room made, which
is what lets the chair hold people to them.

## 2. Run the checks before reading anything by hand

```bash
python scripts/review-pr.py --agenda <issue>
```

This is the deterministic layer and it is where accuracy comes from. It
reports, per pull request: merge state and the exact colliding files; CI and
DCO; whether the change amends a document that is already
`Approved-Specification`; sequence collisions for new entries; references it
introduces that do not resolve, separated from problems it merely inherits
from `main`; cross-links that break the site conventions; and who was asked
to review but never replied.

Never restate these by eye. Run the script and trust it over your reading of
a diff.

## 3. Read each contribution properly

For every pull request on the agenda:

```bash
gh pr view <n> --repo finos/ai-governance-framework --json title,body,author,files,reviews,comments
gh pr diff <n> --repo finos/ai-governance-framework
```

Read the actual diff, not just the description. For a catalogue contribution
the substance is usually in the body text, and the interesting question is
almost never "is this correct" but one of:

- Who was asked for review and has gone silent, and is their review a gate?
- Does it amend approved content, and does the project have a rule for that?
- Is there an unanswered objection, and what would resolve it?
- Does it duplicate or contradict another open contribution?

## 4. Gather what is not in the repository

Attendance decides what can actually be settled. Contributor absence is
usually known only from the mailing list, so ask the user for any relevant
mail before assuming everyone will be there. A pull request whose author
cannot attend needs a different treatment from one whose author is present —
usually "get the one blocking sign-off in the room" rather than "discuss".

## 5. Build the run sheet

Use `assets/runsheet.html` as the shell — it carries the theme tokens, the
tab machinery, the live-notes surface and the Markdown export. Fill the
panels with content written for this session; do not template the analysis,
because the analysis is the deliverable.

Panels that have earned their place:

- **Brief** — session shape, roll call with the source for each attendance
  claim, three or four things needing action before the call, and any thread
  that runs across several agenda items.
- **Pull requests** — one dossier each: what it changes, where it stands,
  what needs attention, a recommendation, and a decision-forcing question
  written in the chair's own voice.
- **Other repository** — when the session is combined.
- **Run script** — timed to the agenda order, opening with the FINOS
  standing notices, with the words to say at each transition.
- **Notes** — left empty for the call.
- **Context** — live threads not on the agenda, and commitments from the
  previous session.

Publish it with the Artifact tool and give the user the link.

## Rules

- **The standing notices are not optional.** A FINOS project lead must open
  by noting the Linux Foundation antitrust policy, the FINOS code of conduct,
  and that meetings may be recorded. Put them in the script.
- **Say what is blocked before what is interesting.** A pull request that
  cannot merge today should be labelled as such at the top, so the room does
  not debate toward an outcome that is not available.
- **Attribute every attendance claim.** "Confirmed" is worth nothing without
  "Luca, 12 Aug". The chair will be asked.
- **Never state an outcome that has not happened.** A brief describes the
  state of play and recommends; it does not record decisions.
- **Check for movement immediately before the call.** Contributors often push
  the night before.
