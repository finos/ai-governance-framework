// Which raw HTML in repository Markdown the site passes through, held to
// what GitHub's own README rendering allows. The Markdown parser gives raw
// HTML a fragment at a time, an opening tag in one and its closing tag in
// another, so each fragment is read tag by tag. A tag GitHub allows keeps the
// attributes it allows and loses the rest, as on GitHub, and an address
// that is not http, https, mailto, a path or a fragment is dropped. A
// fragment with any other tag, or markup that is not one plain tag, is
// shown as text. Concept bodies come from a scheduled agent and are
// reviewed in a pull request. This check keeps a script that got past review
// off the site.

const TAGS = new Set([
  "a", "abbr", "b", "bdi", "bdo", "blockquote", "br", "caption", "center", "cite", "code", "col", "colgroup",
  "dd", "del", "details", "dfn", "div", "dl", "dt", "em", "figcaption", "figure",
  "h1", "h2", "h3", "h4", "h5", "h6", "hr", "i", "img", "ins", "kbd", "li", "mark", "ol", "p", "picture",
  "pre", "q", "rp", "rt", "ruby", "s", "samp", "small", "source", "span", "strike", "strong", "sub", "summary",
  "sup", "table", "tbody", "td", "tfoot", "th", "thead", "time", "tr", "tt", "u", "ul", "var", "wbr",
]);
const ATTRIBUTES = new Set([
  "abbr", "align", "alt", "border", "cite", "class", "colspan", "datetime", "dir", "headers", "height", "href",
  "hreflang", "id", "lang", "loading", "media", "name", "open", "rel", "reversed", "rowspan", "scope", "sizes",
  "span", "src", "srcset", "start", "summary", "target", "title", "type", "valign", "width",
]);
const ADDRESSES = new Set(["href", "src", "srcset", "cite"]);
const TAG = /^<(\/?)([a-zA-Z][a-zA-Z0-9-]*)((?:\s+[a-zA-Z][a-zA-Z0-9-]*(?:\s*=\s*(?:"[^"]*"|'[^']*'))?)*)\s*(\/?)>/;
const ATTRIBUTE = /([a-zA-Z][a-zA-Z0-9-]*)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'))?/g;

/** Whether an address is one a page may carry: http, https or mailto, a fragment, or a path. */
function safeAddress(value) {
  // A character reference can spell a scheme a browser reads, so any but
  // &amp; makes the address refused rather than decoded here.
  if (/&(?!amp;)/i.test(value)) return false;
  const v = value.replace(/&amp;/gi, "&").trim();
  const scheme = /^([a-zA-Z][a-zA-Z0-9+.-]*):/.exec(v);
  return !scheme || ["http", "https", "mailto"].includes(scheme[1].toLowerCase());
}

/**
 * The fragment as the site passes it, with what was dropped, or `html: null`
 * and the reason when it is shown as text instead.
 */
export function cleanRawHtml(fragment) {
  const out = [];
  const dropped = [];
  let rest = fragment;
  while (rest.length) {
    const lt = rest.indexOf("<");
    if (lt === -1) {
      out.push(rest);
      break;
    }
    out.push(rest.slice(0, lt));
    rest = rest.slice(lt);
    if (rest.startsWith("<!--")) {
      const end = rest.indexOf("-->", 4);
      if (end === -1) return { html: null, reason: "a comment that does not close" };
      out.push(rest.slice(0, end + 3));
      rest = rest.slice(end + 3);
      continue;
    }
    const m = TAG.exec(rest);
    if (!m) return { html: null, reason: `markup that is not one plain tag: ${rest.slice(0, 40)}` };
    const [whole, close, rawName, attrs, selfClosing] = m;
    const name = rawName.toLowerCase();
    if (!TAGS.has(name)) return { html: null, reason: `the tag <${name}>` };
    if (close) {
      out.push(`</${name}>`);
    } else {
      const kept = [];
      for (const a of attrs.matchAll(ATTRIBUTE)) {
        const attr = a[1].toLowerCase();
        const value = a[2] ?? a[3];
        const parts = attr === "srcset" ? (value ?? "").split(",").map((p) => p.trim().split(/\s+/)[0]) : [value ?? ""];
        if (!ATTRIBUTES.has(attr) || (ADDRESSES.has(attr) && !parts.every(safeAddress))) {
          dropped.push(`${attr} on <${name}>`);
          continue;
        }
        kept.push(value === undefined ? ` ${attr}` : ` ${attr}="${value.replace(/"/g, "&quot;")}"`);
      }
      out.push(`<${name}${kept.join("")}${selfClosing ? " /" : ""}>`);
    }
    rest = rest.slice(whole.length);
  }
  return { html: out.join(""), dropped };
}
