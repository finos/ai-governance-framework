# AI Governance Risk Register

Core register: 38 risks across Operational, Security, Regulatory, Agent Operations, Infrastructure & Supply, Data Pipeline, and Business Outcome domains. Each risk carries inherent and residual scoring (Likelihood x Impact, 1-5 each), owner, controls, and status. Referenced against the [FINOS AI Governance Framework risk catalog](https://github.com/finos/ai-governance-framework/tree/main/docs/_risks). Intended to act as framework, will not be exhaustive. There may be gaps that may be addressed in the playbook to ensure all scenarios are covered. Indicated status listed here are illustrative, not actual statuses and may contain domain values of In Progress, Planned, Completed, etc. 

## R-01 — Hallucination & Inaccurate Outputs

- **FINOS Ref (if available):** ri-4
- **Domain:** Operational
- **Description:** Model generates confident but fabricated or incorrect information not grounded in fact, RAG reduces but cannot eliminate it.
- **Potential Impact:** Poor decisions, fabricated financial data/advice, customer harm, mis-statement in regulated outputs.
- **Likelihood:** 3
- **Impact:** 5
- **Inherent:** 15
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** RAG grounding, human-in-the-loop on material outputs, output validation, confidence thresholds.
- **Ctrl Effectiveness:** 3
- **Residual:** 9
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of Data Science
- **Status:** In Progress
- **FINOS Coverage:** FINOS
- **Stack Layer:** L9

## R-02 — Foundation Model Versioning

- **FINOS Ref (if available):** ri-5
- **Domain:** Operational
- **Description:** Silent or unmanaged upstream model/version changes alter behavior and break prior validation and reproducibility.
- **Potential Impact:** Untracked behavioral drift, broken testing, compliance/audit gaps.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Version pinning, change notification SLAs, regression test suite on version change.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** ML Platform Lead
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L6

## R-03 — Non-Deterministic Behavior

- **FINOS Ref (if available):** r1_6
- **Domain:** Operational
- **Description:** Identical inputs can yield different outputs due to probabilistic sampling, complicating testing and assurance.
- **Potential Impact:** Inconsistent customer experience, unreliable compliance checks, hard-to-reproduce defects.
- **Likelihood:** 3
- **Impact:** 3
- **Inherent:** 9
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** Moderate
- **Existing Controls:** Temperature/seed control where supported, tolerance-based test assertions, output logging.
- **Ctrl Effectiveness:** 3
- **Residual:** 5
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** ML Platform Lead
- **Status:** In Progress
- **FINOS Coverage:** FINOS
- **Stack Layer:** L7

## R-04 — Availability of Foundation Model

- **FINOS Ref (if available):** ri-7
- **Domain:** Operational
- **Description:** Dependence on third-party GPU-hosted models creates outage, throttling, Denial-of-Wallet and VRAM-exhaustion exposure.
- **Potential Impact:** Service disruption, cost spikes, business-continuity breach.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Multi-provider failover, rate limiting, capacity planning, usage monitoring & alerts.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of AI Engineering
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L3

## R-05 — Inadequate System Alignment

- **FINOS Ref (if available):** r1-14
- **Domain:** Operational
- **Description:** RAG/agent outputs diverge from intended business purpose or compliance constraints despite appearing relevant.
- **Potential Impact:** Regulatory violations, customer harm, scaled operational error.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** System-acceptance testing, scope guardrails, prompt templates, continuous response-quality monitoring.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L9

## R-06 — Bias & Discrimination

- **FINOS Ref (if available):** ri-16
- **Domain:** Operational
- **Description:** Systems disadvantage protected groups via skewed data, proxies, or feedback loops (e.g. credit, fraud, pricing).
- **Potential Impact:** Fair-lending breach, discriminatory outcomes, regulatory penalty, reputational damage.
- **Likelihood:** 3
- **Impact:** 5
- **Inherent:** 15
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Bias testing on protected attributes, fairness metrics, diverse data review, human review of high-impact decisions.
- **Ctrl Effectiveness:** 3
- **Residual:** 9
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** In Progress
- **FINOS Coverage:** FINOS
- **Stack Layer:** L7

## R-07 — Lack of Explainability

- **FINOS Ref (if available):** ri-17
- **Domain:** Operational
- **Description:** Black-box decisions cannot be adequately interpreted or justified to regulators, stakeholders, or customers.
- **Potential Impact:** Reduced trust, inability to contest decisions, regulatory non-compliance.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Model documentation, explainability tooling, user-facing disclosures, decision logging.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L6

## R-08 — Model Overreach / Expanded Use

- **FINOS Ref (if available):** ri-18
- **Domain:** Operational
- **Description:** A model is used beyond its validated scope or intended purpose, often due to over-trust / anthropomorphism.
- **Potential Impact:** Non-compliant outputs, unsuitable advice, operational error in high-stakes tasks.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Approved use-case registry, scope constraints, user training, periodic use review.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L6

## R-09 — Data Quality & Drift

- **FINOS Ref (if available):** ri-19
- **Domain:** Operational
- **Description:** Outdated or poor-quality data and concept drift erode accuracy over time (model aging).
- **Potential Impact:** Flawed risk assessments, stale compliance logic, degraded decisions.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Data-quality monitoring, scheduled revalidation/retraining, drift detection, lineage controls.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of Data Governance
- **Status:** In Progress
- **FINOS Coverage:** FINOS
- **Stack Layer:** L5

## R-10 — Reputational Risk

- **FINOS Ref (if available):** ri-20
- **Domain:** Operational
- **Description:** Customer-facing AI failures scale rapidly into public incidents that erode brand and trust.
- **Potential Impact:** Media backlash, customer attrition, regulatory scrutiny, brand damage.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Guardrails on customer-facing outputs, incident response playbook, pre-release red-teaming.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Risk Officer
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L10

## R-11 — Multi-Agent Trust Boundary Violations

- **FINOS Ref (if available):** ri-28
- **Domain:** Operational
- **Description:** Compromise in one agent propagates across a multi-agent system via shared state or communication channels.
- **Potential Impact:** Cascading failures, cross-function impact, amplified loss, complex incident response.
- **Likelihood:** 2
- **Impact:** 5
- **Inherent:** 10
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Agent isolation, inter-agent authN/authZ, shared-resource controls, cross-agent monitoring.
- **Ctrl Effectiveness:** 2
- **Residual:** 8
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L8

## R-12 — Information Leaked to Hosted Model

- **FINOS Ref (if available):** ri-1
- **Domain:** Security
- **Description:** Sensitive data sent to a third-party hosted model may be memorized, logged, or exposed (incl. cross-user leakage).
- **Potential Impact:** PII/PHI exposure, IP loss, GDPR/GLBA breach, regulatory fines.
- **Likelihood:** 4
- **Impact:** 5
- **Inherent:** 20
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** Critical
- **Existing Controls:** Enterprise no-train agreements, input filtering/redaction, private endpoints, DLP on prompts.
- **Ctrl Effectiveness:** 3
- **Residual:** 12
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Chief Privacy Officer
- **Status:** In Progress
- **FINOS Coverage:** FINOS
- **Stack Layer:** L4

## R-13 — Information Leaked to Vector Store

- **FINOS Ref (if available):** ri-2
- **Domain:** Security
- **Description:** Confidential data embedded in a vector store can be reconstructed via inversion or membership-inference attacks.
- **Potential Impact:** Reconstruction of sensitive data, confidentiality breach, poisoning.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Embedding access controls (RBAC), encryption at rest, pre-embedding data filtering, audit logging.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Information Security Officer
- **Status:** In Progress
- **FINOS Coverage:** FINOS
- **Stack Layer:** L5

## R-14 — Tampering with the Foundation Model

- **FINOS Ref (if available):** ri-8
- **Domain:** Security
- **Description:** Model supply chain (weights, training data, firmware, ML libs) compromised, poisoned, or back-doored upstream.
- **Potential Impact:** Backdoors, unsafe behavior under triggers, integrity loss.
- **Likelihood:** 2
- **Impact:** 5
- **Inherent:** 10
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Provenance checks, trusted providers, tamper-detection, SBOM for ML dependencies.
- **Ctrl Effectiveness:** 2
- **Residual:** 8
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Information Security Officer
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L6

## R-15 — Data Poisoning

- **FINOS Ref (if available):** ri-9
- **Domain:** Security
- **Description:** Adversaries tamper with training/fine-tuning/retrieval data to manipulate model behavior, often subtly.
- **Potential Impact:** Biased decisioning, fraud approval, degraded performance, hidden failures.
- **Likelihood:** 2
- **Impact:** 5
- **Inherent:** 10
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Source validation, third-party feed integrity checks, anomaly detection, continuous-learning safeguards.
- **Ctrl Effectiveness:** 2
- **Residual:** 8
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Information Security Officer
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L5

## R-16 — Prompt Injection

- **FINOS Ref (if available):** ri-10
- **Domain:** Security
- **Description:** Crafted direct or indirect inputs override instructions to leak data or trigger unintended actions.
- **Potential Impact:** Data leakage, unsafe automated actions, misinformation, reputational harm.
- **Likelihood:** 4
- **Impact:** 4
- **Inherent:** 16
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** Critical
- **Existing Controls:** Input/output firewalling, LLM-as-judge, indirect-injection scanning of ingested content, least privilege.
- **Ctrl Effectiveness:** 3
- **Residual:** 10
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Chief Information Security Officer
- **Status:** In Progress
- **FINOS Coverage:** FINOS
- **Stack Layer:** L8

## R-17 — Agent Action Authorization Bypass

- **FINOS Ref (if available):** ri-24
- **Domain:** Security
- **Description:** Agents act beyond authorized scope — discovering APIs, chaining tools, or circumventing approval workflows.
- **Potential Impact:** Unauthorized transactions, segregation-of-duties breach, regulatory violation.
- **Likelihood:** 3
- **Impact:** 5
- **Inherent:** 15
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Granular per-agent RBAC, tool-manager authZ, approval gates, segregation-of-duties enforcement.
- **Ctrl Effectiveness:** 2
- **Residual:** 12
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L8

## R-18 — Tool Chain Manipulation & Injection

- **FINOS Ref (if available):** ri-25
- **Domain:** Security
- **Description:** Inputs manipulate an agent's tool selection or inject malicious parameters into legitimate API calls.
- **Potential Impact:** Payment redirection, data exfiltration, compliance bypass, fraud.
- **Likelihood:** 3
- **Impact:** 5
- **Inherent:** 15
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Tool-selection validation, parameter sanitization, constrained tool scopes, sequence monitoring.
- **Ctrl Effectiveness:** 2
- **Residual:** 12
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Chief Information Security Officer
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L8

## R-19 — MCP Server Supply Chain Compromise

- **FINOS Ref (if available):** ri-26
- **Domain:** Security
- **Description:** Compromised Model Context Protocol servers feed agents tainted data, logic, or capabilities at scale.
- **Potential Impact:** Systematic decision corruption, credential harvesting, widespread compliance failure.
- **Likelihood:** 3
- **Impact:** 5
- **Inherent:** 15
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** MCP server vetting, pre-approved server registry, signed/encrypted MCP comms, response monitoring.
- **Ctrl Effectiveness:** 2
- **Residual:** 12
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L1

## R-20 — Agent State Persistence Poisoning

- **FINOS Ref (if available):** ri-27
- **Domain:** Security
- **Description:** Malicious instructions persist in agent memory across sessions, creating long-lived backdoors.
- **Potential Impact:** Persistent fraud bypass, systematic compliance violation, accumulated loss.
- **Likelihood:** 2
- **Impact:** 5
- **Inherent:** 10
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** State validation/sanitization, memory access controls, state-change auditing, session isolation.
- **Ctrl Effectiveness:** 2
- **Residual:** 8
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L8

## R-21 — Agent-Mediated Credential Harvesting

- **FINOS Ref (if available):** ri-29
- **Domain:** Security
- **Description:** Agents are exploited to discover and exfiltrate credentials, API keys, and secrets across systems.
- **Potential Impact:** Infrastructure-wide compromise, lateral movement, large-scale breach.
- **Likelihood:** 2
- **Impact:** 5
- **Inherent:** 10
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Credential segmentation from agent runtime, secrets-vault isolation, tool restrictions, access-pattern monitoring.
- **Ctrl Effectiveness:** 2
- **Residual:** 8
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Information Security Officer
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L8

## R-22 — Regulatory Compliance & Oversight

- **FINOS Ref (if available):** ri-22
- **Domain:** Regulatory
- **Description:** AI systems must meet the same obligations as human-driven processes, evolving regimes (EU AI Act, SR 11-7, SS1/23) raise the bar.
- **Potential Impact:** Fines, enforcement, restrictions, legal action, mandated remediation.
- **Likelihood:** 3
- **Impact:** 5
- **Inherent:** 15
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Use-case-to-regulation mapping, model governance & validation, record-keeping, FRIA for high-risk uses.
- **Ctrl Effectiveness:** 3
- **Residual:** 9
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Compliance Officer
- **Status:** In Progress
- **FINOS Coverage:** FINOS
- **Stack Layer:** L6

## R-23 — Intellectual Property & Copyright

- **FINOS Ref (if available):** ri-23
- **Domain:** Regulatory
- **Description:** Training data or outputs may infringe IP, or staff may leak trade secrets into public AI tools.
- **Potential Impact:** Infringement claims, trade-secret loss, licensing breach, contractual liability.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Vendor IP indemnity, acceptable-use policy, output IP screening, DLP on public tools.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** General Counsel
- **Status:** Planned
- **FINOS Coverage:** FINOS
- **Stack Layer:** L6

## R-24 — Information Leaked To Hosted Model - Data Protection & Privacy Compliance

- **FINOS Ref (if available):** ri-1
- **Domain:** Regulatory
- **Description:** Failure to meet GDPR/CCPA/GLBA data-subject rights and purpose-limitation in AI processing of PII/PHI.
- **Potential Impact:** Privacy fines, data-subject complaints, mandated deletion, reputational harm.
- **Likelihood:** 3
- **Impact:** 5
- **Inherent:** 15
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Data minimization, DPIAs, lawful-basis mapping, retention controls, data-subject-rights workflow.
- **Ctrl Effectiveness:** 3
- **Residual:** 9
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Privacy Officer
- **Status:** In Progress
- **FINOS Coverage:** FINOS
- **Stack Layer:** L4

## R-25 — Model Overreach / Expanded Use - Autonomous Decision-Making Beyond Mandate

- **FINOS Ref (if available):** ri-18
- **Domain:** Agent Operations
- **Description:** An agent makes and executes decisions independently that should require human judgement or fall outside its approved decision rights, due to over-broad autonomy or ambiguous scope.
- **Potential Impact:** Unauthorized or unreviewed actions, decisions made without accountability, regulatory and financial exposure.
- **Likelihood:** 3
- **Impact:** 5
- **Inherent:** 15
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Defined decision-rights matrix, autonomy tiering (suggest/approve/auto), approval gates on sensitive actions, full action audit log, KILL-SWITCH on out-of-mandate actions.
- **Ctrl Effectiveness:** 2
- **Residual:** 12
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** FINOS-adjacent
- **Stack Layer:** L8

## R-26 — Outcome Deviation & Detection Gap

- **FINOS Ref (if available):** ri-14?? Alignment tbd
- **Domain:** Agent Operations
- **Description:** An agent's outputs drift from expected/normalized outcomes and the deviation is not detected promptly because monitoring lacks an outcome baseline, or the agent self-reports success while producing wrong results.
- **Potential Impact:** Silent accumulation of wrong outcomes, delayed detection, eroded trust, scaled error before intervention.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Outcome baselining vs golden datasets, continuous deviation monitoring & alerting, independent (non-self-reported) validation, canary checks, auto-pause on threshold breach.
- **Ctrl Effectiveness:** 2
- **Residual:** 10
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** ML Platform Lead
- **Status:** Planned
- **FINOS Coverage:** FINOS-adjacent
- **Stack Layer:** L9

## R-27 — DQ issues/non-deterministic behavior. Pattern-Shift Rejected as Anomaly

- **FINOS Ref (if available):** ri-6/ri-19? Align agentic
- **Domain:** Agent Operations
- **Description:** When a genuine, legitimate shift in data distribution occurs (a new normal / pattern shift, not a one-off anomaly), the agent rejects the data as anomalous and fails to adapt continuing to act on outdated normalized values.
- **Potential Impact:** Agent operates on stale assumptions, rejects valid inputs, produces systematically wrong results during regime change.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Distinguish drift vs anomaly (trend vs outlier tests), human review of sustained 'anomaly' clusters, adaptive thresholds, scheduled re-baselining, escalation when rejection rate spikes.
- **Ctrl Effectiveness:** 2
- **Residual:** 10
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Head of Data Science
- **Status:** Planned
- **FINOS Coverage:** GAP
- **Stack Layer:** L5

## R-28 — hallucination/inadequate system alignment, Fabricated Outcome Under Inability to Respond

- **FINOS Ref (if available):** ri-4/ri/14? 
- **Domain:** Agent Operations
- **Description:** When an agent cannot generate a valid response (missing data, tool failure, low confidence) it guesses or fabricates an outcome instead of failing safe or escalating — masking the gap as a confident result.
- **Potential Impact:** Fabricated decisions enter downstream processes, false confidence, undetected wrong outputs in regulated workflows.
- **Likelihood:** 4
- **Impact:** 5
- **Inherent:** 20
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** Critical
- **Existing Controls:** Mandatory confidence thresholds with fail-safe/abstain path, 'I-don't-know' escalation route, tool-failure handling that halts not guesses, output provenance & confidence logging, KILL-SWITCH on repeated low-confidence fabrication.
- **Ctrl Effectiveness:** 2
- **Residual:** 16
- **Residual Rating:** Critical
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** GAP
- **Stack Layer:** L9

## R-29 — Toolchain / injection/boundary violations Cascading Deviation in Connected Agents (No Rollback)

- **FINOS Ref (if available):** ri-25/ri-28??
- **Domain:** Agent Operations
- **Description:** One agent depends on another agent's outcome, a dependent agent receives corrupt, skewed, or fabricated input and propagates it, creating a sequence of deviations that is hard to detect and has no rollback plan to a known-good state.
- **Potential Impact:** Compounding errors across the chain, unrecoverable state, systemic failure, very high detection difficulty.
- **Likelihood:** 3
- **Impact:** 5
- **Inherent:** 15
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Inter-agent input validation & contracts, provenance/lineage tagging across hops, circuit-breakers between agents, transactional checkpoints with rollback/compensation, chain-level kill-switch, MANDATORY pre-release review for connected-agent chains.
- **Ctrl Effectiveness:** 2
- **Residual:** 12
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Head of AI Governance
- **Status:** Planned
- **FINOS Coverage:** FINOS-adjacent
- **Stack Layer:** L8

## R-30 — non-deterministic behavior/boundary violations/Result Skew from Upstream Agent Non-Response

- **FINOS Ref (if available):** ri-28/ri-6??
- **Domain:** Agent Operations
- **Description:** An upstream agent is unable to generate a response (timeout, failure, empty output), the dependent agent proceeds on incomplete/default input, skewing its own result rather than halting.
- **Potential Impact:** Skewed downstream decisions, silent degradation of the whole chain, masked single-point failure.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Explicit handling of null/empty/timeout upstream results, fail-closed defaults, dependency health checks, require positive acknowledgement before proceeding, degrade-gracefully vs proceed-blindly policy.
- **Ctrl Effectiveness:** 2
- **Residual:** 10
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** ML Platform Lead
- **Status:** Planned
- **FINOS Coverage:** FINOS-adjacent
- **Stack Layer:** L8

## R-31 — Agent state persistence posioningCorrupt-Input Propagation Across Agent Trust Boundary

- **FINOS Ref (if available):** ri-27?
- **Domain:** Agent Operations
- **Description:** A dependent agent implicitly trusts an upstream agent and ingests corrupt or poisoned input without revalidation, allowing corruption to cross the trust boundary and skew or poison the dependent agent's reasoning or state.
- **Potential Impact:** Cross-agent corruption, poisoned state, manipulated decisions propagated as trusted, broad blast radius.
- **Likelihood:** 2
- **Impact:** 5
- **Inherent:** 10
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Zero-trust between agents (revalidate every hop), schema & sanity checks on inter-agent payloads, signed/attested messages, isolate agent state, anomaly detection on inter-agent traffic.
- **Ctrl Effectiveness:** 2
- **Residual:** 8
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Information Security Officer
- **Status:** Planned
- **FINOS Coverage:** GAP
- **Stack Layer:** L8

## R-32 — Compute Supply Chain & Concentration

- **FINOS Ref (if available):** ?
- **Domain:** Infrastructure & Supply
- **Description:** GPU/accelerator shortage, single-vendor or single-region dependency, or capacity unavailability constrains training/inference and creates cost and continuity exposure at the hardware layer (L1).
- **Potential Impact:** Inability to train/serve, runaway cost, business continuity breach, strategic dependency.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Multi-vendor/region sourcing, reserved capacity & commitments, demand forecasting, FinOps controls, fallback to alternate accelerators.
- **Ctrl Effectiveness:** 2
- **Residual:** 10
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Chief Technology Officer
- **Status:** Planned
- **FINOS Coverage:** GAP
- **Stack Layer:** L1

## R-33 — Infrastructure Resilience & DR Gap

- **FINOS Ref (if available):** ?
- **Domain:** Infrastructure & Supply
- **Description:** GPU node failure, network partition, region outage, or absent/untested disaster recovery for AI platform components (L2-L3) disrupts model availability and breaks continuity expectations.
- **Potential Impact:** Service outage, failed failover, SLA/continuity breach, data-in-flight loss.
- **Likelihood:** 2
- **Impact:** 4
- **Inherent:** 8
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** Moderate
- **Existing Controls:** HA cluster design, tested DR runbooks, multi-AZ/region failover, chaos/resilience testing, RTO/RPO targets for AI services.
- **Ctrl Effectiveness:** 2
- **Residual:** 6
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Head of AI Engineering
- **Status:** Planned
- **FINOS Coverage:** GAP
- **Stack Layer:** L2

## R-34 — Cloud Cost Overrun & FinOps Gap (Denial-of-Wallet)

- **FINOS Ref (if available):** ?
- **Domain:** Infrastructure & Supply
- **Description:** Uncontrolled token/inference spend, runaway agent loops, or unmonitored GPU utilization drive cost overruns, absent FinOps translation layer between finance and infra (L3).
- **Potential Impact:** Budget overrun, untracked spend, throttling, ROI erosion.
- **Likelihood:** 4
- **Impact:** 3
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Per-use-case API keys & quotas, spend alerts & budgets, utilization monitoring, rate limiting, agent step/cost caps (links kill-switch).
- **Ctrl Effectiveness:** 2
- **Residual:** 10
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Chief Financial Officer / FinOps
- **Status:** Planned
- **FINOS Coverage:** GAP
- **Stack Layer:** L3

## R-35 — Vendor Lock-in & Concentration

- **FINOS Ref (if available):** ?
- **Domain:** Infrastructure & Supply
- **Description:** Tight coupling to a single model provider, cloud, or platform limits failover, pricing leverage, and portability (L3), concentration risk if that provider degrades or changes terms.
- **Potential Impact:** Reduced resilience, pricing exposure, migration cost, strategic dependency.
- **Likelihood:** 3
- **Impact:** 3
- **Inherent:** 9
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** Moderate
- **Existing Controls:** Abstraction/gateway layer over providers, portability standards, contractual exit terms, periodic alternative-provider evaluation.
- **Ctrl Effectiveness:** 2
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Technology Officer
- **Status:** Planned
- **FINOS Coverage:** GAP
- **Stack Layer:** L3

## R-36 — Data drift/Training-Serving Skew & Feature Pipeline Drift

- **FINOS Ref (if available):** ri-19??
- **Domain:** Data Pipeline
- **Description:** Feature distributions at serving diverge from training (training-serving skew), or pipeline transformations differ between offline and online paths, silently degrading model accuracy (L5).
- **Potential Impact:** Silent accuracy loss, wrong decisions, hard-to-detect degradation.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Shared feature definitions / feature store, skew monitoring (PSI/KS), offline-online parity tests, pipeline versioning.
- **Ctrl Effectiveness:** 2
- **Residual:** 10
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Head of Data Science
- **Status:** Planned
- **FINOS Coverage:** FINOS-adjacent
- **Stack Layer:** L5

## R-37 — Data Lineage & Provenance Gap

- **FINOS Ref (if available):** ?
- **Domain:** Data Pipeline
- **Description:** Missing or incomplete lineage means the origin, consent basis, transformations, and downstream use of training/feature data cannot be traced — blocking impact analysis, erasure, and audit (L5).
- **Potential Impact:** Unauditable data, blocked right-to-erasure, undetected poisoning, compliance failure.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** End-to-end lineage capture, dataset/version registry, consent & license tagging, provenance attestation, lineage in DPIA.
- **Ctrl Effectiveness:** 2
- **Residual:** 10
- **Residual Rating:** High
- **Treatment:** Mitigate
- **Owner:** Head of Data Governance
- **Status:** Planned
- **FINOS Coverage:** GAP
- **Stack Layer:** L5

## R-38 — Strategic Misalignment & Failed ROI

- **FINOS Ref (if available):** ?
- **Domain:** Business Outcome
- **Description:** AI investment fails to deliver expected business value, or use cases drift from strategy, benefits unrealized relative to spend, eroding executive confidence and funding (L10).
- **Potential Impact:** Wasted investment, lost confidence, defunding, opportunity cost.
- **Likelihood:** 3
- **Impact:** 4
- **Inherent:** 12
- **Threshold (determined by use case/context):** 
- **Inherent Rating:** High
- **Existing Controls:** Value-tracking vs business case, benefits realization reviews, portfolio prioritization, outcome KPIs tied to AI strategy pillars.
- **Ctrl Effectiveness:** 3
- **Residual:** 7
- **Residual Rating:** Moderate
- **Treatment:** Mitigate
- **Owner:** Chief Data & Analytics Officer
- **Status:** Planned
- **FINOS Coverage:** GAP
- **Stack Layer:** L10
