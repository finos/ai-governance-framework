#!/usr/bin/env bash
#
# Wrapper for the scheduled knowledge-librarian loop (Karpathy rule).
#
# `.github/workflows/knowledge-librarian.yaml` invokes this script directly: a
# fixed, reviewed path, not an arbitrary command from a repo variable. To turn
# on the scheduled run, set the `KNOWLEDGE_LIBRARIAN_ENABLED` repository
# variable to "true". Then set `AGENT_CLI` (repo variable or secret) to the
# command that runs your coding agent non-interactively, for example the GitHub
# Copilot CLI, Claude Code or an internal agent runner. The prompt follows
# `-p` unless AGENT_PROMPT_FLAG names another flag, or `arg` for an agent that
# takes the prompt as its last argument.
#
# CONTRACT (the workflow relies on this):
#   - The agent WRITES one file, .lokf/patch.yaml, and nothing else. After it
#     returns, this script applies that file with knowledge-apply.sh. So
#     .lokf/knowledge/, a handled feedback.md entry and the ledger line it
#     becomes in questions.md change only through that script, and a run in
#     which the agent changed any other path is refused.
#   - What the pen refuses before it writes is then checked on the result, by
#     knowledge-provenance.sh --unattended: a run that touched a person's
#     event, note or text is refused too.
#   - The lines the patch file holds for the reviewer, its `handoff`, reach
#     the file KNOWLEDGE_HANDOFF_OUT names through the same script, cleaned.
#     That file and the retrieval score's are removed once the agent returns,
#     so what the workflow reads from them was written after it. The
#     retrieval test calls the agent a second time, so the hand-off is
#     written again after that call, as the pen left it.
#   - It MUST NOT git commit, push, or open pull requests: the workflow owns
#     that.
#   - On success it exits 0 whether or not it changed anything; the workflow
#     diffs the working tree to decide whether to open a pull request. A run that
#     knowledge-report.sh finds quiet, when the caller allows a skip, ends
#     with exit 0 before the agent is called.
#
# Inputs (env):
#   AGENT_CLI           command that runs the agent given a prompt via -p "<prompt>"
#   AGENT_PROMPT_FLAG   optional: the flag the prompt follows, -p by default,
#                       or the word arg when the agent takes the prompt as a
#                       bare last argument, as `codex exec` does
#   AGENT_API_KEY       optional: the agent's API key or token, from a secret
#   AGENT_API_KEY_ENV   the name the agent reads that key from, such as
#                       ANTHROPIC_API_KEY; required when AGENT_API_KEY is set
#   KNOWLEDGE_SKIP_QUIET optional: "true" skips the agent when
#                       knowledge-report.sh finds nothing waiting for it; the
#                       workflow sets it on a scheduled run, never on one a
#                       person starts
#   KNOWLEDGE_DECLINED  optional: a file naming what a person declined, by
#                       closing a pull request of the workflow's without
#                       merging. knowledge-report.sh reads it, so the quiet
#                       check and the agent's work list count none of those
#                       changes until they change again. The workflow writes
#                       it on a scheduled run only, never on one a person
#                       starts
#   KNOWLEDGE_HANDOFF_OUT  optional: a file to write the patch's hand-off lines to
#   KNOWLEDGE_RETRIEVAL optional: "true" scores, after the bundle is written,
#                       whether the index leads an agent to the concept behind
#                       each question readers asked (one more agent call)
#   KNOWLEDGE_RETRIEVAL_OUT  optional: a file to write that one score line to
#
set -euo pipefail

# Resolve the repo root from this script's location so it works regardless of cwd.
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"

# The ktl-librarian skill may live under any of these skill-directory
# conventions: the three install targets, plus bare skills/ for a repo that
# publishes the skills it also uses. If this repo uses a different one, add it
# here. A candidate list that does not match the repo fails this whole script
# at run time, not when the sidecar is installed.
skill=""
for candidate in .claude/skills/ktl-librarian/SKILL.md .github/skills/ktl-librarian/SKILL.md \
                 .agents/skills/ktl-librarian/SKILL.md skills/ktl-librarian/SKILL.md; do
  if [ -f "$candidate" ]; then skill="$candidate"; break; fi
done
[ -n "$skill" ] || {
  echo "knowledge-librarian: ktl-librarian SKILL.md not found in .claude/skills/, .github/skills/, .agents/skills/, or skills/" >&2
  exit 2
}

# This wrapper writes the bundle through knowledge-apply.sh and nothing else.
# A sidecar can lack that script when a newer copy was synced over an older
# one, since a sync adds no file that was not there. So say it now, before an
# agent run is spent on a patch nothing could apply.
if [ ! -f .lokf/scripts/knowledge-apply.sh ] || [ ! -f .lokf/scripts/knowledge-apply.py ]; then
  echo "knowledge-librarian: .lokf/scripts/knowledge-apply.sh and knowledge-apply.py are not both here, and the bundle is written through them alone; ktl-sidecar's repair path lays them down" >&2
  exit 2
fi

if [ -z "${AGENT_CLI:-}" ]; then
  cat >&2 <<'EOF'
knowledge-librarian: AGENT_CLI is not set.

Set AGENT_CLI to your non-interactive agent command (e.g. a Copilot CLI or
internal runner). This wrapper hands it a prompt built from the ktl-librarian
skill; the agent is expected to write one file, .lokf/patch.yaml, which this
wrapper then applies with knowledge-apply.sh.
EOF
  exit 2
fi

# The patch file's format comes from knowledge-apply.sh, which prints it
# with --format, so the prompt below names no file inside the skill. That
# matters because the skill a scheduled run installs is pinned one release
# behind the scripts beside this one: a skill that predates the patch file
# still gets a prompt it can follow. Say so when that is the case, since
# nothing else would tell the operator why the skill and the prompt differ.
if [ ! -f "$(dirname "$skill")/references/patch.md" ]; then
  echo "knowledge-librarian: $skill predates the patch file, so the prompt takes the format from knowledge-apply.sh --format; move the skills pin to a release that carries references/patch.md once one is tagged" >&2
fi

# The workflow passes the key under one fixed name, and the agent CLI reads it
# under its own. Check the name here, before anything runs: it must look like a
# credential (ending _API_KEY, _TOKEN or _KEY), so a slip cannot overwrite
# PATH, BASH_ENV or LD_PRELOAD. It must not start GITHUB_, GH_, GIT_, RUNNER_ or
# ACTIONS_, because gh, git and the runner read those names too, and the key
# would reach them as well as the agent. The key moves into an unexported
# variable, so the git commands this script runs never see it.
key_name="${AGENT_API_KEY_ENV:-}"
agent_key="${AGENT_API_KEY:-}"
unset AGENT_API_KEY AGENT_API_KEY_ENV
# The pen's dry-run-only switch belongs to the agent's process alone (see
# run_agent): one set outside would stop this script applying the patch.
unset KNOWLEDGE_PEN_DRY_RUN_ONLY
if [ -n "$agent_key" ] || [ -n "$key_name" ]; then
  if [ -z "$agent_key" ]; then
    echo "knowledge-librarian: AGENT_API_KEY_ENV is $key_name but the AGENT_API_KEY secret is empty" >&2
    exit 2
  fi
  if [ -z "$key_name" ]; then
    echo "knowledge-librarian: AGENT_API_KEY is set; set AGENT_API_KEY_ENV to the name your agent reads it from, such as ANTHROPIC_API_KEY" >&2
    exit 2
  fi
  if ! [[ "$key_name" =~ ^[A-Z][A-Z0-9_]*_(API_KEY|TOKEN|KEY)$ ]] \
     || [[ "$key_name" =~ ^(GITHUB|GH|GIT|RUNNER|ACTIONS)_ ]]; then
    echo "knowledge-librarian: AGENT_API_KEY_ENV '$key_name' is refused: use the upper-case name your agent reads its key from, ending _API_KEY, _TOKEN or _KEY and not starting GITHUB_, GH_, GIT_, RUNNER_ or ACTIONS_" >&2
    exit 2
  fi
fi

# How the prompt reaches the agent. Most agent CLIs take it after -p (Claude
# Code, Copilot CLI, Gemini CLI); some take it as the last argument and give
# -p another meaning (codex exec). Only a short flag, a long flag or the word
# arg is accepted, so the variable can add nothing but the prompt's position.
prompt_flag="${AGENT_PROMPT_FLAG:--p}"
if ! [[ "$prompt_flag" =~ ^(-[A-Za-z]|--[a-z][a-z0-9-]*|arg)$ ]]; then
  echo "knowledge-librarian: AGENT_PROMPT_FLAG '$prompt_flag' is refused: use a flag such as -p or --prompt, or the word arg for an agent that takes the prompt as its last argument" >&2
  exit 2
fi

# Build the prompt. The agent should follow the skill verbatim, write only
# .lokf/patch.yaml, and make no VCS operations.
# The heredoc is unquoted so $skill expands. So any backtick in the text MUST
# be escaped (\`), or bash runs it as a command and blanks the word.
prompt="$(cat <<EOF
You are the repository knowledge librarian. Follow this skill file verbatim:
  - $skill

Task (Karpathy rule - continuous small corrections, not a rewrite):
  1. Follow the skill's Scrape & build procedure: bootstrap discovery if the
     bundle has no real concepts yet, otherwise the steady-state refresh of the
     sources recorded in the bundle (concept provenance and
     .lokf/knowledge/playbooks/knowledge-sources.md). Start a refresh from
     "bash .lokf/scripts/knowledge-report.sh worklist" where that script
     exists: a program has already found which sources moved, which notes a
     person left, and how much reader feedback waits. Where that list names
     changes a person declined, by closing a pull request without merging,
     propose none of them again, and say in the hand-off what you left.
  2. Reconcile the .lokf/ knowledge bundle with the repository: add missing
     concepts, correct stale facts, wire typed relations, and give every
     operation its log line - but only when the bundle content actually
     changed. If nothing changed, write no patch file at all; do not log
     administrative no-op runs.
  3. Write every change as an operation in .lokf/patch.yaml, in the shape
     "bash .lokf/scripts/knowledge-apply.sh --format" prints, and check it
     with "bash .lokf/scripts/knowledge-apply.sh --dry-run". Create and edit
     that file with your own file-writing tool, never with a shell redirect,
     a heredoc or a script. An unattended run may deny a shell command that
     writes, and a denied shell write does not mean the file cannot be
     written. Do NOT edit any
     file under .lokf/knowledge/, .lokf/feedback.md or .lokf/questions.md
     yourself, do NOT run the apply script without --dry-run, and do NOT run
     git, open PRs, or touch any other path: this wrapper applies the file
     after you finish. Cite sources for any claim whose authority is outside
     the repository.
  4. Mark concepts you create, and claims you cannot settle from the
     repository, as \`status: draft\` (with a plain-prose "## Open questions"
     section for the latter), exactly as the skill says. Put what the person
     reviewing the pull request should know, and that is no change to the
     bundle, in the patch file's "handoff" list, in your own words and never
     a reader's. The workflow writes the rest of the pull request itself, and
     your final reply reaches the job log only.
EOF
)"

# Security rationale (for human and automated reviewers): AGENT_CLI is trusted
# configuration, not untrusted input. A repo admin sets it in Settings, naming
# their own agent command, and it is never derived from repo contents, pull
# request data or model output. It is parsed into a quoted argv array and run
# directly (see below), so bash does NOT re-evaluate it as source. Shell
# metacharacters (; | & $() ``) are passed as inert arguments, not executed:
# there is no eval and no `bash -c`. This step runs only in the workflow's
# read-only `refresh` job (contents: read, no persisted credentials), and the
# post-run check also fails if the agent wrote anything but .lokf/patch.yaml.
#
# That check, and the AGENT_CLI invocation itself, live inside main() below,
# called only from this file's last line. Bash reads a function body in full
# before running any of it, so an agent that truncates this script mid-run
# cannot make it skip anything after the agent call. Top-level statements, as
# these once were, run only as far as the file's length on disk when bash
# reaches them.
#
# Split AGENT_CLI into an argv array (whitespace word-split, no globbing) and
# invoke it as a quoted vector rather than a re-expanded string. Handles the
# usual "cmd --flags" form. Quotes *inside* AGENT_CLI are not honoured, so keep
# it to a plain command plus flags, or wrap richer logic in its own script.
read -r -a agent_cmd <<< "$AGENT_CLI"
if [ "${#agent_cmd[@]}" -eq 0 ]; then
  echo "knowledge-librarian: AGENT_CLI has no command after parsing" >&2
  exit 2
fi

# Become the agent, with the given prompt where AGENT_PROMPT_FLAG says it
# goes. Called with exec from a subshell, so only that subshell's environment
# carries the key. It carries KNOWLEDGE_PEN_DRY_RUN_ONLY too, so the pen only
# checks the patch file while the agent runs, and this script applies it after.
# An agent that followed the skill's live-session step and applied its own
# patch once lost the run's work: the pen deleted the file, and the check below
# refused the bundle it wrote. The switch is a guard against that mistake, not
# a boundary; the check below still is one.
run_agent() {
  export KNOWLEDGE_PEN_DRY_RUN_ONLY=1
  if [ "$prompt_flag" = arg ]; then
    exec "${agent_cmd[@]}" "$1"
  fi
  exec "${agent_cmd[@]}" "$prompt_flag" "$1"
}

# Defence in depth: the prompt asks the agent to write only the patch file, but
# nothing forces it. Record paths already dirty outside the bundle (for example
# a uv.lock the workflow refreshed), so the agent answers only for *new* ones.
# The allowed paths are the bundle under both its names, ktl-docent's
# .lokf/feedback.md, and the ledger the pen moves a handled entry into,
# .lokf/questions.md. The bundle's names are .lokf/knowledge/ and
# knowledge_bundle/. By default the second is ktl-sidecar's doorway link, and
# the pathspec matches nothing there. On a host rearranged by hand it is a real
# folder, with .lokf/knowledge a link onto it, and git pathspecs do not
# traverse a symlink, so both must be named.
outside_bundle() {
  git status --porcelain -- '.' \
    ':(exclude).lokf/knowledge' ':(exclude)knowledge_bundle' ':(exclude).lokf/feedback.md' ':(exclude).lokf/questions.md' \
    | cut -c4- | sort -u
}
# Every path git sees changed, the patch file apart: the agent's one output,
# which .lokf/.gitignore keeps out of git anyway.
changed_paths() {
  git status --porcelain -- '.' ':(exclude).lokf/patch.yaml' | cut -c4- | sort -u
}

# Snapshots of .git/config and .git/hooks/ taken before each agent call.
# File-scope, not local, so the EXIT trap below can reach them.
config_snapshot=""
hooks_snapshot=""
snapshot_git_state() {
  config_snapshot="$(mktemp)"
  hooks_snapshot="$(mktemp -d)"
  cp .git/config "$config_snapshot"
  cp -a .git/hooks/. "$hooks_snapshot/"
}

# Put .git/config and .git/hooks/ back as they were before the agent ran, then
# forget the snapshot so a second call is a no-op. main() calls it right after
# the agent returns, and the EXIT trap calls it for every other way out:
# - the agent exiting non-zero, which `set -e` turns into this script's exit;
# - the job being cancelled, the runner's SIGINT or SIGTERM, which the traps
#   below turn into an exit;
# - an error anywhere after the snapshot.
# Without the trap, a failing agent left the config it had rewritten in the
# checkout, for the workflow's next steps to read.
restore_git_state() {
  [ -n "$config_snapshot" ] || return 0
  cp "$config_snapshot" .git/config
  rm -rf .git/hooks
  mkdir .git/hooks
  cp -a "$hooks_snapshot/." .git/hooks/
  rm -rf "$config_snapshot" "$hooks_snapshot"
  config_snapshot=""
  hooks_snapshot=""
}

# Everything git can see of the working tree, as one checksum: which paths
# differ from HEAD, how the tracked ones differ, and what the untracked ones
# hold. Two readings that agree mean nothing in the checkout changed between
# them.
tree_state() {
  {
    git status --porcelain --untracked-files=all
    git diff HEAD
    git ls-files --others --exclude-standard | while IFS= read -r f; do cksum "$f"; done
  } 2>/dev/null | cksum
}

# The index-only retrieval test (knowledge-report.sh's `retrieval`), run only
# when KNOWLEDGE_RETRIEVAL is "true". The bundle is written by now. The agent
# answers one prompt, holding the table of contents and the questions readers
# asked, from an empty directory, so the index is all it has. A program scores
# its reply as one line, "n of m". The prompt carries readers' words. So
# the reply is read for concept paths and for nothing else, the same
# snapshot guards .git/config and .git/hooks/, and a call that changed
# anything in the checkout refuses the run like any other stray write.
# The hand-off file sits outside the checkout, where this call could write
# too. So the lines the pen put there are held across the call and written
# back after it, and the reviewer never reads a hand-off this call left.
score_retrieval() {
  local prompt scratch before line handoff=""
  prompt="$(bash .lokf/scripts/knowledge-report.sh retrieval --prompt 2>/dev/null || true)"
  if [ -z "$prompt" ]; then
    echo "knowledge-librarian: no reader's question is on file, so retrieval is not scored"
    return 0
  fi
  scratch="$(mktemp -d)"
  before="$(tree_state)"
  if [ -n "${KNOWLEDGE_HANDOFF_OUT:-}" ] && [ -f "$KNOWLEDGE_HANDOFF_OUT" ] && [ ! -L "$KNOWLEDGE_HANDOFF_OUT" ]; then
    handoff="$(cat "$KNOWLEDGE_HANDOFF_OUT")"
  fi
  snapshot_git_state
  (
    cd "$scratch" || exit 1
    if [ -n "$key_name" ]; then export "$key_name=$agent_key"; fi
    run_agent "$prompt"
  ) > "$scratch/reply" 2>/dev/null || true
  restore_git_state
  if [ -n "${KNOWLEDGE_HANDOFF_OUT:-}" ]; then
    rm -f "$KNOWLEDGE_HANDOFF_OUT"
    [ -z "$handoff" ] || printf '%s\n' "$handoff" > "$KNOWLEDGE_HANDOFF_OUT"
  fi
  if [ "$(tree_state)" != "$before" ]; then
    echo "knowledge-librarian: the retrieval call changed files in the checkout - refusing" >&2
    rm -rf "$scratch"
    exit 3
  fi
  line="$(bash .lokf/scripts/knowledge-report.sh retrieval "$scratch/reply" 2>/dev/null | sed -n 1p)"
  rm -rf "$scratch"
  echo "knowledge-librarian: $line"
  if [ -n "${KNOWLEDGE_RETRIEVAL_OUT:-}" ]; then rm -f "$KNOWLEDGE_RETRIEVAL_OUT"; printf '%s\n' "$line" > "$KNOWLEDGE_RETRIEVAL_OUT"; fi
}

# The files the workflow reads after this script: the hand-off and the
# retrieval score. The agent could write anywhere this job can, those paths
# included, and could leave a link there that sends a later write into the
# checkout. So each is removed once the agent returns, and what the workflow
# reads was put there after the agent, by the pen or the retrieval test.
clear_outputs() {
  local out
  for out in "${KNOWLEDGE_HANDOFF_OUT:-}" "${KNOWLEDGE_RETRIEVAL_OUT:-}"; do
    [ -z "$out" ] || rm -f "$out"
  done
}

main() {
  # A run with nothing to do ends here, before the agent is called, when the
  # caller allows it. The workflow sets KNOWLEDGE_SKIP_QUIET on a scheduled
  # run. knowledge-report.sh decides, from frontmatter and history, and runs
  # from the checkout before any agent has touched it. Anything but a clear
  # "quiet" runs the agent as before: work waiting, no history, or a report
  # script too old to know the command.
  if [ "${KNOWLEDGE_SKIP_QUIET:-}" = true ] && [ -f .lokf/scripts/knowledge-report.sh ]; then
    local verdict rc=0
    verdict="$(bash .lokf/scripts/knowledge-report.sh quiet 2>/dev/null)" || rc=$?
    case "$rc" in
      0) echo "knowledge-librarian: $verdict - the agent is not run this time"; return 0 ;;
      1) echo "knowledge-librarian: $verdict" ;;
      *) echo "knowledge-librarian: knowledge-report.sh could not say whether this run is quiet, so the agent runs" ;;
    esac
  fi

  # A local, well-formed AGENT_CLI can still run code that writes anywhere in
  # this job's checkout, which is what the check above is for. But that check
  # is only as good as the `git status` it reads. An agent that sets
  # core.fsmonitor or core.hooksPath in .git/config, or drops a file in
  # .git/hooks/, gets it run by *this script's own* later git commands. The
  # workflow's detect and package steps share this job's checkout and run it
  # too, after this script exits.
  #
  # So snapshot both around the agent call and restore them on every exit
  # (success, agent failure, cancellation), and neither this check nor
  # anything the workflow does afterwards can be defeated or taken over that
  # way. Only SIGKILL escapes this, and a runner that kills the step with it
  # also discards the job, so nothing reads the checkout after it. This is
  # defence in depth, not the backstop: a person reviewing the pull request
  # before merge is.
  snapshot_git_state
  trap restore_git_state EXIT
  # A signal caught by a trap does not end the shell, so these turn it into an
  # exit, which runs the EXIT trap above. Bash delivers them only once the
  # foreground agent has itself exited, so the restore never races the agent.
  trap 'exit 129' HUP
  trap 'exit 130' INT
  trap 'exit 143' TERM

  local before_outside before_all
  before_outside="$(outside_bundle)"
  before_all="$(changed_paths)"

  echo "knowledge-librarian: refreshing the .lokf/ bundle via AGENT_CLI"
  # The subshell exports the key under the agent's own name and then becomes
  # the agent, so only the agent's environment carries it. The key never
  # appears in a process's argument list.
  (
    if [ -n "$key_name" ]; then export "$key_name=$agent_key"; fi
    run_agent "$prompt"
  )

  # Restore before the checks below read git, not only at exit.
  restore_git_state
  clear_outputs

  # The agent's one output is .lokf/patch.yaml. Anything else it changed,
  # inside the bundle or out, is refused before the file is applied: the
  # bundle changes only through knowledge-apply.sh, so a direct edit never
  # reaches the publish job.
  local touched
  touched="$(comm -13 <(printf '%s\n' "$before_all") <(changed_paths))"
  if [ -n "${touched//[$'\n\t ']/}" ]; then
    echo "knowledge-librarian: the agent changed files other than .lokf/patch.yaml - refusing:" >&2
    printf '%s\n' "$touched" | sed '/^$/d; s/^/  /' >&2
    rm -f .lokf/patch.yaml
    exit 3
  fi
  if [ -f .lokf/patch.yaml ]; then
    echo "knowledge-librarian: applying .lokf/patch.yaml with knowledge-apply.sh"
    if ! bash .lokf/scripts/knowledge-apply.sh ${KNOWLEDGE_HANDOFF_OUT:+--handoff "$KNOWLEDGE_HANDOFF_OUT"} .lokf/patch.yaml; then
      echo "knowledge-librarian: knowledge-apply.sh refused the patch, so nothing was written" >&2
      rm -f .lokf/patch.yaml
      exit 4
    fi
  else
    echo "knowledge-librarian: the agent wrote no .lokf/patch.yaml, so the bundle is unchanged"
  fi

  local stray
  stray="$(comm -13 <(printf '%s\n' "$before_outside") <(outside_bundle))"
  if [ -n "${stray//[$'\n\t ']/}" ]; then
    echo "knowledge-librarian: agent modified paths outside .lokf/knowledge/ - refusing:" >&2
    printf '%s\n' "$stray" | sed '/^$/d; s/^/  /' >&2
    exit 3
  fi

  # What the pen refuses before it writes, checked on the result: the change
  # adds, changes and removes no person's event or note, and rewrites no text
  # a person wrote. The publish job runs the same check on a checkout the
  # agent never shared; this one fails fast.
  if [ -f .lokf/scripts/knowledge-provenance.sh ] && ! bash .lokf/scripts/knowledge-provenance.sh --unattended; then
    echo "knowledge-librarian: the change touches a person's record - refusing" >&2
    exit 3
  fi

  if [ "${KNOWLEDGE_RETRIEVAL:-}" = true ] && [ -f .lokf/scripts/knowledge-report.sh ]; then
    score_retrieval
  fi
}

main "$@"
