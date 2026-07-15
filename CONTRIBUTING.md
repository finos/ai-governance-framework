# Contributing to AI Governance Framework

AI Readiness is [CC-BY-4.0 licensed](LICENSE) and accepts contributions via git pull requests.

## DCO (required before your PR can merge)

Every commit on the PR must include a **Developer Certificate of Origin** sign-off line.  
The DCO bot will **fail** the PR until this is present on **all** commits.

### Before you open a PR

1. Configure git with your real name and the email on your GitHub account:
   ```bash
   git config user.name "Your Name"
   git config user.email "you@example.com"
   ```
2. Create each commit with the **`-s`** flag (adds `Signed-off-by` for you):
   ```bash
   git commit -s -m "Your change description"
   ```
3. Or add the line yourself as the last line of the commit message:
   ```
   Signed-off-by: Your Name <you@example.com>
   ```
4. Full legal text: [Developer Certificate of Origin](https://developercertificate.org/).

### After the PR is open (if DCO fails)

1. On GitHub, open the failed **DCO** check for the exact missing commits.
2. Fix locally, then force-push the branch (history rewrite is normal for DCO repair):
   ```bash
   # single bad commit on tip
   git commit --amend -s --no-edit
   git push --force-with-lease

   # several commits
   git rebase HEAD~N -x "git commit --amend -s --no-edit"
   # or interactive rebase and re-commit each with -s
   git push --force-with-lease
   ```
3. Do **not** open a second PR to “add DCO later” — amend/rebase the same branch.

### Quick check

```bash
git log -1 --format=%B   # last lines should include Signed-off-by:
```

## Contributing Issues

### Prerequisites

* [ ] Have you [searched for duplicates](https://github.com/finos/ai-governance-framework/issues?utf8=%E2%9C%93&q=)?  A simple search for exception error messages or a summary of the unexpected behaviour should suffice.
* [ ] Are you running the latest version?
* [ ] Are you sure this is a bug or missing capability?

### Raising an Issue
* Create your issue [here](https://github.com/finos/ai-governance-framework/issues/new).
* New issues contain two templates in the description: bug report and enhancement request. Please pick the most appropriate for your issue, **then delete the other**.
  * Please also tag the new issue with either "Bug" or "Enhancement".
* Please use [Markdown formatting](https://help.github.com/categories/writing-on-github/)
liberally to assist in readability.
  * [Code fences](https://help.github.com/articles/creating-and-highlighting-code-blocks/) for exception stack traces and log entries, for example, massively improve readability.

## Contributing Pull Requests (Code & Docs)
To make review of PRs easier, please:

 * Please make sure your PRs will merge cleanly - PRs that don't are unlikely to be accepted.
 * For code contributions, follow the existing code layout.
 * For documentation contributions, follow the general structure, language, and tone of the [existing docs](https://github.com/finos/ai-governance-framework/wiki).
 * Keep commits small and cohesive - if you have multiple contributions, please submit them as independent commits (and ideally as independent PRs too).
 * Reference issues if your PR has anything to do with an issue (even if it doesn't address it).
 * Minimise non-functional changes (e.g. whitespace).
 * If necessary (e.g. due to 3rd party dependency licensing requirements), update the [NOTICE file](https://github.com/finos/ai-governance-framework/blob/master/NOTICE) with any new attribution or other notices


### Commit and PR Messages

* **Reference issues, wiki pages, and pull requests liberally!**
* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move button left..." not "Moves button left...")
* Limit the first line to 72 characters or less
