import { defineRouteMiddleware } from "@astrojs/starlight/route-data";
import { cardFor } from "./socialCards";
import { TITLE } from "../site.config.mjs";

export const onRequest = defineRouteMiddleware((context) => {
  const route = context.locals.starlightRoute;

  // On a concept page the top of the page is the concept's record, and its
  // body usually starts with its own "Overview", so the contents list names
  // the top "Record" rather than showing "Overview" twice.
  const first = route.toc?.items[0];
  if (route.entry.data.lokf && first) first.text = "Record";

  // A link preview shows the page's social card, or the home page's. Starlight
  // writes the other Open Graph tags.
  const card = cardFor(route.id);
  const base = import.meta.env.BASE_URL.replace(/\/$/, "");
  route.head.push(
    { tag: "meta", attrs: { property: "og:image", content: new URL(`${base}/og/${card}.png`, context.site).href } },
    { tag: "meta", attrs: { property: "og:image:width", content: "1200" } },
    { tag: "meta", attrs: { property: "og:image:height", content: "630" } },
    {
      tag: "meta",
      attrs: { property: "og:image:alt", content: card === "index" ? TITLE : route.entry.data.title },
    },
  );
});
