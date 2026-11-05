// Every page the sync wrote gets a social card at og/<its id>.png, which
// src/pages/og/[...route].ts draws. Any other page, a release or the graph,
// shares the home page's card, and so do the schema's pages, hundreds of
// them, under schema/. src/routeData.ts points each page at its card.
import { getCollection } from "astro:content";

const entries = (await getCollection("docs")).filter(({ id }) => id !== "schema" && !id.startsWith("schema/"));

/** The sync's pages, by the name their card is served under. */
export const CARD_PAGES = Object.fromEntries(entries.map(({ id, data }) => [id || "index", data]));

/** The card a page shares: its own, or the home page's. */
export const cardFor = (routeId: string) => (CARD_PAGES[routeId || "index"] ? routeId || "index" : "index");
