#!/usr/bin/env bash
# The pen, the librarian's only way to write the bundle. ktl-librarian
# describes each change to the bundle as an operation in .lokf/patch.yaml and
# never edits .lokf/knowledge/ itself. This script checks every operation and
# writes the files, or refuses the whole file and writes nothing. The
# scheduled wrapper runs it after the agent has finished.
#
# The rules live in the Python half beside it, knowledge-apply.py. This
# script runs it with the sidecar's own .venv when that holds pyyaml, then
# through `uv run` (the script's own header names pyyaml), then through
# python3 where pyyaml is installed. The .venv comes first because `uv sync`
# installed it from uv.lock, so a run needs no package index and each file is
# checked by hash. Each interpreter must be Python 3.9 or later. On an
# enterprise host python3 is often older, and the script would stop at its
# first line.
#
# uv_ready installs the header's packages before the run, so uv's exit 1 on
# a failed resolution never reads as findings. It tries offline first, so a
# script environment that is already complete runs with the index down. On
# an index with no upload times, as a Nexus or Artifactory mirror often is,
# uv drops each file and warns that it "is missing an upload date". Only
# then does uv_ready lift the date, round by round, for each package uv
# names that the header pins with ==, so the versions stay pinned. It turns
# uv's colour off, since FORCE_COLOR would hide that warning. Any other
# failure is not retried, nor a package uv names again once lifted.
# knowledge-conventions.sh and knowledge-ingest.sh carry the same function,
# and the contract holds the three equal.
#
# Usage: knowledge-apply.sh [--dry-run] [--keep] [--handoff <file>] [--root <repo-root>] [<patch-file>]
#        knowledge-apply.sh --format
#   --dry-run   report every finding and what would be written; write nothing
#   --keep      leave the patch file in place after applying it
#   --handoff   after applying, write the patch's lines for the reviewer to
#               <file>, or leave it empty when the patch has none
#   --root      the repository root; default: two levels above this script
#   --format    print the patch file's shape, every operation with its keys,
#               and exit, so the format comes from the script that enforces it
# Exit 0 applied (or would apply); 1 findings, nothing written; 2 usage or no runner.
[ -n "${BASH_VERSION:-}" ] || { echo "run this with bash: bash ${0##*/} [--dry-run] [--keep] [--format] [--handoff <file>] [--root <dir>] [<patch-file>]" >&2; exit 2; }
set -u
usage() { echo "usage: ${0##*/} [--dry-run] [--keep] [--format] [--handoff <file>] [--root <dir>] [<patch-file>]" >&2; exit 2; }
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
root=""
args=()
while [ $# -gt 0 ]; do
  case "$1" in
    --root) [ $# -ge 2 ] || usage; root="$2"; shift 2 ;;
    --handoff) [ $# -ge 2 ] || usage; args+=("$1" "$2"); shift 2 ;;
    --dry-run|--keep|--format) args+=("$1"); shift ;;
    -h|--help) usage ;;
    --) shift; while [ $# -gt 0 ]; do args+=("$1"); shift; done ;;
    -*) echo "unknown option: $1" >&2; usage ;;
    *) args+=("$1"); shift ;;
  esac
done
[ -n "$root" ] || root="$(cd "$here/../.." && pwd)"
py="$here/knowledge-apply.py"
[ -f "$py" ] || { echo "knowledge-apply: $py is missing beside this script; run ktl-sidecar's repair path" >&2; exit 2; }
usable() { command -v "$1" >/dev/null 2>&1 && "$1" -c 'import sys; assert sys.version_info >= (3, 9); import yaml' >/dev/null 2>&1; }
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
if usable "$venv"; then
  exec "$venv" "$py" --root "$root" ${args[@]+"${args[@]}"}
elif uv_ready "$py"; then
  exec uv run --quiet ${uvflags[@]+"${uvflags[@]}"} "$py" --root "$root" ${args[@]+"${args[@]}"}
elif usable python3; then
  [ -z "$uverr" ] || echo "knowledge-apply: uv could not install pyyaml, so this run uses python3's own" >&2
  exec python3 "$py" --root "$root" ${args[@]+"${args[@]}"}
fi
[ -z "$uverr" ] || printf '%s\n' "$uverr" >&2
echo "knowledge-apply: needs the sidecar's .venv (uv sync in .lokf/), uv that can install pyyaml, or python3 3.9 or later with pyyaml; nothing was written. The sidecar's references/prerequisites.md says who installs uv." >&2
exit 2
