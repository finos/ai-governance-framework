// A social card for every page the sync wrote: its title in the book face,
// and for a concept its trust label, type, genre and ID beside an edge in
// its trust colour, theme.css's light chart steps. The fonts are read from
// the installed packages, relative to the site's folder, so the build
// fetches nothing.
import { OGImageRoute } from "astro-og-canvas";
import { CARD_PAGES } from "../../socialCards";
import { TITLE } from "../../../site.config.mjs";

type Rgb = [number, number, number];
const EDGE: Record<string, Rgb> = {
  person: [24, 95, 165],
  edited: [201, 154, 62],
  automation: [122, 78, 11],
  nobody: [171, 169, 160],
  retired: [171, 169, 160],
};
const GREEN: Rgb = [59, 109, 17];

// A description stays within three lines, ending on a whole word.
const clip = (text: string, max = 160) => {
  if (text.length <= max) return text;
  const cut = text.slice(0, max);
  return cut.slice(0, cut.lastIndexOf(" ")) + "…";
};

// The type, and the genre when it is not the type's own word.
const typeLine = ({ typeName, genre }: { typeName: string; genre?: string }) =>
  genre && genre.toLowerCase() !== typeName.toLowerCase() ? `${typeName} · ${genre}` : typeName;

export const { getStaticPaths, GET } = await OGImageRoute({
  param: "route",
  pages: CARD_PAGES,
  getImageOptions: (_path, page: (typeof CARD_PAGES)[string]) => ({
    title: page.title,
    description: page.lokf
      ? `${page.lokf.label.charAt(0).toUpperCase()}${page.lokf.label.slice(1)}\n${typeLine(page.lokf)}\n${page.lokf.id} · ${TITLE}`
      : `${clip(page.description ?? "")}\n${TITLE}`,
    bgGradient: [[253, 252, 250]],
    border: { color: page.lokf ? EDGE[page.lokf.tone] : GREEN, width: 24, side: "inline-start" },
    padding: 72,
    font: {
      title: { families: ["Source Serif 4"], color: [31, 30, 27], size: 68, weight: "SemiBold", lineHeight: 1.1 },
      description: { families: ["Atkinson Hyperlegible Next"], color: [80, 78, 72], size: 32, lineHeight: 1.4 },
    },
    fonts: [
      "./node_modules/@fontsource-variable/source-serif-4/files/source-serif-4-latin-wght-normal.woff2",
      "./node_modules/@fontsource-variable/atkinson-hyperlegible-next/files/atkinson-hyperlegible-next-latin-wght-normal.woff2",
    ],
  }),
});
