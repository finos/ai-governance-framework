#!/usr/bin/env bash
# Record one reader-feedback entry in .lokf/feedback.md without reading it.
#
# ktl-docent appends a Miss or a Disagreement here and ktl-librarian consumes
# it. Entries already in the file are other readers' reports: free text that
# can come from someone with no access to this repository. The file is kept
# newest first, so adding an entry used to mean the docent read it, edited it
# and wrote it back. Those reports then entered the session of an agent that
# had just been fetching URLs and reading repository files, held off by
# nothing but a line of prose telling it not to act on them. This script does
# the insertion instead. The caller hands over its own entry and never opens
# the file, so no other reader's text reaches the model. The guard is
# the call, not a rule an agent has to keep (docs/threat-model.md,
# "Prompt-injection guards").
#
# It prints one line, with the kind, the date and how many entries now wait,
# and never any entry's text, the new one included. A caller that wants to show
# the reader what it recorded already has that text; it does not need this
# file to tell it.
#
# Bash 3.2 and POSIX tools only, so it runs on macOS's stock bash and on Git
# for Windows, like the other scripts here.
#
# Usage:
#   knowledge-feedback.sh [--root <dir>] [--for <login>] [--concept <path>] <kind> <text>
#
#   kind    Miss or Disagreement, in any letter case, and nothing else: the
#           two shapes ktl-librarian knows how to consume.
#   text    the entry itself, one argument. Whitespace is collapsed, so a
#           multi-line string is still written as one line per entry.
#   --for   an authenticated login (gh api user --jq .login, or glab), which
#           records the entry as `- docent, for human:<login>`. Left out, the
#           entry is `- docent` alone. It is never a name typed in
#           conversation and never git config user.name: the attribution is
#           only worth carrying if the forge stands behind it.
#   --root  the repository root (default: the nearest ancestor of the current
#           directory holding .lokf/, else the current directory).
#   --concept  with a Disagreement only, the bundle path of the concept the
#           reader disputes, such as services/orders-api.md. It must name a
#           concept file under .lokf/knowledge, in the bundle's lowercase
#           spelling. The entry then reads `- **Disagreement** (on `<path>`) -`,
#           and knowledge-report.sh labels that concept as disputed until the
#           librarian handles the entry. The report reads the path and never
#           the text.
#
# The day heading is today in UTC, as the bundle's own timestamps are, so two
# machines in different zones file one day under one heading.
#
# Exit:
#   0  recorded;
#   2  the call was wrong, and nothing was written;
#   1  the file could not be written (a read-only .lokf/, most often, or
#      another run holding it), and the caller should tell the reader the gap
#      out loud instead.
[ -n "${BASH_VERSION:-}" ] || { echo "run this with bash: bash ${0##*/} [--root <dir>] [--for <login>] <kind> <text>" >&2; exit 2; }
set -u
# A-Z, a-z and 0-9 in a case glob mean the ASCII letters and digits, not
# whatever a locale collates between them, so a login check below cannot be
# widened by the host's locale. A no-op where the option is unknown (bash 3.2).
shopt -s globasciiranges 2>/dev/null || :

usage() {
  echo "usage: ${0##*/} [--root <dir>] [--for <login>] [--concept <path>] <Miss|Disagreement> <text>" >&2
  exit 2
}

root=""; asker=""; concept=""
while [ $# -gt 0 ]; do
  case "$1" in
    --root) [ $# -ge 2 ] || usage; root="$2"; shift 2 ;;
    --for)  [ $# -ge 2 ] || usage; asker="$2"; shift 2 ;;
    --concept) [ $# -ge 2 ] || usage; concept="$2"; shift 2 ;;
    -h|--help) usage ;;
    --) shift; break ;;
    -*) echo "unknown option: $1" >&2; usage ;;
    *) break ;;
  esac
done
[ $# -eq 2 ] || usage
kind="$1"; text="$2"

# ---- what the librarian can consume ----------------------------------------
# A third kind would reach the librarian as an entry it has no rule for, so
# the set is closed here rather than left to whatever the caller typed. Letter
# case is the caller's slip, not a third kind, and is put right.
case "$kind" in
  [Mm][Ii][Ss][Ss]) kind=Miss ;;
  [Dd][Ii][Ss][Aa][Gg][Rr][Ee][Ee][Mm][Ee][Nn][Tt]) kind=Disagreement ;;
  *) echo "kind must be Miss or Disagreement, not '$kind'" >&2; exit 2 ;;
esac

# The attribution is the one field a later reader may take as evidence that a
# named person asked. So it must hold only a login's characters before it is
# written, the shape both provenance gates accept. A login they would pass is
# then never refused here, and one they would refuse never gets in.
if [ -n "$asker" ]; then
  case "$asker" in
    *[!A-Za-z0-9._-]*|[!A-Za-z0-9]*)
      echo "--for takes a forge login (a letter or digit, then letters, digits, '.', '_' or '-'), not '$asker'" >&2; exit 2 ;;
  esac
fi

# The concept a Disagreement names is the one field a program reads back:
# knowledge-report.sh labels that concept as disputed while the entry waits.
# So it holds only the bundle's own path spelling (conventions rule 8), no
# `..`, and must name a concept file that exists. A Miss names a gap, not a
# concept, so it takes none.
if [ -n "$concept" ]; then
  [ "$kind" = Disagreement ] || { echo "--concept goes with a Disagreement only; a Miss names a gap, not a concept the bundle holds" >&2; exit 2; }
  case "$concept" in
    *[!a-z0-9._/-]*|[!a-z0-9]*|*..*|*/|*//*|*/./*)
      echo "--concept takes a concept's path in the bundle, in lowercase with no '..' or '.' segment, such as services/orders-api.md, not '$concept'" >&2; exit 2 ;;
  esac
  case "$concept" in *.md) ;; *) echo "--concept takes the concept's file, ending in .md, not '$concept'" >&2; exit 2 ;; esac
  case "${concept##*/}" in index.md|log.md) echo "--concept takes a concept, not the bundle's $concept" >&2; exit 2 ;; esac
fi

# One entry is one line. Collapse every whitespace run, drop control
# characters, and trim: a caller that passes a paragraph still cannot break
# the file's shape or forge a second entry with an embedded newline.
text="$(printf '%s' "$text" | tr -d '\000-\010\013\014\016-\037\177' | tr '\t\n\r' '   ' | sed -e 's/  */ /g' -e 's/^ //' -e 's/ $//')"
[ -n "$text" ] || { echo "the entry text is empty" >&2; exit 2; }

# ---- root ------------------------------------------------------------------
if [ -z "$root" ]; then
  d="$(pwd -P)"; root="$d"
  while [ "$d" != "/" ]; do
    if [ -d "$d/.lokf" ]; then root="$d"; break; fi
    d="$(dirname "$d")"
  done
fi
root="$(cd "$root" 2>/dev/null && pwd -P)" || { echo "no such directory: $root" >&2; exit 2; }
# Feedback is a report against a bundle. With no bundle there is nothing for
# the librarian to fix, and ktl-docent is told to say so instead of writing.
[ -d "$root/.lokf/knowledge" ] || { echo "no .lokf/knowledge under $root - no bundle to record a gap against; say the gap out loud, and that ktl-sidecar can create one" >&2; exit 2; }
if [ -n "$concept" ] && [ ! -f "$root/.lokf/knowledge/$concept" ]; then
  echo "--concept names no concept in this bundle: $concept - record the Disagreement without it" >&2; exit 2
fi

file="$root/.lokf/feedback.md"
tmp="$file.$$"
lock="$file.lock"
today="$(date -u +%Y-%m-%d)"
entry="- **$kind**${concept:+ (on \`$concept\`)} - $text - docent${asker:+, for human:$asker}"

# ---- the file --------------------------------------------------------------
readonly_bundle() {
  echo "cannot write $file - if .lokf/ is read-only, say the gap out loud to the reader instead" >&2
  exit 1
}
# The rewrite below writes a temporary file beside this one, so the directory
# has to be writable even when the file itself already is.
[ -w "$root/.lokf" ] || readonly_bundle

# Two runs at once, such as parallel agents in one checkout, would each read
# the file, and the second mv would drop the first entry without a word. A
# directory is the one lock every platform here creates atomically. A run
# killed before it can clean up leaves it behind; the message says what to
# remove. When mkdir fails and no lock is there, nothing can be created here,
# on a read-only mount that -w did not see, and that is the other message.
tries=0
until mkdir "$lock" 2>/dev/null; do
  [ -d "$lock" ] || readonly_bundle
  tries=$((tries + 1))
  if [ "$tries" -ge 5 ]; then
    echo "another run holds $lock - if nothing else is recording feedback, remove that directory and try again" >&2
    exit 1
  fi
  sleep 1
done
trap 'rmdir "$lock" 2>/dev/null; rm -f "$tmp"' EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

# feedback.md is not knowledge and has no frontmatter; it appears the first
# time a reader's agent records a gap, which may be this call.
if [ ! -s "$file" ]; then
  {
    echo "# Reader feedback for the librarian"
    echo ""
    echo "Written by ktl-docent; consumed and cleared by ktl-librarian on its next run. Newest first. One line per entry."
  } > "$file" 2>/dev/null || readonly_bundle
fi
[ -w "$file" ] || readonly_bundle

# Newest first, which is why this cannot be a plain append: today goes above
# every older day and its entry above today's earlier ones. The entry is
# passed in the environment rather than through -v, which would read a
# backslash in the text as an escape.
KF_ENTRY="$entry" awk -v hdr="## $today" '
  BEGIN { entry = ENVIRON["KF_ENTRY"]; done = 0; skipblank = 0; last = "" }
  # Headings are days, newest first, and ISO dates order as strings. Today
  # goes under the first heading that is today, or above the first that is
  # older. A heading after today, from another machine on a clock ahead of
  # this one or from a wrong clock, stays where it is. So the file keeps its
  # order instead of gaining a second heading for today further down.
  /^## / && done == 0 {
    h = $0; sub(/[ \t\r]+$/, "", h)
    if (h == hdr) { print hdr; print ""; print entry; skipblank = 1; done = 1; next }
    if (h < hdr) { print hdr; print ""; print entry; print ""; print; last = $0; done = 1; next }
  }
  # Skip the blank line that followed that heading: we printed our own.
  skipblank == 1 { skipblank = 0; if ($0 ~ /^[ \t\r]*$/) next }
  { print; last = $0 }
  # No heading today could go above: a file that has only ever held its
  # intro, or whose every day is after today.
  END { if (done == 0) { if (last != "" && last != "\r") print ""; print hdr; print ""; print entry } }
' "$file" > "$tmp" || { echo "could not record the entry in $file" >&2; exit 1; }
mv "$tmp" "$file" || { echo "could not record the entry in $file" >&2; exit 1; }

# The same expression ktl-curator counts with, so the two never disagree about
# how many entries are waiting. It reads no entry's text, and neither does the
# caller from this line.
waiting="$(grep -c '^- \*\*' "$file" 2>/dev/null || true)"
printf 'recorded: %s under %s in .lokf/feedback.md (%s waiting for the librarian)\n' "$kind" "$today" "${waiting:-1}"
