// Where a repository path is published. The Markdown plugin and the sync both
// use this, so a link means the same page wherever it is written.
import { statSync } from "node:fs";
import { posix, resolve } from "node:path";
import { ASSETS, BASE, DOCS, HOME, PAGES, REF, REPO_ROOT, REPO_URL, SCHEMA, docsPages, docsRoute, schemaPages } from "./config.mjs";

const ABSOLUTE = /^(?:[a-z][a-z0-9+.-]*:|\/\/)/i;
// The docs pages the site renders: a link to any other file under the docs
// folder goes to the repository.
const DOC_PAGES = new Set(docsPages());
// The schema's pages, read the first time a link needs them after the folder
// exists, since the sync builds the folder after this module loads.
let schemaNames = null;
function isSchemaPage(name) {
  if (!schemaNames) {
    const pages = schemaPages();
    if (pages.length === 0) return false;
    schemaNames = new Set(pages.map((p) => p.name));
  }
  return schemaNames.has(name);
}

function isDirectory(repoPath) {
  try {
    return statSync(resolve(REPO_ROOT, repoPath)).isDirectory();
  } catch {
    return false;
  }
}

/** The site path, or the GitHub address, for a path relative to the repository root. */
export function route(repoPath) {
  const p = repoPath.replace(/^knowledge_bundle(?=\/|$)/, ".lokf/knowledge").replace(/\/$/, "");
  if (p === "" || (HOME.source && p === HOME.source)) return `${BASE}/`;
  const extra = PAGES.find((page) => page.source === p);
  if (extra) return `${BASE}/${extra.slug}/`;
  if (p === ".lokf/knowledge" || p === ".lokf/knowledge/index.md") return `${BASE}/knowledge/`;
  if (ASSETS && p === ASSETS) return `${REPO_URL}/tree/${REF}/${ASSETS}`;
  if (SCHEMA && (p === SCHEMA.dir || p === `${SCHEMA.dir}/index.md`)) return `${BASE}/schema/`;
  if (SCHEMA && p.startsWith(`${SCHEMA.dir}/`) && p.endsWith(".md")) {
    const name = p.slice(SCHEMA.dir.length + 1, -3);
    if (isSchemaPage(name)) return `${BASE}/schema/${name}/`;
  }
  if (DOCS && p.startsWith(`${DOCS.dir}/`) && p.endsWith(".md")) {
    const name = p.slice(DOCS.dir.length + 1, -3);
    if (DOC_PAGES.has(name)) return BASE + docsRoute(name);
  }
  let m = p.match(/^\.lokf\/knowledge\/(.+)\.md$/);
  if (m) {
    const id = m[1];
    if (id.endsWith("/index")) return `${BASE}/knowledge/${id.slice(0, -"/index".length)}/`;
    return `${BASE}/knowledge/${id}/`;
  }
  m = p.match(/^\.lokf\/knowledge\/([^/]+)$/);
  if (m && isDirectory(p)) return `${BASE}/knowledge/${m[1]}/`;
  if (ASSETS && p.startsWith(`${ASSETS}/`)) return `${BASE}/assets/${p.slice(ASSETS.length + 1)}`;
  return `${REPO_URL}/${isDirectory(p) ? "tree" : "blob"}/${REF}/${p}`;
}

/** Rewrite a link written in the file at `fromPath` (repository-relative). */
export function rewriteUrl(fromPath, url) {
  if (!url || ABSOLUTE.test(url) || url.startsWith("#") || url.startsWith("/")) return url;
  const hashAt = url.indexOf("#");
  const pathPart = hashAt < 0 ? url : url.slice(0, hashAt);
  const hash = hashAt < 0 ? "" : url.slice(hashAt);
  if (pathPart === "") return url;
  let decoded = pathPart;
  try {
    decoded = decodeURI(pathPart);
  } catch {
    /* keep it as written */
  }
  const target = posix.normalize(posix.join(posix.dirname(fromPath), decoded));
  if (target.startsWith("..")) return url;
  return route(target === "." ? "" : target) + hash;
}

/** A `srcset` value holds one or more "url descriptor" pairs. */
export function rewriteSrcset(fromPath, value) {
  return value
    .split(",")
    .map((part) => {
      const [u, ...rest] = part.trim().split(/\s+/);
      return [rewriteUrl(fromPath, u), ...rest].join(" ");
    })
    .join(", ");
}

/** Rewrite the src, srcset and href attributes in a fragment of raw HTML. */
export function rewriteHtml(fromPath, html) {
  return html.replace(/\b(src|srcset|href)=("([^"]*)"|'([^']*)')/g, (all, attr, _q, dq, sq) => {
    const value = dq ?? sq;
    const out = attr === "srcset" ? rewriteSrcset(fromPath, value) : rewriteUrl(fromPath, value);
    return `${attr}="${out}"`;
  });
}
