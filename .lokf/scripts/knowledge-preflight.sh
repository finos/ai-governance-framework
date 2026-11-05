#!/usr/bin/env bash
# What this host can and cannot do for the KTL skills: one read-only
# screen, no toolkit needed. Every skill runs it first and repeats its summary
# line in the hand-off, so a missing tool disables a step out loud instead of
# being discovered after a report has already offered that step.
#
# Each line is `ok`, `warn`, `missing` or `info`, then one summary line:
#   Preflight: <n> missing, <m> warnings. Missing disables: <steps>.
# Exit 0 always: the skills read the lines; nothing here is a gate.
#
# Bash 3.2 and POSIX tools only, so it runs on macOS's stock bash and on Git
# for Windows. From PowerShell, run it through Git for Windows' bash: the
# one-liner is in ktl-sidecar/references/portability.md.
#
# Usage: knowledge-preflight.sh [repo-root]   (default: the nearest ancestor of
# the current directory holding `.lokf/`, else the current directory)
[ -n "${BASH_VERSION:-}" ] || { echo "run this with bash: bash ${0##*/} [repo-root]" >&2; exit 2; }
set -u

missing=0; warns=0; disables=""
line() { printf '%-8s%-13s%s\n' "$1" "$2" "$3"; }
ok()   { line ok "$1" "$2"; }
info() { line info "$1" "$2"; }
warn() { line warn "$1" "$2"; warns=$((warns + 1)); }
miss() { line missing "$1" "$2"; missing=$((missing + 1)); [ -n "${3:-}" ] && disables="${disables}${disables:+; }$3"; }
have() { command -v "$1" >/dev/null 2>&1; }
# The host of a URL, without its scheme, user, password, port and path. An
# index URL may carry a password, so a URL is only ever printed this way.
hostof() { printf '%s\n' "$1" | sed -e 's#^[A-Za-z][A-Za-z0-9+.-]*://##' -e 's#^[^/@]*@##' -e 's#[/:?].*$##'; }

# ---- root ------------------------------------------------------------------
root="${1:-}"
if [ -z "$root" ]; then
  d="$(pwd -P)"; root="$d"
  while [ "$d" != "/" ]; do
    if [ -d "$d/.lokf" ]; then root="$d"; break; fi
    d="$(dirname "$d")"
  done
fi
root="$(cd "$root" 2>/dev/null && pwd -P)" || { echo "no such directory: ${1:-.}" >&2; exit 2; }

# ---- host ------------------------------------------------------------------
os="$(uname -s 2>/dev/null || echo unknown)"
case "$os" in
  Linux) host=Linux ;;
  Darwin) host=macOS ;;
  MINGW*|MSYS*|CYGWIN*) host="Windows (Git for Windows bash)" ;;
  *) host="$os" ;;
esac
if have sha256sum; then digest="sha256sum"; elif have shasum; then digest="shasum -a 256"; else digest=""; fi
# Only python3 is probed, because bare `python` is Python 2 on some hosts.
# The skills' scripts need 3.9 or later, which an enterprise host's python3
# often is not.
pyv=""
have python3 && pyv="$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])' 2>/dev/null)"
printf 'Preflight for %s\n' "$root"
ok host "$host, bash ${BASH_VERSION%%(*}; digest: ${digest:-none (macOS: install coreutils, or use uv run python)}; python3: ${pyv:-none (use uv run python)}"
case "$pyv" in
  2.*|3.[0-8]) warn python "python3 is $pyv and the skills' scripts need 3.9 or later: run each through uv run or the sidecar's .venv, never python3 or python" ;;
esac
# The skill's copy of this script, run from the skill's folder or a folder in
# it, screens the skill, not the host. Step 0 runs it from the host
# repository's root. A host's own copy sits in .lokf/scripts/. A repository
# that holds the skill, as the skills repository does, is the skill's parent.
# Neither is warned about.
self="$(cd "$(dirname "$0")" 2>/dev/null && pwd -P)"
case "$self" in
  */templates/scripts)
    skill="${self%/templates/scripts}"
    if [ -f "$skill/SKILL.md" ]; then
      case "$root/" in
        "$skill"/*) warn root "$root is in the ktl-sidecar skill's own folder, not a repository to screen: run this from the host repository's root, or pass that root" ;;
      esac
    fi ;;
esac

# ---- bundle ----------------------------------------------------------------
# Every find takes a trailing slash. A host may have made .lokf/knowledge a
# link onto a visible knowledge_bundle/ folder, and find never enters a link
# it is handed bare: it would count zero concepts and say nothing.
bundle="$root/.lokf/knowledge"
if [ -d "$bundle" ]; then
  n="$(find "$bundle/" -name '*.md' -not -path '*/.obsidian/*' -not -name index.md -not -name log.md -not -name diataxis.md | wc -l | tr -d ' ')"
  door="$root/knowledge_bundle"
  if [ -L "$door" ]; then doorway="knowledge_bundle -> $(readlink "$door")"
  elif [ -d "$door" ]; then doorway="knowledge_bundle is a folder or junction"
  else doorway="no knowledge_bundle doorway (ln -s .lokf/knowledge knowledge_bundle, or mklink /J on Windows)"; fi
  ok bundle ".lokf/knowledge, $n concepts; $doorway"
else
  miss bundle "no .lokf/knowledge under $root - run ktl-sidecar first" "every skill but ktl-sidecar"
fi
case "$root" in
  *OneDrive*|*Dropbox*|*iCloud*|*"Google Drive"*|*GoogleDrive*|*Nextcloud*)
    info sync "synced folder: links are per machine, and a conflict copy shows up as a duplicate id (conventions rule 7)" ;;
esac

# ---- git -------------------------------------------------------------------
ingit=0; tracked=""; forge=none
if have git && git -C "$root" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  ingit=1
  if [ -n "$(git -C "$root" ls-files .lokf/knowledge 2>/dev/null | head -n 1)" ]; then tracked="tracked"
  elif git -C "$root" check-ignore -q .lokf 2>/dev/null; then tracked="gitignored (no gate, no pull requests, no scheduled librarian)"
  else tracked="not yet committed"; fi
  shallow="$(git -C "$root" rev-parse --is-shallow-repository 2>/dev/null || echo false)"
  crlf="$(git -C "$root" config --get core.autocrlf 2>/dev/null || echo unset)"
  attrs="absent"; [ -f "$root/.lokf/.gitattributes" ] && attrs="present"
  ok git "bundle $tracked; history $([ "$shallow" = true ] && echo shallow || echo full); core.autocrlf=$crlf; .lokf/.gitattributes $attrs"
  [ "$shallow" = true ] && warn git "shallow clone: the conventions script cannot resolve a revision - fetch the full history"
  [ "$attrs" = absent ] && [ -d "$bundle" ] && warn git "no .lokf/.gitattributes: a Windows checkout may differ from CI - ktl-sidecar Step 1 lays it down"
  remote="$(git -C "$root" remote get-url origin 2>/dev/null || true)"
  case "$remote" in
    *github*) forge=github ;;  # github.com, or an Enterprise Server host named after it
    *gitlab*) forge=gitlab ;;
    *codeberg*|*forgejo*|*gitea*) forge=forgejo ;;
    *bitbucket*) forge=bitbucket ;;
    "") forge=none ;;
    *) forge=other ;;
  esac
  gate="$root/.github/workflows/knowledge-registrar.yaml"
  case "$forge" in
    github) if [ -f "$gate" ]; then ok forge "github; gate workflow present"; else warn forge "github; no knowledge-registrar.yaml - ktl-sidecar Step 5 lays it down"; fi ;;
    none) info forge "no origin remote - no gate applies; the host's own review is the record" ;;
    *) info forge "$forge - no gate template for it; the porting recipe is in ktl-sidecar/references/portability.md" ;;
  esac
else
  info git "no git: gate, pull requests and signed-commit checks do not apply; the host's own version history is the record"
fi
if [ -d "$bundle" ]; then
  crlf_files="$(grep -rl "$(printf '\r')" "$bundle" --include='*.md' 2>/dev/null | wc -l | tr -d ' ')"
  [ "${crlf_files:-0}" -gt 0 ] && warn endings "$crlf_files file(s) use CRLF - the conventions script reads them; other tools may not"
  bom_files=0
  while IFS= read -r f; do
    [ "$(head -c 3 "$f" | od -An -tx1 | tr -d ' \n')" = "efbbbf" ] && bom_files=$((bom_files + 1))
  done < <(find "$bundle/" -name '*.md' -not -path '*/.obsidian/*')
  [ "$bom_files" -gt 0 ] && warn endings "$bom_files file(s) start with a byte order mark - conventions rule 9 reports them"
fi

# ---- identity and signing --------------------------------------------------
id=""
if have gh; then
  if gh auth status >/dev/null 2>&1; then
    id="$(gh api user --jq .login 2>/dev/null || true)"
    [ -n "$id" ] && ok identity "gh logged in: confirmations record as human:$id"
    [ -z "$id" ] && warn identity "gh logged in but the login could not be read - a CI token has no user; otherwise offline"
  else
    warn identity "gh installed but not logged in - gh auth login"
  fi
elif have glab; then
  if glab auth status >/dev/null 2>&1; then
    id="$(glab api user 2>/dev/null | sed -n 's/.*"username":"\([^"]*\)".*/\1/p' | head -n 1)"
    [ -n "$id" ] && ok identity "glab logged in: confirmations record as human:$id"
  else
    warn identity "glab installed but not logged in - glab auth login"
  fi
fi
if [ -z "$id" ]; then
  case "$forge" in
    github) miss identity "no authenticated login (gh) - the signing-key route in ktl-curator/references/portability.md is the alternative" "Confirm, Correct now (ktl-curator), named feedback (ktl-docent)" ;;
    gitlab|forgejo|bitbucket|other) miss identity "no authenticated login (glab, or the signing-key route in ktl-curator/references/portability.md)" "Confirm, Correct now (ktl-curator), named feedback (ktl-docent)" ;;
    none) info identity "no forge: on a synced folder the id is the account the platform's version history shows (ktl-curator/references/portability.md)" ;;
  esac
fi
key=""; fmt=openpgp
if [ "$ingit" -eq 1 ]; then
  # --bool reads yes/on/1 as git does; no user.signingkey means git picks the
  # key by the committer's email, which is signing, not its absence.
  sign="$(git -C "$root" config --bool --get commit.gpgsign 2>/dev/null || echo false)"
  key="$(git -C "$root" config --get user.signingkey 2>/dev/null || true)"
  fmt="$(git -C "$root" config --get gpg.format 2>/dev/null || echo openpgp)"
  headsig="unsigned"; git -C "$root" cat-file commit HEAD 2>/dev/null | grep -qE '^gpgsig' && headsig="signed"
  if [ "$sign" = true ]; then
    if [ -n "$key" ]; then keyshow="${key##*/}"; else keyshow="by committer email"; fi
    ok signing "commit.gpgsign on ($fmt key $keyshow); HEAD $headsig"
    if [ "$fmt" = ssh ]; then have ssh-keygen || warn signing "gpg.format is ssh but ssh-keygen is not installed - commits will fail to sign"
    else have gpg || warn signing "gpg.format is $fmt but gpg is not installed - commits will fail to sign"; fi
  else
    warn signing "commit signing off - a curation pull request you open yourself fails the gate (docs/signing-commits.md in knowledge-trust-ladder)"
  fi
fi

# ---- the forge-free gate: keys on file under .lokf/curators/ ---------------
if [ -d "$root/.lokf/curators" ]; then
  nk="$(find "$root/.lokf/curators/" \( -name '*.asc' -o -name '*.pub' \) | wc -l | tr -d ' ')"
  mine="your signing key is not checked (none configured)"
  if [ -n "$key" ]; then
    onfile=0
    if [ "$fmt" = ssh ]; then
      # user.signingkey is a public key file, the private key beside one, or the key itself
      case "$key" in ssh-*|ecdsa-*|sk-*) pub="$key" ;; *.pub) pub="$(cat "$key" 2>/dev/null)" ;; *) pub="$(cat "$key.pub" 2>/dev/null)" ;; esac
      blob="$(printf '%s\n' "$pub" | awk 'NR==1 {print $2}')"
      [ -n "$blob" ] && grep -qsF -- "$blob" "$root/.lokf/curators"/*.pub && onfile=1
    elif have gpg; then
      for fp in $(gpg --batch --with-colons --list-keys "$key" 2>/dev/null | awk -F: '$1=="fpr" {print $10}'); do
        for k in "$root/.lokf/curators"/*.asc; do
          [ -f "$k" ] && gpg --batch --quiet --with-colons --import-options show-only --import "$k" 2>/dev/null | grep -q ":$fp:" && onfile=1
        done
      done
    fi
    if [ "$onfile" -eq 1 ]; then mine="yours is on file"; else mine="yours is not on file - confirmations you sign will fail it until a maintainer adds it in its own change"; fi
  fi
  if [ "${nk:-0}" -eq 0 ]; then warn curators ".lokf/curators/ exists but holds no .asc or .pub key - the forge-free gate fails every confirmation"
  elif [ "$mine" = "yours is on file" ]; then ok curators "$nk key(s) on file; $mine"
  else warn curators "$nk key(s) on file; $mine"; fi
  if ! have gpg && ls "$root/.lokf/curators"/*.asc >/dev/null 2>&1; then warn curators "GPG keys on file but gpg is not installed - knowledge-provenance.sh cannot verify them here"; fi
  if ! have ssh-keygen && ls "$root/.lokf/curators"/*.pub >/dev/null 2>&1; then warn curators "SSH keys on file but ssh-keygen is not installed - knowledge-provenance.sh cannot verify them here"; fi
else
  info curators "no .lokf/curators/ - the forge-free gate skips; only the forge's own gate, if any, checks a confirmation"
fi

# ---- toolkit ---------------------------------------------------------------
# The index uv installs from: UV_DEFAULT_INDEX (a URL, or name=URL), the
# older UV_INDEX_URL, else the default index of a user or system uv.toml,
# else PyPI. The lock and network lines name its host.
index="${UV_DEFAULT_INDEX:-${UV_INDEX_URL:-}}"
case "$index" in *=http*) index="${index#*=}" ;; esac
if [ -z "$index" ]; then
  for f in "${XDG_CONFIG_HOME:-${HOME:-}/.config}/uv/uv.toml" /etc/uv/uv.toml; do
    [ -f "$f" ] || continue
    # An [[index]] table with `default = true` names the default index; a
    # top-level index-url is the older spelling of the same.
    index="$(awk '
      function flush() { if (inidx && dflt && url != "") found = url }
      /^[[:space:]]*\[\[index\]\]/ { flush(); inidx = 1; url = ""; dflt = 0; next }
      /^[[:space:]]*\[/ { flush(); inidx = 0; next }
      inidx && /^[[:space:]]*url[[:space:]]*=/ { url = $0; sub(/^[^"]*"/, "", url); sub(/".*$/, "", url) }
      inidx && /^[[:space:]]*default[[:space:]]*=[[:space:]]*true/ { dflt = 1 }
      !inidx && /^[[:space:]]*index-url[[:space:]]*=/ { top = $0; sub(/^[^"]*"/, "", top); sub(/".*$/, "", top) }
      END { flush(); if (found != "") print found; else if (top != "") print top }' "$f")"
    [ -n "$index" ] && break
  done
fi
index="${index:-https://pypi.org/simple}"
ihost="$(hostof "$index")"
if have uv; then
  floor="$(sed -n 's/.*"lokf\[build\]>=\([0-9.]*\)".*/\1/p' "$root/.lokf/pyproject.toml" 2>/dev/null | head -n 1)"
  if [ -d "$root/.lokf/.venv" ]; then
    installed="$(cd "$root/.lokf" && uv run --no-sync lokf --version 2>/dev/null | sed -n 's/^lokf //p')"
    ok toolkit "uv $(uv --version 2>/dev/null | sed 's/^uv //'); lokf ${installed:-unknown} installed (floor >=${floor:-?})"
  elif [ -f "$root/.lokf/pyproject.toml" ]; then
    warn toolkit "uv present, toolkit not installed - run just lokf-install (or uv sync) in .lokf/ (floor >=${floor:-?})"
  else
    info toolkit "uv $(uv --version 2>/dev/null | sed 's/^uv //') present; no .lokf/pyproject.toml yet"
  fi
  # The recipes pass --check-excerpts, and --schema to convert and serve,
  # which lokf 0.8.0 does not take.
  case "${floor:-}" in
    0.[0-8]|0.[0-8].*) warn toolkit "the floor is >=$floor and the justfile's recipes need lokf 0.9.0 - raise it to \"lokf[build]>=0.9.0\" in .lokf/pyproject.toml and run uv lock there" ;;
  esac
  # A domain schema imports the copy of LOKF core beside it, and the gate
  # runs the lokf that uv.lock pins, which may be newer than the floor. A
  # copy from another release can reject a concept that lokf reads: 0.9.0
  # reads a bare-date stale_after as a datetime, which 0.8.0's copy rejects.
  copy="$(sed -n 's/^version: *\([0-9.]*\).*/\1/p' "$root/.lokf/lokf.yaml" 2>/dev/null | head -n 1)"
  pinned="$(awk '/^name = "lokf"$/ { hit = 1; next } hit { if (sub(/^version = "/, "")) { sub(/".*$/, ""); print } exit }' "$root/.lokf/uv.lock" 2>/dev/null)"
  pinned="${pinned:-${installed:-}}"
  if [ -n "$copy" ] && [ -n "$pinned" ] && [ "$copy" != "$pinned" ]; then
    warn core ".lokf/lokf.yaml is lokf $copy's schema and the toolkit is lokf $pinned - copy the installed package's lokf.yaml over it, as step 1 of ktl-librarian's domain-schema recipe shows"
  fi
  if have just; then ok just "just $(just --version 2>/dev/null | sed 's/^just //')"; else info just "just not installed - uvx --from rust-just just works the same"; fi
  # The workflows run the just uv.lock pins, checked by hash, where it pins one.
  if [ -f "$root/.lokf/uv.lock" ] && ! grep -qx 'name = "rust-just"' "$root/.lokf/uv.lock"; then
    info just-pin "uv.lock pins no just, so the workflows fetch rust-just by version; uv add rust-just==1.47.0 in .lokf/ pins it by hash"
  fi
else
  miss toolkit "uv not installed - lokf validate, convert and query unavailable, and the conventions script skips its parser's half (rules 2, 3, 4, 7, 9, 10, 12, 13, 14, 15, 16, 17, 18); only the manual schema cross-check remains" "lokf validate and thirteen of the eighteen conventions (every skill's audit)"
fi

# A lokf command given no --schema reads `[tool.lokf] schema` in
# pyproject.toml. The recipes pass the justfile's `schema :=` line when it is
# set, and the release, the website and the librarian read only that line, so
# the two must name one file.
jschema="$(sed -n 's/^schema := "\([^"]*\)"$/\1/p' "$root/.lokf/justfile" 2>/dev/null | head -n 1)"
tschema="$(awk -v q="'" '
  /^[[:space:]]*\[/ { intool = ($0 ~ /^[[:space:]]*\[tool\.lokf\][[:space:]]*(#.*)?$/); next }
  intool && /^[[:space:]]*schema[[:space:]]*=/ {
    v = $0; sub(/^[^=]*=[[:space:]]*/, "", v)
    if (match(v, /^"[^"]*"/) || match(v, "^" q "[^" q "]*" q)) print substr(v, 2, RLENGTH - 2)
    exit
  }' "$root/.lokf/pyproject.toml" 2>/dev/null)"
jschema="${jschema#./}"
tschema="${tschema#./}"
if [ -n "$tschema" ] && [ -z "$jschema" ]; then
  warn schema "[tool.lokf] schema in .lokf/pyproject.toml is $tschema and the justfile's schema line is empty - the recipes check against it, the release and the librarian do not; put the same path on the line"
elif [ -n "$tschema" ] && [ "$tschema" != "$jschema" ]; then
  warn schema "[tool.lokf] schema in .lokf/pyproject.toml is $tschema and the justfile's schema line is $jschema - the recipes check against the line, a bare lokf command against pyproject.toml; set both to one path"
fi

# The gate, the release and the scheduled librarian install the toolkit with
# `uv sync --locked`, which fails when git holds no lock to install from.
if [ "$ingit" = 1 ] && [ "$tracked" = tracked ] && [ -f "$root/.lokf/pyproject.toml" ] && [ -f "$root/.github/workflows/knowledge-registrar.yaml" ] \
   && [ -z "$(git -C "$root" ls-files .lokf/uv.lock 2>/dev/null | head -n 1)" ]; then
  warn toolkit ".lokf/uv.lock is not in git - the gate installs the toolkit with uv sync --locked and fails without it; run uv lock in .lokf/ and commit the file"
fi
# A lock records the index it was made against, and every file's address
# there. Where uv reads another index, uv sync --locked fails on it, and
# uv sync rewrites every address to the index uv reads.
if [ -f "$root/.lokf/uv.lock" ]; then
  lhost="$(hostof "$(sed -n 's/.*registry = "\([^"]*\)".*/\1/p' "$root/.lokf/uv.lock" | sort | uniq -c | sort -rn | head -n 1 | sed 's/^ *[0-9]* *//')")"
  if [ -n "$lhost" ] && [ "$lhost" != "$ihost" ]; then
    warn lock ".lokf/uv.lock was made against $lhost, and uv here reads $ihost - uv sync in .lokf/ rewrites it to $ihost; commit that only where the gate's runner reads $ihost too"
  fi
fi

# ---- installed skills, and drift between copies -----------------------------
found=""; templates=""
for dir in .claude/skills .github/skills .agents/skills skills; do
  here=""
  for s in ktl-sidecar ktl-librarian ktl-curator ktl-docent ktl-prose ktl-website; do
    [ -f "$root/$dir/$s/SKILL.md" ] && here="$here ${s#ktl-}"
  done
  [ -n "$here" ] && found="${found}${found:+; }$dir:$here"
done
# The templates to compare host copies against: bare skills/ first (a
# repository that publishes the skills is its own canonical copy), then the
# wrapper's install locations in its order.
for dir in skills .claude/skills .github/skills .agents/skills; do
  [ -z "$templates" ] && [ -d "$root/$dir/ktl-sidecar/templates" ] && templates="$root/$dir/ktl-sidecar/templates"
done
if [ -n "$found" ]; then
  ok skills "$found"
  for s in ktl-sidecar ktl-librarian ktl-curator ktl-docent ktl-prose ktl-website; do
    first=""
    for dir in .claude/skills .github/skills .agents/skills skills; do
      [ -d "$root/$dir/$s" ] || continue
      if [ -z "$first" ]; then first="$root/$dir/$s"
      elif [ "$(cd "$first" && pwd -P)" != "$(cd "$root/$dir/$s" && pwd -P)" ] && ! diff -rq "$first" "$root/$dir/$s" >/dev/null 2>&1; then
        warn skills "two copies of $s differ: ${first#"$root"/} and $dir/$s - one is stale; reinstall or remove it"
      fi
    done
  done
else
  info skills "no KTL skill installed under .claude/skills, .github/skills, .agents/skills or skills/"
fi
# Skills installed for one user serve that user's live sessions. The
# scheduled librarian runs on a fresh runner and reads only a copy in the
# repository.
user=""
for dir in .claude/skills .copilot/skills .agents/skills; do
  here=""
  for s in ktl-sidecar ktl-librarian ktl-curator ktl-docent ktl-prose ktl-website; do
    [ -f "${HOME:-/nonexistent}/$dir/$s/SKILL.md" ] && here="$here ${s#ktl-}"
  done
  [ -n "$here" ] && user="${user}${user:+; }~/$dir:$here"
done
[ -z "$user" ] || info skills "user scope: $user; the scheduled librarian needs a copy in the repository"

# ---- host copies of the sidecar's templates ----------------------------------
# The conventions script runs its Python half, so a host holding the .sh
# without the .py has a gate that fails, not a stale copy. This is reported
# whether or not a sidecar is installed to compare against. A bundle with no
# knowledge-feedback.sh is the same kind of gap rather than drift. A current
# ktl-docent runs its own copy, but an earlier release runs this one, and
# without it has to open feedback.md to add an entry, which is the one thing
# that script exists to stop. A host on a sidecar that predates it should
# hear so before a reader's first recorded gap, not after.
script_gaps=""
if [ -f "$root/.lokf/scripts/knowledge-conventions.sh" ] && [ ! -f "$root/.lokf/scripts/knowledge-conventions.py" ]; then
  script_gaps=".lokf/scripts/knowledge-conventions.py missing beside the .sh, which runs it"
fi
if [ -d "$bundle" ] && [ ! -f "$root/.lokf/scripts/knowledge-feedback.sh" ]; then
  script_gaps="${script_gaps}${script_gaps:+, }.lokf/scripts/knowledge-feedback.sh missing, so an earlier ktl-docent must edit feedback.md by hand"
fi
if [ -d "$bundle" ] && [ ! -f "$root/.lokf/scripts/knowledge-apply.sh" ]; then
  script_gaps="${script_gaps}${script_gaps:+, }.lokf/scripts/knowledge-apply.sh missing, so ktl-librarian must write the bundle by hand"
fi
if [ -d "$bundle" ] && [ ! -f "$root/.lokf/scripts/knowledge-report.sh" ]; then
  script_gaps="${script_gaps}${script_gaps:+, }.lokf/scripts/knowledge-report.sh missing, so ktl-curator and an earlier ktl-docent must work each trust label out by hand"
fi
# A host moves TRUST_LADDER_SKILLS_REF, and the commit beside it, on its own
# schedule, so a different pin is not drift; every other byte of the
# librarian workflow still counts. The installed sidecar's
# knowledge-sync.manifest says which copies a host may carry, and
# knowledge-sync.sh keeps each at the release's bytes. The justfile is the
# host's from its first line, and is not held here.
unpin() { sed -E -e 's/(TRUST_LADDER_SKILLS_REF: )v[0-9]+\.[0-9]+\.[0-9]+/\1vX.Y.Z/' -e 's/(TRUST_LADDER_SKILLS_SHA: )[0-9a-f]{40}/\1COMMIT/' "$1"; }
if [ -n "$templates" ] && [ -d "$root/.lokf" ] && [ ! -f "$templates/knowledge-sync.manifest" ]; then
  warn copies "${templates#"$root"/} has no knowledge-sync.manifest, so the installed sidecar predates it and the host's copies were not compared; reinstall the sidecar at the release the librarian workflow pins"
elif [ -n "$templates" ] && [ -d "$root/.lokf" ]; then
  drift="$script_gaps"
  while read -r rule template copy _; do
    [ "$rule" = copy ] || continue
    src="$templates/$template"; dst="$root/$copy"
    [ -f "$dst" ] || continue
    [ -f "$src" ] || { drift="${drift}${drift:+, }$copy (the installed sidecar lists it and lacks it)"; continue; }
    cmp -s <(unpin "$src") <(unpin "$dst") || drift="${drift}${drift:+, }$copy"
  done < <(sed 's/#.*//' "$templates/knowledge-sync.manifest")
  if [ -z "$drift" ]; then
    ok copies "host copies match the installed sidecar's templates (${templates#"$root"/})"
  else
    warn copies "differ from ${templates#"$root"/}: $drift - a deliberate host edit, or a template bump not yet copied (ktl-sidecar repair)"
  fi
elif [ -n "$script_gaps" ]; then
  warn copies "$script_gaps - the ktl-sidecar repair lays it down"
fi

# ---- scripts ---------------------------------------------------------------
# The pen and the conventions script each run a Python half: on the
# sidecar's .venv when it holds pyyaml on Python 3.9 or later, else through
# uv after uv_ready, the same function as theirs. Nothing above runs either,
# so a host whose index uv cannot install from would look ready while
# ktl-librarian cannot write and the gate cannot check. uv keeps one
# environment per script, so both are installed here, into uv's cache and
# never into the repository. The pen alone falls back to python3.
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
if [ -d "$bundle" ] && [ -f "$root/.lokf/scripts/knowledge-apply.py" ] && [ -f "$root/.lokf/scripts/knowledge-conventions.py" ]; then
  venv="$root/.lokf/.venv/bin/python"; [ -e "$venv" ] || venv="$root/.lokf/.venv/Scripts/python.exe"
  if [ -x "$venv" ] && "$venv" -c 'import sys; assert sys.version_info >= (3, 9); import yaml' >/dev/null 2>&1; then
    ok scripts "the pen and the conventions script run on .lokf/.venv"
  elif have uv; then
    unready=""; lost=""; pen=""
    for s in apply conventions; do
      uv_ready "$root/.lokf/scripts/knowledge-$s.py" 2>/dev/null && continue
      if [ "$s" = apply ] && have python3 && python3 -c 'import sys; assert sys.version_info >= (3, 9); import yaml' >/dev/null 2>&1; then
        pen="; the pen runs on python3's own pyyaml"; continue
      fi
      unready="${unready}${unready:+ and }knowledge-$s.py"
      case "$s" in
        apply) lost="the pen (ktl-librarian writes nothing)" ;;
        *) lost="${lost}${lost:+ and }the conventions check (the gate fails)" ;;
      esac
    done
    if [ -z "$unready" ]; then
      ok scripts "uv installs the scripts' packages${uvflags[0]+; the index serves no upload times, so exclude-newer is lifted for the pinned ones}$pen"
    else
      # uv prints an informational line before its error, so the error line
      # is named, or else the last line, which is the script's own reason.
      why="$(printf '%s\n' "$uverr" | grep -E '^(error:|x |× )' | head -n 1)"
      [ -n "$why" ] || why="$(printf '%s\n' "$uverr" | grep -v '^[[:space:]]*$' | tail -n 1)"
      miss scripts "uv could not install the packages of $unready${why:+ ($why)}$pen - run uv sync in .lokf/, and both scripts use that .venv" "$lost"
    fi
  elif ! { have python3 && python3 -c 'import sys; assert sys.version_info >= (3, 9); import yaml' >/dev/null 2>&1; }; then
    miss scripts "no .lokf/.venv, no uv, and no python3 3.9 or later with pyyaml - the pen cannot start; install uv, or run uv sync in .lokf/" "the pen (ktl-librarian writes nothing)"
  fi
fi

# ---- ingest ----------------------------------------------------------------
# A host that mirrors sources from outside the repository has .lokf/ingest.yaml.
# The script's own status line says how many entries, how many mirrored files
# and which token names are present; it prints no value. A mirror file the
# lock names and the disk has lost, or a file the lock does not name, is a
# warning: a run restores the first, and the second is nobody's. So is a git
# older than a `git` entry needs, since the run refuses that entry. Without
# the script, the manifest is a wish nothing fulfils.
if [ -f "$root/.lokf/ingest.yaml" ]; then
  if [ -f "$root/.lokf/scripts/knowledge-ingest.sh" ]; then
    status="$(bash "$root/.lokf/scripts/knowledge-ingest.sh" --root "$root" --status 2>/dev/null)" || status=""
    case "$status" in
      "ingest: "*"missing from the mirror"*|"ingest: "*"the lock does not name"*|"ingest: "*"this git is "*) warn ingest "${status#ingest: }" ;;
      "ingest: "*) info ingest "${status#ingest: }" ;;
      *) info ingest ".lokf/ingest.yaml is here; its status was not read (no .lokf/.venv or python3 3.9 or later with pyyaml, and uv could not run it)" ;;
    esac
  else
    warn ingest ".lokf/ingest.yaml is here but .lokf/scripts/knowledge-ingest.sh is not, so nothing is mirrored - the ktl-sidecar repair lays it down"
  fi
fi

# ---- session ---------------------------------------------------------------
unattended=""
for v in CI GITHUB_ACTIONS GITLAB_CI TF_BUILD; do
  val="${!v:-}"; [ -n "$val" ] && unattended="${unattended}${unattended:+, }$v"
done
agent=""
[ -n "${CLAUDECODE:-}" ] && agent="Claude Code"
[ -n "${CODESPACES:-}" ] && agent="${agent}${agent:+, }Codespaces"
[ "${TERM_PROGRAM:-}" = vscode ] && agent="${agent}${agent:+, }VS Code terminal"
if [ -n "$unattended" ]; then
  info session "unattended ($unattended set): ktl-curator stops after its report; ktl-librarian writes the bundle only through knowledge-apply.sh"
else
  info session "attended${agent:+ ($agent)}: a person can answer item by item"
fi
if have curl; then
  if curl -sI --max-time 4 "${index%/}/lokf/" >/dev/null 2>&1; then info network "$ihost reachable"; else warn network "$ihost unreachable - uv cannot install the toolkit here, and version checks fail"; fi
else
  warn network "curl not installed - the signing-key identity route and the version check need it"
fi

printf 'Preflight: %d missing, %d warning(s).%s\n' "$missing" "$warns" "${disables:+ Missing disables: $disables.}"
exit 0
