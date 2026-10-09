---
sequence: 18
title: Agent Authority Least Privilege Framework
layout: mitigation
doc-status: Approved-Specification
type: PREV
iso-42001_references:
  - A-9-2    # ISO 42001: Processes for responsible use of AI systems
  - A-6-2-6  # ISO 42001: AI system operation and monitoring
nist-sp-800-53r5_references:
  - ac-6  # AC-6 Least Privilege
  - ac-2  # AC-2 Account Management
  - ac-3  # AC-3 Access Enforcement
  - ac-5  # AC-5 Separation Of Duties
  - cm-7  # CM-7 Least Functionality
atr_references:
  - ATR-2026-00012  # Unauthorized Tool Call
  - ATR-2026-00040  # Agent Privilege Escalation
  - ATR-2026-00098  # Unauthorized Financial Action by Agent
mitigates:
  - ri-24  # Agent Action Authorization Bypass
  - ri-18  # Model Overreach / Expanded Use
related_mitigations:
  - mi-12  # Role-Based Access Control for AI Data
  - mi-3   # User/App/Model Firewalling/Filtering
  - mi-1   # AI Data Leakage Prevention and Detection
  - mi-19  # Tool Chain Validation and Sanitization
  - mi-20  # MCP Server Security Governance
  - mi-22  # Multi-Agent Isolation and Segmentation
iosco-supervisory-toolkit_references:
  - t3-5  # Table 3.5: Risk Management of Advanced AI Systems
  - t3-7  # Table 3.7: Controls and Human Oversight of AI Systems
---

## Purpose

The **Agent Authority Least Privilege Framework** implements granular access controls ensuring agents can only access APIs, tools, and data strictly necessary for their designated functions. This preventive control establishes dynamic privilege management, contextual access restrictions, and comprehensive authorization enforcement to prevent agents from exceeding their intended operational scope and causing unauthorized actions or regulatory violations.

This framework extends traditional least privilege principles to address the unique challenges of agentic AI systems, where agents make autonomous decisions about tool selection and API usage, requiring more sophisticated controls than static role-based access systems.

---

## Key Principles

Effective agent privilege management must address the dynamic and autonomous nature of agentic systems:

* **Granular API Access Control**: Agents should have access only to specific API endpoints and methods required for their designated use case, with restrictions enforced at the tool manager and API gateway levels. Agent identity and role must be included in all API invocations to enable authorization decisions.
* **Contextual Privilege Adjustment**: Agent privileges should dynamically adjust based on current context, risk level, transaction value, or customer sensitivity, ensuring appropriate controls for different scenarios.
* **Time-Bounded Privileges**: Agent access should be time-limited where appropriate, with privileges automatically expiring after task completion or specified time periods.
* **Separation of Duties Enforcement**: Multi-step processes requiring approval or verification should be enforced through agent privilege restrictions, preventing single agents from completing entire high-risk workflows.
* **Dynamic Privilege De-escalation**: Agent privileges should automatically reduce to minimum levels when not actively engaged in authorized tasks.
* **Business Logic Enforcement**: Access controls should enforce business rules, approval limits, and regulatory requirements at the privilege level, not just through application logic.

---

## Implementation Guidance

### 1. Agent Role and Privilege Definition

* **Role-Based Agent Classification** (examples):
  * **Customer Service Agents**: Read-only access to customer account information, limited transaction inquiry capabilities, no modification or transfer authorities.
  * **Risk Assessment Agents**: Access to risk calculation APIs and customer financial data for analysis purposes only, no decision execution capabilities.
  * **Compliance Agents**: Read-only access to transaction data and regulatory databases for compliance checking, no approval or modification authorities.
  * **Trading Agents**: Limited access to market data APIs and position management systems within defined risk parameters and position limits.
  * **Document Processing Agents**: Access to document analysis APIs and storage systems, no customer-facing or decision-making capabilities.

* **Privilege Matrices and Documentation**:
  * Maintain comprehensive matrices documenting exactly which APIs, endpoints, and data sources each agent type can access.
  * Document the business justification for each privilege grant and regularly review privilege assignments.
  * Implement version control for privilege definitions to track changes over time.

### 2. Dynamic Privilege Management

* **Context-Aware Access Controls**:
  * **Transaction Value Thresholds**: Restrict agent access to high-value transaction APIs based on configurable monetary limits.
  * **Customer Sensitivity Levels**: Implement additional access restrictions for VIP customers, high-net-worth individuals, or customers with privacy flags.
  * **Time-Based Restrictions**: Limit agent access to certain APIs during off-hours, weekends, or maintenance windows.
  * **Geographic Restrictions**: Restrict agent access based on customer location, regulatory jurisdiction, or data residency requirements.

* **Privilege Escalation Controls**:
  * Implement controlled privilege escalation mechanisms requiring human approval for agents needing temporary additional access.
  * Log and monitor all privilege escalation requests and approvals.
  * Automatic privilege de-escalation after specified time periods or task completion.

### 3. API and Tool Access Enforcement

* **Tool Manager Security Layer**:
  * A "tool manager" is the component that mediates between agents and APIs/tools that are external to the agent, translating agent requests into concrete API calls and managing the execution of those calls. This layer provides a critical enforcement point for authorization controls.
  * Implement comprehensive authorization checks at the tool manager level before any API calls are executed, validating the agent's identity and role against the requested operation.
  * Validate that requested API endpoints and parameters are within the agent's authorized scope.
  * Reject and log any attempts to access unauthorized tools or APIs, including the agent identity for audit purposes.

* **API Gateway Integration**:
  * Integrate agent identity and privilege information with API gateway systems.
  * Implement rate limiting and throttling based on agent type and privilege level.
  * Monitor API usage patterns to detect potential privilege abuse or compromise.

* **Parameter Validation and Sanitization**:
  * Validate that API parameters passed by agents conform to expected ranges, formats, and business rules.
  * Sanitize inputs to prevent parameter injection attacks.
  * Implement parameter whitelisting for high-risk APIs.

### 4. Business Logic and Approval Workflow Enforcement

* **Multi-Agent Approval Processes**:
  * For high-risk operations, require multiple agents of different types to participate in approval workflows.
  * Implement separation of duties by ensuring no single agent can complete end-to-end high-risk processes.
  * Require human approval for operations exceeding defined risk thresholds.

* **Regulatory Compliance Integration**:
  * Implement privilege restrictions that enforce regulatory requirements such as transaction limits, reporting thresholds, or approval requirements.
  * Integrate with compliance monitoring systems to ensure agent actions comply with regulatory frameworks.

* **Business Rule Enforcement**:
  * Encode business rules directly into privilege systems rather than relying solely on application logic.
  * Implement privilege-based controls for credit limits, trading limits, fee waivers, and other business constraints.

### 5. Monitoring and Auditing

* **Comprehensive Access Logging**:
  * Log all agent access attempts, successful operations, and authorization failures.
  * Include contextual information such as customer identifiers, transaction amounts, and business justification.
  * Implement centralized logging for cross-agent correlation and analysis.

* **Anomaly Detection**:
  * Monitor agent access patterns to detect unusual API usage, privilege escalation attempts, or deviation from normal behavior patterns.
  * Implement alerting for agents attempting to access unauthorized resources or exceeding normal usage patterns.
  * Use behavioral analytics to identify potentially compromised agents.

* **Regular Privilege Reviews**:
  * Conduct periodic reviews of agent privilege assignments to ensure they remain appropriate and necessary.
  * Remove or reduce privileges that are no longer required for agent functionality.
  * Review and update privilege matrices as business requirements change.

### 6. Integration with Existing Security Systems

* **Identity and Access Management (IAM)**:
  * Integrate agent privilege management with existing IAM systems and directory services.
  * Implement single sign-on (SSO) capabilities for agent authentication where appropriate.
  * Leverage existing role-based access control (RBAC) infrastructure where possible.

* **Security Information and Event Management (SIEM)**:
  * Feed agent access logs into SIEM systems for correlation with other security events.
  * Implement security alerts for suspicious agent behavior or privilege violations.
  * Enable security operations teams to investigate agent-related security incidents.

### 7. OS and Runtime-Layer Enforcement

An agent that can execute commands or reach a shell bypasses gateway and tool-manager controls, so enforce least privilege one layer down, in the operating system and runtime beneath the agent. Command allow-listing constrains what an agent can execute, not what it can disclose; pair it with egress controls and data-leakage prevention ([MI-1](/mitigations/mi-1_ai-data-leakage-prevention-and-detection.html)).

* **Enforcement Point Placement**:
  * Place the enforcement point (an execution broker or OS-level mandatory access control) beneath the agent, where it mediates every invocation and resists tampering. A policy held only in the agent's prompt is guidance, not enforcement.
  * Deny the agent process the ability to start programs directly, so the broker is the only path to process creation, and have the operating system enforce the executable allow-list independently of the broker, failing closed if the OS mechanism is unavailable.
  * Keep the broker small and memory-safe, with no shell inside it and a strict request schema, and launch each program with only the privileges, handles, and capabilities its entry grants. Security-review and penetration-test it.
  * Treat a tool gate as enforcement only if the agent cannot alter, restart, or bypass it; an MCP server the agent spawns or configures is advisory ([MI-20](/mitigations/mi-20_mcp-server-security-governance.html)).

* **Deny-by-Default Command Allow-Listing**:
  * Express each entry as an absolute executable path plus an argument schema, never a command-name pattern, and deny everything not named.
  * Execute allowed commands directly as a program plus argument list, never as a text line handed to a shell.
  * Do not allow-list interpreters or subprocess launchers. Denying flags such as `-c` or `-e` is not enough, because a runtime also takes code from files, standard input, module paths, environment variables, and configuration. Run these as sandboxed jobs instead.
  * Pin allowed executables by hash, or by a version verified against the opened file, on storage the agent cannot modify, and re-validate the allow-list whenever one changes; a new release can add options that launch other programs.
  * Resolve file paths before the authorization check, and ensure the object checked is the object used, so path traversal and symlink swaps cannot redirect a narrow grant.

* **Argument Schema and Injection Defenses**:
  * Classify every option and positional argument as fixed (a literal value), constrained (an enumerated set or strict pattern), or not permitted, and reject everything else, including alternate spellings the target's parser accepts.
  * Validate the complete argument vector against how the pinned program parses it (order, repetition, precedence, subcommands, encodings), with adversarial conformance tests per executable version. Individually valid arguments can combine into a forbidden command.
  * Validate argument values, not only their shape: bound file paths to an authorized root and network destinations to an authorized host list. `rm -rf ./build` and `rm -rf /` have the same shape.
  * Pass each value as exactly one argument element, never concatenated or split on whitespace. Insert the end-of-options marker (`--`) before untrusted values where the target supports it, otherwise reject values beginning with `-`. Reject control characters and NUL bytes, and cap argument length and count.
  * Exclude options that accept a program or script (`find -exec`, `tar --to-command`, `git -c core.pager=...`, `ssh -o ProxyCommand=...`) and indirection such as `@file` response files or options naming a configuration file, plugin, or hook. Tool-parameter sanitization is covered in [MI-19](/mitigations/mi-19_tool-chain-validation-and-sanitization.html).

* **Execution Environment**:
  * Build each command's environment from an allow-list rather than inheriting the agent's. Variables such as `PATH`, `LD_PRELOAD`, `PYTHONPATH`, and `GIT_SSH_COMMAND` change what code runs without changing the command line.
  * Keep the policy and any configuration that drives allowed commands (build files, package manifests, version-control hooks, CI configuration) outside the agent's writable set or pinned by content.
  * Run every invocation in a fixed working directory with resource limits, a timeout, no terminal, and standard input closed. Place it, before it starts, in a kernel-tracked group its descendants cannot leave, and terminate the group when a limit is reached.
  * Let an allowed program start a child directly only when the child is inert: its executable plus the sandbox, credentials, and configuration it inherits bound its authority. A child whose behavior depends on its own arguments, configuration, or destinations (a shell, `ssh`, a compiler) goes back through the broker.

* **Sandboxed Jobs**:
  * Run general-purpose runtimes, builds, tests, and model-written code as sandboxed jobs: short-lived, default-deny network, no credentials, resource limits, an immutable toolchain, and a pinned workspace snapshot as input. The boundary is governed, not each command inside it. See [MI-22](/mitigations/mi-22_multi-agent-isolation-and-segmentation.html).
  * Have a job produce a proposal, not an effect: its output (a diff, a test report) leaves as bounded, validated data, and applying it anywhere is a separate brokered action that can be reviewed or gated.

* **Deny and Persistence Logging**: Log every denied invocation with the agent's identity, and log agent writes to persistence locations (hooks, scheduled tasks, service definitions, CI configuration) as distinct high-signal events, so later out-of-session execution can be traced back.

#### Implementation Notes (Illustrative)

Illustrative, non-normative, accurate as of the cited versions; verify against your pinned kernel, runtime, and tool versions. Example tools are listed under Additional Resources.

* **Linux**:
  * Landlock can grant the execute right to individual files or directory trees. It authorizes the file object, not its contents, so keep allowed files non-writable. Query the Landlock ABI at runtime and fail closed if it is unavailable.
  * Apply Landlock and seccomp before the process creates threads, or use their thread-synchronization options; restrictions then pass to all descendants and cannot be removed.
  * A seccomp filter sees only raw system-call arguments, so it cannot safely inspect the path or argument strings passed to `execve`. Use it to allow only the system calls a process needs, and enforce executable and argument policy elsewhere.
  * `no_new_privs` stops executed programs from gaining privilege through setuid binaries or file capabilities. It does not drop privilege the process already holds; drop that separately.
  * fapolicyd trust checks compare content hashes only with the `sha256` or `ima` integrity setting, though explicit hash rules always do; fs-verity or IMA appraisal enforce content integrity at execution time.
  * Open the executable with `openat2` and the confinement flags you need (for example `RESOLVE_BENEATH` and `RESOLVE_NO_SYMLINKS`), then run that descriptor with `execveat(fd, "", ..., AT_EMPTY_PATH)`, so the object resolved is the object executed.
  * `noexec` on agent-writable mounts is friction, not a boundary: an allowed interpreter can still read and run a script there, and copying code into executable memory (for example `memfd_create` with `execveat`) bypasses it.
  * Track and terminate descendants with a cgroup; a process can leave its process group.
* **Windows**:
  * Use App Control for Business for the executable allow-list. The child-process creation policy is effective only for sandboxed processes such as AppContainer, and accessible process handles can bypass it; job-object process limits cap concurrency rather than allow-list.
  * Create each process suspended, assign it to a job that forbids breakaway, then resume it, so every descendant can be tracked and terminated.
  * A program receives one command-line string and parses it itself, so an argument list is safe only when serialized for that program's parser.
  * Batch files (`.bat`, `.cmd`) are interpreted by `cmd.exe`, whose quoting rules language runtimes have mishandled ([CVE-2024-24576](https://nvd.nist.gov/vuln/detail/CVE-2024-24576), then bypassed via trailing spaces and periods in [CVE-2024-43402](https://nvd.nist.gov/vuln/detail/CVE-2024-43402)). Normalize paths, then refuse batch-file targets.
* **macOS**:
  * Endpoint Security lets an entitled security client approve or deny each execution (`AUTH_EXEC` events), but the client must answer before each event's deadline, so design for availability and fail-safe behavior.
* **Argument parsing**:
  * Whether a program accepts abbreviated long options (`--out` for `--output`) or attached option values (`-ofile`) depends on the program and version, which is why schemas are tested against the pinned binary. Without a shell, wildcards are literal unless the program expands them itself.
* **Broker hardening**:
  * Authenticate requests per task rather than per connection, and check the caller's kernel-reported identity (such as its cgroup or security label) rather than a reusable process ID.
  * Rate-limit denials per session and keep denial messages terse: a retry loop is a search of the policy, and detailed denials teach an adversarial prompt its shape.

---

## Challenges and Considerations

* **Dynamic Privilege Complexity**: Managing context-aware privileges requires sophisticated authorization engines and may introduce performance overhead.
* **Agent Functionality Balance**: Overly restrictive privileges may limit agent effectiveness, requiring careful balance between security and functionality.
* **Cross-System Integration**: Implementing consistent privilege enforcement across multiple APIs and systems requires significant integration effort.
* **Limits of Execution Control**: Process-execution controls do not cover code that runs without starting a new program, such as just-in-time compilation, dynamic library loading, or in-process script loading by an allowed runtime. Dependency installation (`npm install`, `pip install`) runs third-party code by design, so perform it in a controlled build step rather than inside the agent's session.
* **Regulatory Compliance**: Ensuring privilege frameworks comply with various financial regulations and audit requirements.

---

## Importance and Benefits

Implementing comprehensive agent authority least privilege frameworks provides critical security benefits:

* **Attack Surface Reduction**: Limits the potential impact of agent compromise by restricting accessible resources and capabilities.
* **Regulatory Compliance**: Ensures agents operate within regulatory boundaries and approval requirements.
* **Unauthorized Action Prevention**: Prevents agents from executing transactions or operations outside their intended scope.
* **Audit Trail Enhancement**: Provides detailed logging and audit capabilities for regulatory and security investigations.
* **Risk Mitigation**: Reduces operational risk by enforcing business rules and approval workflows at the privilege level.
* **Incident Response Support**: Enables rapid containment of security incidents by restricting compromised agent capabilities.

---

## Additional Resources

* [NIST SP 800-53 Rev. 5 - AC-6 Least Privilege](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#!/control?version=5.1&number=AC-6)
* [ISO 27001:2013 - A.9.1.2 Access to networks and network services](https://www.iso.org/standard/54534.html)
* [FFIEC IT Handbook - Information Security](https://ithandbook.ffiec.gov/it-booklets/information-security.aspx)
* Background for the section 7 approach
    * [NIST SP 800-167: Guide to Application Whitelisting](https://csrc.nist.gov/pubs/sp/800/167/final): NIST guidance on deny-by-default control of which applications may execute, identified by attributes such as path, hash, and digital signature.
    * [OWASP Top 10 for LLM Applications 2025, LLM06: Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/): names an extension meant to run one specific shell command that fails to prevent other commands as a core example of excessive functionality, and recommends minimizing agent extensions and their permissions.
    * [OWASP Top 10 for Agentic Applications 2026, ASI05: Unexpected Code Execution](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/): covers agents that execute prompt-supplied shell commands or generated code in ways the operator did not intend, and recommends sandboxed execution, a version-controlled allowlist for auto-execution, and separating code generation from execution with validation gates.
* Example implementation options for OS and runtime-layer enforcement (section 7). These are illustrative only, not endorsements or an exhaustive list.
    * Restricting which commands an agent can execute
        * [Landlock](https://docs.kernel.org/userspace-api/landlock.html): Linux unprivileged sandboxing; its execute right limits which files or directory trees a process and its children may run programs from.
        * [fapolicyd](https://github.com/linux-application-whitelisting/fapolicyd): Linux policy daemon that allows or denies each program execution against ordered rules and trust data; content hashes are checked by explicit hash rules, or for trust checks when its integrity setting enables them.
        * [App Control for Business](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/): Windows policy-based allow-listing of applications by signer, path or hash.
        * [Endpoint Security](https://developer.apple.com/documentation/endpointsecurity): macOS framework through which an entitled security client can authorize or deny each process execution.
    * Preventing injection through command arguments
        * [OWASP OS Command Injection Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html): invoking programs with structured argument lists instead of shell strings, and validating arguments against an allow-list.
        * [CWE-88: Argument Injection](https://cwe.mitre.org/data/definitions/88.html): how attacker-supplied arguments, such as option flags, change the behavior of an otherwise allowed command.
        * [GTFOBins](https://gtfobins.github.io/) (Unix) and [LOLBAS](https://lolbas-project.github.io/) (Windows): catalogs of common binaries whose options can spawn shells, read or write files, or reach the network; useful for deciding which executables and options must never be allow-listed.
