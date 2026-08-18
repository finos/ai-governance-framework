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
| `superseded_by` | No | Key of the entry (in the same file) that replaces this one in a newer edition of the framework |

---

## Layout

All entries are nested under a top-level `entries:` mapping. Each key is a stable identifier; values follow the entry fields above.

```yaml
title: "OWASP LLM Top 10"
description: "The top ten security risks for LLM-based applications, published by OWASP."
source_url: "https://genai.owasp.org/"

entries:
  llm01-2026:
    title: "LLM01:2026 Prompt Injection"
    url: "https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/final/LLM01_PromptInjection.md"

  llm02-2026:
    title: "LLM02:2026 Sensitive Information Disclosure"
    url: "https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/final/LLM02_SensitiveInformationDisclosure.md"
    description: "Risks of exposing sensitive data through LLM outputs."
```

Where a regulation has natural sections or tiers, these are expressed as `# comments` between entries rather than as structural grouping.


---

## Notes on entry keys

- Keys must be **stable** — they are referenced by mapping files, so renaming or deleting is a breaking change.
- Use lowercase and hyphens (`kebab-case`).
- Where a regulation has an official numbering scheme (article numbers, control IDs), use that as the basis for the key.

## New editions of a framework

When a framework publishes a new edition (e.g. the OWASP LLM Top 10 2025 → 2026), do **not** rename or delete the old keys:

1. Add the new edition's entries under new keys (year-suffixed keys such as `llm01-2026` make this natural).
2. Keep the old edition's entries and mark each one with `superseded_by`, pointing at its successor in the new edition.
3. Update risk/mitigation front matter mappings to the new keys.

Old keys stay resolvable for anything that consumes these files externally, and entries with no mappings are simply not rendered on the reference pages.
