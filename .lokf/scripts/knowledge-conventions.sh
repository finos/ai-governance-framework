#!/usr/bin/env bash
# Conventions of a LOKF bundle that `lokf validate` cannot see.
#
# The toolkit checks frontmatter against the schema and reads a concept body
# as an opaque string; it never reads log.md. The four skills and both
# Obsidian plugins rely on a few conventions beyond that, and each has been
# broken at least once by an agent that had been told the rule in prose:
#
#   1. log.md has one `## YYYY-MM-DD` heading per day: the bare ISO date,
#      newest first, no duplicates. OKF §9 makes the date form a MUST, and the
#      KTL Curator plugin finds today's section by that exact heading.
#   2. Every `at:` is a quoted string, and a UTC time to the second, as
#      `date -u +%Y-%m-%dT%H:%M:%SZ` writes it. Unquoted, YAML hands the
#      toolkit a datetime object and the curator's string comparison a
#      surprise. In another shape the readers disagree. The report cannot
#      read a lower-case `t`, which the federation build reads, and no script
#      reads a lower-case `z`. The workspace's stored queries compare times
#      as written, so they put an offset or a fraction out of order. A
#      person's event that no script reads would confirm every later edit.
#   3. `verified` is a list, never a bare `{ by, at }` mapping, and carries at
#      most one `process:ktl-librarian` event: the librarian replaces its
#      own, and does not stack them.
#   4. A bullet under `## Open questions` is `- YYYY-MM-DD, <actor>: ...`, the
#      shape the curator and both plugins write and read; the curator quotes
#      the first bullet, so a trailing signature would become the question.
#   5. Every `resource:` that is not a URL names a file or directory that
#      exists, relative to the repository root (the nearest directory holding
#      `.lokf/`; failing that, the bundle's parent). A source that has gone
#      should fail the gate now, not wait for the librarian's next refresh.
#      URLs are never fetched.
#   6. A commit-shaped `revision` on a `generated` or `verified` event names
#      a commit in this repository that holds the concept's local `resource`.
#      The field arrived in lokf 0.9.0, and the 0.8.0 validator rejects it,
#      so the skills write it only where `lokf validate` accepts it. ETags,
#      digests and version labels pin URLs and are not checked.
#      The rule needs the full history, and reports a shallow clone.
#   7. One file per `id`. A sync client's conflict copy (OneDrive, Dropbox,
#      Drive, iCloud) or a pasted duplicate carries the same `id`, passes
#      `lokf validate`, and silently merges into the original in the graph.
#   8. Every path in the bundle is lowercase: a-z, 0-9, `.`, `_`, `-`. Two
#      paths that differ only by case collide on Windows, macOS and SharePoint,
#      and a space, a parenthesis or an upper-case host name in a file name is
#      how every sync client names a conflict copy.
#   9. Every concept is a file of its own, not a symbolic link, and starts with
#      a `---` frontmatter block that closes, with no byte order mark in front
#      of it and no `---` inside it. A BOM from a web editor or Notepad, or a
#      file with no block, would otherwise pass this script unread. The toolkit
#      reads a link as the file it points at, and ends the block at the first
#      `---` it meets, so either one would have it read what the gates do not.
#  10. The fields the provenance gates read line by line are spelt so a line
#      reader and a parser see the same thing. They are `id`, `verified`,
#      `generated`, and `by`, `at` and `revision` on an event, and they carry
#      no tags, anchors, aliases, merge keys, quoted or explicit keys, space
#      before the colon, escapes, block scalars or values spanning lines or
#      below their key, and no comment beside them or inside a flow form. The
#      block is not indented whole or one flow mapping, and holds no line
#      break but a line feed. Each of those is valid YAML that `lokf validate`
#      accepts and a line reader cannot follow, and both gates refuse an event
#      they cannot read. A comment is read as part of the value: the actor is
#      then a login nobody holds, and the time one no script can compare, so
#      the concept never reads as edited since.
#  11. No `at:` is later than the commit that first recorded it, or, before
#      it is committed, than now. A time written ahead of the clock, such as
#      local time labelled `Z` or a round placeholder, sorts after the edits
#      and confirmations that really followed it. So a concept reads as edited
#      since it was confirmed when it was not. Each value is looked up in the
#      concept's own history. A rename or a shallow clone can only make that
#      commit look later, so the rule can miss a bad time but never flags a
#      good one. A time with an offset other than `Z` is not compared. The
#      rule needs git, and outside it the rule is skipped.
#  12. An index bullet that names a concept carries that concept's title and
#      description, in the folder's index.md and in the root's. ktl-docent
#      chooses what to open from the bullets alone, so one left behind by an
#      edit hides the concept it names. knowledge-apply.sh keeps the three
#      equal for every concept it writes; this is the check for every other
#      writer, and its `reindex` operation is the repair. A concept no index
#      lists is not a finding.
#  13. A concept labelled confirmed by a person still says what that person
#      confirmed. The label rests on `generated.at` being no later than the
#      confirmation, so an edit that leaves `generated` alone keeps the label
#      while the text moves on. After the commit that recorded the latest
#      confirmation, a change must move `generated.at` past it, which turns
#      the label to edited since. That holds for a change to the body outside
#      `## Open questions` and KTL Registrar's lokf:related block. It holds
#      for a change to any frontmatter field but `generated`, `verified`,
#      `status`, `stale_after`, `timestamp` and `usage_window`.
#
#      knowledge-apply.sh restamps every change it writes; this is the check
#      for every other writer. Parsed values are compared, so a requoted value
#      is no change. The newest commit that recorded the confirmation's time
#      is the one compared with, so the rule can miss an edit but never flags
#      a concept the person saw. The rule needs git, and outside it the rule
#      is skipped.
#  14. A commit that records a person's confirmation changes the verdict, not
#      what the concept says. Rule 13 compares with the commit that recorded
#      the confirmation, so an edit made in that same commit reads as
#      confirmed. With `--since <commit>`, each commit after it is read
#      against every parent. One that adds a `human:` event no parent holds
#      may change the concept's claims only when `generated.by` names that
#      same person, which is how Correct now records an edit the person made.
#      The registrar's gate passes the pull request's base. Without
#      `--since` the rule is skipped, since on a branch's whole history a
#      squash merge folds a librarian's edit and a later confirmation into
#      one commit.
#  15. Every concept names where it came from: a top-level `resource`, or a
#      `sources` list with an entry. The librarian's refresh follows those
#      back to the origin, and the coverage count credits a file to a concept
#      through them, so a concept with neither can be neither re-verified
#      nor counted.
#  16. A footnote joins a claim to a source. In a body, outside a code fence
#      or a code span, each `[^label]` reference and each `[^label]: text`
#      definition line uses the `id` of one of the concept's `sources`
#      entries. Each id is cited at least once, each cited label has its
#      definition line, and the definition holds the entry's `resource`
#      verbatim, so a reader sees the source beside the claim and the
#      footnote cannot drift from its entry. An id is lowercase a-z, 0-9,
#      `.`, `_` and `-`, as rule 8 has a path. It names one resource across
#      the bundle: under LOKF's published context a Source id becomes the
#      IRI of the source's node under the bundle base, so one id for two
#      resources merges them into one RDF node. OKF v0.2 section 5.1 says a
#      footnote whose label equals `id` attributes the claim to that entry.
#  17. A logged write has a file behind it. Each `**Added**` and
#      `**Deprecation**` bullet in log.md names a concept the bundle holds:
#      by its first link, read as knowledge-report.sh reads a Deprecation
#      line, or by starting with a concept's title, as the pen writes an
#      Added line. With `--since <commit>` the bullets added since the base
#      are read; without it, those under the newest day heading, where the
#      latest run's claims sit. A `**Removal**` bullet under the same or a
#      newer day heading excuses a bullet whose concept is gone.
#  18. Each `exclusions` entry (lokf 0.9.0 and later) gives a `reason` that is
#      not blank, and no material is both a source and an exclusion of one
#      concept. An exclusion records that someone looked at a material and
#      set it aside, so a blank reason leaves a reviewer nothing to check, and
#      a material listed both ways is derived from and left out at once.
#      Paths are compared as `lokf validate` compares them, so `./docs/a.md`,
#      `docs/a.md` and `docs/a.md/` name one material. The toolkit only warns
#      of the second; this gate fails it.
#
# Rules 2, 3, 8, 10 and 18 are house rules, stricter than the format. OKF
# permits an unquoted datetime, a bare `verified` mapping, any file name and
# any YAML, and LOKF a blank reason and a material listed both ways.
# Every reader here reads a bare mapping as a one-item list, as it MUST: the
# toolkit, both plugins and the gates. This bundle asks more of itself so that:
#   - an event is always appended to a list and never converted first;
#   - a datetime reaches every consumer as the same string;
#   - a name never collides on a case-insensitive host;
#   - an event reads the same to a line reader as to a parser;
#   - an exclusion always says why, and never contradicts a source.
# A bundle written to the letter of OKF may fail them; that is a policy of the
# gate, not a defect in the bundle.
#
# Rules 2, 3, 7, 9, 10, 12 and 18 are checks on a document's YAML that need a
# parser, and rule 4 is checked with them. So the Python half,
# knowledge-conventions.py in the same directory, checks them. This shell
# half checks rules 1, 5, 6, 8 and 11 itself: they are git and filesystem
# facts, which grep and awk can check wherever bash and git run, with no
# toolchain. Rules 13 and 14 read git too, but they compare parsed values,
# so the Python half checks them as well. Rules 15, 16 and 17 join parsed
# frontmatter to a body and to log.md, so the Python half checks them too.
#
# This script runs the Python half with the sidecar's .venv when the .venv
# holds pyyaml and is Python 3.9 or later, and otherwise through `uv run`
# after uv_ready. knowledge-apply.sh explains both. Without uv, the shell
# half still runs and says so. When uv cannot install the packages, or a
# runner cannot start the Python half, the script reports a runner failure,
# not a finding, and exits 2.
#
# Files are read with carriage returns removed and a leading byte order mark
# stripped, so a Windows checkout (`core.autocrlf`) reads the same as CI. The
# sidecar's `.lokf/.gitattributes` keeps tracked files on LF; rule 9 still
# reports a BOM, because other readers do not strip it.
#
# Usage: knowledge-conventions.sh [bundle-dir] [--since <commit>]   (default:
# knowledge, i.e. run from .lokf/). Exit 1 with one line per finding; nothing
# else is written. Exit 2 when the Python half could not run, with the
# reason on stderr.
[ -n "${BASH_VERSION:-}" ] || { echo "run this with bash: bash ${0##*/} [bundle-dir] [--since <commit>]" >&2; exit 2; }
set -euo pipefail

# The bundle directory may be a link, on a host that keeps the real folder as
# a visible knowledge_bundle/. Handed a link bare, find never enters it, so
# the trailing slash below is what makes it read the files.
bundle="${1:-knowledge}"; bundle="${bundle%/}"
since=""
if [ $# -gt 1 ]; then
  { [ $# -eq 3 ] && [ "$2" = "--since" ] && [ -n "$3" ]; } || { echo "usage: ${0##*/} [bundle-dir] [--since <commit>]" >&2; exit 2; }
  since="$3"
fi
[ -d "$bundle" ] || { echo "no bundle directory at $bundle" >&2; exit 2; }
fail=0
say() { echo "$1"; fail=1; }

# POSIX tools only (head -c, od, tail -c, tr), so this reads the same on
# Linux, macOS and Git for Windows.
has_bom() { [ "$(head -c 3 "$1" | od -An -tx1 | tr -d ' \n')" = "efbbbf" ]; }
clean() { if has_bom "$1"; then tail -c +4 "$1"; else cat "$1"; fi | tr -d '\r'; }

# ---- 1. log.md headings ----------------------------------------------------
log="$bundle/log.md"
if [ -f "$log" ]; then
  if has_bom "$log"; then say "$log: starts with a byte order mark - save as UTF-8 without BOM"; fi
  while IFS= read -r line; do
    say "$log: heading is not a bare ISO date: $line"
  done < <(clean "$log" | grep -E '^## ' | grep -vE '^## [0-9]{4}-[0-9]{2}-[0-9]{2}$' || true)
  dates="$(clean "$log" | grep -oE '^## [0-9]{4}-[0-9]{2}-[0-9]{2}$' | cut -c4- || true)"
  if [ -n "$dates" ]; then
    if ! printf '%s\n' "$dates" | sort -rc 2>/dev/null; then
      say "$log: day headings are not newest-first"
    fi
    while IFS= read -r d; do
      [ -n "$d" ] && say "$log: day $d has more than one heading - add bullets under the existing one"
    done < <(printf '%s\n' "$dates" | uniq -d)
  fi
fi

# ---- 2-9. concept files -----------------------------------------------------
# Repository root for rule 5: the nearest ancestor holding `.lokf/`, else the
# bundle's parent (a bare bundle handed to this script on its own).
real="$(cd "$bundle" && pwd -P)"
root="$(dirname "$real")"
d="$real"
while [ "$d" != "/" ]; do
  if [ -d "$d/.lokf" ]; then root="$d"; break; fi
  d="$(dirname "$d")"
done
# Rule 6 needs git: whether the root is in a work tree, and whether that tree
# has its full history. Outside git the rule is skipped; a shallow clone is
# reported, because a pin the script cannot resolve is not a pin it has checked.
gitroot="$(git -C "$root" rev-parse --show-toplevel 2>/dev/null || true)"
shallow="$(git -C "$root" rev-parse --is-shallow-repository 2>/dev/null || echo false)"
now="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
# Rule 11's comparison. Times are compared as strings, which is exact once
# both are in the one UTC shape: a bare date is its midnight, minutes gain
# `:00`, fractions of a second are dropped. Anything else prints nothing and
# is not compared. History lines come first: \001 carries a commit's time,
# `+` lines are what it added. Then \002 carries now, and \003 each `at:` the
# frontmatter holds today.
# shellcheck disable=SC2016 # awk's own $0, not the shell's
rule11='
function norm(v) {
  gsub(/^["'"'"']|["'"'"']$/, "", v)
  if (v ~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/) return v "T00:00:00Z"
  if (v ~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]Z$/) return substr(v, 1, 16) ":00Z"
  if (v ~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9](\.[0-9]+)?Z$/) return substr(v, 1, 19) "Z"
  return ""
}
function value(line) {
  sub(/^[+]?[ \t]*(- )?at:[ \t]*/, "", line); sub(/[ \t]+$/, "", line)
  gsub(/^["'"'"']|["'"'"']$/, "", line)
  return line
}
/^\001/ { ct = substr($0, 2); next }
/^\002/ { now = substr($0, 2); next }
/^\003/ {
  v = value(substr($0, 2)); n = norm(v)
  if (n == "" || v in seen) next
  seen[v] = 1
  if (v in first) {
    if (n > first[v]) print "at \"" v "\" is later than the commit that recorded it (" first[v] ") - take the time from date -u when the event happens"
  } else if (n > now) {
    print "at \"" v "\" is in the future (now " now ") - take the time from date -u when the event happens"
  }
  next
}
/^[+][ \t]*(- )?at:[ \t]/ { v = value($0); if (!(v in first)) first[v] = ct }
'
while IFS= read -r f; do
  # 8. path shape, checked on every Markdown file, reserved ones included
  rel="${f#"$bundle"/}"
  if ! printf '%s\n' "$rel" | grep -qE '^([a-z0-9][a-z0-9._-]*/)*[a-z0-9][a-z0-9._-]*$'; then
    say "$f: path is not lowercase a-z, 0-9, '.', '_', '-' - case-insensitive hosts and sync conflict copies are why"
  fi
  case "$(basename "$f")" in index.md|log.md|diataxis.md) continue ;; esac
  # Frontmatter only, best effort, for 5 and 6: the text between the first two
  # `---` lines. A missing or malformed block yields nothing here and is
  # rules 2-4, 7 and 9's job below to report, not this loop's. The awk reads
  # the whole file rather than exiting at the second `---`: a CI runner that
  # ignores SIGPIPE (GitHub Actions does) turns an early-closed pipe into a
  # `tr: write error` that pipefail then makes fatal.
  fm="$(clean "$f" | awk 'NR==1 {if ($0!="---") stop=1; next} stop {next} $0=="---" {stop=1; next} {print}')"
  # 5. local resource paths exist: top-level `resource:` and `sources[].resource`
  while IFS= read -r res; do
    [ -z "$res" ] && continue
    case "$res" in *://*) continue ;; esac
    res="${res%%#*}"
    res="${res#\"}"; res="${res%\"}"; res="${res#\'}"; res="${res%\'}"
    res="${res%"${res##*[![:space:]]}"}"
    [ -z "$res" ] && continue
    case "$res" in /*) target="$res" ;; *) target="$root/$res" ;; esac
    [ -e "$target" ] || say "$f: resource not found: $res (looked at $target)"
  done < <(printf '%s\n' "$fm" | sed -nE 's/^[[:space:]]*(- )?resource:[[:space:]]*(.*[^[:space:]])[[:space:]]*$/\2/p')
  # 6. a commit-shaped `revision` names a commit that holds the concept's own
  #    local `resource`. Anything with a character outside [0-9a-f], such as
  #    an ETag, a `sha256:` digest or a version label, pins a URL and is
  #    skipped, as is every revision on a concept whose `resource` is a URL,
  #    absolute or absent.
  res="$(printf '%s\n' "$fm" | sed -nE 's/^resource:[[:space:]]*(.*[^[:space:]])[[:space:]]*$/\1/p' | sed -n 1p)"
  res="${res%%#*}"
  res="${res#\"}"; res="${res%\"}"; res="${res#\'}"; res="${res%\'}"
  res="${res%"${res##*[![:space:]]}"}"
  case "$res" in ""|*://*|/*) res="" ;; esac
  while IFS= read -r rev; do
    rev="${rev#\"}"; rev="${rev%\"}"; rev="${rev#\'}"; rev="${rev%\'}"
    case "$rev" in ""|*[!0-9a-f]*) continue ;; esac
    if [ "${#rev}" -lt 7 ] || [ -z "$res" ] || [ -z "$gitroot" ]; then continue; fi
    if [ "$shallow" = true ]; then
      say "$f: revision $rev cannot be checked in a shallow clone - check out with fetch-depth: 0"
    elif ! git -C "$root" cat-file -e "$rev:./$res" 2>/dev/null; then
      say "$f: revision $rev does not hold $res - no such commit, or the path was absent in it"
    fi
  done < <(printf '%s\n' "$fm" | sed -nE 's/^[[:space:]]*(- )?revision:[[:space:]]*(.*[^[:space:]])[[:space:]]*$/\2/p')
  # 11. no `at:` later than the commit that first recorded it. One `git log`
  #     per concept: the times of the commits that touched it, oldest first,
  #     each followed by the lines it added.
  if [ -n "$gitroot" ]; then
    abs="$(cd "$(dirname "$f")" && pwd -P)/$(basename "$f")"
    while IFS= read -r finding; do
      say "$f: $finding"
    done < <(
      {
        TZ=UTC git -C "$root" log --reverse --no-color --no-ext-diff --unified=0 -p \
          --format='%x01%cd' --date=format-local:'%Y-%m-%dT%H:%M:%SZ' -- "$abs" 2>/dev/null | tr -d '\r' || true
        printf '\002%s\n' "$now"
        printf '%s\n' "$fm" | sed -nE 's/^[[:space:]]*(- )?at:[[:space:]]*(.*[^[:space:]])[[:space:]]*$/\2/p' | awk '{ print "\003" $0 }'
      } | awk "$rule11"
    )
  fi
done < <(find "$bundle/" -name '*.md' -not -path '*/.obsidian/*' | sort)

# ---- 2, 3, 4, 7, 9, 10, 12, 13, 14, 15, 16, 17, 18. the Python half ------------
here="$(dirname "$0")"
py="$here/knowledge-conventions.py"
rules="rules 2, 3, 4, 7, 9, 10, 12, 13, 15, 16, 17 and 18"
[ -z "$since" ] || rules="rules 2, 3, 4, 7, 9, 10, 12, 13, 14, 15, 16, 17 and 18"
uvflags=(); uverr=""; uvhint="Run uv sync in .lokf/ to pin them by hash."
uv_ready() {
  local err names name again unpinned lifted=""
  command -v uv >/dev/null 2>&1 || return 1
  uv sync --offline --quiet --script "$1" >/dev/null 2>&1 && return 0
  until err="$(uv sync --color never --script "$1" ${uvflags[@]+"${uvflags[@]}"} 2>&1 >/dev/null)"; do
    names="$(printf '%s\n' "$err" | sed -n 's/^warning: \([^ ]*\) is missing an upload date.*/\1/p' | tr -d '\140' | sed 's/-[0-9].*//' | tr '[:upper:]' '[:lower:]' | tr '_.' '--' | sort -u)"
    again=""; unpinned=""
    for name in $names; do
      case " $lifted " in *" $name "*) again=1 ;; esac
      case "$name" in *[!a-z0-9-]*) unpinned="$unpinned $name"; continue ;; esac
      grep -qiE "^# dependencies = .*\"${name//-/[-_.]}==" "$1" || unpinned="$unpinned $name"
    done
    if [ -z "$names" ] || [ -n "$again$unpinned" ]; then
      uverr="$(printf '%s\n' "$err" | grep -v ' is missing an upload date' || true)"
      [ -z "$unpinned" ] || uverr+=$'\n'"${0##*/}: the package index serves no upload times for$unpinned, which the script's header does not pin with ==, so exclude-newer stays."
      return 1
    fi
    for name in $names; do uvflags+=(--exclude-newer-package "$name=false"); lifted="$lifted $name"; done
  done
  [ -z "$lifted" ] || echo "${0##*/}: the package index serves no upload times, so exclude-newer is lifted for$lifted. The versions stay pinned. $uvhint" >&2
  return 0
}
venv="$root/.lokf/.venv/bin/python"; [ -e "$venv" ] || venv="$root/.lokf/.venv/Scripts/python.exe"
runner=""
skipped=""; unrun=0
if [ -x "$venv" ] && "$venv" -c 'import sys; assert sys.version_info >= (3, 9); import yaml' >/dev/null 2>&1; then
  runner="$venv"
elif uv_ready "$py"; then
  runner=uv
elif command -v uv >/dev/null 2>&1; then
  unrun=1
  [ -z "$uverr" ] || printf '%s\n' "$uverr" >&2
  echo "$rules not checked: uv could not run $py, because it could not install its packages. Run uv sync in .lokf/ and this script uses that .venv." >&2
fi
if [ -n "$runner" ]; then
  rc=0
  if [ "$runner" = uv ]; then
    out="$(uv run --quiet ${uvflags[@]+"${uvflags[@]}"} "$py" "$bundle" ${since:+--since "$since"} 2>&1)" || rc=$?
  else
    out="$("$runner" "$py" "$bundle" ${since:+--since "$since"} 2>&1)" || rc=$?
  fi
  # The Python half exits 1 for findings. Any other failure is the runner's,
  # or a usage error, and says nothing about the bundle.
  case "$rc" in
    0) ;;
    1) printf '%s\n' "$out"; fail=1 ;;
    *) unrun=1
       printf '%s\n' "$out" >&2
       hint=""
       [ "$runner" = uv ] && hint=" Behind a package mirror, run uv sync in .lokf/ and this script uses that .venv."
       echo "$rules not checked: $runner could not run $py (exit $rc).$hint" >&2 ;;
  esac
elif [ "$unrun" -eq 0 ]; then
  skipped="$rules not checked: uv not found"
  echo "$skipped - install uv, or run $py directly with python3 3.9 or later and pyyaml" >&2
fi

if [ "$fail" -eq 0 ] && [ "$unrun" -eq 0 ]; then
  echo "OK - $bundle keeps the conventions lokf validate cannot check${skipped:+ ($skipped)}"
fi
[ "$fail" -eq 0 ] && [ "$unrun" -eq 1 ] && exit 2
exit "$fail"
