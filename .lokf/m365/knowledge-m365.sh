#!/usr/bin/env bash
# Build the Microsoft 365 Copilot custom skills: one per instructions file
# beside this script, each with a snapshot of the knowledge bundle inside.
#
# Copilot runs a skill with no repository, shell or network, so the bundle
# goes inside it. A new read-only role is just another .md file here.
# The release workflow runs this and attaches each zip; elsewhere, run it by
# hand. Nothing is written if any skill breaks Copilot's limits, and neither
# the source bundle nor an earlier build is ever touched.
#
# Usage: .lokf/m365/knowledge-m365.sh [--repo-url URL] [--ref REF] <bundle-dir> <out-dir>
#   <bundle-dir>  the bundle folder (.lokf/knowledge); in a git clone, only
#                 its tracked files are taken
#   <out-dir>     where each <name>/ and <name>.zip is created; none may
#                 exist there yet
#   --repo-url    the repository's https URL, for the source links and the
#                 place to report gaps; unset means "not recorded"
#   --ref         the tag or commit the bundle was taken at; unset means
#                 "not recorded"
#   SOURCE_DATE_EPOCH  seconds since the epoch: the build date and every
#                 file time, so one input gives one zip; unset means now
#
#   .lokf/m365/knowledge-m365.sh --repo-url https://github.com/o/r --ref v1.2.0 .lokf/knowledge ./dist
#
# Exit 0 when built, 1 when a skill breaks a limit (nothing is left behind),
# 2 when the arguments or the instructions files are wrong.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

usage() {
  echo "usage: .lokf/m365/knowledge-m365.sh [--repo-url URL] [--ref REF] <bundle-dir> <out-dir>" >&2
  exit 2
}

repo_url=""; ref=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-url) [[ $# -ge 2 ]] || usage; repo_url="$2"; shift 2 ;;
    --ref) [[ $# -ge 2 ]] || usage; ref="$2"; shift 2 ;;
    -h|--help) usage ;;
    --) shift; break ;;
    -*) echo "build: unknown option $1" >&2; usage ;;
    *) break ;;
  esac
done
[[ $# -eq 2 ]] || usage
bundle="$1"; out_parent="$2"

if [[ -n "$repo_url" && ! "$repo_url" =~ ^https://[A-Za-z0-9.-]+(:[0-9]+)?/[A-Za-z0-9._/-]+$ ]]; then
  echo "build: --repo-url must be a plain https URL, got '$repo_url'" >&2
  exit 2
fi
if [[ -n "$ref" && ! "$ref" =~ ^[A-Za-z0-9._/-]+$ ]]; then
  echo "build: --ref must be a tag or commit, got '$ref'" >&2
  exit 2
fi
epoch="${SOURCE_DATE_EPOCH:-$(date +%s)}"
if [[ ! "$epoch" =~ ^[0-9]+$ ]]; then
  echo "build: SOURCE_DATE_EPOCH must be seconds since the epoch, got '$epoch'" >&2
  exit 2
fi
# GNU date reads -d @<epoch>; BSD date (macOS) reads -r <epoch>.
built="$(date -u -d "@$epoch" +%Y-%m-%d 2>/dev/null || date -u -r "$epoch" +%Y-%m-%d)"
stamp() { touch -h -d "@$epoch" "$@" 2>/dev/null || touch -h -t "$(date -u -r "$epoch" +%Y%m%d%H%M.%S)" "$@"; }

# The instructions files: every *.md beside this script. The frontmatter's
# `name:` must be the file's basename and a name Copilot accepts, and its
# `description:` is required, 1 to 1024 characters, as Copilot requires.
# A field is read with awk (any awk, bash 3.2): one line, or a `>` or `|`
# block scalar joined into one line, then unquoted in bash.
frontmatter() {
  local v
  v="$(awk -v key="$2" '
    { sub(/\r$/, "") }
    NR == 1 { next }
    /^---$/ { exit }
    block && (/^[[:space:]]/ || /^$/) { sub(/^[[:space:]]+/, ""); if ($0 != "") out = out (out == "" ? "" : " ") $0; next }
    block { exit }
    index($0, key ":") == 1 {
      v = substr($0, length(key) + 2); sub(/^[[:space:]]+/, "", v)
      if (v ~ /^[>|][-+]?[[:space:]]*$/) { block = 1; next }
      out = v; exit
    }
    END { print out }
  ' "$1")"
  v="${v#\"}"; v="${v%\"}"; v="${v#\'}"; v="${v%\'}"
  printf '%s' "$v"
}
names=()
for f in "$here"/*.md; do
  [[ -f "$f" ]] || continue
  base="$(basename "$f" .md)"
  if [[ "$(head -1 "$f" | tr -d '\r')" != "---" ]]; then
    echo "build: $f has no frontmatter, so it cannot be a skill; move it out of this folder" >&2
    exit 2
  fi
  name="$(frontmatter "$f" name)"
  if [[ -z "$name" ]]; then
    echo "build: $f has no name: in its frontmatter, so it cannot be a skill; move it out of this folder" >&2
    exit 2
  fi
  if [[ "$name" != "$base" || ! "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
    echo "build: $f must be named after its frontmatter name '$name', in lower-case letters, digits and hyphens" >&2
    exit 2
  fi
  description="$(frontmatter "$f" description)"
  if [[ -z "$description" || ${#description} -gt 1024 ]]; then
    echo "build: $f needs a description: of 1 to 1024 characters in its frontmatter, which Copilot requires" >&2
    exit 2
  fi
  if [[ -e "$out_parent/$name" || -e "$out_parent/$name.zip" ]]; then
    echo "build: $out_parent/$name or $name.zip already exists - remove it or pick another <out-dir>; this script never overwrites a skill" >&2
    exit 2
  fi
  names+=("$name")
done
if [[ ${#names[@]} -eq 0 ]]; then
  echo "build: no instructions file beside $here/knowledge-m365.sh - ktl-sidecar lays down ktl-docent-m365.md there" >&2
  exit 2
fi

if [[ ! -d "$bundle" || ! -f "$bundle/index.md" ]]; then
  echo "build: $bundle is not a bundle folder (no index.md) - point at the bundle itself (.lokf/knowledge)" >&2
  exit 2
fi
src="$(cd "$bundle" && pwd -P)"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

# The snapshot, staged once and shared by every skill. In a git clone only
# tracked files are taken, as the release zip packs them, so an ignored file
# (an Obsidian vault's .obsidian/, a local note) never reaches the tenant.
# Elsewhere the folder is copied with links kept as links, never followed.
snap="$work/knowledge"
mkdir -p "$snap"
if git -C "$src" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  while IFS= read -r -d '' f; do
    if [[ -e "$src/$f" || -L "$src/$f" ]]; then printf '%s\0' "$f"; fi
  done < <(git -C "$src" ls-files -z -- .) \
    | tar -C "$src" --null -T - -cf - | tar -C "$snap" -xf -
else
  cp -R -P "$src/." "$snap"
fi
# A hidden file or folder is tool state (.obsidian/, .DS_Store), not a
# concept, and may hold a plugin's token. It is left out, not refused: a
# bundle opened as a vault always has .obsidian/, and whoever runs this
# build may never have seen it.
hidden="$(cd "$snap" && find . -name '.*' ! -name . -prune -print | sed 's#^\./#knowledge/#')"
if [[ -n "$hidden" ]]; then
  (cd "$snap" && find . -name '.*' ! -name . -prune -exec rm -rf {} +)
  echo "build: left out hidden files, which are tool state, not concepts: $(printf '%s' "$hidden" | tr '\n' ' ')" >&2
fi

# SNAPSHOT.md is what a skill reads first: where the concepts came from, and
# how to turn a concept's resource path into a link pinned to that revision.
source_pattern=""; report_to=""
case "$repo_url" in
  https://github.com/*|https://gitlab.com/*)
    blob="blob"; [[ "$repo_url" == https://gitlab.com/* ]] && blob="-/blob"
    if [[ -n "$ref" ]]; then source_pattern="$repo_url/$blob/$ref/<path>"; fi
    report_to="$repo_url/issues/new, titled \"Knowledge bundle feedback\", or a pull request that adds the line to \`.lokf/feedback.md\`"
    ;;
  "") report_to="the maintainers of the repository, as a line for \`.lokf/feedback.md\`" ;;
  *) report_to="the maintainers of $repo_url, as a line for \`.lokf/feedback.md\`" ;;
esac
[[ -n "$source_pattern" ]] || source_pattern="none - give the path and the revision"
{
  echo "# Snapshot"
  echo ""
  echo "- Repository: ${repo_url:-not recorded}"
  echo "- Revision: ${ref:-not recorded}"
  echo "- Built: $built (UTC)"
  echo "- Source link pattern: $source_pattern"
  echo "- Report gaps to: $report_to"
  echo ""
  echo "The concepts under \`knowledge/\` are copied unchanged from that revision. The repository may have moved on since the build date."
} > "$work/SNAPSHOT.md"

# Copilot's limits for a custom skill added through Agents Toolkit, checked
# on each assembled skill. One failure refuses the whole run, so a release
# never carries half a set.
fail=0
limit() { echo "build: $*" >&2; fail=1; }
allowed='json|xml|yaml|yml|ini|config|utf8|docx|doc|docm|pdf|txt|rtf|md|ppt|pptx|ppsm|xlsx|xls|xlsm|csv|tsv|html|htm|png|jpg|jpeg|gif|bmp|log'
summary=()
for name in "${names[@]}"; do
  stage="$work/$name"
  mkdir -p "$stage"
  cp -R -P "$snap" "$stage/knowledge"
  cp "$here/$name.md" "$stage/SKILL.md"
  cp "$work/SNAPSHOT.md" "$stage/SNAPSHOT.md"

  body_chars="$(awk 'BEGIN{n=0} /^---$/ && n<2 {n++; next} n>=2' "$stage/SKILL.md" | wc -m | tr -d ' ')"
  [[ "$body_chars" -lt 20000 ]] || limit "$name: SKILL.md instructions are $body_chars characters; Copilot allows under 20,000"

  links="$(find "$stage" -type l | sed "s#^$stage/##")"
  [[ -z "$links" ]] || limit "$name: the bundle holds links, which this build refuses to follow: $links"

  deep="$(cd "$stage" && find . -type f | awk -F/ 'NF-2 > 3 {print substr($0, 3)}')"
  [[ -z "$deep" ]] || limit "$name: these files sit more than 3 directories deep: $deep"

  bad_type="$(cd "$stage" && find . -type f | { grep -viE "\.($allowed)$" || true; } | sed 's#^\./##')"
  [[ -z "$bad_type" ]] || limit "$name: Copilot does not accept these file types: $bad_type"

  files="$(find "$stage" -type f | wc -l | tr -d ' ')"
  [[ "$files" -le 350 ]] || limit "$name: $files files; Copilot allows 350 across all of an agent's skills"

  # Bytes, not disk blocks, so the number is the same on every filesystem.
  bytes="$(find "$stage" -type f -exec cat {} + | wc -c | tr -d ' ')"
  kb=$(( (bytes + 1023) / 1024 ))
  [[ "$kb" -lt 10240 ]] || limit "$name: ${kb} KB; the whole app package, this skill included, must stay under 10 MB"

  summary+=("$name: $files files, ${kb} KB, SKILL.md $body_chars characters")
done
if [[ "$fail" -ne 0 ]]; then
  echo "build: nothing written to $out_parent" >&2
  exit 1
fi

# The same input gives the same bytes: fixed modes, every file at the
# epoch's time, names sorted, and no uid, gid or extended-time fields (-X).
# `atk add skill --from` takes a zip from any path, but a folder only from
# inside the agent's appPackage/, so the zip is the form to hand it.
mkdir -p "$out_parent"
for i in "${!names[@]}"; do
  name="${names[$i]}"
  chmod -R u=rwX,go=rX "$work/$name"
  find "$work/$name" -print0 | while IFS= read -r -d '' f; do stamp "$f"; done
  mv "$work/$name" "$out_parent/$name"
  echo "built $out_parent/${summary[$i]}"
  if command -v zip >/dev/null 2>&1; then
    (cd "$out_parent" && find "$name" -type f | LC_ALL=C sort | TZ=UTC zip -q -X -@ "$name.zip")
    echo "zipped $out_parent/$name.zip for Agent Builder or atk add skill"
  else
    echo "build: zip not found, so no $name.zip; zip the folder before adding it" >&2
  fi
done
echo "snapshot: ${repo_url:-repository not recorded} at ${ref:-revision not recorded}, built $built"
