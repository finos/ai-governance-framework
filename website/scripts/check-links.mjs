// This script runs after `astro build`. Every link and image from one page
// of the site to another must reach a file in dist/, and a link to a heading
// must reach an element with that id. A page's social card, named by its
// full address, must be a file too. The generated text files, llms.txt,
// llms-full.txt and the bundle log's feed, name the site's pages by their
// full addresses, and those must reach a file as well. Each redirect page
// that REDIRECTS writes must point at a page. This script does not check a
// link that leaves the site. validate.yml's lychee run checks the
// repository's own Markdown.
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { relative, resolve } from "node:path";
import { BASE, SITE, SITE_DIR, SITE_URL } from "./config.mjs";

const DIST = resolve(SITE_DIR, "dist");
const pages = [];
const walk = (dir) => {
  for (const name of readdirSync(dir)) {
    const full = resolve(dir, name);
    if (statSync(full).isDirectory()) walk(full);
    else if (name.endsWith(".html")) pages.push(full);
  }
};
walk(DIST);

const ids = new Map();
const idsOf = (file) => {
  if (!ids.has(file)) {
    const html = readFileSync(file, "utf8");
    ids.set(file, new Set([...html.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1])));
  }
  return ids.get(file);
};

/** The file in dist/ that a site path is served from, or null. */
function target(path) {
  if (!path.startsWith(BASE + "/") && path !== BASE) return null;
  let rel = decodeURIComponent(path.slice(BASE.length)).replace(/^\//, "");
  const file = resolve(DIST, rel);
  if (rel === "" || rel.endsWith("/")) return existsSync(resolve(file, "index.html")) ? resolve(file, "index.html") : null;
  if (existsSync(file) && statSync(file).isFile()) return file;
  if (existsSync(resolve(file, "index.html"))) return resolve(file, "index.html");
  return null;
}

const broken = [];
let checked = 0;
for (const file of pages) {
  const html = readFileSync(file, "utf8");
  const from = "/" + relative(DIST, file);
  for (const m of html.matchAll(/\s(?:href|src)="([^"]+)"/g)) {
    const url = m[1].replace(/&amp;/g, "&");
    if (/^(?:[a-z]+:|\/\/)/i.test(url) || url.startsWith("#") || url.startsWith("data:")) {
      if (url.startsWith("#") && url.length > 1 && !idsOf(file).has(decodeURIComponent(url.slice(1)))) {
        broken.push(`${from}: no heading ${url}`);
      }
      continue;
    }
    checked++;
    // A relative link resolves against the address its page is served at.
    const { pathname, hash } = new URL(url, `https://site.invalid${BASE}${from}`);
    const hit = target(pathname);
    if (!hit) broken.push(`${from}: ${url}`);
    else if (hash.length > 1 && hit.endsWith(".html") && !idsOf(hit).has(decodeURIComponent(hash.slice(1)))) {
      broken.push(`${from}: ${url} (no such heading)`);
    }
  }
  for (const m of html.matchAll(/<meta http-equiv="refresh" content="\d+;url=([^"]+)"/g)) {
    checked++;
    if (!target(new URL(m[1].replace(/&amp;/g, "&"), `https://site.invalid${BASE}${from}`).pathname)) broken.push(`${from}: sends the browser on to ${m[1]}`);
  }
  for (const m of html.matchAll(/<meta property="og:image" content="([^"]+)"/g)) {
    checked++;
    if (!m[1].startsWith(SITE_URL + "/") || !target(m[1].slice(SITE.length))) broken.push(`${from}: social card ${m[1]}`);
  }
}

// The text files hold Markdown and escaped HTML, so an address is read up to
// the first character that ends one in either, less any punctuation after it.
const unescape = (text) => text.replace(/&quot;/g, '"').replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&");
let files = 0;
for (const name of ["llms.txt", "llms-full.txt", "knowledge/log.xml"]) {
  const file = resolve(DIST, name);
  if (!existsSync(file)) continue;
  files++;
  // A backtick ends an address too: a concept names one in a code span, as
  // markdownlint asks, and the span's closing backtick is not part of it.
  for (const m of unescape(readFileSync(file, "utf8")).matchAll(/https?:\/\/[^\s)"<>`]+/g)) {
    const url = m[0].replace(/[.,;:]+$/, "");
    if (!url.startsWith(SITE_URL + "/")) continue;
    checked++;
    const { pathname, hash } = new URL(url);
    const hit = target(pathname);
    if (!hit) broken.push(`/${name}: ${url}`);
    else if (hash.length > 1 && hit.endsWith(".html") && !idsOf(hit).has(decodeURIComponent(hash.slice(1)))) {
      broken.push(`/${name}: ${url} (no such heading)`);
    }
  }
}

if (broken.length) {
  console.error(`check-links: ${broken.length} broken link(s) in ${pages.length} pages and ${files} text files:`);
  for (const b of [...new Set(broken)].sort()) console.error("  " + b);
  process.exit(1);
}
console.log(`check-links: ${checked} links between ${pages.length} pages and ${files} text files all resolve`);
