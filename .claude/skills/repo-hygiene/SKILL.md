---
name: repo-hygiene
description: Run an issue and pull request hygiene pass over the AI Governance Framework repository. Verifies which issues have already been delivered, closes what is done or abandoned with a reason on each, states where every open pull request stands, chases proposals nobody answered, and produces a maintainer report. Use when the backlog has drifted, before a working session, or when someone asks what is actually still open.
---

# An AIGF hygiene pass

An open issue is a claim that the project intends to do something. A backlog
full of issues nobody is working on makes that claim untrue about all of them,
and the cost lands on contributors, who cannot tell whether their proposal is
queued or forgotten.

The job is to make the open list mean something again. The job is *not* to get
the number down — a closure with no reason on it destroys more than the open
issue did.

## 1. Establish the state before touching anything

```bash
gh issue list --repo finos/ai-governance-framework --state open --limit 200 \
  --json number,title,createdAt,updatedAt,author,assignees,comments,labels
gh pr list --repo finos/ai-governance-framework --state open --limit 100 \
  --json number,title,author,updatedAt,isDraft,reviewDecision,mergeStateStatus
```

Sort issues by `updatedAt`, not by number. The shape of the debt is visible
immediately: a cluster that stopped moving a year ago, and a cluster of recent
proposals with `comments=0`, which is the more urgent of the two.

Read the last two meeting agenda issues as well (`📆 meeting`). They record
what the room committed to, which frequently resolves whether an issue is live.

## 2. Run the deterministic checks

```bash
python scripts/review-pr.py <every open PR number>
python scripts/review-pr.py --tree origin/main
```

The second command matters and is easy to skip. It audits the catalogue itself
rather than a contribution, and it is how you find defects that merged cleanly
and have been silently wrong since.

Cross-branch collisions are invisible to a per-pull-request check: two branches
can each add `mi-24` and each pass, because each is measured against `main`.
Compare the new entries reported across all open pull requests by hand.

## 3. Classify every issue into exactly one bucket

**Delivered.** The work happened and nobody closed the issue. Prove it before
you write it — find the merged pull request, or the file in the catalogue:

```bash
gh pr view <n> --repo finos/ai-governance-framework --json state,mergedAt,files
ls docs/_risks/ docs/_mitigations/ docs/_usecases/
```

Close as `completed`, and say *what* delivered it with a link. "This is done"
without a citation is worthless to anyone reading it later.

**Stale.** No owner, no movement, nobody is going to do it. Close as
`not planned`. The comment must say which of these it is, because they are
different facts and contributors can tell:

- superseded — name the issue or pull request that replaced it
- event-bound and the event has passed
- blocked on an unanswered question — name the question and who can answer it
- simply untouched for a year with no owner

**Live.** Leave open. Anything with an assignee stays open by default: chase
the assignee instead of closing their work out from under them.

Where a closed issue contained a good idea, carry the idea into the closing
comment and point at whatever is live now. Ideas are the asset; the issue is
just where it was parked.

## 4. State where every open pull request stands

Every open pull request gets a comment, including the ones that are fine —
silence is indistinguishable from neglect. Each says what the checks report,
what it is waiting for, and who has the next move. Distinguish:

- **Ready** — checks green, needs only review. Say so plainly; this is the
  group most likely to have been sitting for weeks.
- **Waiting on the author** — conflicts, unresolved review points, still a
  draft. Say exactly what to do.
- **Waiting on us** — a review that was requested and never came. Name it.
  This is the project's failure, not the contributor's, and saying so is the
  point.

For anything stale enough to close, give a deadline and a reopen invitation
rather than closing it on the spot. Contributions are harder to replace than
issues.

## 5. Chase the proposals nobody answered

Filter for issues with no maintainer response. These are the most expensive
items in the backlog: someone did unpaid work and heard nothing.

Each gets a substantive reply — engage with the actual proposal, name the
related work it should be aligned with, and put it on the next agenda. An
acknowledgement that says only "thanks, we'll look at it" is worse than the
silence, because it uses up the contributor's goodwill without giving them
anything to act on.

## 6. Label so the open list is filterable

Labels do not notify anyone, so this is free. Every live issue should carry a
type (`💡 Idea`, `❓ question`, `📄 Documentation`, `🗻 epic`) and, where it
applies, `help wanted`, `good-first-issue` or `governance-needed`.

## 7. Attribution

Everything posted in this pass is written with assistance and posted under a
human's name. Each comment, and any issue body authored in the pass, ends with:

```markdown
---
*Drafted with [Claude Code](https://claude.com/claude-code) (Claude <model>).
Claims verified against the repository; posted and owned by @<handle>.*
```

Commits made during the pass carry the trailer instead, matching the
convention used by the Linux kernel, Kubernetes and the ASF:

```
Assisted-by: Claude <model> (Claude Code)
```

Minutes and other governance records name their source as well as the tool —
see `session-minutes`. The disclosure names the tool; it does not move
accountability, which stays with the person whose handle is on the post, the
same way the DCO works. See `CONTRIBUTING.md`.

Never write the line on something you have not verified. It is a claim about
process, and it is worth nothing the first time it turns out to be false.

## 8. Write the maintainer report

A Markdown report for the user to send. It states what changed, in numbers;
what needs a maintainer *decision* rather than a contributor; and any defect
the pass uncovered. Group the closures by reason rather than listing sixty
issue numbers.

End with standing recommendations aimed at the process failure, not the
symptom — if minutes went unwritten, the recommendation is about when minutes
get written, not about the one meeting.

## Rules

- **Verify before closing.** Every "this is delivered" needs a merged pull
  request or a file in the catalogue behind it. Guessing here is how a
  contributor's work gets erased.
- **Never close silently.** A reason and a reopen invitation on every closure,
  written for the person who opened it.
- **Assigned means open.** Chase the assignee; do not close their work out
  from under them.
- **Do not merge.** A hygiene pass states where things stand. Merging is a
  maintainer decision made in the open, usually on a call.
- **Say when the project is at fault.** Unanswered review requests and ignored
  proposals go in the report as our failures, named as such.
- **Batch edits, never batch judgement.** Sixty closures can be scripted;
  sixty *reasons* cannot. If two comments could be swapped without anyone
  noticing, neither was worth posting.
- **Count honestly.** Report the before and after, and do not quietly exclude
  the issues you opened during the pass.
