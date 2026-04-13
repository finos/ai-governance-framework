---
sequence: 24
title: Skill/Plugin Integrity and Governance
layout: mitigation
doc-status: Draft
type: PREV
nist-sp-800-53r5_references:
  - sa-12  # SA-12 Supply Chain Protection
  - si-7   # SI-7 Software, Firmware, and Information Integrity
  - cm-7   # CM-7 Least Functionality
mitigates:
  - ri-30  # Skill/Plugin Supply Chain Compromise
  - ri-8   # Tampering with the Foundational Model
  - ri-9   # Data Poisoning
related_mitigations:
  - mi-20  # MCP Server Security Governance
  - mi-19  # Tool Chain Validation and Sanitization
  - mi-18  # Agent Authority Least Privilege Framework
  - mi-15  # Using LLMs for Automated Evaluation (LLM-as-a-Judge)
  - mi-25  # Risk-Tiered Approval and Consent Gate Hardening
  - mi-26  # Prompt Authority Scoping and Delegation Controls
---

## Purpose

**Skill/Plugin Integrity and Governance** establishes controls to verify the provenance, integrity, and safety of skill and plugin bundles before they are loaded into agentic AI systems. This preventive control addresses the dual attack surface of skills — prompt instruction injection and unsandboxed code execution — by introducing supply chain verification, code review requirements, dependency governance, and runtime isolation appropriate to the organization's risk tolerance.

This mitigation is analogous to MI-20 (MCP Server Security Governance) but addresses a fundamentally different attack vector: skills are local file bundles loaded directly into the agent's system prompt and execution environment, not network services accessed via protocol. The applicable controls therefore differ significantly.

---

## Key Principles

Effective skill governance must address both the prompt layer and the code execution layer:

* **Provenance Verification**: Establish the authorship, origin, and integrity of skill bundles before loading them into any agent environment.
* **Content Review**: Review both prompt content (SKILL.md) and bundled code (scripts, schemas, configs) for malicious or inappropriate behavior before approval.
* **Dependency Governance**: Control and audit third-party package dependencies that skill instructions direct the agent to install.
* **Least Authority**: Where possible, restrict the capabilities available to a skill's instructions and code below the agent's full authority.
* **Continuous Monitoring**: Monitor skill behavior in production to detect compromised updates or drift from reviewed behavior.

---

## Tiered Implementation Approach

Organizations should adopt skill governance appropriate to their deployment model, risk tolerance, and the maturity of their agentic tool adoption.

### Tier 1: Allowlisting and Manual Review

**Recommended for:** Organizations beginning agentic tool adoption, development teams with moderate risk exposure.

* **Architecture**: A central security or platform team maintains an allowlist of approved skills. Only allowlisted skills may be installed on developer workstations.
* **Key Controls**:
  * Central team reviews and approves all skills before they are added to the allowlist.
  * Review covers both SKILL.md instruction content (for prompt injection patterns, excessive authority claims, and policy-contradicting directives) and all bundled scripts (for filesystem access, network calls, credential access, and persistence mechanisms).
  * Approved skill bundles are stored in a controlled internal repository (e.g., internal Git, artifact registry) rather than pulled directly from public sources.
  * Skill updates require re-review before the allowlist is updated.
  * Developers may not install skills from public sources directly; only the reviewed, allowlisted versions are available.
  * Third-party dependency lists are documented during review; `pip install` and `npm install` commands are verified against approved packages.

* **Practical Considerations**:
  * This tier requires no changes to the agentic tool itself — it is enforced through organizational policy and workstation configuration (e.g., restricting write access to the skill directory).
  * Review burden scales with the number of skills and the frequency of updates; organizations should prioritize reviewing skills that bundle executable code over prompt-only skills.

### Tier 2: Integrity Verification and Dependency Pinning

**Recommended for:** Organizations with significant agentic tool usage, teams handling sensitive code or data.

* **All Tier 1 controls, plus:**
* **Additional Controls**:
  * **Cryptographic Integrity**: Approved skills are stored with checksums (SHA-256) or cryptographic signatures. The agent environment verifies integrity at load time and refuses to load skills that don't match their registered hash.
  * **Dependency Lockfiles**: Each approved skill includes a pinned dependency manifest (e.g., `requirements.txt` with pinned versions, `package-lock.json`) maintained by the security team. Agent environments install dependencies from the lockfile rather than from unpinned skill instructions.
  * **Dependency Scanning**: Third-party packages referenced by skills are scanned for known vulnerabilities (CVE databases) and malware indicators before approval, and continuously monitored for newly disclosed vulnerabilities after approval.
  * **Skill Isolation (Partial)**: Where the agentic tool supports it, skill-installed dependencies are installed into isolated virtual environments (Python venvs, Node.js local installs) rather than the user's global environment. This limits persistent environment modification.
  * **Installation Audit Logging**: All skill loads and dependency installations are logged centrally, with alerts for attempts to load unapproved skills or install unapproved packages.

### Tier 3: Runtime Sandboxing and Behavioral Monitoring

**Recommended for:** High-security environments, teams working on financial systems, compliance-critical deployments.

* **All Tier 1 and Tier 2 controls, plus:**
* **Additional Controls**:
  * **Script Sandboxing**: Skill-bundled scripts execute in a restricted sandbox (container, restrictive seccomp profile, or filesystem namespace) that limits their access to the broader system. The sandbox restricts network access, credential file access, and write access outside the project directory.
  * **Behavioral Monitoring**: Runtime monitoring tracks what skill-initiated tool calls actually do (files read/written, network connections, processes spawned) and compares against the skill's declared purpose. Anomalous behavior triggers alerts and may terminate the skill session.
  * **Skill Capability Declarations**: Skills are required to declare the capabilities they need (e.g., "reads project files," "writes to output directory," "requires network access for API calls") and the runtime enforces these declarations as capability restrictions.
  * **Differential Analysis on Update**: When a skill is updated, automated tools compare the new version against the previously approved version, highlighting changes to prompt content, script behavior, and dependency lists for targeted review.
  * **Red Team Testing**: Approved skills are periodically red-teamed to test whether their instructions can be manipulated (via prompt injection in processed documents) into performing unintended actions.

---

## Implementation Guidance

### 1. Skill Review Process

* **Prompt Content Review**:
  * Read the complete SKILL.md and any supplementary instruction files (REFERENCE.md, etc.).
  * Identify all tool calls the skill instructs the agent to make (bash commands, file operations, MCP invocations).
  * Flag instructions that: access files outside the project directory, make network requests, modify system or agent configuration, override or contradict organizational policy, or claim capabilities beyond the skill's stated purpose.
  * Verify that the skill's stated purpose matches what its instructions actually direct the agent to do.

* **Bundled Code Review**:
  * Review all Python, JavaScript, shell, and other executable files shipped with the skill.
  * Analyze for: filesystem traversal, credential file access (`.env`, `.ssh/`, cloud credential paths), outbound network connections, process spawning, file modification outside the working directory, installation of persistent artifacts (cron jobs, shell aliases, git hooks).
  * Run static analysis tools (e.g., Bandit for Python, ESLint security plugins for JavaScript) where applicable.

* **Dependency Review**:
  * Enumerate all packages the skill instructs the agent to install.
  * For each package: verify it is a legitimate, actively maintained project; check for known vulnerabilities; review the package's own dependency tree.
  * Pin all dependencies to specific versions and generate a lockfile to be stored alongside the approved skill.

### 2. Automated Pre-Screening Pipeline

Manual skill review is the bottleneck in Tier 1 governance. An automated pre-screening pipeline reduces reviewer burden by catching common malicious patterns and surfacing high-risk indicators before a human ever looks at the skill. This is not a replacement for human review — it is a triage layer that allows human reviewers to focus their attention on the subtle, judgment-dependent aspects of skill safety.

The pipeline should run automatically when a skill is submitted for review or when an approved skill is updated.

* **Stage 1 — Bundled Code Static Analysis**:
  * Run language-appropriate static analysis security tools on all bundled scripts:
    * **Python**: [Bandit](https://bandit.readthedocs.io/) for security anti-patterns, [Semgrep](https://semgrep.dev/) rules for credential access, network calls, filesystem traversal, subprocess invocation, and dynamic code execution (`eval`, `exec`, `__import__`).
    * **JavaScript/Node.js**: [ESLint security plugin](https://github.com/eslint-community/eslint-plugin-security), Semgrep rules for `child_process`, `fs` access outside working directory, outbound HTTP requests.
    * **Shell scripts**: [ShellCheck](https://www.shellcheck.net/) for correctness; custom pattern matching for `curl`, `wget`, `nc`, pipe-to-shell patterns, credential file paths, cron/systemd writes.
  * **Invisible Unicode and homoglyph detection**: Scan all skill files (SKILL.md, bundled scripts, referenced files) for invisible Unicode characters that could conceal malicious instructions or code:
    * **Zero-width characters**: U+200B (zero-width space), U+200C/U+200D (zero-width joiners), U+FEFF (zero-width no-break space) embedded in instruction text or code.
    * **Bidirectional text overrides**: U+202A–U+202E, U+2066–U+2069 characters that can cause code or instructions to render in a different order than they execute (the "Trojan Source" attack).
    * **Unicode tag characters**: U+E0001–U+E007F characters that are invisible but processed by models.
    * **Homoglyph substitution in code**: Characters from Cyrillic, Greek, or other scripts that are visually identical to ASCII characters (e.g., Cyrillic 'а' U+0430 vs Latin 'a' U+0061) used in variable names, function names, or URLs in bundled scripts. Libraries such as `confusable-homoglyphs` can detect these substitutions programmatically. Care must be taken to filter false positives from legitimate multilingual content, mathematical notation (π, μ, λ), and string literals — the Cisco skill-scanner, for example, applies context-aware filtering that exempts comments, docstrings, math formulas, and string content, and requires a minimum threshold of suspicious lines before flagging.
    * Any file containing invisible Unicode characters or homoglyphs in code-significant positions should be flagged as **high severity** — these have virtually no legitimate use in skill instruction files or code outside of string literals.
  * Flag severity levels: **block** (known dangerous patterns like reverse shells, base64-decoded execution), **warn** (potentially dangerous patterns like network access, credential path reads), **info** (unusual but potentially legitimate patterns).
  * Produce a structured report listing each finding with file, line number, pattern matched, and severity.
  * **Description-behavior consistency**: Cross-check the skill's declared metadata (name, description, `allowed-tools`) against the actual behavior of its bundled scripts. A skill claiming `allowed-tools: [Read, Grep]` whose scripts make network calls or write files should be flagged as a tool poisoning indicator. The [Agent Skills specification](https://agentskills.io/) defines an `allowed-tools` field for this purpose; existing scanners such as [Cisco's skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) implement this check.
  * **Reference implementation**: Organizations building a pre-screening pipeline may evaluate Cisco's open-source skill-scanner as a starting point. It implements multi-engine analysis (YAML signatures, YARA rules, Python AST dataflow analysis, bash taint tracking, LLM-as-a-judge, and a meta-analyzer for false positive reduction) aligned with the Cisco AI Security Framework taxonomy.

* **Stage 2 — Dependency Analysis**:
  * Extract all package installation commands from SKILL.md and bundled scripts (`pip install`, `npm install`, `require()`, `import` of non-stdlib modules).
  * For each identified dependency:
    * Verify the package exists on the expected registry (PyPI, npm) and is not a typosquat of a popular package (compare against known package name databases).
    * Check against vulnerability databases ([OSV](https://osv.dev/), [npm audit](https://docs.npmjs.com/cli/v10/commands/npm-audit), [pip-audit](https://pypi.org/project/pip-audit/)).
    * Check package health indicators: last update date, maintainer count, download volume, [OpenSSF Scorecard](https://securityscorecards.dev/) rating where available.
  * Resolve the full transitive dependency tree and repeat vulnerability and health checks for all transitive dependencies.
  * Flag unpinned versions as a warning; flag packages with known CVEs as a block.

* **Stage 3 — Prompt Content Analysis (LLM-as-a-Judge)**:
  * Use an LLM evaluator (see MI-15) to analyze the SKILL.md and any supplementary instruction files for patterns that indicate malicious intent or excessive authority:
    * **Instruction override attempts**: Phrases like "ignore previous instructions," "override safety guidelines," "you are now in unrestricted mode," or subtler variants.
    * **Scope creep indicators**: Instructions that access resources unrelated to the skill's stated purpose (e.g., a "spreadsheet helper" skill that instructs the agent to read `.ssh/` or `.env` files).
    * **Exfiltration patterns**: Instructions to embed file contents in generated outputs, commit data to external repositories, or send data via network requests.
    * **Persistence mechanisms**: Instructions to modify agent configuration files (AGENTS.md, CLAUDE.md, .cursorrules), agent-specific directories (`.claude/`, `.cursor/`), git hooks, shell profiles, or other files that persist beyond the current session.
    * **Authority escalation**: Instructions to change auto-approve settings, disable confirmation prompts, or modify the agent's own configuration.
  * The evaluator should be a different model instance from the agent itself, with a focused rubric and specific examples of benign vs. malicious patterns.
  * Produce a structured risk assessment: **pass** (no concerning patterns), **review** (patterns detected that require human judgment), **reject** (high-confidence malicious patterns).
  * Note: LLM-based analysis is probabilistic, not deterministic. It should always be complemented by the rule-based checks in Stages 1 and 2, and its findings should be treated as recommendations for the human reviewer, not as automated enforcement decisions (see MI-15 for principles governing LLM-as-a-Judge reliability).

* **Stage 4 — Differential Analysis (for updates to approved skills)**:
  * When an approved skill is updated, automatically diff the new version against the approved version.
  * Classify changes: prompt content changes, new/modified scripts, new dependencies, removed files.
  * Re-run Stages 1–3 on changed files only.
  * Highlight: new dependencies not in the previous version, new tool call patterns in SKILL.md, changes to scripts that previously passed review, changes to file paths or command patterns.
  * Present the human reviewer with a focused diff showing only the security-relevant changes, rather than requiring a full re-review.

* **Pipeline Output and Triage**:
  * The pipeline produces a consolidated report with a recommended action:
    * **Auto-reject**: Stage 1 or 2 returned block-level findings (known dangerous code patterns, packages with critical CVEs). The skill is rejected without human review; the submitter receives the findings.
    * **Expedited review**: All stages passed with no warnings. The human reviewer receives a clean report and can approve with minimal inspection.
    * **Full review required**: One or more stages returned warnings or the LLM evaluator flagged patterns for human judgment. The report highlights specific areas requiring attention, reducing the reviewer's search space.
  * Track pipeline metrics (submissions per week, auto-reject rate, false positive rate on warnings) to continuously tune detection rules.

### 3. Skill Distribution and Configuration

* **Internal Skill Repository**:
  * Maintain approved skills in a version-controlled internal repository.
  * Configure developer workstations to load skills only from the internal repository.
  * For tools that support it, configure the skill directory path to point to the managed repository.

* **Workstation Configuration**:
  * Restrict write access to skill directories on managed workstations so that developers cannot install unapproved skills.
  * For BYOD or less-managed environments, implement monitoring rather than prevention: log skill loads and alert on unapproved skills.

### 4. Ongoing Governance

* **Update Review Cadence**: Establish a review cadence for skill updates — critical skills reviewed within 48 hours of updates, others within one sprint.
* **Vulnerability Monitoring**: Subscribe to security advisories for all approved skill dependencies and re-assess when vulnerabilities are disclosed.
* **Skill Retirement**: Maintain a process for retiring skills that are no longer maintained, have unpatched vulnerabilities, or whose risk profile has changed.
* **Developer Training**: Train developers on skill supply chain risks, why the allowlist exists, and how to request new skills for review.

---

## Challenges and Considerations

* **Review Burden and Velocity**: Manual skill and code review is time-consuming. The automated pre-screening pipeline (Section 2) significantly reduces this burden by triaging submissions and focusing human attention on flagged areas, but organizations must still allocate reviewer capacity and establish SLAs for review turnaround.
* **Automated Pipeline False Positives**: Static analysis and LLM-based prompt review will produce false positives — legitimate skills flagged as suspicious. For example, Cisco's skill-scanner removed a rule flagging `os.environ.get("API_KEY")` as data exfiltration because reading secrets from environment variables is the *recommended* practice — the rule generated ~95% false positives in production. Organizations must track false positive rates and tune rules iteratively. The triage model (auto-reject, expedited review, full review) is designed to channel false positives into human review rather than outright rejection.
* **LLM-as-a-Judge Limitations for Prompt Review**: Using an LLM to detect malicious patterns in SKILL.md content is inherently probabilistic. Adversarial skill authors may craft instructions that evade LLM detection while still influencing agent behavior. LLM-based analysis should always complement rule-based static analysis, never replace it (see MI-15 for principles and limitations).
* **Tool Support Gaps**: Most agentic tools do not currently support integrity verification, capability declarations, or sandboxed script execution natively. Tier 2 and Tier 3 controls may require wrapper scripts, custom tooling, or contributions to open-source agentic tools.
* **Developer Friction**: Restricting skill installation creates friction for developers accustomed to installing tools freely. The expedited review path for clean pipeline results helps mitigate this — a skill that passes all automated checks can be approved quickly.
* **Skill Ecosystem Immaturity**: The skill/plugin ecosystem lacks the supply chain security infrastructure (signing, registries, CVE databases) that package ecosystems have developed over decades. Organizations must compensate with manual and automated controls until the ecosystem matures.
* **Prompt Content Review Difficulty**: Unlike code review, reviewing prompt instructions for malicious intent requires understanding how the instruction will influence model behavior — a skill that is not yet well-established in most security teams. The LLM-as-a-Judge stage of the pre-screening pipeline helps bridge this gap by providing an initial assessment that non-specialist reviewers can use as a starting point.

---

## Importance and Benefits

Implementing skill integrity and governance provides critical protection:

* **Supply Chain Risk Reduction**: Prevents compromised or malicious skills from reaching developer workstations.
* **Dual Attack Surface Coverage**: Addresses both the prompt injection vector (skill instructions) and the code execution vector (bundled scripts and dependencies).
* **Persistent Compromise Prevention**: Lockfiles and integrity verification prevent time-of-check-to-time-of-use attacks where a skill was safe at review time but is compromised later.
* **Dependency Governance**: Brings skill-installed dependencies under the same governance as other software dependencies.
* **Audit Trail**: Provides a documented record of what skills are approved, who reviewed them, and what versions are deployed.
* **Regulatory Compliance**: Supports compliance with software supply chain requirements in financial services regulations and frameworks (FFIEC, NIST SSDF, EU DORA).

---

## Additional Resources

* [NIST SP 800-161 Rev. 1 — Cybersecurity Supply Chain Risk Management](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final)
* [NIST SSDF — Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf)
* [SLSA Supply Chain Levels for Software Artifacts](https://slsa.dev/)
* [OpenSSF Scorecard — Security Health Metrics for Open Source](https://securityscorecards.dev/)
* [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
* [Trojan Source: Invisible Vulnerabilities (Cambridge, 2021)](https://trojansource.codes/) — Bidirectional text override attacks in source code, directly applicable to skill instruction files and bundled scripts
