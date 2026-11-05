// The site's values and options, in one place. scripts/config.mjs reads this
// file, fills in every option left out, settles each "auto" against the
// repository and checks the required values. `node scripts/config.mjs`
// prints the result. Nothing here runs code, so the pages that show the
// title import it too.
//
// The first five values are required. The rest are optional: leave one out,
// or set it to "auto", and the site shows that part of the repository when
// the repository has it. Set it to null to leave that part out.

// The repository, as owner/name, and the site's address: the owner's GitHub
// Pages domain and the path under it. A user site (the <owner>.github.io
// repository) or a custom domain sets BASE to "".
export const REPO = "lmodel/ai-governance-framework";
export const SITE = "https://lmodel.github.io";
export const BASE = "/ai-governance-framework";

// The site's title, in the header and on every social card, and its
// description, for search engines and as the home page's tagline when
// HOME.tagline is not set.
export const TITLE = "ai-governance-framework";
export const DESCRIPTION = "FINOS AI Governance Framework v3 (LinkML)";

// The branch an "Edit page" link opens.
export const BRANCH = "main";

// A custom domain, which the sync writes to public/CNAME, or null for a
// Pages address. The site leaves the domain's DNS to the repository.
export const CUSTOM_DOMAIN = null;

// The logo, as paths from the repository root: a light version, a dark one
// (the light one again when left out) and a favicon (the light logo when it
// is an SVG, else the site's own ladder mark). "auto" takes the Knowledge
// Trust Ladder logo: a knowledge-trust-ladder-logo.svg the repository
// already has, or else the copy in src/assets/. A single path is the light
// version alone. null shows the title as text.
//   export const LOGO = { light: ".assets/logo.svg", dark: ".assets/logo-dark.svg" };
export const LOGO = "auto";

// The folder of figures the README and the docs pages show, served under
// /assets/. "auto" takes .assets/ when there is one.
export const ASSETS = null;

// The docs pages: a folder, the sidebar groups its pages sit in (each page
// named by its path under the folder, without .md), and the paths under the
// folder that are not pages of the site, each a file or a folder. With no
// groups, every page sits in one Guides group, by title, with the folder's
// index.md first as its Overview. With groups, the sync stops with an error
// when a group names a missing page or a page has no group, so a new page
// cannot go missing from the sidebar. "auto" takes docs/ when there is one.
// null shows no docs pages.
//   export const DOCS = { dir: "docs", groups: [{ label: "Guides", pages: ["install", "usage"] }], exclude: ["templates-linkml"] };
// FINOS's Jekyll docs/ stays out: the site shows this project's own pages.
export const DOCS = { dir: "linkml/docs", exclude: ["templates-linkml", "schema", "elements"] };

// Old addresses under BASE, each redirected to a page of the site, such as
// the addresses a retired mkdocs site gave its pages and a w3id rule still
// names. An entry whose key and value both end in /[...slug] stands for one
// redirect per schema page.
//   export const REDIRECTS = { "/elements": "/schema/", "/elements/[...slug]": "/schema/[...slug]", "/about": "/docs/about/" };
export const REDIRECTS = {
  "/about": "/docs/about/",
  "/elements": "/schema/",
  "/elements/[...slug]": "/schema/[...slug]",
};

// A Keep a Changelog file, read as a page per release. "auto" takes
// CHANGELOG.md when it holds a released version.
export const CHANGELOG = "linkml/CHANGELOG.md";

// The tag a release carries, with {version} for its number. A release page
// links the repository, the docs and the bundle at that tag, and the release
// itself, when git has the tag. A repository whose tags carry no "v" sets
// "{version}". null links nothing.
export const RELEASE_TAG = "v{version}";

// Pages from files outside the docs folder, each at /<slug>/, listed in the
// Guide sidebar after Home under its label. An entry's `retells` names the
// file whose page it retells, and `level` the words for its reading level
// (the label when left out): both pages then offer each other under their
// titles.
//   export const PAGES = [{ slug: "simple", source: "docs/overview.en-simple.md", label: "In short", retells: "docs/overview.md" }];
export const PAGES = [];

// The LinkML schema's pages, which gen-doc writes, under a Schema topic: a
// folder, and the command that writes it, which the sync runs when the
// folder is missing. "auto" takes the first of the root, a linkmo project
// and .linkml/ whose justfile has a gen-doc recipe, else the sidecar's
// domain schema. null shows no schema.
//   export const SCHEMA = { dir: "docs/elements", build: "just gen-doc" };
export const SCHEMA = { dir: "linkml/docs/elements", build: "just --justfile linkml/justfile gen-doc" };

// The data: a folder of SQLite databases and their Datasette metadata, served
// under /browse/ with a page that opens each in Datasette Lite, and the
// command that writes it. The databases go on the public site, so it is null
// until set. "auto" takes a linkmo project's browse/ folder.
//   export const BROWSE = { dir: "browse", build: "just build-browse" };
export const BROWSE = null;

// The workspace of a domain host, which the knowledge-federation workflow
// serves at workspace/ under the site, and which the graph page offers to
// draw beside the bundle's own graph. "auto" offers it when the repository
// has that workflow; true offers it always, and null never.
export const WORKSPACE = "auto";

// The home page: its source, from the file's `# ` title down ("auto" takes
// the README when it has one, else the bundle's own introduction); the
// tagline under the title (a string, { boldLineOf: <file> } for the first
// line of that file that is bold throughout, or DESCRIPTION when null); and
// the buttons, with site-relative links (Browse the bundle, Architecture when
// the docs have an architecture page, Schema when the site shows the schema,
// Bundle health and Knowledge graph when null).
// FINOS's README stays FINOS's home page: this site's is this project's.
export const HOME = { source: "linkml/README.md", tagline: null, actions: null };
