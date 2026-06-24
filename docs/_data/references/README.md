# Reference Data Schema

This directory contains YAML files defining external regulatory references and frameworks used throughout the AI Readiness assessment. They are consumed by templates and mapping files to render citations, links, and compliance cross-references.

---

## Standard Schema

### Top-level fields

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Full name of the regulation, framework, or standard |
| `description` | Yes | One or two sentence description of scope and purpose |
| `source_url` | No | URL this file was generated from, or a canonical index page |

### Entry fields

Entries are the individual citable items — articles, sections, controls, etc. They are represented as a YAML mapping where each **key is a stable identifier** used for cross-referencing in mapping files.

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Short, human-readable citation title |
| `url` | Yes | Canonical URL for this specific entry |
| `description` | No | Richer contextual description; not always rendered in UI |
| `issuer` | No | Issuing body (e.g. `OSFI`, `CSA`, `CIRO`) |

---

## Layout

All entries are nested under a top-level `entries:` mapping. Each key is a stable identifier; values follow the entry fields above.

```yaml
title: "OWASP LLM Top 10"
description: "The top ten security risks for LLM-based applications, published by OWASP."
source_url: "https://genai.owasp.org/"

entries:
  llm01-2025:
    title: "LLM01:2025 Prompt Injection"
    url: "https://genai.owasp.org/llmrisk/llm01-prompt-injection/"

  llm02-2025:
    title: "LLM02:2025 Sensitive Information Disclosure"
    url: "https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/"
    description: "Risks of exposing sensitive data through LLM outputs."
```

Where a regulation has natural sections or tiers, these are expressed as `# comments` between entries rather than as structural grouping.


---

## Notes on entry keys

- Keys must be **stable** — they are referenced by mapping files, so renaming is a breaking change.
- Use lowercase and hyphens (`kebab-case`).
- Where a regulation has an official numbering scheme (article numbers, control IDs), use that as the basis for the key.
