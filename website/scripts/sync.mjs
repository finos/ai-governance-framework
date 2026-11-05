// Writes the site's generated sources from the repository before every
// build, so that no page is written twice. Nothing it writes is committed.
// website/.gitignore lists each place:
//
//   src/content/docs/  a page for the README, each docs/ page, each concept,
//                      each of the schema's pages and the data page
//   src/generated/     the logo, for the header and the home page;
//                      health.json, the numbers the health page charts;
//                      changelogs.ts, the releases collection or none; and
//                      CHANGELOG.md, which the releases section reads
//   public/            the figures, llms.txt, llms-full.txt, the favicon,
//                      the databases under browse/, the home page, each
//                      docs page and each extra page as Markdown beside its
//                      page, and under knowledge/ the four files `lokf
//                      export` writes, every bundle file as it is in the
//                      repository, each concept's JSON-LD, and log.xml, the
//                      bundle log as a feed
//
// It runs two programs the repository already has: the lokf toolkit's
// `export`, from the sidecar's own environment, and knowledge-report.sh,
// whose labels the concept pages show, so the site never derives a label a
// second way. When site.config.mjs shows the schema's pages or the data, it
// also runs the command that builds each, when its folder is not built yet.
import { execFileSync, spawnSync } from "node:child_process";
import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, realpathSync, rmSync, statSync, writeFileSync } from "node:fs";
import { dirname, extname, relative, resolve, sep } from "node:path";
import { markdownToHtml } from "satteri";
import { parse as parseYaml } from "yaml";
import {
  ASSETS,
  BASE,
  BRANCH,
  BROWSE,
  BUNDLE_DIR,
  CHANGELOG,
  CUSTOM_DOMAIN,
  DESCRIPTION,
  DOCS,
  HOME,
  LOGO,
  LOGO_FILES,
  PAGES,
  REF,
  RELEASE_TAG,
  REPO_ROOT,
  REPO_URL,
  SCHEMA,
  SITE,
  SITE_URL,
  SITE_DIR,
  TITLE,
  browseFiles,
  bundleGroups,
  conceptIds,
  docsPages,
  docsRoute,
  groupLabel,
  schemaPages,
  workspaceLinks,
} from "./config.mjs";
import { WIKILINK, cleanHtmlNode, resolveWikilink } from "./markdown-ktl.mjs";
import { rewriteUrl, route } from "./routes.mjs";

const CONTENT = resolve(SITE_DIR, "src", "content", "docs");
const GENERATED = resolve(SITE_DIR, "src", "generated");
const PUBLIC = resolve(SITE_DIR, "public");
const PUBLIC_KNOWLEDGE = resolve(PUBLIC, "knowledge");
const REPORT = resolve(REPO_ROOT, ".lokf", "scripts", "knowledge-report.sh");
// The bundle log's feed holds the log's newest days, a day to an entry. The
// log page holds them all.
const FEED_DAYS = 20;

const read = (path) => readFileSync(path, "utf8");
const repoFile = (rel) => read(resolve(REPO_ROOT, rel));

function write(path, text) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, text);
}

// A fence whose language is mermaid, indented or quoted, with or without more
// words after the language, as the Markdown parser reads one.
const MERMAID = /^[ \t>]*(`{3,}|~{3,})[ \t]*mermaid(?=\s|$)/m;

// JSON is YAML, so the frontmatter needs no YAML writer. A page with a
// mermaid diagram is marked, and only such a page loads the script that draws
// it (src/components/Mermaid.astro). Only on such a page does the Markdown
// plugin leave a diagram for that script. Elsewhere it stays code.
function page(path, frontmatter, body) {
  const marked = MERMAID.test(body) ? { ...frontmatter, ktlMermaid: true } : frontmatter;
  write(path, `---\n${JSON.stringify(marked, null, 2)}\n---\n\n${body.trim()}\n`);
}

// ---------------------------------------------------------------------------
// Markdown helpers. Each one leaves fenced code alone.
// ---------------------------------------------------------------------------

/** Call fn(line, index) on every line outside a fenced code block; fn returns the replacement line(s). */
function mapProse(text, fn) {
  const out = [];
  let fence = null;
  text.split("\n").forEach((line, index) => {
    const m = line.match(/^\s*(`{3,}|~{3,})/);
    if (fence) {
      if (m && m[1][0] === fence[0] && m[1].length >= fence.length) fence = null;
      out.push(line);
    } else if (m) {
      fence = m[1];
      out.push(line);
    } else {
      const r = fn(line, index);
      if (Array.isArray(r)) out.push(...r);
      else if (r !== null) out.push(r);
    }
  });
  return out.join("\n");
}

function splitFrontmatter(text) {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  if (!m) return { data: {}, body: text };
  return { data: parseYaml(m[1]) ?? {}, body: text.slice(m[0].length) };
}

/** The first `# ` heading as a plain title, and the text without it. */
function takeTitle(body) {
  let title = null;
  const rest = mapProse(body, (line) => {
    if (title === null && /^# /.test(line)) {
      title = plain(line.slice(2));
      return null;
    }
    return line;
  });
  return { title, body: rest };
}

function hasH1(body) {
  let found = false;
  mapProse(body, (line) => {
    if (/^# /.test(line)) found = true;
    return line;
  });
  return found;
}

function demoteHeadings(body) {
  return mapProse(body, (line) => (/^#{1,5} /.test(line) ? "#" + line : line));
}

/** The bullets under a `## Open questions` heading, each `- <day>, <actor>: <text>`,
 *  read as knowledge-report.sh reads them: the heading whole on its line, a
 *  fenced example skipped. The card shows them beside the trust label, so a
 *  reader sees why a concept was reopened without scrolling to the foot. */
function openQuestions(body) {
  const found = [];
  let inside = false;
  mapProse(body, (line) => {
    if (/^#+ /.test(line)) inside = /^## Open questions\s*$/.test(line);
    else if (inside) {
      const m = line.match(/^- (\d{4}-\d{2}-\d{2}), (\S+): (.*)$/);
      if (m) found.push({ date: m[1], by: m[2], text: m[3] });
    }
    return line;
  });
  return found;
}

/** Markdown inline syntax stripped to its words, for titles and descriptions. */
function plain(md) {
  return md
    .replace(/!\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/`([^`]*)`/g, "$1")
    .replace(/(\*\*|__)(.*?)\1/g, "$2")
    .replace(/(^|[^\w*])[*_]([^*_]+)[*_](?=[^\w*]|$)/g, "$1$2")
    .replace(/<[^>]+>/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

/** The first sentence of the first paragraph, or of the first note, as a page description. */
function describe(body) {
  const para = body
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .find((p) => p && !/^(#|<|:::|```|~~~|\||[-*] |\d+\. )/.test(p.replace(/^>\s*(\[![A-Z]+\]\s*)?/gm, "")));
  if (!para) return undefined;
  const text = plain(para.replace(/^>\s?(\[![A-Z]+\]\s*)?/gm, ""));
  const sentence = text.match(/^.+?[.!?](?=\s|$)/);
  return (sentence ? sentence[0] : text).slice(0, 300);
}

const ALERTS = { NOTE: "note", TIP: "tip", IMPORTANT: "note", WARNING: "caution", CAUTION: "danger" };

/** GitHub's `> [!NOTE]` alerts become Starlight's `:::note` asides; fenced code is left alone. */
function alertsToAsides(body) {
  const segments = [];
  let fence = null;
  let buf = [];
  for (const line of body.split("\n")) {
    const m = line.match(/^\s*(`{3,}|~{3,})/);
    if (fence) {
      buf.push(line);
      if (m && m[1][0] === fence[0] && m[1].length >= fence.length) {
        segments.push({ code: true, text: buf.join("\n") });
        buf = [];
        fence = null;
      }
    } else if (m) {
      if (buf.length) segments.push({ code: false, text: buf.join("\n") });
      buf = [line];
      fence = m[1];
    } else {
      buf.push(line);
    }
  }
  if (buf.length) segments.push({ code: Boolean(fence), text: buf.join("\n") });
  return segments.map((s) => (s.code ? s.text : asidesInProse(s.text))).join("\n");
}

function asidesInProse(text) {
  const out = [];
  let open = null;
  const close = () => {
    if (open) out.push(":::", "");
    open = null;
  };
  for (const line of text.split("\n")) {
    const start = line.match(/^>\s*\[!([A-Z]+)\]\s*$/);
    if (start && ALERTS[start[1]]) {
      close();
      open = ALERTS[start[1]];
      out.push("", `:::${open}`);
    } else if (open && /^>/.test(line)) {
      out.push(line.replace(/^>\s?/, ""));
    } else {
      close();
      out.push(line);
    }
  }
  close();
  return out.join("\n");
}

/**
 * A `<picture>` with a source for a dark system theme becomes two images,
 * one shown in each of Starlight's themes, so the figure follows the site's
 * theme switch rather than the system's. The theme's class goes
 * on a wrapper, so the zoom button image zoom adds beside each image is
 * hidden with it, and a keyboard or a screen reader meets one per figure.
 */
function picturesToThemedImages(body) {
  return body.replace(/<picture>([\s\S]*?)<\/picture>/g, (whole, inner) => {
    const dark = inner.match(/<source\b[^>]*media="\(prefers-color-scheme:\s*dark\)"[^>]*srcset="([^"]+)"/);
    const img = inner.match(/<img\b([^>]*?)\s*\/?>/);
    if (!dark || !img) return whole;
    const attrs = img[1].replace(/\s+class="[^"]*"/, "");
    const darkAttrs = attrs.replace(/\bsrc="[^"]*"/, `src="${dark[1]}"`);
    return `<span class="dark:sl-hidden"><img${attrs} /></span><span class="light:sl-hidden"><img${darkAttrs} /></span>`;
  });
}

const prepare = (body) => picturesToThemedImages(alertsToAsides(body));

// ---------------------------------------------------------------------------
// The bundle, as the toolkit and the report script see it.
// ---------------------------------------------------------------------------

// The domain schema the justfile's `schema :=` line names, relative to .lokf/
// as the recipes read it, so the four files carry its classes and relations
// as `just lokf-convert` does. An empty line leaves the choice to lokf.
function schemaArgs() {
  const justfile = resolve(REPO_ROOT, ".lokf", "justfile");
  const m = existsSync(justfile) && read(justfile).match(/^schema := "([^"]*)"$/m);
  return m && m[1] ? ["--schema", resolve(REPO_ROOT, ".lokf", m[1])] : [];
}

function lokfExport() {
  mkdirSync(PUBLIC_KNOWLEDGE, { recursive: true });
  execFileSync(
    "uv",
    [
      "run",
      "--project",
      resolve(REPO_ROOT, ".lokf"),
      "--frozen",
      "--quiet",
      "lokf",
      "export",
      ...schemaArgs(),
      BUNDLE_DIR,
      "--out-dir",
      PUBLIC_KNOWLEDGE,
      "--source-base",
      `${REPO_URL}/blob/${REF}/.lokf/knowledge`,
    ],
    { stdio: "inherit" },
  );
  return {
    graph: JSON.parse(read(resolve(PUBLIC_KNOWLEDGE, "graph.json"))),
    jsonld: JSON.parse(read(resolve(PUBLIC_KNOWLEDGE, "concepts.jsonld"))),
  };
}

function report(...args) {
  const run = spawnSync("bash", [REPORT, "--root", REPO_ROOT, ...args], { encoding: "utf8" });
  if (run.error) throw run.error;
  if (run.status !== 0 && !run.stdout) {
    throw new Error(`knowledge-report.sh ${args.join(" ")} failed: ${run.stderr}`);
  }
  return run.stdout.trimEnd();
}

/** knowledge-report.sh labels: "- Title (group/name.md) - label, label". */
function readLabels() {
  const labels = new Map();
  for (const line of report("labels").split("\n")) {
    const m = line.match(/^- (.*) \(([^()]+\.md)\) - (.*)$/);
    if (m) labels.set(m[2].replace(/\.md$/, ""), m[3]);
  }
  return labels;
}

function toneOf(label) {
  if (label.startsWith("retired")) return "retired";
  if (label.startsWith("confirmed by a person")) return "person";
  if (label.startsWith("edited since a person")) return "edited";
  if (label.startsWith("checked by automation")) return "automation";
  return "nobody";
}
// The ladder, top first. src/trust.ts words each state in the same order.
const TONE_ORDER = ["person", "edited", "automation", "nobody", "retired"];

/**
 * Whom a concept is retold for, as words: its `audience` field, or an
 * `audience-` tag, where `audience-13-18` reads "Ages 13 to 18" and
 * `audience-beginners` reads "Beginners". Null for a concept written for
 * everyone.
 */
function audienceOf(data) {
  if (data.audience) return [].concat(data.audience).map(String).join(", ");
  const tag = (Array.isArray(data.tags) ? data.tags : []).map(String).find((t) => t.startsWith("audience-"));
  if (!tag) return null;
  const ages = tag.match(/^audience-(\d+)-(\d+)$/);
  if (ages) return `Ages ${ages[1]} to ${ages[2]}`;
  const words = tag.slice("audience-".length).replace(/[-_]+/g, " ");
  return words.charAt(0).toUpperCase() + words.slice(1);
}

// How the bundle's prose spells a word with a capital past its first letter,
// such as SLSA or GitHub, by the word in lower case. A name gives no sign
// that Slsa is an acronym, so the prose decides. The spellings are found
// before any name is worded.
let spellings = new Map();

/**
 * The spellings the bundle's titles, descriptions, definitions and bodies
 * use, leaving out code, links and addresses. A spelling counts only where it
 * is at least as common as the word in lower case, so "it" never reads "IT".
 */
function findSpellings(concepts) {
  const counts = new Map();
  for (const c of concepts) {
    const prose = [c.data.title, c.data.description, c.data.definition, c.body]
      .filter(Boolean)
      .join("\n")
      .replace(/^(`{3,}|~{3,})[^]*?^\1/gm, "")
      .replace(/`[^`]*`/g, "")
      .replace(/\]\([^)]*\)/g, "]")
      .replace(/<?https?:\/\/\S+/g, "");
    for (const word of prose.match(/[A-Za-z][A-Za-z0-9]*/g) ?? []) {
      const key = word.toLowerCase();
      if (!counts.has(key)) counts.set(key, new Map());
      counts.get(key).set(word, (counts.get(key).get(word) ?? 0) + 1);
    }
  }
  const found = new Map();
  for (const [key, forms] of counts) {
    const [best, n] = [...forms].filter(([w]) => /^.+[A-Z]/.test(w)).sort((a, b) => b[1] - a[1])[0] ?? [];
    if (best && n >= (forms.get(key) ?? 0)) found.set(key, best);
  }
  return found;
}

/**
 * A class or slot name as words, so derivedFrom reads "Derived from" and
 * SlsaSourceControlSystem "SLSA source control system": a word the name
 * writes in capitals keeps them, and so does one the prose spells with them.
 * Within a sentence, the first word takes no capital of its own.
 */
function slotName(slot, { inSentence = false } = {}) {
  const words = slot
    .replace(/([a-z0-9])([A-Z])/g, "$1 $2")
    .replace(/([A-Z]+)([A-Z][a-z])/g, "$1 $2")
    .split(/[\s_]+/)
    .filter(Boolean)
    .map((w) => spellings.get(w.toLowerCase()) ?? (/^[A-Z0-9]{2,}$/.test(w) ? w : w.toLowerCase()));
  const text = words.join(" ");
  return !inSentence && words[0] === words[0]?.toLowerCase() ? text.charAt(0).toUpperCase() + text.slice(1) : text;
}

function githubFile(repoPath) {
  let kind = "blob";
  try {
    if (statSync(resolve(REPO_ROOT, repoPath)).isDirectory()) kind = "tree";
  } catch {
    /* a source that is gone still gets its address */
  }
  return `${REPO_URL}/${kind}/${REF}/${repoPath}`;
}

// A licence as the site names it: a Creative Commons or SPDX address by its
// short name, an `spdx:` CURIE by its identifier with the address that
// resolves it, and any other value as it is written, linked when it is an
// address.
function licenceOf(value) {
  const licence = String(value);
  const cc = licence.match(/creativecommons\.org\/licenses\/([a-z-]+)\/(\d\.\d)/i);
  if (cc) return { text: `CC ${cc[1].toUpperCase()} ${cc[2]}`, href: licence };
  if (/creativecommons\.org\/publicdomain\/zero\/1\.0/i.test(licence)) return { text: "CC0 1.0", href: licence };
  const spdx = licence.match(/^(?:https?:\/\/spdx\.org\/licenses\/|spdx:)([^/]+?)(?:\.html)?\/?$/i);
  if (spdx) return { text: spdx[1], href: `https://spdx.org/licenses/${spdx[1]}` };
  return /^https?:\/\//.test(licence) ? { text: licence, href: licence } : { text: licence };
}

// A licence in Markdown: its name, linked to its address when it has one.
const licenceMd = (value) => {
  const l = licenceOf(value);
  return l.href ? `[${l.text}](${l.href})` : l.text;
};

// The page head carries the concept as JSON-LD. Escaping <, > and & keeps a
// field value such as "</script>" from ending the block, and \uXXXX is still JSON.
const scriptSafe = (doc) =>
  JSON.stringify(doc).replace(/</g, "\\u003c").replace(/>/g, "\\u003e").replace(/&/g, "\\u0026");

function buildConcepts(exported, labels) {
  const context = exported.jsonld["@context"];
  const docs = new Map(exported.jsonld["@graph"].map((d) => [d.id ?? d["@id"], d]));
  const nodes = new Map(exported.graph.nodes.map((n) => [n.data.id, n.data]));
  const edges = exported.graph.edges.map((e) => e.data);
  const root = splitFrontmatter(read(resolve(BUNDLE_DIR, "index.md"))).data;
  const baseIri = root.base_iri ?? "";

  const concepts = conceptIds().map((id) => {
    const text = read(resolve(BUNDLE_DIR, `${id}.md`));
    const { data, body } = splitFrontmatter(text);
    const iri = data.id ?? baseIri + id;
    const label = labels.get(id) ?? "nobody has checked this yet";
    return { id, iri, data, body, text, label, tone: toneOf(label), title: String(data.title ?? id) };
  });
  spellings = findSpellings(concepts);
  const byIri = new Map(concepts.map((c) => [c.iri, c]));
  const linkTo = (iri) => {
    const c = byIri.get(iri);
    if (c) return { text: c.title, href: `${BASE}/knowledge/${c.id}/`, tone: c.tone };
    const node = nodes.get(iri);
    if (node?.concept_id) return { text: node.label ?? iri, href: `${BASE}/knowledge/${node.concept_id}/` };
    return { text: iri, href: iri };
  };

  for (const c of concepts) {
    const out = new Map();
    for (const e of edges.filter((e) => e.source === c.iri)) {
      const name = slotName(e.slot ?? e.predicate);
      if (!out.has(name)) out.set(name, []);
      out.get(name).push(linkTo(e.target));
    }
    const sources = (Array.isArray(c.data.sources) ? c.data.sources : [])
      .map((s) => (typeof s === "string" ? s : s.resource ?? s.url ?? s.id))
      .filter(Boolean)
      .map(String);
    if (sources.length === 0 && c.data.resource) sources.push(String(c.data.resource));
    const event = (e) => ({ by: String(e.by ?? ""), at: String(e.at ?? ""), ...(e.note ? { note: String(e.note) } : {}) });
    // A concept takes the bundle's licence unless it declares its own.
    const licence = c.data.license ?? root.license;

    c.record = {
      id: c.id,
      iri: c.iri,
      type: String(c.data.type ?? "Concept"),
      typeName: slotName(String(c.data.type ?? "Concept")),
      ...(c.data.genre ? { genre: String(c.data.genre) } : {}),
      group: c.id.includes("/") ? c.id.split("/")[0] : "",
      ...(c.data.status ? { status: String(c.data.status) } : {}),
      label: c.label,
      tone: c.tone,
      ...(c.data.definition ? { definition: String(c.data.definition) } : {}),
      ...(c.data.stale_after ? { reviewBy: String(c.data.stale_after) } : {}),
      tags: (Array.isArray(c.data.tags) ? c.data.tags : []).map(String),
      ...(c.data.generated ? { generated: event(c.data.generated) } : {}),
      verified: (Array.isArray(c.data.verified) ? c.data.verified : []).map(event),
      questions: openQuestions(c.body),
      sources: sources.map((s) => {
        if (/^https?:/.test(s)) return { text: s, href: s };
        const path = s.replace(/^\.(?:\/|$)/, "").replace(/\/$/, "");
        if (path === "") return { text: "the whole repository", href: `${REPO_URL}/tree/${REF}` };
        // The schema's pages are built, never committed, so a source among
        // them links its page on this site.
        if (SCHEMA && (path === SCHEMA.dir || path.startsWith(`${SCHEMA.dir}/`))) return { text: s, href: route(path) };
        return { text: s, href: githubFile(path) };
      }),
      relations: [...out].map(([name, targets]) => ({
        name,
        targets: targets.sort((a, b) => a.text.localeCompare(b.text)),
      })),
      incoming: edges
        .filter((e) => e.target === c.iri && byIri.has(e.source))
        .map((e) => ({ name: slotName(e.slot ?? e.predicate, { inSentence: true }), from: linkTo(e.source) }))
        .sort((a, b) => a.from.text.localeCompare(b.from.text)),
      ...(licence ? { licence: licenceOf(licence) } : {}),
      // The graph explorer opened on this concept. The id keeps its slashes.
      graph: `${BASE}/graph/?concept=${encodeURIComponent(c.id).replace(/%2F/g, "/")}`,
      files: {
        markdown: `${BASE}/knowledge/${c.id}.md`,
        jsonld: `${BASE}/knowledge/${c.id}.jsonld`,
        github: githubFile(`.lokf/knowledge/${c.id}.md`),
        // Every commit that changed the file, up to the one the site was built from.
        history: `${REPO_URL}/commits/${REF}/.lokf/knowledge/${c.id}.md`,
      },
    };

    const doc = docs.get(c.iri);
    c.jsonld = doc ? { "@context": context, ...doc } : null;

    // A retelling for an audience names its audience, and `derivedFrom`
    // names the one concept it retells.
    c.audience = audienceOf(c.data);
    const derived = [].concat(c.data.derivedFrom ?? []).map((iri) => byIri.get(String(iri))).filter(Boolean);
    c.retells = c.audience && derived.length === 1 ? derived[0] : null;
  }
  return { concepts, root, context };
}

// The reading levels of each page that has a retelling, by the page's site
// path, found before the pages are written: the page as Full, then each
// retelling by its audience. The same list sits on the page and on each of
// its retellings, so a reader can move between them from either.
let readingLevels = new Map();

function findReadingLevels(concepts) {
  const retellings = [];
  for (const p of PAGES) {
    if (!p.retells) continue;
    const of = route(p.retells);
    if (/^https?:/.test(of)) throw new Error(`site.config.mjs PAGES: ${p.source} retells ${p.retells}, which has no page on this site`);
    retellings.push({ of, href: `${BASE}/${p.slug}/`, level: p.level });
  }
  for (const c of concepts) {
    if (c.retells) retellings.push({ of: `${BASE}/knowledge/${c.retells.id}/`, href: `${BASE}/knowledge/${c.id}/`, level: c.audience });
  }
  const levels = new Map();
  for (const of of new Set(retellings.map((r) => r.of))) {
    const list = [
      { label: "Full", href: of },
      ...retellings
        .filter((r) => r.of === of)
        .sort((a, b) => a.level.localeCompare(b.level))
        .map((r) => ({ label: r.level, href: r.href })),
    ];
    for (const { href } of list) levels.set(href, list);
  }
  return levels;
}

/** The `ktlLevels` frontmatter of the page at `path`, its own level unlinked, or nothing. */
function levelsOf(path) {
  const list = readingLevels.get(path);
  return list ? { ktlLevels: list.map((l) => (l.href === path ? { label: l.label } : l)) } : {};
}

// ---------------------------------------------------------------------------
// Pages.
// ---------------------------------------------------------------------------

function writeConceptPages(concepts) {
  const byGroup = new Map();
  for (const c of concepts) {
    const g = c.record.group;
    if (!byGroup.has(g)) byGroup.set(g, []);
    byGroup.get(g).push(c);
  }
  for (const list of byGroup.values()) list.sort((a, b) => a.title.localeCompare(b.title));

  for (const c of concepts) {
    const order = byGroup.get(c.record.group).indexOf(c) + 1;
    const head = [
      { tag: "link", attrs: { rel: "alternate", type: "text/markdown", href: c.record.files.markdown } },
      ...(c.record.licence?.href ? [{ tag: "link", attrs: { rel: "license", href: c.record.licence.href } }] : []),
    ];
    if (c.jsonld) {
      const { body: _body, ...summary } = c.jsonld;
      head.push(
        { tag: "link", attrs: { rel: "alternate", type: "application/ld+json", href: c.record.files.jsonld } },
        { tag: "script", attrs: { type: "application/ld+json" }, content: scriptSafe(summary) },
      );
      write(resolve(PUBLIC_KNOWLEDGE, `${c.id}.jsonld`), JSON.stringify(c.jsonld, null, 2) + "\n");
    }
    page(
      resolve(CONTENT, "knowledge", `${c.id}.md`),
      {
        title: c.title,
        // Plain words: the description is the page's meta description, which
        // link previews and search engines show as it is.
        ...(c.data.description ? { description: plain(String(c.data.description)) } : {}),
        ktlSource: `.lokf/knowledge/${c.id}.md`,
        ktlShiftHeadings: hasH1(c.body),
        editUrl: false,
        // The sidebar entry carries the concept's trust: catalogue.css draws a
        // dot from the tone, and the label is its tooltip.
        sidebar: { order, attrs: { "data-ktl-tone": c.tone, title: c.label } },
        head,
        lokf: c.record,
        ...levelsOf(`${BASE}/knowledge/${c.id}/`),
      },
      c.body,
    );
  }
  return byGroup;
}

const labelSpan = (c) => `<span class="ktl-label ktl-label--${c.tone}">${c.label}</span>`;

/**
 * What a link to a concept shows before the reader follows it: the title,
 * the type and genre, the trust label and the definition, by concept id, for
 * src/components/ConceptPreviews.astro to read. The definition keeps its
 * code spans, as the card shows them. A concept with no definition shows its
 * description instead.
 */
function writePreviews(concepts) {
  const previews = Object.fromEntries(
    [...concepts]
      .sort((a, b) => a.id.localeCompare(b.id))
      .map((c) => {
        const definition = c.data.definition ?? c.data.description;
        return [
          c.id,
          {
            title: c.title,
            type: c.record.typeName,
            ...(c.record.genre ? { genre: c.record.genre } : {}),
            label: c.label,
            tone: c.tone,
            ...(definition ? { definition: String(definition) } : {}),
          },
        ];
      }),
  );
  write(resolve(PUBLIC_KNOWLEDGE, "previews.json"), JSON.stringify(previews) + "\n");
}

function writeGroupPages(byGroup) {
  for (const group of bundleGroups()) {
    const list = byGroup.get(group) ?? [];
    const items = list.map(
      (c) => `- [${c.title}](${BASE}/knowledge/${c.id}/) ${labelSpan(c)}\\\n  ${String(c.data.description ?? "")}`,
    );
    page(
      resolve(CONTENT, "knowledge", group, "index.md"),
      {
        title: groupLabel(group),
        description: `The concepts in the knowledge bundle's ${group} folder, with how far each has been checked.`,
        editUrl: false,
        sidebar: { label: "Overview", order: 0 },
      },
      `<div class="ktl-list">\n\n${items.join("\n\n")}\n\n</div>`,
    );
  }
}

function parseHealth(line) {
  return line
    .split(" · ")
    .map((part) => part.match(/^(.+?):\s*(.+)$/))
    .filter(Boolean)
    .map((m) => [m[1], m[2]]);
}

function writeOverview(root, concepts, health) {
  const text = read(resolve(BUNDLE_DIR, "index.md"));
  const { body } = splitFrontmatter(text);
  const { body: rest } = takeTitle(body);
  const [intro, ...after] = rest.trim().split(/\n(?=# )/);
  const k = `${BASE}/knowledge`;
  const license = root.license ? licenceMd(root.license) : "not stated";
  const publisher = root.publisher?.name ?? root.publisher?.id ?? "not stated";
  const facts = [
    "| The root file declares | |",
    "| --- | --- |",
    `| Base IRI | \`${root.base_iri ?? ""}\` |`,
    `| JSON-LD context | \`${root.context ?? ""}\` |`,
    `| Licence | ${license} |`,
    `| Publisher | ${publisher} |`,
    `| Concepts | ${concepts.length} |`,
  ].join("\n");
  const healthList = parseHealth(health)
    .map(([k2, v]) => `- ${k2}: ${v}`)
    .join("\n");
  const files = [
    `- [concepts.jsonld](${k}/concepts.jsonld): every concept's frontmatter and body under one JSON-LD context.`,
    `- [graph.nt](${k}/graph.nt): the whole bundle as N-Triples.`,
    `- [graph.json](${k}/graph.json): the typed relations as cytoscape.js elements, which the [knowledge graph](${BASE}/graph/) draws.`,
    `- [datasets.jsonld](${k}/datasets.jsonld): a schema.org Dataset description for each Dataset or Table concept.`,
    `- [index.md](${k}/index.md): the bundle's root file, which declares the header above.`,
    `- [log.xml](${k}/log.xml): the [bundle log](${k}/log/) as an Atom feed, its newest ${FEED_DAYS} days.`,
    `- [previews.json](${k}/previews.json): each concept's title, type, genre, trust label and definition, which a link to the concept shows before it is followed.`,
    `- Each concept page links the concept's own Markdown file and its JSON-LD, at the concept's path with \`.md\` or \`.jsonld\` added.`,
    ...(existsSync(resolve(REPO_ROOT, ".github", "workflows", "knowledge-release.yaml"))
      ? [`- The bundle as it stood at each release is a zip on the [releases page](${REPO_URL}/releases).`]
      : []),
  ].join("\n");
  const generated = [
    intro.trim(),
    facts,
    `# How far it has been checked\n\nThe [bundle health](${BASE}/health/) page gives each concept's label. The counts, computed from frontmatter when the site was built:\n\n${healthList}`,
    `# Files\n\n${files}`,
    `# Contents`,
    after.map((s) => s.replace(/^# /, "## ")).join("\n"),
  ].join("\n\n");
  page(
    resolve(CONTENT, "knowledge", "index.md"),
    {
      title: String(root.title ?? "Knowledge bundle"),
      ...(root.description ? { description: String(root.description) } : {}),
      ktlSource: ".lokf/knowledge/index.md",
      editUrl: false,
      head: [
        { tag: "link", attrs: { rel: "alternate", type: "application/ld+json", href: `${k}/concepts.jsonld` } },
        { tag: "link", attrs: { rel: "alternate", type: "application/n-triples", href: `${k}/graph.nt` } },
      ],
    },
    demoteHeadings(generated),
  );
}

function writeLog() {
  const { body } = splitFrontmatter(read(resolve(BUNDLE_DIR, "log.md")));
  const { body: rest } = takeTitle(body);
  page(
    resolve(CONTENT, "knowledge", "log.md"),
    {
      title: "Bundle log",
      description: "What changed in the knowledge bundle, newest first, as the bundle's log.md records it.",
      ktlSource: ".lokf/knowledge/log.md",
      ktlShiftHeadings: hasH1(rest),
      editUrl: false,
    },
    `A feed reader can follow this log: [log.xml](${BASE}/knowledge/log.xml) holds its newest ${FEED_DAYS} days.\n\n${rest}`,
  );
}

const isoTime = (seconds) => new Date(seconds * 1000).toISOString().replace(/\.\d{3}Z$/, "Z");

/**
 * The commit time of each line of the log, line number to time, as git
 * blame reports it. A line changed in the working tree is dated now. The map
 * is empty without git, or for a log not yet committed.
 */
function logLineTimes() {
  const times = new Map();
  try {
    const log = relative(REPO_ROOT, resolve(BUNDLE_DIR, "log.md")).replaceAll("\\", "/");
    const out = execFileSync("git", ["-C", REPO_ROOT, "blame", "--porcelain", "--", log], {
      encoding: "utf8",
      stdio: ["ignore", "pipe", "ignore"],
      maxBuffer: 256 * 1024 * 1024,
    });
    // Each line opens with its commit and its number. The commit's details
    // follow the first line it owns, and a tab opens the line's own text.
    const bySha = new Map();
    let sha = null;
    let line = 0;
    for (const row of out.split("\n")) {
      const head = row.match(/^([0-9a-f]{40}) \d+ (\d+)/);
      if (head) [sha, line] = [head[1], Number(head[2])];
      else if (row.startsWith("committer-time ")) bySha.set(sha, isoTime(Number(row.slice("committer-time ".length))));
      else if (row.startsWith("\t") && bySha.has(sha)) times.set(line, bySha.get(sha));
    }
  } catch {
    /* no git: each day is dated at its midnight, with no published time */
  }
  return times;
}

// XML allows no control character but tab and the two line ends, so one in
// the log is dropped rather than left to break the whole feed.
const xml = (text) =>
  String(text)
    .replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");

/**
 * The bundle log as an Atom feed, so a reader can follow what changed without
 * watching the repository. Each `## YYYY-MM-DD` section the pen writes is an
 * entry, titled with the kinds of change it holds, which are its categories
 * too, and rendered as the page renders it. Git dates it: published when its
 * first line was committed, updated when its newest was, so a correction to
 * an old day reaches a reader too. An entry's id is the bundle's `base_iri`
 * with `log#` and the date, the identity that outlives a move of the site.
 */
async function writeLogFeed(root) {
  const text = read(resolve(BUNDLE_DIR, "log.md"));
  const { body } = splitFrontmatter(text);
  // The file's number for the body's first line, which git blame counts from.
  const first = text.slice(0, text.length - body.length).split("\n").length;
  // The day headings, outside fenced code, by line; a `#` or another `##`
  // heading ends a day.
  const headings = new Map();
  mapProse(body, (line, index) => {
    const m = line.match(/^(#{1,2}) (.*?)\s*$/);
    if (m) headings.set(index, m[1] === "##" && /^\d{4}-\d{2}-\d{2}$/.test(m[2]) ? m[2] : null);
    return line;
  });
  // A date written twice is still one day, since an entry's id is its date.
  // Blank lines are left undated: a diff may credit one to an older commit.
  const byDate = new Map();
  let day = null;
  body.split("\n").forEach((line, index) => {
    if (headings.has(index)) {
      const date = headings.get(index);
      if (date && !byDate.has(date)) byDate.set(date, { date, lines: [], numbers: [] });
      day = date ? byDate.get(date) : null;
      if (day) day.numbers.push(first + index);
    } else if (day) {
      day.lines.push(line);
      if (line.trim()) day.numbers.push(first + index);
    }
  });
  const days = [...byDate.values()].sort((a, b) => b.date.localeCompare(a.date)).slice(0, FEED_DAYS);
  const times = logLineTimes();
  const span = (d) => {
    const at = d.numbers.map((n) => times.get(n)).filter(Boolean).sort();
    return { published: at[0], updated: at.at(-1) ?? `${d.date}T00:00:00Z` };
  };
  const log = `${SITE_URL}/knowledge/log/`;
  const feedId = `${String(root.base_iri ?? `${SITE_URL}/knowledge/`).replace(/\/?$/, "/")}log`;

  const entries = [];
  let newest = "1970-01-01T00:00:00Z";
  for (const d of days) {
    const text = d.lines.join("\n").trim();
    const kinds = new Map();
    for (const m of text.matchAll(/^[*-] \*\*([^*]+)\*\*:/gm)) kinds.set(m[1], (kinds.get(m[1]) ?? 0) + 1);
    const title = [d.date, ...[...kinds].sort((a, b) => b[1] - a[1]).map(([kind, n]) => `${kind}: ${n}`)].join(" · ");
    const { html } = await markdownToHtml(text, {
      mdastPlugins: [{ name: "ktl-raw-html", html: (node, ctx) => cleanHtmlNode(node, ctx, ".lokf/knowledge/log.md") }],
    });
    const content = html.replace(
      /(<(?:a|img)\b[^>]*?\s(?:href|src)=")([^"]*)"/g,
      (_, before, url) => `${before}${absoluteUrl(".lokf/knowledge/log.md", log, url)}"`,
    );
    const { published, updated } = span(d);
    if (updated > newest) newest = updated;
    entries.push(
      [
        "  <entry>",
        `    <title>${xml(title)}</title>`,
        `    <link rel="alternate" type="text/html" href="${xml(`${log}#${d.date}`)}"/>`,
        `    <id>${xml(`${feedId}#${d.date}`)}</id>`,
        ...(published ? [`    <published>${published}</published>`] : []),
        `    <updated>${updated}</updated>`,
        ...[...kinds.keys()].map((kind) => `    <category term="${xml(kind)}"/>`),
        `    <content type="html">${xml(content)}</content>`,
        "  </entry>",
      ].join("\n"),
    );
  }
  const licence = root.license ? licenceOf(root.license) : null;
  const lines = [
    '<?xml version="1.0" encoding="utf-8"?>',
    '<feed xmlns="http://www.w3.org/2005/Atom">',
    `  <title>${xml(`${TITLE}: bundle log`)}</title>`,
    "  <subtitle>What changed in the knowledge bundle, a day to an entry, newest first.</subtitle>",
    `  <link rel="self" type="application/atom+xml" href="${xml(`${SITE_URL}/knowledge/log.xml`)}"/>`,
    `  <link rel="alternate" type="text/html" href="${xml(log)}"/>`,
    `  <link rel="alternate" type="text/markdown" href="${xml(`${SITE_URL}/knowledge/log.md`)}"/>`,
    `  <id>${xml(feedId)}</id>`,
    `  <updated>${newest}</updated>`,
    `  <author><name>${xml(root.publisher?.name ?? TITLE)}</name></author>`,
    ...(licence ? [`  <rights>${xml(licence.text)}</rights>`] : []),
    ...(licence?.href ? [`  <link rel="license" href="${xml(licence.href)}"/>`] : []),
    ...entries,
    "</feed>",
    "",
  ];
  write(resolve(PUBLIC_KNOWLEDGE, "log.xml"), lines.join("\n"));
}

// The health page is an Astro page, src/pages/health.astro, which charts
// these numbers. The sync only gathers them.
function writeHealth(concepts, health, full) {
  const count = (list) => Object.fromEntries(TONE_ORDER.map((t) => [t, list.filter((c) => c.tone === t).length]));
  const groups = bundleGroups().map((group) => {
    const list = concepts.filter((c) => c.record.group === group);
    return { group, label: groupLabel(group), href: `${BASE}/knowledge/${group}/`, total: list.length, ...count(list) };
  });
  const sorted = [...concepts].sort(
    (a, b) => TONE_ORDER.indexOf(a.tone) - TONE_ORDER.indexOf(b.tone) || a.title.localeCompare(b.title),
  );
  const data = {
    line: parseHealth(health),
    total: concepts.length,
    counts: count(concepts),
    groups,
    concepts: sorted.map((c) => ({
      title: c.title,
      href: `${BASE}/knowledge/${c.id}/`,
      group: groupLabel(c.record.group),
      label: c.label,
      tone: c.tone,
    })),
    report: full,
  };
  write(resolve(GENERATED, "health.json"), JSON.stringify(data, null, 2) + "\n");
}

function writeDocs() {
  if (!DOCS) return [];
  const found = docsPages();
  const groups = DOCS.groups;
  if (groups) {
    const placed = new Set(groups.flatMap((g) => g.pages));
    const missing = found.filter((p) => !placed.has(p));
    const gone = [...placed].filter((p) => !found.includes(p));
    if (missing.length || gone.length) {
      throw new Error(
        `site.config.mjs DOCS.groups is out of step with ${DOCS.dir}/: ` +
          (missing.length ? `not placed: ${missing.join(", ")}. ` : "") +
          (gone.length ? `placed but missing: ${gone.join(", ")}.` : ""),
      );
    }
  }
  const docs = found.map((name) => {
    const source = `${DOCS.dir}/${name}.md`;
    const { title, body } = takeTitle(repoFile(source));
    return { name, source, title: title ?? name, description: describe(body), body, route: docsRoute(name) };
  });
  // Grouped pages keep their group's order. Ungrouped ones sit by title, with
  // the folder's index first as its overview, and each one's sidebar entry
  // says where.
  const order = groups ? groups.flatMap((g) => g.pages) : null;
  const rank = (d) => (d.name === "index" ? 0 : 1);
  docs.sort((a, b) => (order ? order.indexOf(a.name) - order.indexOf(b.name) : rank(a) - rank(b) || a.title.localeCompare(b.title)));
  docs.forEach((d, i) => {
    d.markdown = writeMarkdown(d.source, d.route);
    page(
      resolve(CONTENT, "docs", `${d.name}.md`),
      {
        title: d.title,
        ...(d.description ? { description: d.description } : {}),
        // A page named after its sidebar group opens the group, labelled as
        // each bundle group's index is.
        ...(groups && groups.some((g) => g.label.toLowerCase() === d.name) ? { sidebar: { label: "Overview" } } : {}),
        ...(groups ? {} : { sidebar: { order: i + 1, ...(d.name === "index" ? { label: "Overview" } : {}) } }),
        ktlSource: d.source,
        editUrl: `${REPO_URL}/edit/${BRANCH}/${d.source}`,
        head: [markdownAlternate(d.markdown)],
        ...levelsOf(BASE + d.route),
      },
      prepare(d.body),
    );
  });
  return docs.map(({ name, title, description, markdown }) => ({ name, title, description, markdown: SITE + markdown }));
}

/** The text from its first `# ` title down, passing over a `# ` inside fenced code. */
function fromTitle(text, file) {
  const lines = text.split("\n");
  let fence = null;
  for (const [i, line] of lines.entries()) {
    const m = line.match(/^\s*(`{3,}|~{3,})/);
    if (fence) {
      if (m && m[1][0] === fence[0] && m[1].length >= fence.length) fence = null;
    } else if (m) fence = m[1];
    else if (/^# /.test(line)) return lines.slice(i).join("\n");
  }
  throw new Error(`${file} has no '# ' title, and the home page starts at it`);
}

/** The text from its first `# ` title down, or after its frontmatter when it has no title. */
const fromTitleOrAll = (text) => (hasH1(text) ? fromTitle(text, "") : splitFrontmatter(text).body);

const markdownAlternate = (href) => ({ tag: "link", attrs: { rel: "alternate", type: "text/markdown", href } });

/**
 * A page's source as a Markdown file beside the page, at the page's path with
 * `.md` added, for a reader or a model that wants the words without the
 * site: the text from its title down, with every link a full address. It
 * returns the file's site path, which the page's head names as an alternate.
 */
function writeMarkdown(source, pagePath) {
  const path = `${pagePath.replace(/\/$/, "") || "/index"}.md`;
  const text = absoluteMarkdown(source, SITE_URL + pagePath, fromTitleOrAll(repoFile(source)));
  write(resolve(PUBLIC, path.slice(1)), text.trim() + "\n");
  return BASE + path;
}

/** The tagline under the home page's title: as given, the first line bold throughout of the file named, or the site's description. */
function homeTagline() {
  const given = HOME.tagline;
  if (typeof given === "string") return given;
  if (!given) return DESCRIPTION;
  let tagline = null;
  mapProse(repoFile(given.boldLineOf), (line) => {
    const bold = tagline === null && line.match(/^\*\*((?:(?!\*\*).)+)\*\*\s*$/);
    if (bold) tagline = plain(bold[1]);
    return line;
  });
  if (!tagline) {
    throw new Error(`${given.boldLineOf} has no line bold throughout, and HOME.tagline takes the home page's tagline from it`);
  }
  return tagline;
}

function writeHome() {
  // The home page: the source from its title down, under a hero. The logo
  // above a README's title is for GitHub, and the hero shows the logo itself.
  // A line that links this site's home page is left out, since here it would
  // link to the page it is on. The README keeps that link on a line of its
  // own, together with the pointers the site gives as buttons. Each step
  // passes over fenced code, and a source with no title stops the build. With no source,
  // the page opens with the bundle's own introduction, the text its overview
  // page opens with.
  const home = [`](${SITE_URL})`, `](${SITE_URL}/)`, `<${SITE_URL}>`, `<${SITE_URL}/>`];
  let body;
  if (HOME.source) {
    body = takeTitle(
      mapProse(fromTitle(repoFile(HOME.source), HOME.source), (line) =>
        home.some((link) => line.includes(link)) ? null : line,
      ),
    ).body;
  } else {
    const { body: index } = splitFrontmatter(read(resolve(BUNDLE_DIR, "index.md")));
    body = takeTitle(index).body.trim().split(/\n(?=# )/)[0];
  }
  const tagline = homeTagline();
  const actions = HOME.actions.map((a) => ({ ...a, link: a.link.startsWith("/") ? BASE + a.link : a.link }));
  page(
    resolve(CONTENT, "index.md"),
    {
      title: TITLE,
      description: tagline,
      template: "splash",
      hero: {
        tagline,
        ...(LOGO_FILES
          ? { image: { light: `../../generated/${LOGO_FILES.light}`, dark: `../../generated/${LOGO_FILES.dark}`, alt: "" } }
          : {}),
        actions,
      },
      ktlSource: HOME.source ?? ".lokf/knowledge/index.md",
      editUrl: HOME.source ? `${REPO_URL}/edit/${BRANCH}/${HOME.source}` : false,
      ...(HOME.source ? { head: [markdownAlternate(writeMarkdown(HOME.source, "/"))] } : {}),
      ...levelsOf(`${BASE}/`),
    },
    prepare(body),
  );
}

/** A page per PAGES entry, from its file's title down; each is returned as llms.txt lists it. */
function writePages() {
  return PAGES.map((extra) => {
    const { title, body } = takeTitle(repoFile(extra.source));
    const description = describe(body);
    const markdown = writeMarkdown(extra.source, `/${extra.slug}/`);
    page(
      resolve(CONTENT, `${extra.slug}.md`),
      {
        title: title ?? extra.label,
        ...(description ? { description } : {}),
        ktlSource: extra.source,
        editUrl: `${REPO_URL}/edit/${BRANCH}/${extra.source}`,
        head: [markdownAlternate(markdown)],
        ...levelsOf(`${BASE}/${extra.slug}/`),
      },
      prepare(body),
    );
    // llms.txt names the page by its label, which says what the page is for.
    return { title: extra.label, description, markdown: SITE + markdown };
  });
}

/** The summary under the title: the repository's own llms.txt line when it has one. */
function llmsSummary() {
  const llms = existsSync(resolve(REPO_ROOT, "llms.txt")) ? repoFile("llms.txt") : "";
  return (llms.match(/^> (.+)$/m) ?? [, DESCRIPTION])[1];
}

// The bundle's licence, as a sentence for the two text files, or nothing.
function licenceSentence(root) {
  if (!root.license) return "";
  const { text, href } = licenceOf(root.license);
  return ` The bundle is offered under ${text}${href ? ` (${href})` : ""}.`;
}

function writeLlmsTxt(docs, extra, concepts, root) {
  const summary = llmsSummary();
  const inputs = [
    ...(HOME.source ? [HOME.source === "README.md" ? "its README" : `its ${HOME.source}`] : []),
    ...(docs.length ? [`its ${DOCS.dir}/ pages`] : []),
    "its LOKF knowledge bundle",
  ];
  const from = inputs.length > 1 ? `${inputs.slice(0, -1).join(", ")} and ${inputs[inputs.length - 1]}` : inputs[0];
  const pages = [...docs, ...extra];
  const lines = [
    `# ${TITLE}`,
    "",
    `> ${summary}`,
    "",
    `This site is built from ${REPO_URL}: ${from}. Each page below links its own Markdown file: a docs page's text with its links made full addresses, and a concept's file as it is in the repository, followed by the label that says how far it has been checked. A concept marked \`status: draft\` has not yet been confirmed by a person; one with a \`human:\` entry under \`verified\` has. Weigh them accordingly.${licenceSentence(root)}`,
    "",
    ...(pages.length
      ? ["## Docs", "", ...pages.map((d) => `- [${d.title}](${d.markdown})${d.description ? `: ${d.description}` : ""}`), ""]
      : []),
    "## Knowledge bundle",
    "",
    ...[...concepts]
      .sort((a, b) => a.id.localeCompare(b.id))
      .map((c) => `- [${c.title}](${SITE_URL}/knowledge/${c.id}.md): ${String(c.data.description ?? "")} (${c.label})`),
    "",
    "## Optional",
    "",
    `- [The bundle in full](${SITE_URL}/llms-full.txt): every concept's text in one file, each after its label`,
    `- [concepts.jsonld](${SITE_URL}/knowledge/concepts.jsonld): every concept's frontmatter and body under one JSON-LD context`,
    `- [graph.nt](${SITE_URL}/knowledge/graph.nt): the whole bundle as N-Triples`,
    ...(SCHEMA ? [`- [Schema](${SITE_URL}/schema/): the LinkML schema's classes, slots, enumerations and types, a page each`] : []),
    ...(BROWSE ? [`- [Browse the data](${SITE_URL}/browse/): the repository's data as SQLite databases`] : []),
    `- [${HOME.source === "README.md" ? "README" : "Home"}](${SITE_URL}/${HOME.source ? "index.md" : ""}): what ${TITLE} is`,
    "",
  ];
  write(resolve(PUBLIC, "llms.txt"), lines.join("\n"));
}

/**
 * A link written in the file at `fromPath`, as an address that works
 * anywhere, for text read away from its page: a link to a heading goes to
 * that heading on `page`.
 */
function absoluteUrl(fromPath, page, url) {
  if (url.startsWith("#")) return page + url;
  const out = rewriteUrl(fromPath, url);
  return /^\/(?!\/)/.test(out) ? SITE + out : out;
}

// A Markdown link's address: bare, or in angle brackets, with a title or
// none; the brackets and the title are kept.
const MD_LINK = /\]\((<[^>]*>|[^)\s]+)((?:\s+"[^"]*")?)\)/g;
// A src, srcset or href attribute in raw HTML, quoted either way.
const HTML_ATTR = /\b(src|srcset|href)=("([^"]*)"|'([^']*)')/g;

/**
 * Markdown written in the file at `fromPath` and shown at `page`, as text
 * read away from the site: every link, image and raw-HTML address becomes a
 * full one, and in a concept the wikilinks too, since the text has no
 * address of its own to resolve them against. Fenced code is left as written.
 */
function absoluteMarkdown(fromPath, page, text, selfId = null, ids = []) {
  return mapProse(text, (line) => {
    const out = line
      .replace(MD_LINK, (_, url, title) => {
        const bare = url.startsWith("<") ? url.slice(1, -1) : url;
        const abs = absoluteUrl(fromPath, page, bare);
        return `](${url.startsWith("<") ? `<${abs}>` : abs}${title})`;
      })
      .replace(HTML_ATTR, (_, attr, _q, dq, sq) => {
        const value = dq ?? sq;
        const each = (u) => absoluteUrl(fromPath, page, u);
        const abs =
          attr === "srcset"
            ? value
                .split(",")
                .map((part) => {
                  const [u, ...rest] = part.trim().split(/\s+/);
                  return [each(u), ...rest].join(" ");
                })
                .join(", ")
            : each(value);
        return `${attr}="${abs}"`;
      });
    if (selfId === null) return out;
    return out.replace(WIKILINK, (_, name, heading = "", alias) => {
      const id = resolveWikilink(name, selfId, ids);
      const text = alias ?? name.trim();
      return id ? `[${text}](${SITE_URL}/knowledge/${id}/${heading})` : text;
    });
  });
}

/**
 * The whole bundle in one file, for a model that reads it at once: each
 * concept's text after its label, its type, its addresses and its sources.
 * Its headings move under its title and its links become absolute, the
 * wikilinks too, since the file has no address of its own to resolve them
 * against.
 */
function writeLlmsFullTxt(concepts, root) {
  const ids = concepts.map((c) => c.id);
  const entry = (c) => {
    const levels = [];
    mapProse(c.body, (line) => {
      const m = line.match(/^(#{1,6}) /);
      if (m) levels.push(m[1].length);
      return line;
    });
    const shift = levels.length ? 3 - Math.min(...levels) : 0;
    const from = `.lokf/knowledge/${c.id}.md`;
    const page = `${SITE_URL}/knowledge/${c.id}/`;
    const shifted = mapProse(c.body, (line) => line.replace(/^(#{1,6}) /, (_, h) => "#".repeat(Math.min(6, h.length + shift)) + " "));
    const body = absoluteMarkdown(from, page, shifted, c.id, ids);
    const sources = c.record.sources.map((s) => `[${s.text}](${s.href})`);
    return [
      `## ${c.title}`,
      "",
      `- Label: ${c.label}`,
      `- Type: ${c.record.typeName}`,
      `- Address: ${c.iri}`,
      `- Page: ${page}`,
      `- Markdown: ${SITE_URL}/knowledge/${c.id}.md`,
      ...(sources.length ? [`- Sources: ${sources.join(", ")}`] : []),
      ...(c.data.license ? [`- Licence: ${licenceMd(c.data.license)}`] : []),
      ...(c.data.definition ? [`- Definition: ${plain(String(c.data.definition))}`] : []),
      "",
      body.trim(),
    ].join("\n");
  };
  const lines = [
    `# ${TITLE}: the knowledge bundle in full`,
    "",
    `> ${llmsSummary()}`,
    "",
    `Every concept in the knowledge bundle of ${REPO_URL}, as the site at ${SITE_URL}/ shows it. Each one opens with its label, which says how far it has been checked. Only a label that starts "confirmed by a person" means that a named person has confirmed the text as it stands. Weigh the rest accordingly.${licenceSentence(root)}`,
    "",
    ...[...concepts].sort((a, b) => a.id.localeCompare(b.id)).map((c) => entry(c) + "\n"),
  ];
  write(resolve(PUBLIC, "llms-full.txt"), lines.join("\n"));
}

// What makes an SVG a page that runs code when it is opened on its own.
const ACTIVE_SVG = /<script|<foreignObject|\son[a-z]+\s*=|javascript:/i;

/**
 * Copy a file or folder of the repository into the site. A link is followed
 * only when it ends inside the repository, and the copy holds the file, not
 * the link: a link that left the repository would publish a file of the
 * runner's, since the build copies what a link points at. An SVG that holds
 * a script, an event handler or a javascript: address is left out too, since
 * the site serves it as a page of its own.
 */
function copyFromRepository(from, to) {
  const root = realpathSync(REPO_ROOT) + sep;
  cpSync(from, to, {
    recursive: true,
    dereference: true,
    filter: (src) => {
      let real;
      try { real = realpathSync(src); } catch { real = ""; }
      if (!real || !(real + sep === root || real.startsWith(root))) {
        console.warn(`sync: left out ${relative(REPO_ROOT, src)}, a link to something outside the repository`);
        return false;
      }
      if (/\.svg$/i.test(real) && statSync(real).isFile() && ACTIVE_SVG.test(readFileSync(real, "latin1"))) {
        console.warn(`sync: left out ${relative(REPO_ROOT, src)}, an SVG that holds a script, an event handler or a javascript: address`);
        return false;
      }
      return true;
    },
  });
}

/** Every file of the bundle as it is in the repository, so `<concept>.md` sits beside its page. */
function copyBundleFiles() {
  const walk = (dir) => {
    for (const name of readdirSync(dir)) {
      if (name.startsWith(".")) continue;
      const full = resolve(dir, name);
      if (statSync(full).isDirectory()) walk(full);
      else if (name.endsWith(".md")) {
        const dest = resolve(PUBLIC_KNOWLEDGE, relative(BUNDLE_DIR, full));
        mkdirSync(dirname(dest), { recursive: true });
        copyFromRepository(full, dest);
      }
    }
  };
  walk(BUNDLE_DIR);
}

/**
 * The releases collection for src/content.config.ts: a page per release from
 * the sync's copy of the changelog, kept out of search, where dozens of
 * versions would bury every other page; or an empty object when the site
 * shows no changelog, so that nothing imports the plugin's loader.
 */
function writeCollections() {
  const lines = CHANGELOG
    ? [
        "// Written by scripts/sync.mjs before each build: the releases collection, since site.config.mjs shows a changelog.",
        'import { defineCollection } from "astro:content";',
        'import { changelogsLoader } from "starlight-changelogs/loader";',
        "",
        "export const changelogs = {",
        "  changelogs: defineCollection({",
        "    loader: changelogsLoader([",
        '      { provider: "keep-a-changelog", base: "changelog", changelog: "src/generated/CHANGELOG.md", title: "Releases", pagefind: false },',
        "    ]),",
        "  }),",
        "};",
      ]
    : [
        "// Written by scripts/sync.mjs before each build: no releases collection, since site.config.mjs shows no changelog.",
        "export const changelogs = {};",
      ];
  write(resolve(GENERATED, "changelogs.ts"), lines.join("\n") + "\n");
}

/** The repository's tags, as git has them; none without git. */
function gitTags() {
  try {
    const out = execFileSync("git", ["-C", REPO_ROOT, "tag", "--list"], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] });
    return new Set(out.split("\n").filter(Boolean));
  } catch {
    return new Set();
  }
}

/**
 * The releases section's copy of the changelog. Its version headings lose
 * their brackets, so each release page is titled with the bare version and
 * starlight-changelogs skips `## Unreleased`, which it knows only unbracketed.
 * Its links to repository files point at their pages, since a release page
 * has no source file for the Markdown plugin to resolve them from. Under the
 * heading of a release whose tag git has, a line links the repository, the
 * docs and the bundle at that tag, and the release itself, so a reader can
 * see each as it stood. A release promoted but not yet tagged, or a tag not
 * yet fetched, gets no line.
 */
function writeChangelog() {
  const tags = RELEASE_TAG ? gitTags() : new Set();
  const frozen = (version) => {
    const tag = RELEASE_TAG.replace("{version}", version);
    if (!tags.has(tag)) return [];
    const at = `${REPO_URL}/tree/${tag}`;
    const links = [
      `[the repository](${at})`,
      ...(DOCS ? [`[the docs](${at}/${DOCS.dir})`] : []),
      `[the knowledge bundle](${at}/.lokf/knowledge)`,
      `[the release](${REPO_URL}/releases/tag/${tag})`,
    ];
    return ["", `*As it stood at this release:* ${links.join(" · ")}`];
  };
  const text = mapProse(repoFile(CHANGELOG), (line) => {
    const out = line
      .replace(/^## \[([^\]]+)\]/, "## $1")
      .replace(/\]\(([^)\s]+)\)/g, (_, url) => `](${rewriteUrl("CHANGELOG.md", url)})`);
    const release = line.match(/^## \[([^\]]+)\] - \d{4}-\d{2}-\d{2}/);
    return release ? [out, ...frozen(release[1])] : out;
  });
  write(resolve(GENERATED, "CHANGELOG.md"), text);
}

function copyAssets() {
  if (ASSETS) copyFromRepository(resolve(REPO_ROOT, ASSETS), resolve(PUBLIC, "assets"));
  mkdirSync(GENERATED, { recursive: true });
  mkdirSync(PUBLIC, { recursive: true });
  if (LOGO) {
    copyFromRepository(resolve(REPO_ROOT, LOGO.light), resolve(GENERATED, LOGO_FILES.light));
    copyFromRepository(resolve(REPO_ROOT, LOGO.dark), resolve(GENERATED, LOGO_FILES.dark));
  }
  // The favicon: the one the logo gives, or the site's own ladder mark.
  if (LOGO?.favicon) copyFromRepository(resolve(REPO_ROOT, LOGO.favicon), resolve(PUBLIC, `favicon${extname(LOGO.favicon)}`));
  else cpSync(resolve(SITE_DIR, "src", "assets", "favicon.svg"), resolve(PUBLIC, "favicon.svg"));
  if (CUSTOM_DOMAIN) write(resolve(PUBLIC, "CNAME"), `${CUSTOM_DOMAIN}\n`);
  // Where a domain host's workspace is served, for the graph page, or null.
  // The workspace itself arrives after the build, from the federation
  // workflow, so the page names it and fetches it when a reader asks.
  write(resolve(GENERATED, "workspace.json"), JSON.stringify(workspaceLinks()) + "\n");
}

// ---------------------------------------------------------------------------
// The schema's pages and the data, which the repository's own commands build.
// ---------------------------------------------------------------------------

/**
 * Runs the command that builds a part's folder when the folder is not built:
 * in CI every time, since a checkout has none, and locally only the first
 * time, so after a change a person runs the same command again. It runs from
 * the repository's root through the shell, as a person would type it, and
 * its output goes to the build's log.
 */
function buildFolder(name, part, isBuilt) {
  if (!part || isBuilt(part.dir)) return;
  if (!part.build) throw new Error(`site.config.mjs ${name} names ${part.dir}, which is not built, and no command to build it`);
  console.log(`sync: building ${part.dir} with \`${part.build}\``);
  const run = spawnSync(part.build, { cwd: REPO_ROOT, shell: true, stdio: "inherit" });
  if (run.error) throw run.error;
  if (run.status !== 0) throw new Error(`\`${part.build}\`, which builds ${part.dir} for site.config.mjs ${name}, exited with ${run.status}`);
  if (!isBuilt(part.dir)) {
    throw new Error(`\`${part.build}\` ran, but ${part.dir} is still not built; set site.config.mjs ${name}.dir to the folder it writes`);
  }
}

/**
 * A gen-doc page as Markdown the site renders. mkdocs-material's
 * frontmatter and its search wrapper are removed. A blank line goes after
 * each line that opens a <details> or holds its <summary>, and before each
 * that closes it, so the YAML inside is a code block, not raw HTML. The
 * mermaid diagrams stay as written: the Markdown plugin leaves them for the
 * browser to draw, and their links, such as ../Action/, resolve because each
 * page's address keeps its element's name.
 */
function fromGenDoc(text) {
  let wrapped = false;
  const body = mapProse(splitFrontmatter(text).body, (line) => {
    if (/^<div data-search-exclude markdown="1">\s*$/.test(line)) {
      wrapped = true;
      return null;
    }
    if (/^<details( open)?>\s*$|^<summary>.*<\/summary>\s*$/.test(line)) return [line, ""];
    if (/^<\/details>/.test(line)) return ["", line];
    return line;
  });
  if (!wrapped) return body;
  // The wrapper's closing tag is the last </div> outside fenced code.
  const lines = body.split("\n");
  const inCode = [];
  let fence = null;
  for (const line of lines) {
    const m = line.match(/^\s*(`{3,}|~{3,})/);
    inCode.push(fence !== null || m !== null);
    if (fence) {
      if (m && m[1][0] === fence[0] && m[1].length >= fence.length) fence = null;
    } else if (m) fence = m[1];
  }
  const last = lines.findLastIndex((line, i) => !inCode[i] && line.includes("</div>"));
  if (last >= 0) {
    const at = lines[last].lastIndexOf("</div>");
    lines[last] = lines[last].slice(0, at) + lines[last].slice(at + "</div>".length);
  }
  return lines.join("\n");
}

/** gen-doc's description of an element, the italic paragraph under its title, as plain words. */
function genDocDescription(body) {
  const para = body
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .find(Boolean);
  return para && /^_[\s\S]+_$/.test(para) ? describe(para) : undefined;
}

function writeSchemaPages() {
  if (!SCHEMA) return 0;
  const index = `${SCHEMA.dir}/index.md`;
  const overview = takeTitle(fromGenDoc(repoFile(index)));
  const summary = describe(overview.body);
  page(
    resolve(CONTENT, "schema", "index.md"),
    {
      title: overview.title ?? "Schema",
      ...(summary ? { description: summary } : {}),
      slug: "schema",
      // The schema's hundreds of pages would outnumber the bundle's in search.
      pagefind: false,
      ktlSource: index,
      editUrl: false,
      sidebar: { label: "Overview" },
    },
    overview.body,
  );
  const pages = schemaPages();
  for (const p of pages) {
    const { title, body } = takeTitle(fromGenDoc(repoFile(p.file)));
    const description = genDocDescription(body);
    page(
      resolve(CONTENT, "schema", `${p.name}.md`),
      {
        title: title ?? p.label,
        ...(description ? { description } : {}),
        slug: `schema/${p.name}`,
        pagefind: false,
        ktlSource: p.file,
        editUrl: false,
        sidebar: { label: p.label },
      },
      body,
    );
  }
  return pages.length;
}

// Datasette Lite runs Datasette in the reader's browser, from a database at
// any address that allows cross-origin requests, as GitHub Pages does. Each
// link turns its analytics off, so the reader's visit is not logged there.
const DATASETTE_LITE = "https://lite.datasette.io/";

const fileSize = (bytes) => (bytes >= 1e6 ? `${(bytes / 1e6).toFixed(1)} MB` : `${Math.max(1, Math.round(bytes / 1e3))} kB`);

/**
 * Datasette metadata without its plugins' settings, at the top, for each
 * database and for each table: Datasette Lite runs no plugin, and a plugin's
 * settings can hold a credential that must not reach a public site.
 */
function withoutPlugins(metadata) {
  const drop = (part) => {
    if (part === null || typeof part !== "object" || Array.isArray(part)) return part;
    const { plugins, ...rest } = part;
    return rest;
  };
  const each = (map, fn) =>
    map !== null && typeof map === "object" && !Array.isArray(map) ? Object.fromEntries(Object.entries(map).map(([k, v]) => [k, fn(v)])) : map;
  const top = drop(metadata);
  if (top === null || typeof top !== "object" || !("databases" in top)) return top;
  return {
    ...top,
    databases: each(top.databases, (database) => {
      const db = drop(database);
      return db !== null && typeof db === "object" && "tables" in db ? { ...db, tables: each(db.tables, drop) } : db;
    }),
  };
}

/**
 * The data: each database in BROWSE's folder, served under /browse/ with its
 * Datasette metadata, and a page that opens each in Datasette Lite.
 * config.mjs's browseFiles says which files those are. The rest of the
 * folder is never copied. The metadata is published as metadata.json, which
 * Datasette reads as readily as YAML, without its plugins' settings.
 */
function writeBrowse() {
  if (!BROWSE) return [];
  const dir = resolve(REPO_ROOT, BROWSE.dir);
  const { databases, metadata: metadataFile } = browseFiles();
  mkdirSync(resolve(PUBLIC, "browse"), { recursive: true });
  for (const { file } of databases) copyFromRepository(resolve(dir, file), resolve(PUBLIC, "browse", file));
  let metadata = null;
  if (metadataFile) {
    // JSON is YAML, so one parser reads either form.
    try {
      metadata = parseYaml(read(resolve(dir, metadataFile))) ?? {};
    } catch (error) {
      throw new Error(`${BROWSE.dir}/${metadataFile} is neither YAML nor JSON: ${error.message}`);
    }
    write(resolve(PUBLIC, "browse", "metadata.json"), `${JSON.stringify(withoutPlugins(metadata))}\n`);
  }
  const sections = databases.map(({ file, name }) => {
    const about = metadata?.databases?.[name] ?? {};
    const query = new URLSearchParams({ url: `${SITE_URL}/browse/${file}` });
    if (metadata) query.set("metadata", `${SITE_URL}/browse/metadata.json`);
    query.set("analytics", "off");
    const size = fileSize(statSync(resolve(dir, file)).size);
    const lite = `${DATASETTE_LITE}?${query}#/${encodeURIComponent(name)}`.replaceAll("&", "&amp;");
    return [
      `## ${about.title ? plain(String(about.title)) : name}`,
      ...(about.description ? [plain(String(about.description))] : []),
      `<p class="ktl-browse not-content"><a class="ktl-button ktl-button--primary" href="${lite}" target="_blank" rel="noopener">Open in Datasette Lite</a> <a class="ktl-button" href="${BASE}/browse/${file}" download>Download ${file}</a> <span class="ktl-browse__size">${size}</span></p>`,
    ].join("\n\n");
  });
  const count = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][databases.length] ?? databases.length;
  const which = `${count} SQLite database${databases.length === 1 ? "" : "s"}`;
  const intro = [
    `This site serves the repository's data as ${which}${BROWSE.build ? `, built by \`${BROWSE.build}\`` : ""}.`,
    `[Datasette Lite](https://github.com/simonw/datasette-lite) opens each one in your browser, where you can filter its tables, follow their links and run SQL.`,
    `It downloads Datasette and the whole database first, so the first page takes a while to appear.`,
  ].join(" ");
  page(
    resolve(CONTENT, "browse.md"),
    {
      title: "Browse the data",
      description: `The repository's data as ${which}, to open in Datasette Lite or download.`,
      editUrl: false,
    },
    [intro, ...sections].join("\n\n"),
  );
  return databases;
}

// ---------------------------------------------------------------------------

for (const dir of [CONTENT, GENERATED, PUBLIC]) {
  if (!dir.startsWith(SITE_DIR + "/")) throw new Error(`refusing to clear ${dir}`);
  rmSync(dir, { recursive: true, force: true });
}

if (!existsSync(resolve(BUNDLE_DIR, "index.md"))) throw new Error(`no bundle at ${BUNDLE_DIR}`);
// First, since a concept may cite one of the schema's pages.
buildFolder("SCHEMA", SCHEMA, (dir) => existsSync(resolve(REPO_ROOT, dir, "index.md")));
buildFolder("BROWSE", BROWSE, () => browseFiles().databases.length > 0);
const exported = lokfExport();
const labels = readLabels();
const health = report("health");
const full = report();
const { concepts, root } = buildConcepts(exported, labels);
readingLevels = findReadingLevels(concepts);

copyAssets();
copyBundleFiles();
const byGroup = writeConceptPages(concepts);
writeGroupPages(byGroup);
writePreviews(concepts);
writeOverview(root, concepts, health);
writeLog();
await writeLogFeed(root);
writeHealth(concepts, health, full);
const docs = writeDocs();
writeHome();
const extra = writePages();
const schemaCount = writeSchemaPages();
const databases = writeBrowse();
writeLlmsTxt(docs, extra, concepts, root);
writeLlmsFullTxt(concepts, root);
writeCollections();
if (CHANGELOG) writeChangelog();

console.log(
  `sync: ${concepts.length} concept pages, ${byGroup.size} groups, ${docs.length} docs pages, ` +
    (SCHEMA ? `${schemaCount} schema pages, ` : "") +
    (BROWSE ? `${databases.length} databases, ` : "") +
    `${labels.size} labels, built from ${REF.slice(0, 12)}`,
);
