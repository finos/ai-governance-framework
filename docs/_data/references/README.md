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

## Layouts

Files may organise entries in one of two layouts. Do not mix both in the same file.

### Flat (ungrouped)

Use when entries do not divide naturally into sections, or when the file is short enough that grouping adds no value. Structure is implicit in key naming.

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

### Grouped

Use when entries divide naturally into chapters, sections, tiers, or domains. Each group has a required `title`, an optional `description`, and its own `entries` map.

```yaml
title: "EU AI Act"
description: "Regulation (EU) 2024/1689 establishing harmonised rules on artificial intelligence."
source_url: "https://artificialintelligenceact.eu/ai-act-explorer/"

groups:
  - id: chapter-i
    title: "Chapter I: General Provisions"
    description: "Subject matter, scope, definitions, and AI literacy obligations."
    entries:
      c1-a1:
        title: "I.A1 Subject Matter"
        url: "https://artificialintelligenceact.eu/article/1/"
      c1-a2:
        title: "I.A2 Scope"
        url: "https://artificialintelligenceact.eu/article/2/"

  - id: chapter-ii
    title: "Chapter II: Prohibited AI Practices"
    entries:
      c2-a5:
        title: "II.A5 Prohibited AI Practices"
        url: "https://artificialintelligenceact.eu/article/5/"
```

Group fields:

| Field | Required | Description |
|-------|----------|-------------|
| `id` | No | Machine-readable identifier for the group (kebab-case) |
| `title` | Yes | Human-readable group name |
| `description` | No | Brief description of what this group covers |
| `entries` | Yes | Map of entries belonging to this group |

---

## Choosing flat vs. grouped

- Use **flat** for short, self-explanatory lists (OWASP Top 10, NIST AI 600-1) or where key prefixes already make structure clear (NIST SP 800-53 control families).
- Use **grouped** for large regulations with explicit chapter/section/tier structure (EU AI Act, Canada regulations) or where tier/domain boundaries carry meaning for readers.

---

## Current files

| File | Title | Layout | Notes |
|------|-------|--------|-------|
| `eu-ai-act.yml` | EU AI Act | flat | Groups implicit in key naming (`c1-`, `c2-`, etc.) |
| `nist-ai-600-1.yml` | NIST AI 600-1 | flat | |
| `nist-sp-800-53r5.yml` | NIST SP 800-53 Rev 5 | flat | Control families implicit in key prefix (`ac-`, `si-`, etc.) |
| `iso-42001.yml` | ISO/IEC 42001 | flat | |
| `owasp-llm.yml` | OWASP LLM Top 10 | flat | |
| `owasp-ml.yml` | OWASP ML Security Top 10 | flat | |
| `sr11-7.yml` | SR 11-7 Model Risk Management | flat | Sections marked by comments only |
| `ffiec-itbooklets.yml` | FFIEC IT Booklets | flat | Booklet grouping via `booklet_abbrev` field on each entry |
| `canada-regulations.yml` | Canada AI & Financial-Sector Regulations | flat | Tiers expressed via comments; entries have `issuer` and `description` |

---

## Notes on entry keys

- Keys must be **stable** — they are referenced by mapping files, so renaming is a breaking change.
- Use lowercase and hyphens (`kebab-case`).
- Where a regulation has an official numbering scheme (article numbers, control IDs), use that as the basis for the key.
