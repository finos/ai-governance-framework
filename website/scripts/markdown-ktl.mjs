// A plugin for Sätteri, Astro's Markdown processor, that renders repository
// Markdown on the site. A page the sync wrote names its source file in the
// `ktlSource` frontmatter key, and for such a page the plugin:
//   - points each relative link, image and raw-HTML src/href at the page or
//     file it names (scripts/routes.mjs);
//   - turns an Obsidian [[wikilink]] in a concept into a link to that concept;
//   - moves every heading down one level when `ktlShiftHeadings` is set,
//     since a concept's body starts its sections at `#` and the page title is
//     already the one h1;
//   - leaves a ```mermaid block's source in a pre.ktl-mermaid, out of the
//     code highlighter's reach, for src/components/Mermaid.astro to draw.
//     It does so only on a page the sync marked `ktlMermaid`, since only
//     those pages load that script. On any other page the block stays code.
// On every page, raw HTML passes only as GitHub would render it
// (scripts/raw-html.mjs): a tag GitHub allows keeps the attributes it
// allows, and any other markup is shown as text.
import { BASE } from "./config.mjs";
import { cleanRawHtml } from "./raw-html.mjs";
import { rewriteHtml, rewriteUrl } from "./routes.mjs";

// Both are shared with the sync, which resolves a concept's wikilinks the
// same way where it writes the bundle in full.
export const WIKILINK = /\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]+))?\]\]/g;
const escapeHtml = (text) => text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

/** The one concept a wikilink names, by its whole path or its last segment, or null. */
export function resolveWikilink(name, selfId, ids) {
  const want = name.trim().replace(/\.md$/, "");
  const hits = ids.filter((id) => id !== selfId && (id === want || id.endsWith("/" + want)));
  return hits.length === 1 ? hits[0] : null;
}

/** Put a raw HTML node through cleanRawHtml, saying in the build's log what it dropped or showed as text. */
export function cleanHtmlNode(node, ctx, where, value = node.value) {
  const clean = cleanRawHtml(value);
  if (clean.html === null) {
    console.warn(`markdown: ${where}: raw HTML shown as text, since it holds ${clean.reason}`);
    ctx.replaceNode(node, { type: "html", value: escapeHtml(node.value) });
    return;
  }
  for (const d of clean.dropped) console.warn(`markdown: ${where}: dropped ${d}`);
  if (clean.html !== node.value) ctx.setProperty(node, "value", clean.html);
}

/** The plugin factory: called once per document. A page the sync did not write gets the raw HTML check alone. */
export default function markdownKtl({ conceptIds = [] } = {}) {
  return ({ data }) => {
    const fm = data?.astro?.frontmatter ?? {};
    const source = fm.ktlSource;
    if (!source) return { name: "ktl-raw-html", html: (node, ctx) => cleanHtmlNode(node, ctx, "a page of the site") };
    const selfId = source.startsWith(".lokf/knowledge/")
      ? source.slice(".lokf/knowledge/".length).replace(/\.md$/, "")
      : null;
    const relink = (node, ctx) => {
      const url = rewriteUrl(source, node.url);
      if (url !== node.url) ctx.setProperty(node, "url", url);
    };
    return {
      name: "ktl-repository-markdown",
      link: relink,
      image: relink,
      definition: relink,
      html(node, ctx) {
        cleanHtmlNode(node, ctx, source, rewriteHtml(source, node.value));
      },
      heading(node, ctx) {
        if (fm.ktlShiftHeadings) ctx.setProperty(node, "depth", Math.min(6, node.depth + 1));
      },
      code(node, ctx) {
        if (fm.ktlMermaid && node.lang === "mermaid") ctx.replaceNode(node, { type: "html", value: `<pre class="ktl-mermaid">${escapeHtml(node.value)}</pre>` });
      },
      text(node, ctx) {
        if (selfId === null || !node.value.includes("[[")) return;
        const parts = [];
        let last = 0;
        for (const m of node.value.matchAll(WIKILINK)) {
          const [whole, name, heading = "", alias] = m;
          if (m.index > last) parts.push({ type: "text", value: node.value.slice(last, m.index) });
          const id = resolveWikilink(name, selfId, conceptIds);
          const text = alias ?? name.trim();
          parts.push(
            id
              ? { type: "link", url: `${BASE}/knowledge/${id}/${heading}`, children: [{ type: "text", value: text }] }
              : { type: "text", value: text },
          );
          last = m.index + whole.length;
        }
        if (parts.length === 0) return;
        if (last < node.value.length) parts.push({ type: "text", value: node.value.slice(last) });
        ctx.replaceNode(node, parts);
      },
    };
  };
}
