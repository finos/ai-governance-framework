#!/usr/bin/env bash
# Open an issue for a failed upstream-watch check, or comment on the open
# issue with the same title, so a weekly finding is one issue, not many.
#
# The body is the check's Markdown report from "$RUNNER_TEMP/report.md", or
# a note that the check stopped before writing one, plus a link to the run.
#
# Usage (in a workflow step): TITLE=... GH_TOKEN=... .github/scripts/report-issue.sh
set -euo pipefail

: "${TITLE:?set TITLE to the issue title}"
report="${RUNNER_TEMP:?}/report.md"
body="${RUNNER_TEMP}/issue-body.md"

{
  if [ -s "$report" ]; then
    cat "$report"
  else
    echo "The check stopped before writing a report, for example on a network error."
  fi
  echo
  echo "Run: ${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID}"
} > "$body"

# gh's --search is fuzzy, so match the exact title before reusing an issue.
number="$(gh issue list --repo "$GITHUB_REPOSITORY" --state open \
  --search "in:title \"$TITLE\"" --json number,title \
  --jq 'map(select(.title == env.TITLE)) | .[0].number // empty')"

if [ -n "$number" ]; then
  gh issue comment "$number" --repo "$GITHUB_REPOSITORY" --body-file "$body"
  echo "Commented on issue #$number."
else
  gh issue create --repo "$GITHUB_REPOSITORY" --title "$TITLE" --body-file "$body"
fi
