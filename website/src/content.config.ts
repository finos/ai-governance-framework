import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { docsLoader } from "@astrojs/starlight/loaders";
import { docsSchema } from "@astrojs/starlight/schema";
// The releases collection, or nothing: scripts/sync.mjs writes the file,
// since the changelogs loader reads a module the plugin provides only when
// site.config.mjs shows a changelog, and a bundler resolves even an import
// that never runs.
import { changelogs } from "./generated/changelogs";

// scripts/sync.mjs writes every page under src/content/docs/. The extra keys
// say which repository file a page was rendered from and whether it has a
// mermaid diagram to draw. They also hold the reading levels of a page that
// has a retelling (the page's own level has no link), and what a concept
// page shows above its body.
const tone = z.enum(["person", "edited", "automation", "nobody", "retired"]);
// A link to a concept carries its tone, which the neighbourhood map colours.
const link = z.object({ text: z.string(), href: z.string(), tone: tone.optional() });

const concept = z.object({
  id: z.string(),
  iri: z.string(),
  type: z.string(),
  // The type as words, as the cards show it.
  typeName: z.string(),
  // The Diátaxis genre, which the card shows beside the type.
  genre: z.string().optional(),
  group: z.string(),
  status: z.string().optional(),
  label: z.string(),
  tone,
  definition: z.string().optional(),
  reviewBy: z.string().optional(),
  tags: z.array(z.string()).default([]),
  generated: z.object({ by: z.string(), at: z.string() }).optional(),
  verified: z.array(z.object({ by: z.string(), at: z.string(), note: z.string().optional() })).default([]),
  // The open questions under the concept's `## Open questions` heading, shown
  // on the card beside a reopened label.
  questions: z.array(z.object({ date: z.string(), by: z.string(), text: z.string() })).default([]),
  sources: z.array(link).default([]),
  relations: z.array(z.object({ name: z.string(), targets: z.array(link) })).default([]),
  incoming: z.array(z.object({ name: z.string(), from: link })).default([]),
  licence: z.object({ text: z.string(), href: z.string().optional() }).optional(),
  graph: z.string(),
  files: z.object({ markdown: z.string(), jsonld: z.string(), github: z.string(), history: z.string() }),
});

export const collections = {
  ...changelogs,
  docs: defineCollection({
    loader: docsLoader(),
    schema: docsSchema({
      extend: z.object({
        ktlSource: z.string().optional(),
        ktlShiftHeadings: z.boolean().optional(),
        ktlMermaid: z.boolean().optional(),
        ktlLevels: z.array(z.object({ label: z.string(), href: z.string().optional() })).optional(),
        lokf: concept.optional(),
      }),
    }),
  }),
};
