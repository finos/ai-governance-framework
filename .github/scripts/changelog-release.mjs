#!/usr/bin/env node
// Reads and rewrites this repository's own linkml/CHANGELOG.md "## [Unreleased]"
// section for the semantic-release pipeline in
// .github/workflows/semantic-release.yml. Plain Node, no dependencies:
// reviewable in one read, matching this project's preference for a fixed,
// in-repo script over an inline command string (see knowledge-librarian.sh).
//
// Usage:
//   node changelog-release.mjs check
//       Exits 1 if "## [Unreleased]" is empty. Used as semantic-release's
//       verifyReleaseCmd, so a release with nothing written up never ships.
//
//   node changelog-release.mjs notes [version]
//       Prints the Unreleased section's body to stdout; it becomes the
//       release notes when used as generateNotesCmd. With a version arg,
//       also appends `next_version=<version>` to $GITHUB_OUTPUT if that
//       env var is set (a side channel a caller can read even from a
//       --dry-run invocation, where nothing else is written anywhere).
//
//   node changelog-release.mjs promote <version> <date>
//       Retitles "## [Unreleased]" to "## [<version>] - <date>" and
//       inserts a fresh, empty "## [Unreleased]" above it. Used as
//       semantic-release's prepareCmd (never called in --dry-run). Also
//       appends `released=true` and `version=<version>` to $GITHUB_OUTPUT
//       if set.

import { readFileSync, writeFileSync, appendFileSync } from "node:fs";

const FILE = "linkml/CHANGELOG.md";
const HEADING = "## [Unreleased]";

function readUnreleased() {
  const text = readFileSync(FILE, "utf8");
  const start = text.indexOf(HEADING);
  if (start === -1) {
    throw new Error(`${FILE} has no "${HEADING}" heading - this pipeline expects one.`);
  }
  const bodyStart = start + HEADING.length;
  const next = text.indexOf("\n## [", bodyStart);
  const bodyEnd = next === -1 ? text.length : next;
  return { text, body: text.slice(bodyStart, bodyEnd).trim() };
}

function writeOutput(line) {
  if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, line);
}

const [, , cmd, ...args] = process.argv;

switch (cmd) {
  case "check": {
    const { body } = readUnreleased();
    if (!body) {
      console.error(
        `${FILE}'s "${HEADING}" section is empty. This pipeline only releases what a ` +
          "person or agent has already described there - write it before merging to main."
      );
      process.exit(1);
    }
    console.error(`ok - "${HEADING}" has ${body.length} characters to release.`);
    break;
  }

  case "notes": {
    const [version] = args;
    const { body } = readUnreleased();
    if (version) writeOutput(`next_version=${version}\n`);
    process.stdout.write(body + "\n");
    break;
  }

  case "promote": {
    const [version, date] = args;
    if (!version || !date) {
      console.error("usage: changelog-release.mjs promote <version> <date>");
      process.exit(1);
    }
    const { text, body } = readUnreleased();
    if (!body) {
      console.error(`${FILE}'s "${HEADING}" section is empty; refusing to promote nothing.`);
      process.exit(1);
    }
    const promoted = text.replace(HEADING, `${HEADING}\n\n## [${version}] - ${date}`);
    if (promoted === text) {
      throw new Error(`Replacement had no effect - is "${HEADING}" definitely in ${FILE}?`);
    }
    writeFileSync(FILE, promoted);
    console.error(`promoted "${HEADING}" to "## [${version}] - ${date}" in ${FILE}`);
    writeOutput(`released=true\nversion=${version}\n`);
    break;
  }

  default:
    console.error("usage: changelog-release.mjs <check|notes|promote> ...");
    process.exit(1);
}
