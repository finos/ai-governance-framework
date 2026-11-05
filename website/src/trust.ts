// The five states a concept's trust label can name, top of the ladder first,
// in the words the health page, its chart and the search filter use. The
// sync's TONE_ORDER keeps the same order.
export const TRUST_STATES = [
  { tone: "person", label: "Confirmed by a person" },
  { tone: "edited", label: "Edited since a person confirmed it" },
  { tone: "automation", label: "Checked by automation only" },
  { tone: "nobody", label: "Nobody has checked" },
  { tone: "retired", label: "Retired" },
] as const;

export type Tone = (typeof TRUST_STATES)[number]["tone"];

export const trustLabel = (tone: Tone) => TRUST_STATES.find((s) => s.tone === tone)?.label ?? tone;
