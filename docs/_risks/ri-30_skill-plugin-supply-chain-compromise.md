---
sequence: 30
title: Skill/Plugin Supply Chain Compromise
layout: risk
doc-status: Draft
type: SEC
owasp-llm_references:
  - llm03-2025  # LLM03:2025 Supply Chain
  - llm06-2025  # LLM06:2025 Excessive Agency
related_risks:
  - ri-8   # Tampering with the Foundational Model
  - ri-9   # Data Poisoning
  - ri-10  # Prompt Injection
  - ri-25  # Tool Chain Manipulation and Injection
  - ri-26  # MCP Server Supply Chain Compromise
  - ri-29  # Agent-Mediated Credential Discovery and Harvesting
---

## Summary

Agentic coding tools and AI assistants increasingly support community-authored "skills" or "plugins" — bundles of prompt instructions and executable code that extend agent capabilities. When loaded, skill prompt content is injected directly into the agent's system prompt with full instruction-level authority, while bundled scripts execute unsandboxed on the user's machine. A compromised or malicious skill therefore gains both the ability to steer the agent's reasoning and tool selection (prompt layer) and to execute arbitrary code with the user's full local privileges (code layer). Unlike MCP server compromise (RI-26), skills operate without network-level security controls, protocol authentication, or service isolation — they are local files treated as trusted instructions.

## Description

**Skill/Plugin Supply Chain Compromise** targets the growing ecosystem of community-authored, shareable agent extensions used in tools such as Claude Code, Cursor, Windsurf, and similar agentic development environments. These systems allow users to install "skills" — typically a markdown instruction file (e.g. SKILL.md) bundled with helper scripts (Python, shell, etc.), templates, schemas, and configuration files — that extend the agent's capabilities for specific tasks like document generation, code analysis, or deployment workflows.

The fundamental security challenge is that skills present a **dual attack surface** that combines two distinct compromise vectors in a single installable package:

### Deceptive Metadata and Tool Poisoning

A skill's externally visible metadata — its name, description, and declared capabilities — may deliberately misrepresent what the skill actually does. A skill named `safe-code-analyzer` with a description of "read-only static analysis" and an `allowed-tools: [Read, Grep, Glob]` declaration may bundle scripts that write files, make network requests, or access credentials. This deceptive metadata serves two purposes: it passes superficial review by human and automated screeners, and it socially engineers the user into trusting the skill (see also RI-31 on approval fatigue). Existing skill scanning tools such as Cisco's skill-scanner classify this as "tool poisoning" — a form of supply chain attack where the deception is in the metadata layer rather than (or in addition to) the code layer.

### Layer 1: Prompt Injection via Skill Instructions

Skill instruction files (SKILL.md, REFERENCE.md, and similar) are read from the filesystem and injected directly into the agent's system prompt or context window. The foundation model cannot distinguish between its own system instructions and skill-injected content — both carry identical authority over the agent's reasoning, tool selection, and code generation patterns.

This means a malicious skill author can craft instructions that:

* Direct the agent to execute specific commands or access specific files while appearing to perform the skill's stated function
* Override or subvert safety guidelines and organizational policies present elsewhere in the system prompt
* Instruct the agent to exfiltrate data through seemingly legitimate tool calls (e.g., embedding sensitive content in API requests, commit messages, or generated files)
* Steer the agent to invoke other tools or MCP servers in ways that amplify the compromise

A particularly insidious variant uses **invisible Unicode characters** to conceal malicious instructions within otherwise benign-looking skill files. Zero-width characters (U+200B zero-width space, U+200C/U+200D zero-width joiners, U+FEFF zero-width no-break space), bidirectional text override characters (U+202A–U+202E, U+2066–U+2069), and Unicode tag characters (U+E0001–U+E007F) can embed instructions that are invisible when the file is viewed in a text editor or code review tool but are processed by the model when the file is loaded into the context window. Similarly, **Unicode homoglyph substitution** — replacing ASCII characters with visually identical characters from other scripts (e.g., Cyrillic 'а' for Latin 'a', Greek 'ο' for Latin 'o') — can disguise malicious variable names, function calls, or URLs in bundled scripts so they pass visual code review while executing differently than expected. These techniques are especially effective against human review because the files appear clean to visual inspection.

Unlike adversarial prompt injection (RI-10) where an attacker must smuggle malicious instructions through an input channel, skill instructions are loaded by design into the most privileged position in the prompt — the system context. The user explicitly triggers this loading, often without reviewing the full content of the skill files.

### Layer 2: Unsandboxed Code Execution via Bundled Scripts

Skills routinely bundle helper scripts that the skill instructions direct the agent to execute via shell commands (e.g., `python scripts/validate.py`, `python scripts/recalc.py`). In agentic coding environments, these scripts execute directly on the user's machine with the user's full shell permissions — no containerization, sandboxing, or code signing is applied.

A compromised skill can therefore ship trojanized scripts alongside innocuous-looking instruction files. The scripts may:

* Read and exfiltrate credentials, SSH keys, API tokens, `.env` files, and other secrets from the local filesystem
* Modify source code, configuration files, or build artifacts in the user's project
* Install persistent backdoors (cron jobs, shell aliases, git hooks, modified PATH entries)
* Establish reverse shells or outbound data channels
* Modify other skill files or the project's agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules) to propagate the compromise to future sessions (see RI-27)

### Supply Chain Distribution Vectors

* **Community Sharing and Social Engineering**
  Skills are shared via GitHub repositories, blog posts, social media, and community forums. Unlike package managers (npm, PyPI) there is typically no registry-level malware scanning, no publisher verification, and no download auditing. Social proof (stars, recommendations) can be manufactured.

* **Skill Update Poisoning**
  A previously legitimate skill repository may be compromised through account takeover, maintainer social engineering, or malicious pull requests — a pattern well-documented in traditional software supply chains but without the protective infrastructure (signing, reproducible builds, CVE databases) that package ecosystems have developed.

* **Dependency Confusion and Typosquatting**
  As skill ecosystems grow, naming collisions and typosquatting become viable attack vectors, particularly when skills are referenced by name rather than by cryptographic hash or verified publisher identity.

* **Enterprise Internal Skill Distribution**
  Organizations may maintain internal skill repositories where a compromised insider or a single compromised developer workstation can introduce malicious skills that propagate to all team members.

### Transitive Dependency Installation

Skills commonly bundle helper scripts that import third-party packages from public registries (PyPI, npm). Skill instruction files (SKILL.md) routinely direct the agent to install these dependencies via `pip install` or `npm install` commands before executing bundled scripts. This introduces a third layer to the attack surface beyond prompt instructions and bundled code:

* **Agent-Executed Package Installation**
  Skill instructions direct the agent to run commands like `pip install pypdf openpyxl pdfplumber` or `npm install -g docx pptxgenjs`. The agent generates these commands through the same unsandboxed shell execution path, and they are subject to the same approval fatigue dynamics as any other tool call (see RI-31). The user is unlikely to audit the transitive dependency tree of each package before approving the install command.

* **Transitive Dependency Compromise**
  A skill may be authored in good faith, with clean SKILL.md instructions and audited bundled scripts, yet still introduce compromised code through its third-party dependencies. Each `pip install` or `npm install` command pulls in not just the named package but its entire transitive dependency tree — potentially dozens of packages, any of which could be compromised through established supply chain attacks (dependency confusion, typosquatting, maintainer account takeover). This is the same category of risk documented in traditional software supply chain literature, but amplified by the fact that the installation is triggered by an AI agent following untrusted instructions, and occurs on the developer's own machine outside of any project-level lockfile or reproducible build environment.

* **Version Pinning Absence**
  Skill instructions typically specify package names without version pins (e.g., `pip install reportlab` rather than `pip install reportlab==4.1.0`). This means each skill invocation may install a different version of each dependency, and a package that was safe at skill authoring time may have been compromised since. There is no equivalent of a lockfile for skill dependencies.

* **Persistent Environment Modification**
  Unlike bundled scripts that are confined to the skill directory, `pip install` and `npm install -g` modify the user's global Python or Node.js environment. These installed packages persist after the skill session ends, potentially affecting other projects and workflows. A compromised package installed by a skill could execute malicious code in any future Python or Node.js process on the user's machine.

### Financial Services Exploitation Scenarios

* **Development Environment Credential Harvesting**
  A skill marketed for "secure code review" or "compliance checking" includes bundled scripts that systematically search the developer's machine for cloud credentials, database connection strings, and API keys used in financial system development.

* **Source Code Exfiltration**
  A popular "code documentation" skill's instructions direct the agent to read entire source files and embed their contents in generated documentation that is then committed to a repository visible to the attacker.

* **Build Pipeline Compromise**
  A "CI/CD helper" skill's bundled scripts modify build configurations, Dockerfiles, or deployment manifests to introduce backdoors into production financial systems.

* **Persistent Project Infection**
  A malicious skill writes instructions into the project's agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules) or agent-specific directories (.claude/, .cursor/), ensuring that the compromise persists across all future sessions and affects every developer who works in that repository.

### Key Differentiators from RI-26 (MCP Server Supply Chain Compromise)

While both risks involve supply chain compromise of agent-adjacent components, they differ fundamentally in attack surface and applicable controls:

| Dimension | MCP Servers (RI-26) | Skills/Plugins (RI-30) |
|-----------|---------------------|----------------------|
| Trust boundary | Network service with protocol-level isolation | Local files injected directly into system prompt |
| Communication | MCP protocol over TLS — inspectable, filterable | Filesystem read — no protocol to monitor |
| Authentication | Mutual auth, API keys, OAuth applicable | None — file presence implies trust |
| Code execution | Server-side, in provider's environment | Client-side, on user's machine, unsandboxed |
| Integrity verification | Checksums, signatures, SBOMs applicable | Typically none |
| Monitoring | Network traffic analysis, response validation | No established monitoring patterns |
| Blast radius | Limited by MCP server's capabilities and data access | Full agent authority + user's local shell privileges |

### Consequences

Skill/plugin supply chain compromise can result in severe consequences:

* **Full Local System Compromise**: Bundled scripts execute with user privileges, potentially compromising the entire development workstation and any systems accessible from it.
* **Credential and Secret Theft**: Systematic harvesting of credentials, API keys, and tokens stored on the developer's machine or accessible through their environment.
* **Source Code and IP Theft**: Exfiltration of proprietary source code, algorithms, or business logic through skill-directed agent behavior.
* **Persistent Compromise Propagation**: Infection of project agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules) and agent-specific directories (.claude/, .cursor/) that spread the compromise to other developers and future sessions.
* **Supply Chain Amplification**: Compromised development environments may produce compromised software artifacts that propagate to production systems and customers.
* **Regulatory and Compliance Violations**: Unauthorized data access and exfiltration may violate data protection regulations, financial services compliance requirements, and contractual obligations.

### Key Risk Factors

- **Absence of Skill Signing and Verification**: No cryptographic mechanism to verify skill authorship, integrity, or provenance — unlike package managers that support publisher signing and checksum verification.
- **No Skill Review Infrastructure**: No equivalent of security scanning, dependency analysis, or malware detection for skill bundles.
- **Prompt-Level Authority by Default**: Skill instructions inherit system-prompt authority with no mechanism to scope or restrict their influence on agent behavior.
- **Unsandboxed Script Execution**: Bundled scripts execute with full user privileges, with no containerization, capability restriction, or filesystem isolation.
- **User Trust Assumptions**: Users install skills based on described functionality without reviewing instruction files or auditing bundled code, particularly when skills are recommended by trusted community members.
- **No Auditability of Skill Behavior**: Lack of tooling to monitor what a skill's instructions actually cause the agent to do versus what the skill's documentation claims.
- **Uncontrolled Transitive Dependency Installation**: Skill instructions direct the agent to install third-party packages from public registries without version pinning, lockfiles, or dependency auditing, extending the supply chain attack surface beyond the skill bundle itself into the broader package ecosystem.

## Links

- [OWASP LLM03: Supply Chain](https://genai.owasp.org/llmrisk/llm03-supply-chain/)
- [OWASP LLM06: Excessive Agency](https://genai.owasp.org/llmrisk/llm06-excessive-agency/)
- [NIST Supply Chain Risk Management - SP 800-161](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final)
- [Backstabber's Knife Collection: A Review of Open Source Software Supply Chain Attacks](https://arxiv.org/abs/2005.09535)
- [Agent Skills Specification](https://agentskills.io/) — Emerging spec for skill metadata including capability declarations
- [Cisco AI Defense Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner) — Open-source multi-engine scanner detecting prompt injection, data exfiltration, tool poisoning, and supply chain threats in skill packages
