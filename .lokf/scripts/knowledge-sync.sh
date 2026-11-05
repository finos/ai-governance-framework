#!/usr/bin/env bash
# Bring this host's sidecar copies and skills pin to one release of Knowledge
# Trust Ladder, the repository that publishes the skills, and leave the diff
# for a person to review.
#
# A host carries byte-identical copies of the templates under
# skills/ktl-sidecar/templates/, and pins its scheduled librarian to one tag
# of that repository with TRUST_LADDER_SKILLS_REF, and to the commit that tag
# names with TRUST_LADDER_SKILLS_SHA. The copies and the pin move together.
# The skill that tag installs is written against the wrapper, gate and
# preflight that tag includes. And once the librarian is turned on, the pin
# decides which agent instructions run unattended with a credential in the
# job. So this script:
#   - takes a release tag and nothing looser;
#   - reads the release's knowledge-sync.manifest, which lists each template
#     a host may carry, its copy and the rule for it, out of that tag, from
#     a clone it makes or from a clone it is given, never from a working
#     tree. The release is data to this script: the list and the templates
#     it names. No code from the release runs;
#   - refuses a tag that is not on the remote, which settles the order:
#     release first, then sync;
#   - copies every template the host already carries, and adds one the host
#     never had in two cases only: ktl-sidecar installs it on every host, or
#     a file the host carries needs it. Any other is reported, not added:
#     that is ktl-sidecar's Step 5, a decision for the host;
#   - moves the pin to the tag and the commit it names;
#   - writes the changelog entry under "## [Unreleased]" and "### Security",
#     so no release goes out with the entry missing or mistyped;
#   - runs the sidecar's own checks on the synced copies.
# It never touches the default branch. With --branch it works on a branch of
# its own, sync-<tag>, made from the default branch as origin has it, and
# refuses a tree with uncommitted changes, so the diff is the sync's alone.
#
# Three callers run it:
#   - a person, in the host: .lokf/scripts/knowledge-sync.sh --pr v0.47.0;
#   - the host's knowledge-sync.yaml workflow, which runs it in place and
#     opens the pull request itself;
#   - the skills repository's scripts/sync-sidecar.sh, which runs each
#     sibling's own copy, or the tag's copy in a sibling that has none.
#
# The copy that runs is the host's: reviewed and merged there, as every file
# the host runs is. A manifest rule this copy does not know is reported and
# left for the next run, once the pull request that brings the newer copy of
# this script is merged.
#
# Usage: knowledge-sync.sh [options] <tag>
#   --host <dir>      the host to sync; by default the nearest parent of the
#                     working directory that holds .lokf/
#   --source <dir>    a clone of the skills repository that holds the tag;
#                     by default the tag is cloned from --repo
#   --repo <url>      where to clone the tag from; by default the URL the
#                     host's librarian workflow names, or the published one
#   --branch          work on sync-<tag>, from origin's default branch
#   --commit          --branch, then commit the sync there
#   --push            --commit, then push the branch to origin
#   --pr              --push, then open the pull request with gh, from the
#                     template under .github/PULL_REQUEST_TEMPLATE/
#   --changed <file>  write the paths the sync changed or added, one a line
#   --report <file>   write the report as Markdown, for a pull request body
#   --no-checks       skip the sidecar's checks on the synced copies
#   --apply <patch>   instead of a sync, put a patch a sync made onto this
#                     clean checkout, for the workflow's privileged job.
#                     Refuse a path or a change a sync may not make, and keep
#                     every workflow as it is but for the pin. Set the pin to
#                     <tag> and --pin-sha, and write the workflow changes the
#                     patch carried to --held, for a person to apply
#   --held <file>     where --apply writes the workflow changes it held
#   --pin-sha <sha>   the commit <tag> names, checked by the caller
#
# Exit 0 when the host is synced, or had nothing to sync. Exit 1 when the
# host was skipped (no .lokf/, no git, uncommitted changes, the branch
# exists) or a check failed after the copy: fix the bundle in the same
# change, or the host's gate fails on it. Exit 2 when the arguments are wrong
# or the tag is not usable.
#
# Everything runs inside main(), called on the last line. Bash reads a
# function in full before it runs any of it, so the sync may copy a newer
# release of this script over the file it is running from.
set -euo pipefail

default_repo="https://github.com/noelmcloughlin/knowledge-trust-ladder"
templates="skills/ktl-sidecar/templates"
website_templates="skills/ktl-website/templates"
librarian_copy=".github/workflows/knowledge-librarian.yaml"

# The manifest in the release lists what a sync keeps current: each
# template, its copy and the rule for it. Its header says what each rule
# means. The rules this copy of the script knows:
manifest="knowledge-sync.manifest"
rules="copy titled always needs"
# The website skill's templates, for a host that built its site with
# ktl-website: every file under skills/ktl-website/templates/website/ but the
# three the host owns, and the deploy workflow. A host with no
# website/site.config.mjs gets none of them: that is ktl-website's decision.
website_owned=("site.config.mjs" "README.md" "src/styles/custom.css")

usage() {
  sed -n '/^# Usage:/,/^# Exit 0/p' "$0" | sed -e '$d' -e 's/^# \{0,1\}//' >&2
  exit 2
}
die() { echo "knowledge-sync: $*" >&2; exit 2; }

# The pin lines are each host's own to move, so they are not drift.
unpin() { sed -E -e 's/(TRUST_LADDER_SKILLS_REF: )v[0-9]+\.[0-9]+\.[0-9]+/\1vX.Y.Z/' -e 's/(TRUST_LADDER_SKILLS_SHA: )[0-9a-f]{40}/\1COMMIT/'; }

# The repository's web address, from a clone URL: no trailing .git, and
# an ssh address written as https, so the links in the entry open.
web_url() {
  local url="${1%.git}"
  url="${url%/}"
  case "$url" in
    git@github.com:*) url="https://github.com/${url#git@github.com:}" ;;
    ssh://git@github.com/*) url="https://github.com/${url#ssh://git@github.com/}" ;;
  esac
  printf '%s\n' "$url"
}

# Add the entry to the changelog under "## [Unreleased]", in its
# "### Security" section. A section that has none gets one at its end. A
# file with CRLF line endings keeps them, and the lines added get the same.
# Exit 3 when the file has no "## [Unreleased]" heading.
add_entry() {
  local file="$1" entry="$2" tmp
  tmp="$(mktemp)"
  if awk -v entry="$entry" '
    { line[NR] = $0; key[NR] = $0; sub(/\r$/, "", key[NR]) }
    END {
      u = 0; e = NR + 1; s = 0; nl = ""
      for (i = 1; i <= NR; i++) if (key[i] == "## [Unreleased]") { u = i; break }
      if (u == 0) exit 3
      if (line[u] ~ /\r$/) nl = "\r"
      for (i = u + 1; i <= NR; i++) if (key[i] ~ /^## /) { e = i; break }
      for (i = u + 1; i < e; i++) if (key[i] ~ /^### Security[ \t]*$/) { s = i; break }
      if (s) {
        t = e
        for (i = s + 1; i < e; i++) if (key[i] ~ /^### /) { t = i; break }
        last = s
        for (i = s + 1; i < t; i++) if (key[i] !~ /^[ \t]*$/) last = i
        for (i = 1; i <= last; i++) print line[i]
        if (last == s) print nl
        print entry nl
      } else {
        last = u
        for (i = u + 1; i < e; i++) if (key[i] !~ /^[ \t]*$/) last = i
        for (i = 1; i <= last; i++) print line[i]
        print nl
        print "### Security" nl
        print nl
        print entry nl
      }
      for (i = last + 1; i <= NR; i++) print line[i]
    }' "$file" > "$tmp"; then
    cat "$tmp" > "$file"
    rm -f "$tmp"
    return 0
  fi
  rm -f "$tmp"
  return 3
}

# The paths a sync may touch: the sidecar's copies, the site's copies, the
# pin and the changelog. The three site files the host owns are refused by
# name, and so is a path with a character outside the plain set the
# templates use, or a .git segment.
sync_paths='^(\.github/workflows/knowledge-[a-z]+\.yaml|\.github/PULL_REQUEST_TEMPLATE/knowledge-[a-z]+\.md|\.lokf/scripts/knowledge-[a-z]+\.(sh|py)|\.lokf/m365/[A-Za-z0-9._-]+|\.lokf/domain\.yaml|\.lokf/\.gitattributes|\.lokf/\.gitignore|\.lokf/justfile|website/.+|CHANGELOG\.md)$'
owned_paths='^website/(site\.config\.mjs|README\.md|src/styles/custom\.css)$'
plain_path='^[]A-Za-z0-9._/@+[-]+$'

# --apply: put a patch another run of this script made onto this checkout,
# for knowledge-sync.yaml's privileged job. That run read a release nobody
# here has reviewed, so nothing it decided is trusted. The patch may only
# edit and add plain files on the paths above. Then every workflow goes
# back to what the checkout has, but for the pin, which is set here from
# the tag and the commit the caller checked at the skills repository. A
# workflow on a branch pushed with a token runs on that push, with the
# repository's secrets and a token its own permissions: key can raise. So
# no workflow the release wrote may reach the branch before a person reads
# it. Those changes go to <held>, a patch that applies on top of the result.
apply_patch() {
  local patch="$1" held="$2" tag="$3" sha="$4" paths wrong f full lane
  [[ -f "$patch" ]] || die "no such patch: $patch"
  [[ "$sha" =~ ^[0-9a-f]{40}$ ]] || die "--pin-sha takes the 40-hex commit the tag names, not '$sha'"
  [[ -z "$(git status --porcelain)" ]] || die "the checkout has changes of its own; --apply takes a clean one"
  paths="$(git -c core.quotePath=false apply --numstat -- "$patch" | cut -f3-)" || die "$patch is not a patch git can read"
  wrong="$(printf '%s\n' "$paths" | grep -Ev "$sync_paths" || true)"
  wrong+=$'\n'"$(printf '%s\n' "$paths" | grep -E "$owned_paths" || true)"
  wrong+=$'\n'"$(printf '%s\n' "$paths" | grep -Ev "$plain_path" || true)"
  wrong+=$'\n'"$(printf '%s\n' "$paths" | grep -iE '(^|/)\.git(/|$)' || true)"
  if [[ -n "${wrong//[$'\n\t ']/}" ]]; then
    printf '%s\n' "$wrong" | sed '/^$/d; s/^/   refused  /' >&2
    die "the patch touches paths a sync may not"
  fi
  # A sync edits and adds plain files. It never deletes, renames or links,
  # and a file's mode is 644 or 755.
  local summary; summary="$(git apply --summary -- "$patch")"
  wrong="$(printf '%s\n' "$summary" | grep -E '^ (delete mode|rename|copy) ' || true)"
  wrong+=$'\n'"$(printf '%s\n' "$summary" | grep -E '^ create mode ' | grep -vE '^ create mode 100(644|755) ' || true)"
  wrong+=$'\n'"$(printf '%s\n' "$summary" | grep -E '^ mode change ' | grep -vE '^ mode change 100(644|755) => 100(644|755) ' || true)"
  if [[ -n "${wrong//[$'\n\t ']/}" ]]; then
    printf '%s\n' "$wrong" | sed '/^$/d; s/^ */   refused  /' >&2
    die "the patch does more than edit and add plain files"
  fi
  if printf '%s\n' "$paths" | grep -qxF "$librarian_copy" && [[ ! -f "$librarian_copy" ]]; then
    die "the patch adds $librarian_copy, which this host does not carry, so it would set a pin nobody checked"
  fi
  git apply --index --whitespace=nowarn -- "$patch"
  full="$(git write-tree)"
  while IFS= read -r f; do
    [[ -n "$f" ]] || continue
    if git cat-file -e "HEAD:$f" 2>/dev/null; then
      cmp -s <(git show "HEAD:$f" | unpin) <(git show ":$f" | unpin) && continue
      git show "HEAD:$f" > "$f"
    else
      git rm --cached --quiet -- "$f"
      rm -f -- "$f"
    fi
  done < <(git -c core.quotePath=false diff --cached --name-only -- .github/workflows/)
  if [[ -f "$librarian_copy" ]]; then
    sed -i.sync-bak -E -e "s/(TRUST_LADDER_SKILLS_REF: )v[0-9]+\.[0-9]+\.[0-9]+/\1$tag/" \
                       -e "s/(TRUST_LADDER_SKILLS_SHA: )[0-9a-f]{40}/\1$sha/" "$librarian_copy"
    rm -f "$librarian_copy.sync-bak"
  fi
  if [[ -d .github/workflows ]]; then git add -- .github/workflows/; fi
  lane="$(git write-tree)"
  git diff --binary "$lane" "$full" -- .github/workflows/ > "$held"
  # What the branch carries under .github/workflows/ differs from the
  # checkout by the two pin lines alone.
  if git diff --cached -U0 -- .github/workflows/ | grep -E '^[-+][^-+]' | grep -qvE '^[-+] *TRUST_LADDER_SKILLS_(REF|SHA): '; then
    die "a workflow change other than the pin is still staged; nothing is pushed"
  fi
  for f in $(git -c core.quotePath=false diff --cached --name-only); do echo "   staged   $f"; done
  for f in $(git -c core.quotePath=false diff --name-only "$lane" "$full"); do echo "   held     $f (a workflow change, for a person to apply)"; done
}

main() {
  local host="" source="" repo="" tag="" changed_out="" report_out="" out
  local apply="" held="" pin_sha=""
  local branch_mode=0 commit=0 push=0 pr=0 checks=1
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --host) [[ $# -ge 2 ]] || usage; host="$2"; shift 2 ;;
      --source) [[ $# -ge 2 ]] || usage; source="$2"; shift 2 ;;
      --repo) [[ $# -ge 2 ]] || usage; repo="$2"; shift 2 ;;
      --branch) branch_mode=1; shift ;;
      --commit) commit=1; branch_mode=1; shift ;;
      --push) push=1; commit=1; branch_mode=1; shift ;;
      --pr) pr=1; push=1; commit=1; branch_mode=1; shift ;;
      --changed) [[ $# -ge 2 ]] || usage; changed_out="$2"; shift 2 ;;
      --report) [[ $# -ge 2 ]] || usage; report_out="$2"; shift 2 ;;
      --no-checks) checks=0; shift ;;
      --apply) [[ $# -ge 2 ]] || usage; apply="$2"; shift 2 ;;
      --held) [[ $# -ge 2 ]] || usage; held="$2"; shift 2 ;;
      --pin-sha) [[ $# -ge 2 ]] || usage; pin_sha="$2"; shift 2 ;;
      -h|--help) usage ;;
      -*) echo "knowledge-sync: unknown option $1" >&2; usage ;;
      *) [[ -z "$tag" ]] || usage; tag="$1"; shift ;;
    esac
  done
  [[ -n "$tag" ]] || usage
  if [[ ! "$tag" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    die "'$tag' is not a release tag (vMAJOR.MINOR.PATCH); a branch or a commit would let unreleased instructions into this host"
  fi

  # The host: the directory given, or the nearest parent of the working
  # directory that holds .lokf/.
  if [[ -z "$host" ]]; then
    local d; d="$(pwd -P)"; host="$d"
    while [[ "$d" != "/" ]]; do
      if [[ -d "$d/.lokf" ]]; then host="$d"; break; fi
      d="$(dirname "$d")"
    done
  fi
  host="$(cd "$host" 2>/dev/null && pwd -P)" || die "no such directory: $host"
  if [[ ! -d "$host/.lokf" ]]; then
    echo "   no .lokf/ in $host: not a sidecar host; skipped" >&2
    return 1
  fi
  if ! git -C "$host" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "   $host is not a git work tree: the sync leaves a diff for review, and there is no diff to leave here; skipped" >&2
    return 1
  fi
  if [[ -n "$apply" ]]; then
    [[ -n "$held" && -n "$pin_sha" ]] || die "--apply needs --held <file> and --pin-sha <commit>"
    apply="$(cd "$(dirname "$apply")" && pwd -P)/$(basename "$apply")"
    held="$(cd "$(dirname "$held")" && pwd -P)/$(basename "$held")"
    ( cd "$host" && apply_patch "$apply" "$held" "$tag" "$pin_sha" )
    return
  fi
  for out in "$changed_out" "$report_out"; do
    [[ -z "$out" ]] || : > "$out"
  done

  # The repository to read the tag from: the clone given, or one made here.
  local repo_url tmp_clone=""
  if [[ -z "$repo" && -f "$host/$librarian_copy" ]]; then
    repo="$(grep -oE 'TRUST_LADDER_SKILLS_REPO: *[^ ]+' "$host/$librarian_copy" | head -1 | sed -E 's/^TRUST_LADDER_SKILLS_REPO: *//' || true)"
  fi
  [[ -n "$repo" ]] || repo="$default_repo"
  [[ "$repo" != -* ]] || die "'$repo' is not an address to clone from"
  if [[ -n "$source" ]]; then
    source="$(cd "$source" 2>/dev/null && pwd -P)" || die "no such directory: $source"
    git -C "$source" rev-parse --is-inside-work-tree >/dev/null 2>&1 || die "$source is not a git work tree"
    if ! git -C "$source" rev-parse -q --verify "refs/tags/$tag^{commit}" >/dev/null; then
      die "no tag $tag in $source: publish the release first, then sync (that order is the point)"
    fi
    repo_url="$(web_url "$(git -C "$source" remote get-url origin 2>/dev/null || printf '%s' "$repo")")"
  else
    if ! git ls-remote --exit-code --tags "$repo" "refs/tags/$tag" >/dev/null 2>&1; then
      die "no release tag $tag at $repo: publish the release first, then sync (that order is the point)"
    fi
    tmp_clone="$(mktemp -d)"
    echo "   cloning $tag from $repo"
    git -c advice.detachedHead=false clone --quiet --no-checkout --depth 1 --branch "$tag" -- "$repo" "$tmp_clone"
    source="$tmp_clone"
    repo_url="$(web_url "$repo")"
  fi
  if ! git -C "$source" cat-file -e "$tag:skills/ktl-librarian/SKILL.md" 2>/dev/null; then
    [[ -z "$tmp_clone" ]] || rm -rf "$tmp_clone"
    die "$tag has no skills/ktl-librarian/SKILL.md; the install step copies that path, so a host pinned to it fails every scheduled run"
  fi
  if ! git -C "$source" cat-file -e "$tag:$templates/$manifest" 2>/dev/null; then
    [[ -z "$tmp_clone" ]] || rm -rf "$tmp_clone"
    die "$tag has no $templates/$manifest, so it predates the sync this script does; sync to a release that carries it"
  fi
  local tag_sha; tag_sha="$(git -C "$source" rev-parse "$tag^{commit}")"

  # The manifest, read as data: each copy or titled line is a pair to sync,
  # in the release's order; the always and needs lines say when a copy the
  # host lacks is added. A copy path is held to the plain characters the
  # templates use and to the host's tree, so a release cannot name a path
  # outside it. A rule this copy of the script does not know is kept to
  # report. A line with a field missing is a release's mistake, and stops
  # the sync before it writes.
  local pairs=() titled=() always=() needs=() unknown=() rule a b rest line
  while IFS= read -r line; do
    line="${line%%#*}"
    read -r rule a b rest <<< "$line" || true
    [[ -n "$rule" ]] || continue
    case " $rules " in
      *" $rule "*) ;;
      *) unknown+=("$rule $a"); continue ;;
    esac
    [[ -n "$a" && -n "$b" ]] || die "$tag's $manifest has a $rule line with a field missing: $line"
    case "$rule" in
      copy|titled)
        if [[ ! "$b" =~ ^[A-Za-z0-9._/@+-]+$ || "$b" == /* || "$b" == *..* || "$a" == /* || "$a" == *..* ]]; then
          die "$tag's $manifest names a path outside the host, or with a character no template uses: $line"
        fi
        # A copy under .git would be git's own configuration, which can name
        # a command git runs: a release could run code in the job that reads it.
        if [[ "/$b/" =~ /\.[Gg][Ii][Tt]/ ]]; then
          die "$tag's $manifest names a path inside a .git folder: $line"
        fi
        pairs+=("$a:$b")
        [[ "$rule" != titled ]] || titled+=("$a") ;;
      always) always+=("$a|$b${rest:+ $rest}") ;;
      needs) needs+=("$a:$b:${rest:-is here}") ;;
    esac
  done < <(git -C "$source" show "$tag:$templates/$manifest")
  [[ ${#pairs[@]} -gt 0 ]] || die "$tag's $manifest lists nothing to sync"

  at_tag() { git -C "$source" show "$tag:$templates/$1"; }
  # The template as the host should carry it: <template> <host copy>.
  rendered() {
    local t
    for t in ${titled[@]+"${titled[@]}"}; do
      if [[ "$t" == "$1" ]]; then
        head -n 1 "$2"
        at_tag "$1" | tail -n +2 | OWN="$(grep -m 1 '^schema := ' "$2" || true)" \
          awk '/^schema := / && ENVIRON["OWN"] != "" { print ENVIRON["OWN"]; next } { print }'
        return
      fi
    done
    at_tag "$1"
  }
  # Why the host needs a template it never installed, or nothing when it
  # does not: <template>.
  needed() {
    local entry
    for entry in ${always[@]+"${always[@]}"}; do
      if [[ "${entry%%|*}" == "$1" ]]; then echo "ktl-sidecar's ${entry##*|} installs it on every host"; return; fi
    done
    for entry in ${needs[@]+"${needs[@]}"}; do
      local t="${entry%%:*}" rest="${entry#*:}"
      local copy="${rest%%:*}" why="${rest#*:}"
      if [[ "$t" == "$1" && -f "$host/$copy" ]]; then echo "$copy $why"; return; fi
    done
  }

  # The branch the copies go on. It starts from the host's default branch as
  # origin has it, not from whatever is checked out, and it does not track
  # that branch, so a plain push goes to a branch of the same name.
  if [[ -n "$(git -C "$host" status --porcelain --untracked-files=no)" ]]; then
    echo "   uncommitted changes in $host: commit or stash them first, so the diff left for review is the sync's alone; skipped" >&2
    [[ -z "$tmp_clone" ]] || rm -rf "$tmp_clone"
    return 1
  fi
  local branch="sync-$tag" base="" previous=""
  if [[ "$branch_mode" -eq 1 ]]; then
    git -C "$host" fetch --quiet origin 2>/dev/null || true
    base="$(git -C "$host" symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null || true)"
    if [[ -z "$base" ]]; then
      local candidate
      for candidate in origin/main origin/master main master; do
        if git -C "$host" rev-parse -q --verify "$candidate^{commit}" >/dev/null; then base="$candidate"; break; fi
      done
    fi
    if [[ -z "$base" ]]; then
      echo "   no default branch to start from (origin/HEAD, main or master); skipped" >&2
      [[ -z "$tmp_clone" ]] || rm -rf "$tmp_clone"
      return 1
    fi
    if git -C "$host" rev-parse -q --verify "refs/heads/$branch" >/dev/null; then
      echo "   $branch already exists in $host: finish it, or delete it, first; skipped" >&2
      [[ -z "$tmp_clone" ]] || rm -rf "$tmp_clone"
      return 1
    fi
    previous="$(git -C "$host" symbolic-ref --quiet --short HEAD 2>/dev/null || git -C "$host" rev-parse HEAD)"
    if ! git -C "$host" switch --quiet --no-track -c "$branch" "$base"; then
      echo "   could not start $branch from $base (git said why above); skipped" >&2
      [[ -z "$tmp_clone" ]] || rm -rf "$tmp_clone"
      return 1
    fi
    echo "   branch   $branch, from $base"
  fi

  # What the host pins today, so the report can say what moves.
  local wf="$host/$librarian_copy" old_pin=""
  if [[ -f "$wf" ]]; then
    old_pin="$(grep -oE 'TRUST_LADDER_SKILLS_REF: v[0-9]+\.[0-9]+\.[0-9]+' "$wf" | head -1 | sed 's/^TRUST_LADDER_SKILLS_REF: //' || true)"
  fi

  local copied=() same=() added=() absent=() pins_only=() pair src dst why want
  for pair in "${pairs[@]}"; do
    src="${pair%%:*}"; dst="${pair##*:}"
    if ! git -C "$source" cat-file -e "$tag:$templates/$src" 2>/dev/null; then
      continue  # a template this release did not have yet
    fi
    if [[ ! -f "$host/$dst" ]]; then
      why="$(needed "$src")"
      if [[ -z "$why" ]]; then
        absent+=("$dst")
        continue
      fi
      mkdir -p "$(dirname "$host/$dst")"
      at_tag "$src" > "$host/$dst"
      if [[ "$(git -C "$source" ls-tree "$tag" -- "$templates/$src" | cut -c1-6)" == 100755 ]]; then
        chmod +x "$host/$dst"
      fi
      added+=("$dst ($why)")
      continue
    fi
    want="$(mktemp)"
    rendered "$src" "$host/$dst" > "$want"
    if cmp -s <(unpin < "$want") <(unpin < "$host/$dst"); then
      same+=("$dst")
    else
      # A copy that differs only on its `uses:` lines was bumped by the
      # host's Dependabot ahead of the template. The template's pins win,
      # since the copy must match it, and the report says so: the next
      # bump in the skills repository brings the same release back. Only
      # awk decides, reading the whole diff: diff exits 1 whenever the
      # files differ, so under pipefail a pipeline from it fails for every
      # copy, whichever lines differ.
      if awk '/^[<>]/ { if (/uses: /) pin = 1; else other = 1 } END { exit (pin && !other) ? 0 : 1 }' <(diff <(unpin < "$want") <(unpin < "$host/$dst")); then
        pins_only+=("$dst")
      fi
      cat "$want" > "$host/$dst"
      copied+=("$dst")
    fi
    rm -f "$want"
  done
  # The template's own pin is one release behind by design: the release
  # commit moves it to the newest tag that existed then. So the copy above
  # would move a host backwards. Set it to the tag being synced, and the
  # commit beside it to the one that tag names, which the install step checks
  # the tag against on every run.
  local pin_moved=0
  if [[ -f "$wf" ]]; then
    sed -i.sync-bak -E -e "s/(TRUST_LADDER_SKILLS_REF: )v[0-9]+\.[0-9]+\.[0-9]+/\1$tag/" \
                       -e "s/(TRUST_LADDER_SKILLS_SHA: )[0-9a-f]{40}/\1$tag_sha/" "$wf"
    rm -f "$wf.sync-bak"
    [[ "$old_pin" == "$tag" ]] || pin_moved=1
  fi

  # The site, when the host has one: a template it lacks is added, since the
  # site cannot build without any of them.
  local website=0 tpath rel skip o
  if [[ -f "$host/website/site.config.mjs" ]]; then
    website=1
    while IFS= read -r tpath; do
      rel="${tpath#"$website_templates/website/"}"
      # The same plain set as --apply's, brackets and all: Astro names a
      # route with them, as in src/pages/og/[...route].ts.
      if [[ ! "$rel" =~ $plain_path ||"/$rel/" =~ /\.[Gg][Ii][Tt]/ || "/$rel/" == */../* ]]; then
        die "$tag's website templates hold a path a host may not carry: $rel"
      fi
      skip=0; for o in "${website_owned[@]}"; do [[ "$rel" == "$o" ]] && skip=1; done
      [[ "$skip" -eq 1 ]] && continue
      dst="website/$rel"; [[ "$rel" == gitignore ]] && dst="website/.gitignore"
      if [[ ! -f "$host/$dst" ]]; then
        mkdir -p "$(dirname "$host/$dst")"
        git -C "$source" show "$tag:$tpath" > "$host/$dst"
        added+=("$dst (the site cannot build without it)")
      elif cmp -s <(git -C "$source" show "$tag:$tpath") "$host/$dst"; then
        same+=("$dst")
      else
        git -C "$source" show "$tag:$tpath" > "$host/$dst"
        copied+=("$dst")
      fi
    done < <(git -C "$source" ls-tree -r --name-only "$tag" -- "$website_templates/website")
    local wsrc="$website_templates/github/knowledge-website.yaml" wdst=".github/workflows/knowledge-website.yaml"
    if git -C "$source" cat-file -e "$tag:$wsrc" 2>/dev/null; then
      if [[ ! -f "$host/$wdst" ]]; then
        absent+=("$wdst")
      elif cmp -s <(git -C "$source" show "$tag:$wsrc") "$host/$wdst"; then
        same+=("$wdst")
      else
        git -C "$source" show "$tag:$wsrc" > "$host/$wdst"
        copied+=("$wdst")
      fi
    fi
  fi

  local f
  for f in ${copied[@]+"${copied[@]}"}; do echo "   copied   $f"; done
  for f in ${same[@]+"${same[@]}"}; do echo "   same     $f"; done
  for f in ${added[@]+"${added[@]}"}; do echo "   added    $f"; done
  for f in ${absent[@]+"${absent[@]}"}; do echo "   absent   $f (never installed here: ktl-sidecar's Step 5 decides, not this script)"; done
  for f in ${pins_only[@]+"${pins_only[@]}"}; do echo "   pins     $f differed only on its action pins, which Dependabot bumped here first; the template's pins are back until the skills repository bumps them"; done
  for f in ${unknown[@]+"${unknown[@]}"}; do echo "   unknown  $f: a manifest rule this copy of knowledge-sync.sh does not know; it is left for the next sync, once the copy $tag brings is merged"; done
  local pin_line
  if [[ -f "$wf" ]]; then
    if [[ "$pin_moved" -eq 0 ]]; then
      pin_line="already $tag"
    elif [[ -n "$old_pin" && "$(printf '%s\n%s\n' "$old_pin" "$tag" | sort -V | tail -n 1)" == "$old_pin" ]]; then
      pin_line="$old_pin back to $tag ($tag_sha): an older release than the host had"
    else
      pin_line="${old_pin:-none} to $tag ($tag_sha)"
    fi
  else
    pin_line="no $librarian_copy here, so no scheduled librarian to pin"
  fi
  echo "   pin      $pin_line"
  # Whether the skill the librarian runs changed between the two pins. The
  # old tag is fetched when the clone is shallow, and the line is left out
  # when neither tag can be read.
  local skill_line=""
  if [[ -n "$old_pin" && "$old_pin" != "$tag" ]]; then
    if ! git -C "$source" rev-parse -q --verify "refs/tags/$old_pin^{commit}" >/dev/null; then
      git -C "$source" fetch --quiet --depth 1 origin "refs/tags/$old_pin:refs/tags/$old_pin" 2>/dev/null || true
    fi
    if git -C "$source" rev-parse -q --verify "refs/tags/$old_pin^{commit}" >/dev/null; then
      local n; n="$(git -C "$source" diff --name-only "$old_pin" "$tag" -- skills/ktl-librarian | wc -l | tr -d ' ')"
      if [[ "$n" -gt 0 ]]; then skill_line="ktl-librarian changed in $n file(s) between $old_pin and $tag"; else skill_line="ktl-librarian unchanged between $old_pin and $tag"; fi
      echo "   skill    $skill_line"
    fi
  fi
  if [[ "$website" -eq 1 ]]; then
    echo "   website  the site's copies are synced; build it there to check: cd website && npm ci --ignore-scripts && npm run build"
  fi

  if [[ ${#copied[@]} -eq 0 && ${#added[@]} -eq 0 && "$pin_moved" -eq 0 ]]; then
    if [[ "$branch_mode" -eq 1 ]]; then
      git -C "$host" switch --quiet "$previous" && git -C "$host" branch --quiet -D "$branch"
      echo "   nothing to sync; back on $previous, and $branch removed"
    else
      echo "   nothing to sync"
    fi
    [[ -z "$tmp_clone" ]] || rm -rf "$tmp_clone"
    return 0
  fi

  # The changelog entry, written from what the sync did and never left as a
  # prompt to fill in: a placeholder merged unfilled became a release's notes,
  # and a heading typed by hand once carried a colon the lint refused. The
  # link is the comparison between the two pins, so a sync that skipped
  # releases points at all of them, or the tag's changelog when the old pin
  # is unknown. "No plugin change" is true only of an Obsidian plugin, whose
  # root manifest.json names the app version it needs.
  local link tail="" entry list=() i changelog_line
  if [[ -n "$old_pin" && "$old_pin" != "$tag" ]]; then
    link="$repo_url/compare/$old_pin...$tag"
  else
    link="$repo_url/blob/$tag/CHANGELOG.md"
  fi
  if [[ -f "$host/manifest.json" ]] && grep -q '"minAppVersion"' "$host/manifest.json"; then
    tail=" No plugin change."
  fi
  if [[ ${#copied[@]} -eq 0 && ${#added[@]} -eq 0 ]]; then
    entry="- **The skills pin is at Knowledge Trust Ladder [$tag]($link).** None of the sidecar copies this repository carries changed.$tail"
  else
    for f in ${copied[@]+"${copied[@]}"} ${added[@]+"${added[@]}"}; do list+=("\`${f%% (*}\`"); done
    local joined="${list[0]}"
    for ((i = 1; i < ${#list[@]}; i++)); do
      if [[ "$i" -eq $((${#list[@]} - 1)) ]]; then joined+=" and ${list[$i]}"; else joined+=", ${list[$i]}"; fi
    done
    entry="- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [$tag]($link).** The release changed $joined here.$tail"
  fi
  local changed=()
  for f in ${copied[@]+"${copied[@]}"}; do changed+=("$f"); done
  for f in ${added[@]+"${added[@]}"}; do changed+=("${f%% (*}"); done
  if [[ "$pin_moved" -eq 1 ]]; then
    local listed=0
    for f in ${changed[@]+"${changed[@]}"}; do [[ "$f" == "$librarian_copy" ]] && listed=1; done
    [[ "$listed" -eq 1 ]] || changed+=("$librarian_copy")
  fi
  if [[ ! -f "$host/CHANGELOG.md" ]]; then
    changelog_line="There is no CHANGELOG.md here, so no entry was written."
  elif grep -qF "[$tag]($link)" "$host/CHANGELOG.md"; then
    changelog_line="CHANGELOG.md already has the entry for $tag."
  elif add_entry "$host/CHANGELOG.md" "$entry"; then
    changelog_line="CHANGELOG.md has the entry, under its Unreleased heading and Security."
    changed+=("CHANGELOG.md")
  else
    changelog_line="CHANGELOG.md has no Unreleased heading, so add the entry by hand:"$'\n'"   $entry"
  fi
  echo "   entry    $changelog_line"

  # The sidecar's own checks, run from the host's copies as its gate would.
  # `set -e` is off inside a subshell followed by `||`, so each check records
  # its own failure, or only the last one's would count.
  local ok=1 check_lines=() status=0
  if [[ "$checks" -eq 1 ]]; then
    local verdicts; verdicts="$(mktemp)"
    (
      rc=0
      cd "$host/.lokf"
      if [[ -x scripts/knowledge-preflight.sh ]]; then
        echo "preflight: $(bash scripts/knowledge-preflight.sh | tail -1)"
      fi
      if command -v uv >/dev/null 2>&1; then
        # The recipe, as the gate runs it, with the just uv.lock pins where
        # it pins one; just's own closing line on a failure is dropped, so
        # the line shown is lokf's verdict.
        just=(uvx --from rust-just==1.47.0 just)
        if grep -qx 'name = "rust-just"' uv.lock 2>/dev/null; then just=(uv run --locked just); fi
        if out="$("${just[@]}" lokf-check-refs 2>&1 | grep -v '^error: Recipe ' | tail -1)"; then
          echo "lokf validate --check-refs: $out"
        else
          echo "lokf validate --check-refs: failed, $out"; rc=1
        fi
      else
        echo "lokf validate --check-refs: skipped, uv is not installed; the conventions script runs without its parser's half"
      fi
      if [[ -f scripts/knowledge-conventions.sh ]]; then
        if out="$(bash scripts/knowledge-conventions.sh knowledge 2>&1)"; then
          echo "conventions: pass"
        else
          echo "conventions: failed"; printf '%s\n' "$out" | sed 's/^/    /'; rc=1
        fi
      fi
      exit "$rc"
    ) > "$verdicts" || ok=0
    while IFS= read -r f; do check_lines+=("$f"); echo "   check    $f"; done < "$verdicts"
    rm -f "$verdicts"
    if [[ "$ok" -eq 0 ]]; then
      echo "   FAIL     a check above failed: fix the bundle in the same change, or the host's gate fails on it"
      status=1
    fi
  else
    check_lines+=("skipped (--no-checks)")
    echo "   check    skipped (--no-checks)"
  fi

  # The files to stage, by name: what the sync changed, and what it added.
  if [[ -n "$changed_out" ]]; then printf '%s\n' "${changed[@]}" > "$changed_out"; fi
  # The report as Markdown, for a pull request body or a job summary.
  local body; body="$(mktemp)"
  {
    if [[ -n "$old_pin" && "$old_pin" != "$tag" ]]; then
      echo "Brings the sidecar copies and the skills pin of this repository to Knowledge Trust Ladder [$tag]($link), from $old_pin."
    else
      echo "Brings the sidecar copies and the skills pin of this repository to Knowledge Trust Ladder [$tag]($link)."
    fi
    if [[ ${#copied[@]} -gt 0 ]]; then
      echo; echo "The release changed these copies:"; echo
      for f in "${copied[@]}"; do echo "- \`$f\`"; done
    fi
    if [[ ${#added[@]} -gt 0 ]]; then
      echo; echo "Added, because a file here needs it:"; echo
      for f in "${added[@]}"; do
        local path="${f%% (*}" why="${f#* (}"; why="${why%)}"
        case "$why" in .*) why="\`${why%% *}\` ${why#* }" ;; esac
        echo "- \`$path\`: $why"
      done
    fi
    if [[ ${#absent[@]} -gt 0 ]]; then
      echo; echo "Not added, for ktl-sidecar's Step 5 to decide:"; echo
      for f in "${absent[@]}"; do echo "- \`$f\`"; done
    fi
    if [[ ${#unknown[@]} -gt 0 ]]; then
      echo; echo "Left for the next sync, since this copy of knowledge-sync.sh does not know their rule:"; echo
      for f in "${unknown[@]}"; do echo "- \`${f//\`/}\`"; done
    fi
    echo
    if [[ "$pin_moved" -eq 1 ]]; then
      echo "The skills pin moves from ${old_pin:-none} to $tag, commit \`$tag_sha\`.${skill_line:+ $skill_line.}"
    else
      echo "The skills pin: $pin_line."
    fi
    echo; echo "The sidecar's checks on the synced copies:"; echo
    for f in ${check_lines[@]+"${check_lines[@]}"}; do echo "- $f"; done
    echo; echo "$changelog_line" | head -1
  } > "$body"
  if [[ -n "$report_out" ]]; then cat "$body" > "$report_out"; fi

  local subject="security(sidecar): sync copies and skills pin from $tag"
  if [[ "$commit" -eq 1 ]]; then
    git -C "$host" add -- "${changed[@]}"
    git -C "$host" commit --quiet -m "$subject"
    echo "   commit   $(git -C "$host" rev-parse --short HEAD) $subject"
  else
    echo ""
    local where="the current branch"; [[ "$branch_mode" -eq 0 ]] || where="$branch"
    echo "   Then commit, from $host, on $where:"
    echo ""
    local staged=("${changed[@]}")
    for i in "${!staged[@]}"; do
      local line="     ${staged[$i]}"; [[ "$i" -eq 0 ]] && line="   git add ${staged[$i]}"
      if [[ "$i" -lt $((${#staged[@]} - 1)) ]]; then echo "$line \\"; else echo "$line"; fi
    done
    echo "   git commit -m \"$subject\""
  fi
  # The pull request body: the report, then the template the host carries,
  # whose checklist is the reviewer's. It is kept under .git/, where no
  # commit can pick it up.
  local gitdir body_file
  gitdir="$(git -C "$host" rev-parse --absolute-git-dir 2>/dev/null || printf '%s' "$host/.git")"
  body_file="$gitdir/knowledge-sync-body.md"
  {
    cat "$body"
    if [[ -f "$host/.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md" ]]; then
      echo
      cat "$host/.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md"
    fi
  } > "$body_file" 2>/dev/null || body_file="$body"
  if [[ "$push" -eq 1 ]]; then
    git -C "$host" push --quiet --set-upstream origin "$branch"
    echo "   pushed   origin/$branch"
  fi
  if [[ "$pr" -eq 1 ]]; then
    if ! command -v gh >/dev/null 2>&1; then
      echo "   gh is not installed, so the pull request was not opened; the branch is pushed" >&2
      [[ -z "$tmp_clone" ]] || rm -rf "$tmp_clone"
      return 1
    fi
    local url
    url="$(cd "$host" && gh pr create --title "$subject" --body-file "$body_file" --head "$branch" --base "${base#origin/}")"
    echo "   pr       $url"
  elif [[ "$push" -eq 1 ]]; then
    echo ""
    echo "   Then open the pull request, from $host:"
    echo ""
    echo "   gh pr create --title \"$subject\" --body-file \"$body_file\""
  fi
  [[ "$body_file" == "$body" ]] || rm -f "$body"
  [[ -z "$tmp_clone" ]] || rm -rf "$tmp_clone"
  return "$status"
}

main "$@"; exit
# The sync copies the release's version of this script over this file while
# it runs. Bash reads a script as it runs it, so when main returns it would
# read on into the new file from where the old one ended. The exit on the
# line above stops it. This comment sits below that line for a copy that
# ends with a bare `main "$@"`: where this file differs from that copy only
# in its last line, the copy reads " exit" next, and stops too.
