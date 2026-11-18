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

## Getting a quick review

Before you start, read [the maintainers' bios](README.md#maintainers) to see whether your topic matches a maintainer's interests. Maintainers review contributions alongside their day jobs, so put the most important thing first:

1. **Start with why it matters, in plain words.** In one or two sentences, say what problem your change addresses and who it affects. Say it once.
2. **Show that the problem is real.** Link to a news story, court ruling or regulator's statement about a case where it happened. A real case with real consequences gets attention faster than a hypothetical one. Choose a reliable source, and describe it accurately, without overstating it. If it hasn't happened yet, say what makes it likely, such as a regulator's warning or published research.
3. **Then give the details:** what you changed, your sources, and any terms that a non-specialist may not know.

This matters most if your topic isn't among the maintainers' interests, because a reviewer will need to learn the area first.

For example, a pull request could start like this:

> **Why it matters:** A firm's chatbot can promise a customer something the firm's own policy doesn't allow, and the firm can be held to that promise.
>
> **It has happened:** In February 2024, a Canadian tribunal ordered Air Canada to pay a passenger, after its chatbot wrongly told him he could claim a bereavement fare after booking ([Daily Hive](https://dailyhive.com/canada/air-canada-chatbot-decision)).
>
> **The change:** Adds the case to ri-4 (Hallucination and Inaccurate Outputs), as evidence that the risk has real costs.

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
