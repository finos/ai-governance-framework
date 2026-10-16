# Contributing to AI Governance Framework

AI Readiness is [CC-BY-4.0 licensed](LICENSE) and accepts contributions via git pull requests. Each commit must include a DCO line in the git commit message:

`Signed-off-by: GitHub User Name <your.email@example.com>`

This sign-off means you agree the commit satisfies the
[Developer Certificate of Origin (DCO).](https://developercertificate.org/)

### Signing your commits

Use the `-s` option when creating each commit. Git will add the required
`Signed-off-by` line using your configured name and email address:

```bash
git commit -s -m "Add a concise commit message"
```

If you have already created an unsigned commit, add the sign-off before
pushing it:

```bash
git commit --amend --signoff
```

Every commit included in a pull request must have a DCO sign-off.

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

## AI-Assisted Contributions

This project accepts contributions written with the help of AI tools. Much of
the catalogue's value comes from people who understand a control and can
explain it, and a tool that helps them write it down faster is welcome. What
is not welcome is output nobody has checked.

### Disclose the assistance

In a commit, use a trailer alongside your DCO sign-off. This is the same
convention used by the Linux kernel, Kubernetes and Apache projects:

```
Assisted-by: Claude Opus 5 (Claude Code)
Signed-off-by: Your Name <your.email@example.com>
```

In an issue, a pull request description, or a comment, close with a single
line naming the tool, the model, and what you checked:

```markdown
---
*Drafted with Claude Code (Claude Opus 5). Claims verified against the
repository; posted and owned by @your-handle.*
```

Name the model, not just the vendor. "Written with AI" tells a reviewer
nothing they can act on.

### You remain accountable

Disclosure records how a contribution was produced. It does not transfer
responsibility for it. Your DCO sign-off certifies the contribution as your
own to submit, exactly as it does for anything you typed yourself, and you
are expected to be able to explain and defend any part of it in review.

A contribution its author cannot explain will be closed, however well written
it is. Reviewer attention is the scarcest resource this project has.

### Verify before you submit

Anything checkable must be checked. This is where AI-assisted contributions
actually fail, and the failure is quiet:

* Run the deterministic checks — `python scripts/review-pr.py <pr>` for a
  contribution, `--tree origin/main` for the catalogue itself.
* Confirm that every risk, mitigation and reference id you cite exists, and
  that cross-links follow [CONVENTIONS.md](CONVENTIONS.md).
* Confirm that any regulation, standard or paper you cite says what you say it
  says.

Plausible and wrong is the characteristic failure mode of generated text, and
this is a governance framework: a control that cites a withdrawn standard, or
a mapping to a clause that does not exist, is worse than no control at all,
because someone will rely on it.

### Licensing

You must also satisfy the Linux Foundation's
[Guidance Regarding Use of Generative AI Tools for Open Source Software
Development](https://www.linuxfoundation.org/legal/generative-ai). In short:
the tool's terms must not restrict the output in ways incompatible with this
project's CC-BY-4.0 licence, and where the output includes pre-existing
third-party material you must have permission to use it and must attribute it.
