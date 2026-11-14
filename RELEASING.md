# Releasing

How to publish a release of the framework and its DOI. Each release is a new version of one [Zenodo](https://zenodo.org/) record, which a maintainer uploads by hand.

The examples use `v3`. Replace it with the version you release.

## 1. Version and tag

1. Set `version` and `release-date` in [`docs/_config.yml`](./docs/_config.yml).
2. In [`CITATION.cff`](./CITATION.cff), set `version`, `date-released`, and the `year` and `month` of `preferred-citation`. Update both author lists: the maintainers in the order of the [README](./README.md), then the working group.
3. Check the file with `cffconvert --validate`.
4. Merge, then tag the merge commit and push the tag.

```sh
git tag v3 <merge commit>
git push origin v3
```

## 2. Files

The Zenodo record gets two files for each version.

The source, as a zip of the repository at the tag:

```sh
git archive --format=zip --prefix=ai-governance-framework-v3/ \
  -o ai-governance-framework-v3.zip v3
```

The document, as a PDF of the [single-page view](https://air-governance-framework.finos.org/single-page.html):

```sh
chromium --headless=new --user-data-dir="$(mktemp -d)" \
  --no-pdf-header-footer --virtual-time-budget=20000 \
  --print-to-pdf=finos-ai-governance-framework-v3.pdf \
  https://air-governance-framework.finos.org/single-page.html
```

The binary is `google-chrome` on most Linux systems, and `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` on macOS. The "Print / Save as PDF" button on the page is the manual way.

NB: the site shows `main`, not the tag. Print the PDF after the site has deployed the release, and before the next change to the content is merged.

## 3. Zenodo

Rehearse on [sandbox.zenodo.org](https://sandbox.zenodo.org/) first. It has its own accounts, and its records are not real. On zenodo.org a published record cannot be deleted.

For the first release, create a new upload. For a later release, open the record and choose "New version".

Fill in the form from `CITATION.cff`:

| Zenodo field | Value |
| --- | --- |
| Resource type | Publication / Report |
| Title | `title` |
| Publication date | `date-released` |
| Creators | `authors`, in the same order. The working group is an organisation. |
| Description | `abstract` |
| Licence | Creative Commons Attribution 4.0 International |
| Keywords | `keywords` |
| Version | `version` |
| Publisher | Fintech Open Source Foundation (FINOS) |
| Related works | "Is variant form of" the site URL, "Is derived from" the URL of the tag on GitHub |

Then:

1. Upload the two files and save the draft.
2. First release only: use "Share" to give ["Can manage" permission](https://help.zenodo.org/docs/share/user-sharing/) to the lead maintainer and to one account of the FINOS staff. The permission covers all later versions, therefore the record does not depend on one person.
3. Publish. After that, a change to the files needs a new version.
4. First release only: add the concept DOI to `CITATION.cff` (`doi:`, at the top level and in `preferred-citation`), to the README and to the site. The concept DOI always resolves to the newest version, and it is the one we cite.

## Why by hand

Zenodo can also archive each GitHub Release [by itself](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content). We upload by hand for two reasons:

- Zenodo [asks for Admin permission](https://support.zenodo.org/help/en-gb/24-github-integration/51-why-does-my-github-organisations-repositories-not-show-up) on the repository to enable that, and maintainers have the Maintain role.
- It archives the source of the site. With an upload by hand, the record also has a PDF that a reader can open.

The framework had three releases since June 2025, therefore the manual step costs little. If it becomes a burden, a script can add versions to the same record through the Zenodo API.
