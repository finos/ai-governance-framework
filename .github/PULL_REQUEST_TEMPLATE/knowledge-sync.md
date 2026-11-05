<!-- A sidecar sync. The lines above this template are the sync's: the release, the files it changed and the pin. The workflow leaves the sidecar's checks to this pull request's own checks; a sync opened by hand with .lokf/scripts/knowledge-sync.sh --pr <tag> writes its check lines above too. -->

## Reviewer checklist

- [ ] The diff touches only the sidecar's copies, the site's copies, the skills pin and `CHANGELOG.md`.
- [ ] `TRUST_LADDER_SKILLS_REF` names the release, and `TRUST_LADDER_SKILLS_SHA` the commit that tag names.
- [ ] Any workflow changes held above are read and applied on this branch, or left for the next sync on purpose.
- [ ] You read the [release notes of Knowledge Trust Ladder](https://w3id.org/ktl/changelog/) for a step the sync cannot do, such as setting a new variable or secret, or running `uv lock`. If there is one, you do it in this pull request or straight after the merge.
- [ ] `CHANGELOG.md` has the entry under `## [Unreleased]` and `### Security`, and the title carries `security(sidecar):`, so the merge releases.
