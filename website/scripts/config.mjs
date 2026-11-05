// The site's configuration as astro.config.mjs and the scripts read it:
// site.config.mjs's values with every option it leaves out filled in, each
// "auto" settled against the repository, and the required values checked.
// `node scripts/config.mjs` prints the result, so a person can see what the
// sync will read before it runs. site.config.mjs itself runs no code, so the
// pages that show the title import it directly.
import { execFileSync, spawnSync } from "node:child_process";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, extname, posix, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as given from "../site.config.mjs";

export const SITE_DIR = resolve(dirname(fileURLToPath(import.meta.url)), "..");
export const REPO_ROOT = resolve(SITE_DIR, "..");
export const BUNDLE_DIR = resolve(REPO_ROOT, ".lokf", "knowledge");

const fail = (what) => {
  throw new Error(`site.config.mjs: ${what}`);
};
const has = (rel) => existsSync(resolve(REPO_ROOT, rel));
const isDir = (rel) => has(rel) && statSync(resolve(REPO_ROOT, rel)).isDirectory();
const isFile = (rel) => has(rel) && statSync(resolve(REPO_ROOT, rel)).isFile();

/** A required value: a string with no placeholder left in it. */
function required(name) {
  const value = given[name];
  if (typeof value !== "string" || value === "") fail(`${name} must be a string`);
  if (/<[A-Z_]+>/.test(value)) fail(`${name} still holds a placeholder (${value}); ktl-website's Step 1 fills it`);
  return value;
}

// ---- the addresses ---------------------------------------------------------

export const REPO = required("REPO");
export const REPO_URL = `https://github.com/${REPO}`;
export const CUSTOM_DOMAIN = given.CUSTOM_DOMAIN ?? null;
// A custom domain serves the site at its root. A project site is served
// under the owner's Pages domain at /<repository>/. The host is lowercased,
// as Astro writes it in every canonical and social card address, so an owner
// spelt with capitals (BretFisher) still matches the links the build checks.
const lowerHost = (url) => url.replace(/^(https?:\/\/)([^/]+)/i, (_, scheme, host) => scheme + host.toLowerCase());
export const SITE = lowerHost(CUSTOM_DOMAIN ? `https://${CUSTOM_DOMAIN}` : required("SITE").replace(/\/$/, ""));
export const BASE = CUSTOM_DOMAIN ? "" : required("BASE").replace(/\/$/, "");
export const SITE_URL = SITE + BASE;
export const TITLE = required("TITLE");
export const DESCRIPTION = required("DESCRIPTION");
export const BRANCH = given.BRANCH ?? "main";

// Links to repository files name the commit the site was built from, so a
// reader opens the text the page was rendered from.
export const REF = (() => {
  if (process.env.GITHUB_SHA) return process.env.GITHUB_SHA;
  try {
    return execFileSync("git", ["-C", REPO_ROOT, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();
  } catch {
    return BRANCH;
  }
})();

// ---- what the site shows beside the bundle ---------------------------------

/** An option left out or set to "auto" takes `fallback` when the repository has it, and null otherwise. */
function settle(name, fallback, present) {
  const value = given[name] === undefined ? "auto" : given[name];
  if (value === "auto") return present(fallback) ? fallback : null;
  if (value !== null && !present(value)) fail(`${name} names ${value}, which is not in the repository`);
  return value;
}

export const ASSETS = settle("ASSETS", ".assets", isDir);

// The Knowledge Trust Ladder logo, which "auto" takes: a copy the repository
// already holds, outside this site and outside a skill's templates, the one
// nearest the root first, or else the copy this site carries in src/assets/.
// The -dark.svg file beside it is the dark version when there is one.
const KTL_LOGO = "knowledge-trust-ladder-logo.svg";
function ktlLogo() {
  const site = relative(REPO_ROOT, SITE_DIR).replaceAll("\\", "/");
  const ls = spawnSync("git", ["-C", REPO_ROOT, "ls-files", "--cached", "--others", "--exclude-standard", "--", `*${KTL_LOGO}`], {
    encoding: "utf8",
  });
  const own = (ls.status === 0 ? ls.stdout.split("\n") : [KTL_LOGO, `.assets/${KTL_LOGO}`])
    .filter((f) => (f === KTL_LOGO || f.endsWith(`/${KTL_LOGO}`)) && !f.startsWith(`${site}/`) && !f.includes("templates/website/"))
    .filter(isFile)
    .sort((a, b) => a.split("/").length - b.split("/").length || (a < b ? -1 : a > b ? 1 : 0));
  const light = own[0] ?? `${site}/src/assets/${KTL_LOGO}`;
  const dark = light.replace(/\.svg$/, "-dark.svg");
  return { light, dark: isFile(dark) ? dark : light };
}

export const LOGO = (() => {
  const value = given.LOGO === undefined ? "auto" : given.LOGO;
  if (value === null) return null;
  const logo = value === "auto" ? ktlLogo() : typeof value === "string" ? { light: value } : value;
  const light = logo.light ?? fail("LOGO needs at least a light file");
  const dark = logo.dark ?? light;
  const favicon = logo.favicon ?? (extname(light) === ".svg" ? light : null);
  for (const file of [light, dark, favicon]) {
    if (file && !isFile(file)) fail(`LOGO names ${file}, which is not in the repository`);
  }
  return { light, dark, favicon };
})();
/** The generated logo files, named by their source's type, and the favicon the site serves. */
export const LOGO_FILES = LOGO ? { light: `logo-light${extname(LOGO.light)}`, dark: `logo-dark${extname(LOGO.dark)}` } : null;
export const FAVICON = LOGO?.favicon ? `/favicon${extname(LOGO.favicon)}` : "/favicon.svg";

// docsPages() keeps its list here once read. It is declared before HOME,
// which asks for the list while this module is still loading.
let docsPagesRead = null;

export const DOCS = (() => {
  const value = given.DOCS === undefined ? "auto" : given.DOCS;
  if (value === null) return null;
  const docs =
    value === "auto"
      ? { dir: "docs" }
      : typeof value === "string"
        ? { dir: value }
        : { dir: value.dir ?? "docs", groups: value.groups, exclude: value.exclude };
  if (!isDir(docs.dir)) {
    if (value === "auto") return null;
    fail(`DOCS names ${docs.dir}, which is not a folder in the repository`);
  }
  // The paths under the folder that are not pages of the site, each a file
  // or a folder. A path that names no file or folder is a typo, and stops
  // the build here.
  const exclude = (docs.exclude ?? []).map((path) => (typeof path === "string" ? path.replace(/^\/+|\/+$/g, "") : path));
  for (const path of exclude) {
    if (typeof path !== "string" || !has(`${docs.dir}/${path}`)) fail(`DOCS.exclude names ${path}, which is not in ${docs.dir}/`);
  }
  return { dir: docs.dir, groups: docs.groups ?? null, exclude };
})();

/**
 * A docs page's address under the site's base, as Starlight gives it: each
 * folder and the file name in lower case, with the characters
 * github-slugger drops left out, and an index page at its folder's address.
 */
export function docsRoute(name) {
  const slug = name
    .split("/")
    .map((part) => part.toLowerCase().replace(/[^\p{L}\p{M}\p{N}\p{Pc}\- ]/gu, "").replace(/ /g, "-"))
    .join("/");
  const folder = slug === "index" ? "" : slug.replace(/\/index$/, "");
  return folder ? `/docs/${folder}/` : "/docs/";
}

export const CHANGELOG = (() => {
  const value = given.CHANGELOG === undefined ? "auto" : given.CHANGELOG;
  if (value === null) return null;
  const file = value === "auto" ? "CHANGELOG.md" : value;
  if (!isFile(file)) {
    if (value === "auto") return null;
    fail(`CHANGELOG names ${file}, which is not in the repository`);
  }
  // A release page needs one released version in Keep a Changelog form.
  if (/^## \[[^\]]+\] - \d{4}-\d{2}-\d{2}/m.test(readFileSync(resolve(REPO_ROOT, file), "utf8"))) return file;
  if (value === "auto") return null;
  return fail(`${file} has no "## [version] - YYYY-MM-DD" heading, which a release page needs`);
})();

// The tag a release carries, with {version} for its number, so that a
// release page can link the repository and the bundle as they stood at the
// release. null links nothing.
export const RELEASE_TAG = (() => {
  const value = given.RELEASE_TAG === undefined ? "v{version}" : given.RELEASE_TAG;
  if (value === null) return null;
  if (typeof value !== "string" || !value.includes("{version}")) fail("RELEASE_TAG must hold {version}, such as \"v{version}\", or be null");
  return value;
})();

export const PAGES = (given.PAGES ?? []).map((p) => {
  if (!p.slug || !p.source) fail("each PAGES entry needs a slug and a source");
  if (!isFile(p.source)) fail(`PAGES names ${p.source}, which is not in the repository`);
  if (p.retells && !isFile(p.retells)) fail(`PAGES names ${p.retells}, which ${p.source} retells, and it is not in the repository`);
  // A retelling's level is the words a reader chooses it by, its label unless given.
  const label = p.label ?? p.slug;
  return { slug: p.slug, source: p.source, label, retells: p.retells ?? null, level: p.level ?? label };
});

// ---- the schema's pages and the data, which the repository's commands build --

/** A folder's justfile, by any name just reads (justfile in any case, or .justfile), or null. */
function justfileIn(dir) {
  if (!isDir(dir)) return null;
  const name = readdirSync(resolve(REPO_ROOT, dir))
    .filter((n) => /^\.?justfile$/i.test(n) && isFile(posix.join(dir, n)))
    .sort()[0];
  return name ? posix.join(dir, name) : null;
}

/**
 * Whether a justfile has a recipe of this name: a line that opens it, with or
 * without parameters and their defaults, and not an assignment such as
 * `name := value`. website-preflight.sh's has_recipe uses the same pattern.
 */
function hasRecipe(justfile, recipe) {
  const opens = new RegExp(`^@?${recipe}(?:[ \\t]+[^:=\\s][^:]*)?:(?!=)`);
  return readFileSync(resolve(REPO_ROOT, justfile), "utf8")
    .split("\n")
    .some((line) => opens.test(line));
}

/**
 * The first of these folders whose justfile has the recipe, as { dir, build }.
 * dir is the folder the recipe writes, `out` under that folder. build is the
 * command that runs the recipe from the repository's root. just runs a recipe
 * in its justfile's own folder.
 */
function recipeIn(dirs, recipe, out) {
  for (const dir of dirs) {
    const justfile = dir ? justfileIn(dir) : null;
    if (justfile && hasRecipe(justfile, recipe)) {
      return { dir: posix.join(dir, out), build: dir === "." ? `just ${recipe}` : `just --justfile ${justfile} ${recipe}` };
    }
  }
  return null;
}

/** A linkmo project's folder, as its answers file at the root names it, or null. */
function linkmoDir() {
  if (!isFile(".copier-answers.linkmo.yml")) return null;
  const m = readFileSync(resolve(REPO_ROOT, ".copier-answers.linkmo.yml"), "utf8").match(/^linkmo_dir:\s*["']?([^"'\s#]+)["']?\s*$/m);
  // The folder goes into a shell command, so only a name linkmo's own question accepts is used.
  return m && /^[A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?$/.test(m[1]) && isDir(m[1]) ? m[1] : null;
}

/**
 * The domain schema on the sidecar's `schema :=` line, which the release and
 * the librarian read, as { dir, build }, or null. gen-doc runs in the
 * sidecar's own environment, which the lokf toolkit's LinkML gives it, and
 * renders the imports, since a host's composite declares nothing of its own.
 * The pages go to .lokf/docs/elements/, which the sidecar's .gitignore keeps
 * out of git. The name goes into a shell command, so only a plain YAML path
 * inside .lokf/ is used.
 */
function sidecarSchema() {
  if (!isFile(".lokf/justfile")) return null;
  const m = readFileSync(resolve(REPO_ROOT, ".lokf/justfile"), "utf8").match(/^schema := "([^"]*)"\r?$/m);
  const name = m ? m[1].replace(/^\.\//, "") : "";
  if (!/^[A-Za-z0-9_][A-Za-z0-9._/-]*\.ya?ml$/.test(name) || name.includes("..") || !isFile(posix.join(".lokf", name))) return null;
  return { dir: ".lokf/docs/elements", build: `cd .lokf && uv run --frozen gen-doc ${name} --directory docs/elements --render-imports` };
}

/** A { dir, build } option given in full or as a folder alone; build is the command that writes the folder, or null. */
function folderOption(name, value) {
  const option = typeof value === "string" ? { dir: value } : value;
  if (typeof option?.dir !== "string" || option.dir === "") fail(`${name} needs a dir, the folder from the repository root`);
  const dir = posix.normalize(option.dir.replaceAll("\\", "/")).replace(/\/$/, "");
  if (dir.startsWith("..") || dir.startsWith("/")) fail(`${name}.dir must be a folder inside the repository`);
  const build = option.build ?? null;
  if (build !== null && typeof build !== "string") fail(`${name}.build must be a command, or null`);
  if (build === null && !isDir(dir)) fail(`${name} names ${dir}, which is not in the repository, and no build command to write it`);
  return { dir, build };
}

// The schema's pages: LinkML's gen-doc writes one per class, slot,
// enumeration and type, which the site renders under a Schema topic. "auto"
// takes the first of the repository's root, a linkmo project's folder and
// the linkml-sidecar's .linkml/ whose justfile has a gen-doc recipe, which
// writes the pages to docs/elements there. Failing those, it takes the KTL
// sidecar's domain schema.
export const SCHEMA = (() => {
  const value = given.SCHEMA === undefined ? "auto" : given.SCHEMA;
  if (value === null) return null;
  if (value !== "auto") return folderOption("SCHEMA", value);
  return recipeIn([".", linkmoDir(), ".linkml"], "gen-doc", "docs/elements") ?? sidecarSchema();
})();

// The data: a folder of SQLite databases, which the site serves under
// /browse/ beside their Datasette metadata, and a page that opens each one in
// Datasette Lite. Left out, it is null: the databases go on a public site,
// so a person turns this on. "auto" takes the browse/ folder a linkmo
// project's build-browse recipe writes.
export const BROWSE = (() => {
  const value = given.BROWSE ?? null;
  if (value === null) return null;
  if (value !== "auto") return folderOption("BROWSE", value);
  return recipeIn([linkmoDir()], "build-browse", "browse");
})();

// The workspace of a domain host, whose graph.json the graph page draws
// beside the bundle's own: the folder under the site where the
// knowledge-federation workflow serves it, or null. The workflow always
// serves it at workspace/, so the setting says only whether the page offers
// it. The workflow adds the folder after the site is built, so the page
// reads it when a reader opens the view.
export const WORKSPACE = (() => {
  const value = given.WORKSPACE === undefined ? "auto" : given.WORKSPACE;
  if (value === null || value === false) return null;
  if (value === true) return "workspace";
  if (value === "auto") return isFile(".github/workflows/knowledge-federation.yaml") ? "workspace" : null;
  fail(`WORKSPACE must be "auto", true or null, since the federation workflow serves the workspace at workspace/ under the site, not ${JSON.stringify(value)}`);
})();

/** Where the graph page finds the workspace: its folder, its graph.json under the site's base, and its index as a full address; null with no workspace. */
export function workspaceLinks() {
  return WORKSPACE ? { folder: WORKSPACE, graph: `${BASE}/${WORKSPACE}/graph.json`, index: `${SITE_URL}/${WORKSPACE}/index.md` } : null;
}

/** The first `# ` line of a file outside fenced code, or null. */
function firstTitle(rel) {
  let fence = null;
  for (const line of readFileSync(resolve(REPO_ROOT, rel), "utf8").split("\n")) {
    const m = line.match(/^\s*(`{3,}|~{3,})/);
    if (fence) {
      if (m && m[1][0] === fence[0] && m[1].length >= fence.length) fence = null;
    } else if (m) fence = m[1];
    else if (/^# /.test(line)) return line.slice(2).trim();
  }
  return null;
}

// The buttons under the home page's title when HOME.actions is not set: the
// bundle, the docs' architecture page when the site has one, the schema's
// pages when the site shows them, the health page and the graph.
function defaultActions() {
  return [
    { text: "Browse the bundle", link: "/knowledge/", icon: "right-arrow" },
    ...(docsPages().includes("architecture") ? [{ text: "Architecture", link: "/docs/architecture/", variant: "secondary" }] : []),
    ...(SCHEMA ? [{ text: "Schema", link: "/schema/", variant: "secondary" }] : []),
    { text: "Bundle health", link: "/health/", variant: "secondary" },
    { text: "Knowledge graph", link: "/graph/", variant: "secondary" },
  ];
}

export const HOME = (() => {
  const home = { source: "auto", tagline: null, actions: null, ...(given.HOME ?? {}) };
  let source = home.source ?? null;
  if (source === "auto") source = isFile("README.md") && firstTitle("README.md") ? "README.md" : null;
  else if (source !== null && !isFile(source)) fail(`HOME.source names ${source}, which is not in the repository`);
  const tagline = home.tagline ?? null;
  if (tagline && typeof tagline === "object" && !isFile(tagline.boldLineOf ?? "")) {
    fail("HOME.tagline.boldLineOf names a file that is not in the repository");
  }
  return { source, tagline, actions: home.actions ?? defaultActions() };
})();

// ---- the bundle and the docs, as folders and files -------------------------

/** The bundle's concept groups: its top-level folders, in name order. */
export function bundleGroups() {
  return readdirSync(BUNDLE_DIR)
    .filter((name) => !name.startsWith(".") && statSync(resolve(BUNDLE_DIR, name)).isDirectory())
    .sort();
}

/** A group's folder name as words, so young-readers reads "Young readers". */
export function groupLabel(group) {
  const words = group.replace(/[-_]+/g, " ");
  return words.charAt(0).toUpperCase() + words.slice(1);
}

/** Every concept's ID: its path in the bundle without `.md`, index and log files left out. */
export function conceptIds() {
  const ids = [];
  const walk = (dir, prefix) => {
    for (const name of readdirSync(dir).sort()) {
      if (name.startsWith(".")) continue;
      const full = resolve(dir, name);
      if (statSync(full).isDirectory()) walk(full, prefix + name + "/");
      else if (name.endsWith(".md") && name !== "index.md" && !(prefix === "" && name === "log.md"))
        ids.push(prefix + name.slice(0, -3));
    }
  };
  if (existsSync(BUNDLE_DIR)) walk(BUNDLE_DIR, "");
  return ids;
}

/**
 * Every docs page, as its path under the docs folder without `.md`. The
 * pages are the files git sees there, tracked or untracked but never
 * ignored, so a folder a generator writes stays out. Where there is no git,
 * they are the files a walk of the folder finds.
 * A file PAGES names has a page of its own and is left out here, and so are
 * the schema's folder, which has a topic of its own, and each path
 * DOCS.exclude names. The list is read once per process, since the home
 * page's buttons, the links and the sync all ask for it.
 */
export function docsPages() {
  if (docsPagesRead) return docsPagesRead;
  if (!DOCS) return (docsPagesRead = Object.freeze([]));
  const dir = DOCS.dir;
  const extra = new Set(PAGES.map((p) => p.source));
  const schema = SCHEMA ? `${SCHEMA.dir}/` : null;
  let files;
  const ls = spawnSync("git", ["-C", REPO_ROOT, "ls-files", "--cached", "--others", "--exclude-standard", "--", dir], {
    encoding: "utf8",
  });
  if (ls.status === 0) {
    files = ls.stdout.split("\n").filter(Boolean);
  } else {
    files = [];
    const walk = (d, prefix) => {
      for (const name of readdirSync(d).sort()) {
        const full = resolve(d, name);
        if (statSync(full).isDirectory()) walk(full, prefix + name + "/");
        else files.push(prefix + name);
      }
    };
    walk(resolve(REPO_ROOT, dir), dir + "/");
  }
  return (docsPagesRead = Object.freeze(
    files
      .filter((f) => f.startsWith(dir + "/") && f.endsWith(".md") && !extra.has(f) && !(schema && f.startsWith(schema)) && isFile(f))
      .map((f) => f.slice(dir.length + 1, -3))
      .filter((name) => !DOCS.exclude.some((path) => `${name}.md` === path || name === path || name.startsWith(`${path}/`)))
      .sort(),
  ));
}

// The kinds of page gen-doc writes, by the word that opens its title
// ("# Class: Action"), and the sidebar group each sits in, in the order
// gen-doc's own index lists them.
export const SCHEMA_KINDS = { Class: "Classes", Slot: "Slots", Enum: "Enumerations", Type: "Types", Subset: "Subsets" };

let schemaPagesRead = null;

/**
 * The schema's pages, its index left out: each page's name, the file name
 * without `.md` and so its address under /schema/; its label, the element's
 * name from its title; its kind; and its file from the repository root. A
 * page of no kind, the schema's own, has a page and no place in the sidebar.
 * The folder is read once it exists, since the sync builds it first.
 *
 * The pages are read from one flat folder, as gen-doc writes them by default.
 * Its --subfolder-type-separation option writes each kind to a folder of its
 * own. The topic would then show no element, and the overview's links would
 * point at GitHub, where the folder is not committed, so such a folder stops
 * the sync here.
 */
export function schemaPages() {
  if (schemaPagesRead) return schemaPagesRead;
  if (!SCHEMA || !isDir(SCHEMA.dir)) return [];
  const markdownIn = (dir) => (isDir(dir) ? readdirSync(resolve(REPO_ROOT, dir)).filter((name) => name.endsWith(".md") && isFile(`${dir}/${name}`)) : []);
  const pages = markdownIn(SCHEMA.dir)
    .filter((name) => name !== "index.md")
    .map((name) => {
      const file = `${SCHEMA.dir}/${name}`;
      // A type's title follows its frontmatter's closing line with no line break: "---# Type: String".
      const m = readFileSync(resolve(REPO_ROOT, file), "utf8").match(/^(?:---)?# (Class|Slot|Enum|Type|Subset): *(.+?) *$/m);
      return { name: name.slice(0, -3), label: m ? m[2] : name.slice(0, -3), kind: m ? m[1] : null, file };
    })
    .sort((a, b) => a.label.localeCompare(b.label, "en", { sensitivity: "base" }) || (a.name < b.name ? -1 : 1));
  const nested = ["classes", "slots", "enums", "types", "subsets", "schemas"].filter((sub) => markdownIn(`${SCHEMA.dir}/${sub}`).length > 0);
  if (nested.length > 0 && !pages.some((p) => p.kind)) {
    fail(
      `SCHEMA's folder ${SCHEMA.dir} holds gen-doc's pages in ${nested.map((sub) => `${sub}/`).join(", ")}, as its ` +
        "--subfolder-type-separation option writes them; the site reads one flat folder, gen-doc's default, so build it without that option",
    );
  }
  return (schemaPagesRead = Object.freeze(pages));
}

/**
 * The old addresses REDIRECTS names, each redirected to a page of the site
 * under its base, as a map for astro.config.mjs. An entry whose key and value
 * both end in [...slug] stands for one redirect per schema page, so the
 * redirects follow the schema as it grows. The schema's folder is read once
 * the sync has built it.
 */
export function redirects() {
  const value = given.REDIRECTS ?? {};
  if (typeof value !== "object" || Array.isArray(value)) fail("REDIRECTS must be an object, each old address to a page of the site");
  const map = {};
  for (const [from, to] of Object.entries(value)) {
    if (typeof to !== "string" || !from.startsWith("/") || !to.startsWith("/")) fail(`REDIRECTS: ${from} and ${to} must each be an address that starts with /`);
    const slug = from.endsWith("/[...slug]");
    if (slug !== to.endsWith("/[...slug]")) fail(`REDIRECTS: ${from} to ${to}; both ends close with /[...slug], or neither does`);
    if (slug && !SCHEMA) fail(`REDIRECTS: ${from} stands for the schema's pages, and the site shows no schema`);
    if (!slug) map[from] = BASE + to;
    else for (const page of schemaPages()) map[from.replace("[...slug]", page.name)] = `${BASE}${to.replace("[...slug]", page.name)}/`;
  }
  return map;
}

const DATABASE = /\.(?:sqlite3?|db)$/;
const METADATA = /^metadata\.(?:ya?ml|json)$/;

/**
 * The data's files in BROWSE's folder: each SQLite database, as its file name
 * and the name Datasette gives it, which is the file name without its
 * extension; and the Datasette metadata file, or null. Nothing else in the
 * folder is published. A database with a journal beside it that is not empty
 * stops the sync: a write to it is unfinished or still open, so a copy of the
 * database could be inconsistent. So do two metadata files, since Datasette
 * reads one.
 */
export function browseFiles() {
  if (!BROWSE || !isDir(BROWSE.dir)) return { databases: [], metadata: null };
  const names = readdirSync(resolve(REPO_ROOT, BROWSE.dir))
    .filter((name) => isFile(`${BROWSE.dir}/${name}`))
    .sort();
  const databases = names.filter((name) => DATABASE.test(name)).map((file) => ({ file, name: file.replace(DATABASE, "") }));
  for (const { file } of databases) {
    for (const journal of [`${file}-wal`, `${file}-journal`]) {
      const path = `${BROWSE.dir}/${journal}`;
      if (isFile(path) && statSync(resolve(REPO_ROOT, path)).size > 0) {
        throw new Error(
          `${path} is not empty: a write to ${file} is unfinished or still open, and a copy of it could be torn. ` +
            "Close what has it open, or build it again, then build the site",
        );
      }
    }
  }
  const metadata = names.filter((name) => METADATA.test(name));
  if (metadata.length > 1) throw new Error(`${BROWSE.dir} holds ${metadata.join(" and ")}, and Datasette reads one: keep one`);
  return { databases, metadata: metadata[0] ?? null };
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const settled = { REPO, SITE, BASE, TITLE, DESCRIPTION, BRANCH, CUSTOM_DOMAIN, REF, LOGO, ASSETS, DOCS, CHANGELOG, RELEASE_TAG, PAGES, HOME, SCHEMA, BROWSE, WORKSPACE };
  console.log(JSON.stringify({ ...settled, docsPages: docsPages(), bundleGroups: bundleGroups(), workspace: workspaceLinks(), redirects: redirects() }, null, 2));
}
