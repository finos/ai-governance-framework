#!/usr/bin/env bash
# The signature half of the registrar's provenance gate, with no forge.
#
# The GitHub `provenance` job asks GitHub whether the person named in a new
# `by: human:<id>` line approved the pull request or signed its commit. Off
# GitHub there is no such job, and on GitHub it is the only check. This
# script does the signature half anywhere git runs.
#
# The repository carries one public key per curator id under
# `.lokf/curators/`: `<id>.asc`, a GPG key as `gpg --armor --export` writes
# it, or `<id>.pub`, an OpenSSH public key as `ssh-keygen` writes it, one key
# per line. Every commit in a range that adds, changes or removes a
# `human:<id>` event under the bundle must be signed by a key on file for
# exactly that id. The event is a `verified` entry, or the `generated` record
# the curator's Correct writes. A GPG key counts with every subkey it carries,
# since most keys sign with a subkey. An SSH key is verified with
# `ssh-keygen -Y verify` (OpenSSH 8.2+) against the commit's own payload.
#
# A removal is a claim too. A person's record is never removed without that
# person. A `verified` event every parent held and the commit no longer holds,
# struck out or gone with its concept, needs the same signature as one that
# was added. A person's `generated` record may be replaced by another
# person's, which is what the curator's Correct writes, and that second
# person signs it as an addition. A record replaced by anything else needs
# the signature of the person it named.
#
# `--unattended` is the other half, for a change nobody stands behind: the
# scheduled librarian's. It compares the working tree, staged or not, with
# HEAD, and needs no key and no forge. It reports every way such a change
# touches a person's record:
#   - a `human:` event added, changed or removed in a layout it reads;
#   - frontmatter it cannot read, which may hold one, added, changed or removed;
#   - a symbolic link left under the bundle;
#   - a person's note under `## Open questions` added or removed;
#   - text a person wrote, changed.
# knowledge-apply.sh refuses each of these before it writes. This is the same
# refusal, checked on the result, by a job the agent never ran in.
#
# Findings, one line each, exit 1:
#   - the commit is unsigned, or its signature does not verify;
#   - it is signed by a key other than the one on file for that id, or by a
#     key that has expired or been revoked;
#   - the id has no key on file (a stranger, or a curator not yet added), or
#     is not a login any forge could list;
#   - the range adds, changes or removes that id's own key file *and* records
#     a confirmation by them: a key is added in its own reviewed change first,
#     so nobody registers a key and vouches with it in one step;
#   - a commit touches a bundle path git has to quote (`"`, `\` or a control
#     character in the name), which this line reader cannot hold;
#   - a commit changes frontmatter this reader cannot follow, or leaves a
#     symbolic link under the bundle, either of which can hold an event it
#     would not see.
# With no `.lokf/curators/` directory it says so and exits 0: there is nothing
# to verify against, and the forge's gate, if any, is the only check.
#
# What a pass proves: the holder of that key made that commit. Not that
# anyone read the source, and not who the person is beyond what the key file's
# reviewed history says. Bash 3.2 and POSIX tools; needs git, and gpg or
# ssh-keygen for the kind of key on file.
#
# Usage: knowledge-provenance.sh <base-ref> [head-ref] [bundle-dir]
#        knowledge-provenance.sh --unattended [bundle-dir]
#   For example:
#        knowledge-provenance.sh origin/main            (a branch, locally)
#        knowledge-provenance.sh "$BASE_SHA" "$HEAD_SHA"  (in CI)
#        knowledge-provenance.sh --unattended            (what the librarian workflow runs)
[ -n "${BASH_VERSION:-}" ] || { echo "run this with bash: bash ${0##*/} <base-ref> [head-ref] | --unattended" >&2; exit 2; }
set -u
# A-Z, a-z and 0-9 in a case glob mean the ASCII letters and digits, not
# whatever a locale collates between them, so the login check cannot be
# widened by the host's locale. A no-op where the option is unknown (bash 3.2).
shopt -s globasciiranges 2>/dev/null || :
# Byte-oriented awk, sort and comm, so this gate reads raw bytes on any awk and
# in any locale. The frontmatter reader strips a byte order mark by its bytes,
# since a UTF-8 gawk would otherwise read those three bytes as one character
# and the strip would miss. And `sort` feeds `comm` a byte order it agrees
# with.
export LC_ALL=C

unattended=0
if [ "${1:-}" = "--unattended" ]; then
  unattended=1; base=HEAD; head=""; bundle="${2:-.lokf/knowledge}"
else
  base="${1:-}"; head="${2:-HEAD}"; bundle="${3:-.lokf/knowledge}"
fi
[ -n "$base" ] || { echo "usage: knowledge-provenance.sh <base-ref> [head-ref] [bundle-dir] | --unattended [bundle-dir]" >&2; exit 2; }
command -v git >/dev/null 2>&1 || { echo "git is required" >&2; exit 2; }
root="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "not inside a git work tree" >&2; exit 2; }
cd "$root" || exit 2
curators=".lokf/curators"
# A range that deletes the folder has not opted out: its confirmations then
# name someone with no key on file. Only a base that never held it has.
if [ "$unattended" -eq 0 ] && [ ! -d "$curators" ] && [ -z "$(git ls-tree "$base" -- "$curators" 2>/dev/null)" ]; then
  echo "skipped - no $curators/ directory; nothing to verify confirmations against (the forge's gate, if any, is the only check)"
  exit 0
fi

fail=0
say() { echo "$1"; fail=1; }
have() { command -v "$1" >/dev/null 2>&1; }

# Throwaway keyring for the GPG keys on file, and a scratch directory for the
# SSH payloads and signatures, both gone on exit.
home="$(mktemp -d)"
trap 'rm -rf "$home"' EXIT
chmod 700 "$home"
gpg_ok=0
if [ "$unattended" -eq 0 ] && have gpg; then
  gpg_ok=1
  for k in "$curators"/*.asc; do
    [ -f "$k" ] || continue
    GNUPGHOME="$home" gpg --batch --quiet --import "$k" 2>/dev/null || say "$k: not an importable armored public key"
  done
fi
gpg_fprs() {  # id -> every fingerprint in .lokf/curators/<id>.asc, primary and subkeys, one per line
  GNUPGHOME="$home" gpg --batch --quiet --with-colons --import-options show-only --import "$curators/$1.asc" 2>/dev/null \
    | awk -F: '$1=="fpr" {print $10}'
}
# ssh-keygen verifies a detached signature against an allowed-signers file
# naming the principal, so each id's .pub becomes `<id> namespaces="git" <key>`.
allowed_of() {  # id -> path of an allowed-signers file listing that id's keys
  awk -v id="$1" '$1 ~ /^(ssh-|ecdsa-|sk-)/ {print id " namespaces=\"git\" " $0}' "$curators/$1.pub" > "$home/$1.allowed"
  echo "$home/$1.allowed"
}
# A commit's signed payload is the object with its `gpgsig` header and that
# header's continuation lines removed; the signature is those lines unindented.
payload_of() {
  git cat-file commit "$1" | awk '
    BEGIN {hdr = 1}
    hdr && $0 == "" {hdr = 0}
    hdr && /^gpgsig(-sha256)? / {skip = 1; next}
    hdr && skip && /^ / {next}
    {skip = 0; print}'
}
signature_of() {
  git cat-file commit "$1" | awk '
    !done && /^gpgsig(-sha256)? / {insig = 1; sub(/^gpgsig(-sha256)? /, ""); print; next}
    insig && /^ / {sub(/^ /, ""); print; next}
    insig {insig = 0; done = 1}'
}
sig_format() {  # commit -> pgp | ssh | none
  case "$(git cat-file commit "$1" | grep -m1 -E '^gpgsig(-sha256)? ' || true)" in
    *"BEGIN PGP SIGNATURE"*) echo pgp ;;
    *"BEGIN SSH SIGNATURE"*) echo ssh ;;
    *) echo none ;;
  esac
}

# The human events of a concept, one per line, as
# `<id or path>\t<by>\t<at>\t<revision>\t<verified|generated>`. They are its
# `verified` list and its `generated` record, since the curator's Correct
# writes `generated.by: human:<id>`. It reads a block list in
# any key order, a flow-style item, a flow sequence and a bare mapping, and
# refuses whatever else it meets, as the actor (unreadable). Only the
# frontmatter is read, so an example event in a body code fence is not a
# claim. Events are keyed by the concept's `id`, so a renamed concept keeps
# its events and a confirmation copied into another concept does not.
#
# An event present in a commit's tree and absent from every parent's is new or
# changed, and its actor must stand behind it. A re-dated `at` or a moved
# `revision` is as much a claim as a new line. Every parent is compared, so a
# merge that brings in another curator's confirmation claims nothing, and one
# that adds an event neither side held is read like any other commit.
human_events() {  # path -> events, reading the concept on stdin
  awk -v path="$1" '
  function val(s) { sub(/^[^:]*:[[:space:]]*/, "", s); gsub(/["'"'"']/, "", s); sub(/[[:space:]]+$/, "", s); return s }
  # Nothing this reader cannot follow is taken for no event. The schema gives
  # an event `by`, `at` and `revision` and no other key, so any other key is a
  # spelling it cannot follow: a quoted `by`, a merge, an alias. Such an event,
  # and one whose actor is outside the shape the schema allows, comes out as the actor
  # (unreadable), which is no login, so each gate refuses it as it refuses any
  # id it cannot check.
  function kv(l,  k) { k = l; sub(/:.*/, "", k); sub(/^[[:space:]]+/, "", k)
    if (k == "by") by = val(l); else if (k == "at") at = val(l); else if (k == "revision") rev = val(l); else odd = 1 }
  function actor(a) { return a !~ /\\/ && (a ~ /^(human|process):[^[:space:]]+$/ || a ~ "^[^[:space:]/]+/[^[:space:]/]+$") }
  # Two revisions of a file must differ here whenever they differ in what a
  # parser could read, or an edit inside an unreadable block passes unseen.
  # So a file holds one unreadable line, and that line carries everything up
  # to the closing delimiter, with control bytes YAML forbids in place of
  # its tabs and line ends.
  function unread() { bad = 1 }
  function emit() { if (inev && (odd || !actor(by))) { bad = 1; by = "" }
    if (inev && by ~ /^human:/) { sub(/^human:/, "", by); out = out (cid ? cid : path) "\t" by "\t" at "\t" rev "\t" kind "\n" }
    inev = 0; odd = 0; by = ""; at = ""; rev = "" }
  function flow(s,  n, parts, i) { emit(); inev = 1; gsub(/[{}]/, "", s); n = split(s, parts, ",")
    for (i = 1; i <= n; i++) if (parts[i] !~ /^[[:space:]]*$/) kv(parts[i]); emit() }
  # A flow verified/generated may span lines: valid YAML that a block-only
  # reader skips, which would let a forged confirmation past the gate.
  # Accumulate from the opener to its closing bracket, then parse: a sequence
  # into its events, a mapping as one event.
  function flushflow(  b, n, items, i) { b = flowbuf
    if (b ~ /(^|[[:space:]])#/) unread()
    if (flowseq) { sub(/^\[/, "", b); sub(/\].*/, "", b) } else { sub(/^\{/, "", b); sub(/\}.*/, "", b) }
    sub(/^[[:space:]]+/, "", b); sub(/[[:space:]]+$/, "", b)
    if (b != "") { if (flowseq) { n = split(b, items, /\}[[:space:]]*,/); for (i = 1; i <= n; i++) if (items[i] !~ /^[[:space:]]*$/) flow(items[i]) } else flow(b) }
    inflow = 0; flowbuf = "" }
  BEGIN { fm = 0; inv = 0; inev = 0; inflow = 0; cid = ""; out = ""; odd = 0; bad = 0; plain = 0; dashes = 0; seen = 0 }
  { sub(/\r$/, ""); line = $0; gsub(/\t/, "\002", line); raw[NR] = line }
  # A byte order mark or a CRLF on the opener would make a block-only reader see
  # no "---", read no events, and wave a forged unsigned event past the gate,
  # though every YAML parser strips both and sees it. Strip them (bytes, under
  # LC_ALL=C) so the gate reads what the parsers read.
  NR == 1 { sub(/^\357\273\277/, ""); if ($0 == "---") { fm = 1; next } else plain = 1 }
  # The toolkit opens a block at the first `---` in the file, on any line, with
  # anything before it. So a file that opens any other way may still hold
  # events this reader never sees. log.md holds none.
  plain { dashes += gsub(/---/, "&"); next }
  # A parser ends a line at a bare carriage return, U+0085, U+2028 and U+2029,
  # and this reader does not, so an event can sit inside one line it reads.
  /\r|\302\205|\342\200[\250\251]/ { unread() }
  inflow && $0 == "---" { flushflow(); exit }
  inflow { flowbuf = flowbuf " " $0; if (index($0, flowseq ? "]" : "}")) flushflow(); next }
  fm && $0 == "---" { emit(); exit }
  # A block indented whole, and a top-level key no plain `key:` spells, such as
  # a quoted key, `? key`, `<<:` or a flow mapping, can each hold an event.
  !seen && /[^[:space:]]/ && !/^[[:space:]]*#/ { seen = 1; if (/^[[:space:]]/) unread() }
  /^["'"'"'?{[<!&*:|>]/ || /^(verified|generated)[[:space:]]+:/ { emit(); inv = 0; unread(); next }
  /^id:/ { cid = val($0) }
  /^(verified|generated):/ { emit(); inv = 1; kind = $0; sub(/:.*/, "", kind); rest = $0; sub(/^(verified|generated):[[:space:]]*/, "", rest); sub(/[[:space:]]+$/, "", rest)
    if (rest ~ /^\{/) { flowseq = 0; flowbuf = rest; inv = 0; if (index(rest, "}")) flushflow(); else inflow = 1 }
    else if (rest ~ /^\[/) { flowseq = 1; flowbuf = rest; inv = 0; if (index(rest, "]")) flushflow(); else inflow = 1 }
    else if (rest != "" && rest !~ /^#/ && rest !~ /^(null|~)$/) unread()
    next }
  inv && /^[^[:space:]-]/ { emit(); inv = 0 }
  inv && /^[[:space:]]*-[[:space:]]*(#.*)?$/ { emit(); inev = 1; next }
  inv && /^[[:space:]]*-[[:space:]]*\{/ { rest = $0; sub(/^[[:space:]]*-[[:space:]]*/, "", rest); flow(rest); next }
  inv && /^[[:space:]]*-[[:space:]]+/ { emit(); inev = 1; rest = $0; sub(/^[[:space:]]*-[[:space:]]+/, "", rest); kv(rest); next }
  inv && /^[[:space:]]+[a-z_]+:/ { inev = 1; kv($0); next }
  inv && /^[[:space:]]+[^[:space:]#]/ { inev = 1; odd = 1; next }
  END { if (plain && dashes >= 2 && path !~ /(^|\/)log\.md$/) unread(); emit(); printf "%s", out; if (bad) { printf "%s\t(unreadable)\t\t", cid ? cid : path; for (i = 1; i <= NR; i++) if (i in raw) printf "%s\001", raw[i]; printf "\tverified\n" } }'
}
events_in() {  # ref, paths on stdin -> the human events of those paths at that ref, sorted
  while IFS= read -r f; do
    git show "$1:$f" 2>/dev/null | human_events "$f"
  done | sort
}
# The paths a commit changes against any of its parents. Without -m, git
# lists nothing for a merge commit. With core.quotePath on, a name
# with a byte above 0x7f would come C-quoted and `.md$` would miss it, so it
# is off. Git still quotes `"`, `\` and control characters, and the caller
# refuses those.
changed_paths() {  # commit, pathspecs... -> paths, one per line
  git -c core.quotePath=false diff-tree --no-commit-id --name-only -r -m "$@" 2>/dev/null | sort -u
}

# The events a commit removes: those every parent held that it no longer
# holds. A `verified` event is never removed without its person. A person's
# `generated` record may be replaced by another person's, the curator's
# Correct, which that person signs as an addition. So it counts only when no
# person's `generated` record stands in its place.
removed_from() {  # events-before file, events-now file -> the removed events that need their person
  comm -23 "$1" "$2" | awk -F'\t' -v now="$2" '
    BEGIN { while ((getline line < now) > 0) { split(line, f, "\t"); if (f[5] == "generated") kept[f[1]] = 1 } }
    $5 == "verified" || !($1 in kept)'
}

# The toolkit reads a symbolic link as the file it points at, and git holds it as
# the path it names. So a concept that is a link onto a file outside the bundle
# carries events no reader here sees, and a later edit of that file changes it
# unseen. The two names of the bundle may be links onto each other, as the
# doorway and a host rearranged by hand have them, and nothing else may be one.
# `.lokf` itself is always asked about: as a link it takes the whole bundle out
# of the paths this script lists, so no change under it would name it.
allowed_link() {  # path, the path it points at -> whether this is one of the bundle's two names
  case "$1:$2" in
    "$bundle:../knowledge_bundle"|"knowledge_bundle:$bundle") return 0 ;;
    *) return 1 ;;
  esac
}
links_in() {  # commit, paths on stdin -> those the commit holds as a link it may not hold
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    case "$(git ls-tree "$1" -- "$f" 2>/dev/null)" in 120000\ *) ;; *) continue ;; esac
    allowed_link "$f" "$(git show "$1:$f" 2>/dev/null)" || printf '%s\n' "$f"
  done
}

# ---- --unattended: a change nobody stands behind may touch no person's record ----
# A concept's body up to `## Open questions`, without trailing blank lines:
# the text a person wrote, which a note added below it does not change.
body_of() {
  awk '{ sub(/\r$/, "") }
       NR == 1 { sub(/^\357\273\277/, "") }
       NR == 1 && $0 == "---" { fm = 1; next }
       fm == 1 { if ($0 == "---") fm = 2; next }
       /^## Open questions[ \t]*$/ { exit }
       /^[ \t]*$/ { blank++; next }
       { while (blank > 0) { print ""; blank-- } print }'
}
notes_of() {  # path, a concept on stdin -> each line a person's note would be, keyed by the path
  grep -E '^- [0-9]{4}-[0-9]{2}-[0-9]{2}, *human:' | awk -v f="$1" '{ print f "\t" $0 }' || true
}
if [ "$unattended" -eq 1 ]; then
  git rev-parse -q --verify HEAD >/dev/null 2>&1 || { echo "no commit to compare with" >&2; exit 2; }
  listed="$( { git -c core.quotePath=false diff --no-renames --name-only HEAD -- "$bundle" knowledge_bundle 2>/dev/null
               git -c core.quotePath=false ls-files --others --exclude-standard -- "$bundle" knowledge_bundle 2>/dev/null; } | sort -u )"
  quoted="$(printf '%s\n' "$listed" | grep '^"' || true)"
  [ -z "$quoted" ] || say "the change touches a bundle path git has to quote, which this script cannot read - rename it: $(printf '%s' "$quoted" | tr '\n' ' ')"
  while IFS= read -r f; do
    if [ -L "$f" ] && ! allowed_link "$f" "$(readlink "$f")"; then
      say "$f: an unattended change leaves a symbolic link under the bundle, which this gate cannot read - a concept is a file of its own"
    fi
  done < <(printf '%s\n%s\n' "$listed" "${bundle%%/*}" | grep -v '^"' || true)
  : > "$home/was.events"; : > "$home/now.events"; : > "$home/was.notes"; : > "$home/now.notes"
  while IFS= read -r f; do
    case "$f" in *.md) ;; *) continue ;; esac
    git show "HEAD:$f" > "$home/was.file" 2>/dev/null || : > "$home/was.file"
    if [ -f "$f" ]; then cat "$f" > "$home/now.file"; else : > "$home/now.file"; fi
    human_events "$f" < "$home/was.file" >> "$home/was.events"
    human_events "$f" < "$home/now.file" >> "$home/now.events"
    notes_of "$f" < "$home/was.file" >> "$home/was.notes"
    notes_of "$f" < "$home/now.file" >> "$home/now.notes"
    if [ -f "$f" ] && human_events "$f" < "$home/was.file" | awk -F'\t' '$5 == "generated" { found = 1 } END { exit !found }' \
       && [ "$(body_of < "$home/was.file")" != "$(body_of < "$home/now.file")" ]; then
      say "$f: a person wrote this text, and an unattended change rewrites it"
    fi
  done < <(printf '%s\n' "$listed" | grep -v '^"' || true)
  # A rename shows above as a delete and an add, so a person-authored concept
  # renamed and rewritten in one change slips the per-path check: the new path
  # has no copy at HEAD. Pair the two by git's rename detection and compare the
  # old HEAD body with the new one, so the body check follows the concept as
  # the event check, keyed by id, already does.
  while IFS="$(printf '\t')" read -r status old new; do
    case "$status" in R*) ;; *) continue ;; esac
    case "$new" in *.md) ;; *) continue ;; esac
    git show "HEAD:$old" > "$home/was.file" 2>/dev/null || continue
    [ -f "$new" ] || continue
    cat "$new" > "$home/now.file"
    if human_events "$old" < "$home/was.file" | awk -F'\t' '$5 == "generated" { found = 1 } END { exit !found }' \
       && [ "$(body_of < "$home/was.file")" != "$(body_of < "$home/now.file")" ]; then
      say "$new: a person wrote this text, which an unattended change rewrites under a new name (was $old)"
    fi
  done < <(git -c core.quotePath=false diff --name-status -M HEAD -- "$bundle" knowledge_bundle 2>/dev/null | grep -E '^R' || true)
  for kind in events notes; do sort -u "$home/was.$kind" -o "$home/was.$kind"; sort -u "$home/now.$kind" -o "$home/now.$kind"; done
  while IFS="$(printf '\t')" read -r id by at _; do
    [ -n "$id" ] || continue
    case "$by" in
      "(unreadable)") say "$id: an unattended change writes frontmatter this gate cannot read - spell it as conventions rule 10 asks" ;;
      *) say "$id: an unattended change adds or changes a confirmation by human:$by ($at)" ;;
    esac
  done < <(comm -13 "$home/was.events" "$home/now.events")
  while IFS="$(printf '\t')" read -r id by at _; do
    [ -n "$id" ] || continue
    case "$by" in
      "(unreadable)") say "$id: an unattended change removes frontmatter this gate could not read, which may have held a person's record" ;;
      *) say "$id: an unattended change removes a confirmation by human:$by ($at)" ;;
    esac
  done < <(comm -23 "$home/was.events" "$home/now.events")
  while IFS="$(printf '\t')" read -r f _; do
    [ -n "$f" ] && say "$f: an unattended change adds a note in a person's name"
  done < <(comm -13 "$home/was.notes" "$home/now.notes")
  while IFS="$(printf '\t')" read -r f _; do
    [ -n "$f" ] && say "$f: an unattended change removes a person's note"
  done < <(comm -23 "$home/was.notes" "$home/now.notes")
  if [ "$fail" -eq 0 ]; then
    echo "OK - the change against HEAD adds, changes and removes no person's event or note, and rewrites no text a person wrote"
  fi
  exit "$fail"
fi

# The range, oldest first, and the ids whose key file it adds, changes or
# removes: a confirmation by one of them in the same range fails before its
# signature is checked.
commits="$(git rev-list --reverse "$base..$head" 2>/dev/null)" || { echo "cannot resolve $base..$head" >&2; exit 2; }
rekeyed=""
for sha in $commits; do
  for f in $(changed_paths "$sha" -- "$curators"); do
    f="${f##*/}"; rekeyed="$rekeyed ${f%.*}"
  done
done
rekeyed_said=""

checked=0
for sha in $commits; do
  short="$(git rev-parse --short "$sha")"
  # The actor of every event new or changed against every parent, in the
  # concepts this commit touches. A path this script cannot read, like an id
  # it cannot check, is a finding, never a skip.
  listed="$(changed_paths "$sha" -- "$bundle" knowledge_bundle)"
  quoted="$(printf '%s\n' "$listed" | grep '^"' || true)"
  if [ -n "$quoted" ]; then
    say "$short touches a bundle path git has to quote, which this script cannot read - rename it: $(printf '%s' "$quoted" | tr '\n' ' ')"
    continue
  fi
  linked="$(printf '%s\n%s\n' "$listed" "${bundle%%/*}" | links_in "$sha")"
  if [ -n "$linked" ]; then
    say "$short leaves a symbolic link under the bundle, which this gate cannot read - a concept is a file of its own: $(printf '%s' "$linked" | tr '\n' ' ')"
    continue
  fi
  files="$(printf '%s\n' "$listed" | grep '\.md$' || true)"
  [ -n "$files" ] || continue
  # every.events: what every parent holds, so a merge that merely lacks what
  # one side never had removes nothing. A root commit has no parent and
  # removes nothing either.
  : > "$home/every.events"; first=1
  for p in $(git rev-parse "$sha^@" 2>/dev/null); do
    printf '%s\n' "$files" | events_in "$p" | sort -u > "$home/one.events"
    if [ "$first" -eq 1 ]; then cp "$home/one.events" "$home/every.events"; first=0
    else comm -12 "$home/every.events" "$home/one.events" > "$home/every.tmp"; mv "$home/every.tmp" "$home/every.events"; fi
    cat "$home/one.events"
  done | sort -u > "$home/parent.events"
  printf '%s\n' "$files" | events_in "$sha" | sort -u > "$home/sha.events"
  added="$(comm -13 "$home/parent.events" "$home/sha.events" | cut -f2 | sort -u)"
  gone="$(removed_from "$home/every.events" "$home/sha.events" | cut -f2 | sort -u)"
  ids="$(printf '%s\n%s\n' "$added" "$gone" | sed '/^$/d' | sort -u)"
  [ -n "$ids" ] || continue
  format="$(sig_format "$sha")"
  status=""; signer=""
  if [ "$format" = pgp ] && [ "$gpg_ok" -eq 1 ]; then
    status="$(GNUPGHOME="$home" git verify-commit --raw "$sha" 2>&1 || true)"
    signer="$(printf '%s\n' "$status" | awk '/^\[GNUPG:\] VALIDSIG/ {print $3; exit}')"
  fi
  for id in $ids; do
    checked=$((checked + 1))
    # What this commit does with that person's record, for the finding's wording.
    does="adds or changes"
    printf '%s\n' "$added" | grep -qxF -- "$id" || does="removes"
    # A forge login is letters, digits, '.', '_' and '-'; anything else names
    # nobody the gate can look up, and could name a path outside $curators.
    case "$id" in
      "(unreadable)")
        say "$short $does frontmatter this gate cannot read, which may hold a person's record - spell it as conventions rule 10 asks"
        continue ;;
      *[!A-Za-z0-9._-]*|[!A-Za-z0-9]*)
        say "$short $does a confirmation by human:$id, which is not a login this gate can check (letters, digits, . _ - only)"
        continue ;;
    esac
    has_asc=0; has_pub=0
    [ -f "$curators/$id.asc" ] && has_asc=1
    [ -f "$curators/$id.pub" ] && has_pub=1
    case " $rekeyed " in
      *" $id "*)
        case " $rekeyed_said " in *" $id "*) ;; *)
          rekeyed_said="$rekeyed_said $id"
          say "$base..$head adds or changes the key on file for human:$id and a confirmation by them in the same range - land the key in its own reviewed change first" ;;
        esac
        continue ;;
    esac
    if [ "$has_asc" -eq 0 ] && [ "$has_pub" -eq 0 ]; then
      say "$short $does a confirmation by human:$id, who has no key on file at $curators/$id.asc or $id.pub"
      continue
    fi
    case "$format" in
      none)
        say "$short $does a confirmation by human:$id but is unsigned" ;;
      pgp)
        if [ "$has_asc" -eq 0 ]; then
          say "$short $does a confirmation by human:$id with a GPG signature, but the key on file for them is an SSH key ($id.pub)"
        elif [ "$gpg_ok" -eq 0 ]; then
          say "$short $does a confirmation by human:$id with a GPG signature, and gpg is not installed here to verify it"
        elif printf '%s\n' "$status" | grep -qE '^\[GNUPG:\] (EXPKEYSIG|REVKEYSIG|EXPSIG)'; then
          say "$short $does a confirmation by human:$id signed by a key that has expired or been revoked"
        elif [ -z "$signer" ]; then
          unknown="$(printf '%s\n' "$status" | awk '/^\[GNUPG:\] NO_PUBKEY/ {print $3; exit}')"
          if [ -n "$unknown" ]; then
            say "$short $does a confirmation by human:$id but is signed by another key ($unknown, on file for nobody)"
          else
            say "$short $does a confirmation by human:$id but its signature does not verify (damaged, or made over different content)"
          fi
        elif ! gpg_fprs "$id" | grep -qx "$signer"; then
          say "$short $does a confirmation by human:$id but is signed by another key (${signer#"${signer%????????????????}"} is not in $id.asc)"
        fi ;;
      ssh)
        if [ "$has_pub" -eq 0 ]; then
          say "$short $does a confirmation by human:$id with an SSH signature, but the key on file for them is a GPG key ($id.asc)"
        elif ! have ssh-keygen; then
          say "$short $does a confirmation by human:$id with an SSH signature, and ssh-keygen is not installed here to verify it"
        else
          signature_of "$sha" > "$home/$sha.sig"
          if ! payload_of "$sha" | ssh-keygen -Y verify -f "$(allowed_of "$id")" -I "$id" -n git -s "$home/$sha.sig" >/dev/null 2>&1; then
            say "$short $does a confirmation by human:$id but its SSH signature is not by a key in $id.pub"
          fi
        fi ;;
    esac
  done
done

if [ "$fail" -eq 0 ]; then
  echo "OK - $checked confirmation(s), new, changed or removed, in $base..$head signed by the key on file for their curator"
fi
exit "$fail"
