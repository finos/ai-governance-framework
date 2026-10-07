---
sequence: 24
title: Human-in-the-Loop Action Approval Gate
layout: mitigation
doc-status: Draft
type: PREV
iso-42001_references:
  - A-6-2-6  # ISO 42001: AI system operation and monitoring
  - A-9-2    # ISO 42001: Processes for responsible use of AI systems
eu-ai-act_references:
  - c3-s2-a14  # III.S2.A14: Human Oversight
nist-sp-800-53r5_references:
  - ac-3   # AC-3 Access Enforcement
  - ac-5   # AC-5 Separation of Duties
  - ac-6   # AC-6 Least Privilege
  - au-10  # AU-10 Non-repudiation
  - si-4   # SI-4 System Monitoring
mitigates:
  - ri-24  # Agent Action Authorization Bypass
  - ri-18  # Model Overreach / Expanded Use
  - ri-22  # Regulatory Compliance and Oversight
related_mitigations:
  - mi-18  # Agent Authority Least Privilege Framework
  - mi-11  # Human Feedback Loop for AI Systems
  - mi-21  # Agent Decision Audit and Explainability
---

## Purpose

A **Human-in-the-Loop (HITL) Action Approval Gate** is a preventive control that interrupts an agent immediately before it executes a designated high-risk action and holds execution until a human with the appropriate authority explicitly decides on the proposed action. Unlike privilege scoping (which governs what an agent *may* access) or feedback loops (which collect evaluative input for detection and improvement but do not themselves authorize the release of a particular action), the approval gate operates on the **specific proposed action at the moment of execution**, evaluating its resolved parameters and context against policy before any side effect occurs.

This control addresses the class of failures where an agent is technically operating within its granted privileges yet is about to take an action that is materially consequential, hard to reverse, or subject to a documented human-authorization requirement. It gives financial institutions a durable, auditable pause point that supports human-oversight obligations without disabling autonomy for low-risk work.

The control applies to the action classes an institution has designated as requiring approval. It is not a requirement that every agent action be confirmed by a human: actions outside the designated set proceed under the institution's baseline authorization controls (`mi-18`). Making the designation explicit, and reviewing it, is the substance of the control.

The relationship to the **Agent Authority Least Privilege Framework** (`mi-18`) is deliberate and complementary. `mi-18` already requires human approval in several of its scenarios (privilege escalation, operations exceeding risk thresholds) but does not define the approval mechanism itself. This control specifies that mechanism: the approval-request lifecycle, the durable pending state, the binding of the human decision to the exact action, and the release protocol. Institutions should deploy the two together, with `mi-18` defining the agent's authority boundary and this control governing designated actions inside that boundary.

---

## Key Principles

* **Gate the Action, Not the Agent:** The decision point is the concrete proposed action (tool call, transaction, external side effect) with its resolved parameters, not the agent's identity or session in the abstract. This lets the same agent proceed unattended for routine work and pause only for actions that policy classifies as requiring approval.
* **Policy-Driven Classification:** Which actions require approval must be defined declaratively (by tool, action type, impact class, monetary threshold, counterparty sensitivity, or jurisdiction) and evaluated by an enforcement component the agent cannot bypass, not left to the model's own judgment or to application code that a prompt-injected agent could route around. Declarative constrains how a gating rule is expressed and enforced, not who writes it or when it is decided: a rule may be set by the institution ahead of time, or granted at runtime by an authorized human as a standing approval covering a bounded class of subsequent actions (see *Standing Approval and Pre-Authorization*). Because gating rules are typically an explicit enumeration, the coverage of that enumeration is itself a policy decision: actions not matched by any gating rule fall through to the institution's baseline authorization controls (`mi-18`), and gate coverage should be reviewed on the same cadence as the privilege model.
* **Fail-Closed by Default:** If the approval policy cannot be evaluated, the approval state cannot be resolved, or the action is matched by no decision and no standing approval in force, the action must not proceed. A missing decision is treated as a rejection, not an implicit allow.
* **Durable, Resumable Approval State:** The pending decision must survive process restarts, worker failover, and time gaps between request and human response. On approval, the action's outcome is committed exactly once; because a crash between issuing the side-effecting call and recording its outcome can cause a re-fire, the side-effecting call itself must be idempotent (see Implementation Guidance).
* **Named Oversight Pattern:** The gate must implement a deliberately chosen oversight pattern, in the institution's standard terminology: **user confirmation** (the requester confirms their own action; the weakest pattern, appropriate only for low-impact cases), **maker-checker / four-eyes** (a second principal, distinct from the requester and from the agent, decides), or **dual authorization / two-person control** (two independent approvers; NIST AC-5, AC-3(2)). In every pattern the agent itself is never a valid approver, the decision identity must come from an authenticated principal, and shared identities are prohibited.
* **Bounded Waiting:** Every gated action has an approval deadline. On expiry the action is rejected or escalated per policy, so actions are never parked indefinitely. Deadlines bound waiting; they do not by themselves protect approver capacity (see Operational Safeguards).
* **Tamper-Evident Record:** The proposed action, the policy decision, the approver identity, the outcome, and the timestamps form a single tamper-evident record suitable for audit. Non-repudiation requires more than tamper-evidence (see Implementation Guidance).

---

## Implementation Guidance

### 1. Defining What Requires Approval

* **Classify by Impact, Not Reversibility Alone:** Assess candidate actions across confidentiality, integrity, financial loss, customer harm, legal effect, external dissemination, and time sensitivity, with reversibility and compensating controls as factors rather than exemptions. A payment may be recallable yet still cause material harm; an order may be cancellable before a fill and irreversible after it; a read-only query can disclose restricted client or trading information. Typical predicates in financial services include:
  * **Impact class:** Actions whose worst-case impact crosses a documented threshold in any of the dimensions above.
  * **Monetary threshold:** Actions above a configurable value, or that would cross an aggregate daily or session limit. Aggregate limits are subject to races between concurrently pending actions; enforce them with atomic reservations rather than read-then-act checks.
  * **Counterparty and data sensitivity:** Actions touching flagged accounts, restricted data classes, or sensitive counterparties require approval or a higher approval tier.
  * **Documented authorization requirements:** Actions for which Legal, Compliance, or the accountable control owner has documented a jurisdiction-specific human-authorization requirement. Two boundaries matter here: limits that policy defines as non-waivable must produce denial, not approval escalation; and workflows with restricted-access obligations (for example suspicious-activity handling) belong in their dedicated case-management procedures, not a general-purpose approval channel.
* **Enforce at a Choke Point the Agent Cannot Skip:** Evaluate the approval policy in the same mediation layer that executes tool and API calls (the tool manager or runtime enforcement point described in `mi-18`). For the choke point to be meaningful, the institution must establish complete mediation: the agent's credentials and network egress are constrained so governed effects are reachable only through mediated tools, generic capabilities (raw HTTP, shell, browser automation) are not available alongside governed tools that reach the same downstream systems, equivalent action paths are inventoried, and alternate-path bypass is tested. Approval releases the agent's existing authority for one specific action; it must never elevate the agent's privileges or lend it the approver's credentials.
* **Bind the Decision to the Resolved Action:** Classify and present the *fully resolved* action (final recipient, final amount, final payload), not the agent's earlier intent, and bind the approval to a canonical digest of that resolved action with a defined validity period. Because conditions change while an action waits (sanctions state, account status, limit consumption, entitlements, policy version), revalidate mutable predicates immediately before release, and define explicitly whether a policy change invalidates or reclassifies outstanding approvals.

### 2. Pausing and Resuming Execution

* **Interrupt Before Side Effects:** The gate must suspend execution *before* the side-effecting call is issued. Approval obtained after partial execution provides no protection.
* **Persist a Minimal Envelope:** Persist the suspended action durably so a pending approval survives restarts and can be resumed by any worker, but persist only a minimal, schema-validated action envelope and the evidence needed for the decision. Encrypt it, restrict access to it, and define retention and deletion. Never persist reusable bearer credentials as approval state: obtain fresh execution credentials and re-authorize when the action resumes.
* **Be Honest About Execution Semantics:** A gating mechanism can guarantee at most exactly-once *commit* of an action's recorded outcome. A crash in the window between issuing the side-effecting call and recording its result yields at-least-once *execution* on recovery. For non-idempotent financial actions this distinction is material: require an idempotency mechanism that the downstream system durably enforces (for example an idempotency key honored by the payment or order API). Where the downstream system cannot enforce idempotency, an ambiguous outcome must transition the action to an `outcome-unknown` state for manual reconciliation, never automatic retry.
* **Single-Effect Resolution:** Ensure that a decision takes effect only once for a given pending action, that duplicate or concurrent decision submissions are inert, and that late decisions arriving after the deadline or after the action has been resolved are rejected. Model the lifecycle as an explicit durable state machine (for example `pending`, `approved`, `rejected`, `expired`, `cancelled`, `failed`, `outcome-unknown`, `executed`) so that these materially different outcomes are distinguishable in the record.

### 3. Routing to the Right Human

* **Approver Selection:** Resolve the required approver(s) from the policy and the action's risk tier, routing to business roles that hold delegated authority for that action type and amount under the institution's delegated-authorities framework and three-lines model. Second-line functions approve only where policy explicitly assigns them that responsibility; a regulatory dimension alone does not make Compliance the operational approver. Support single-approver, maker-checker, N-of-M, and sequential multi-tier patterns.
* **Notification vs. Decision Channels:** Approvers may be *notified* through the channels they already operate (case queue, ticketing, chat, email), but the *decision* must be captured through an authenticated, replay-resistant mechanism that displays the resolved action and its digest, re-checks the approver's authorization at decision time, and safely renders any model-controlled content. Email replies, chat reactions, and forwardable links are not decision-grade: they can be spoofed, replayed, or detached from the exact parameter set, and may expose confidential details in transit.
* **Give the Approver Decision-Grade Context:** Present the resolved parameters, the triggering policy rule, the material consequences, and independently sourced evidence relevant to the decision. The agent's stated rationale may be included but must be labelled as untrusted model output: it can be wrong, and under prompt injection it can be adversarially persuasive. Make reject, escalate, and stop at least as accessible as approve, and ensure approvers are trained for the action type and given adequate time, in line with human-oversight expectations on automation bias.
* **Enforce the Oversight Pattern Programmatically:** For maker-checker and dual-authorization patterns, programmatically prevent the requester (and the agent) from acting as checker, prohibit shared accounts, apply conflict-of-interest and delegation rules, and record the authenticated identity of every decision-maker.

### 4. Handling the Human Decision

* **Approve / Reject / Modify:** Support at minimum approve and reject. Treat any modification as a *new* action version: the original approval is invalidated, the modified action is re-validated and re-classified against the approval policy (it may require a different approval tier), and the record links the original and replacement actions. An approval must never be transferable to an action other than the exact version it was granted for.
* **Deadlines and Escalation:** Attach a deadline to every gated action. On expiry, reject by default or escalate to a higher tier per policy. Surface aging pending items so approval backlog is visible and does not become an operational bottleneck.
* **Feed Decisions Back:** Route decisions and any human rationale into the feedback and monitoring pipeline (`mi-11`, `mi-4`) so recurring rejections inform policy tuning, prompt changes, or narrowing of the agent's scope.

### 5. Standing Approval and Pre-Authorization

A decision may be granted ahead of time for a bounded class of actions rather than one action at a time. Agent tooling already in everyday use does this routinely: the human is prompted on first use and offered some form of "allow for this session", "always allow this tool", or an allowlist held in configuration. Pre-authorization is a legitimate form of the human decision and the control should express it rather than treat every unattended execution as a bypass. What separates an acceptable standing approval from a disabled gate is whether the grant is bounded, attributable, and made by someone entitled to make it.

* **Treat the Grant Itself as a Risk Acceptance:** Enabling standing approval for an action class is a risk acceptance and inherits the institution's rules on who may accept risk at what level. The operative question is not whether pre-approval is permitted, but whether the granting principal holds delegated authority for what the granted tool can reach in that environment. A grant can never exceed the grantor's own approval limit for that action class; where policy assigns an action class to maker-checker or dual authorization, a self-granted standing approval does not satisfy it; and where the grantor is not the accountable owner of the affected system, the grant requires that owner's authorization like any other standing instruction.
* **The Available Forms Are Not One Control:** Distinguish them explicitly, because they carry different authorization requirements. An allowlist set centrally by an administrator and distributed as managed configuration is institution-authored policy and the strongest form. A grant scoped to a named tool *and* constrained on its arguments is a bounded standing approval. A grant scoped to a tool name alone is bounded only by whatever that tool can reach. A session-wide setting that suppresses all prompting is not a standing approval but a suspension of the gate, defensible only where the whole session's blast radius is already bounded by its credentials and network reach. Policy should state which forms are available in which environments rather than leaving it to a client's defaults.
* **Grant Only Against a Bounded Effect Surface:** Standing approval is meaningful only where the tool's *definition*, not its arguments, bounds the effect. Narrow typed tools qualify: reading files inside a designated workspace, querying a read-only reporting view, raising a ticket. Generic capabilities do not. With shell execution, raw HTTP, database clients, or browser automation the parameters are the action, so a grant on the tool name is unbounded by construction and pre-approves anything reachable with the agent's credentials. Where such capabilities exist alongside governed effects they should remain per-action, or be replaced by narrow tools that carry the constraint in the tool definition. This is the same complete-mediation requirement as in *Defining What Requires Approval*.
* **Bound Scope, Environment, and Time:** A grant should name the tools and argument constraints it covers, the environment and credential set it applies to, and an explicit expiry, defaulting to session scope rather than indefinite persistence, and be revocable immediately. Pre-authorizing writes in a sandbox against non-production credentials is a different risk decision from pre-authorizing the same named tool where it reaches a production system; the same click must not be able to do both. Where the client cannot express environment as part of the grant, separate the environments by credentials and configuration instead.
* **Control Persistence and Inheritance:** Decide deliberately where a grant is stored and who inherits it. Grants written into repository configuration propagate to everyone who clones that repository and to any automation running from it, converting one person's local risk acceptance into a standing grant for a shared pipeline. Grants held in workstation configuration should not follow the work onto a shared runner or an unattended job. Managed configuration should be able to set a ceiling that user-level grants cannot widen.
* **Record the Grant as Approval Evidence:** Persist the grantor, the scope and argument constraints, the environment, the grant and expiry times, and any revocation, and link every action released under a grant back to it, so release under standing approval is distinguishable in the record from a per-action decision. An institution that cannot enumerate which actions executed under standing approval cannot evidence its human-oversight arrangements for them.
* **Never Let the Agent Obtain, Widen, or Match Its Own Grant:** Grants originate out of band, from the human or an administrator, through an interface the agent does not drive. Two paths matter. Content the agent has read can instruct the human to enable a standing grant, which turns a prompt injection into a durable authority grant rather than a single unauthorized action. And where grants are matched by display name, an agent able to register, alias, or wrap tools can route a governed action into an existing grant. Match grants against the same canonical action identity and policy version used for per-action decisions.
* **Review and Expire:** Standing grants accumulate and are rarely withdrawn. Review the population on the same cadence as the privilege model (`mi-18`), expire unused grants, and read growth in that population as a signal about gating thresholds rather than a settled state.

### 6. Recording the Approval Evidence

* **Minimum Evidence Set:** For each gated action, persist a tamper-evident record linking: the canonical action version and digest, the policy version and rule that triggered the gate, the agent and session identity, the authenticated approver identity (or identities), the decision including any modification linkage, the lifecycle state transitions with timestamps, and a correlation identifier into the execution trace. Broader audit concerns (retention, explainability, SIEM integration, evidentiary assurance) are the province of `mi-21` and `mi-4`; this control contributes the approval evidence they consume.
* **Tamper-Evidence vs. Non-repudiation:** These are distinct properties and both should be stated deliberately. Append-only storage and hash-chaining make the record *tamper-evident* (alteration is detectable). *Non-repudiation* (NIST AU-10) additionally requires a digital signature binding the record to the authenticated approver's identity or to an institutional signing key, with protected key material and trusted timestamps; hash-chaining alone does not provide it. Institutions claiming non-repudiation for approval records must implement and operate that identity binding.

### 7. Operational Safeguards

* **Availability of the Gate:** Because the gate is fail-closed, its own availability bounds the availability of gated workflows. Define availability targets, queue capacity, rate limiting, and admission controls; a flood of gated requests that exhausts approver capacity is a denial-of-service vector that deadlines alone do not prevent. Any break-glass contingency must be a separately authorized, dual-controlled manual procedure outside the agent path, logged and documented as an explicit risk exception, not a bypass the automated system can take.
* **Prevent Approval Fatigue:** Calibrate thresholds so the volume of gated actions stays meaningful. Over-gating produces rubber-stamping, which defeats the control; a sustained near-100% approval rate is itself a signal to investigate. Review gate hit-rates and rejection rates periodically. Broad standing approvals are the usual end state of this failure: where users routinely elect to stop being prompted for an action class, treat that as evidence the class was gated at the wrong threshold and re-examine the policy, rather than normalizing the grant.
* **Test the Adversarial Path:** Validate not only that legitimate actions are approved and executed, but that an agent cannot execute a gated action without approval, cannot reach the governed effect through an unmediated alternate path, cannot self-approve, cannot double-execute on retry, and cannot smuggle altered parameters past a decision made on an earlier version of the action.

---

## Challenges and Considerations

* **Latency vs. Control:** Gating introduces human-speed latency into otherwise autonomous workflows. Reserve gates for genuinely high-impact actions and keep low-risk paths unattended to preserve the value of automation.
* **Approver Availability and Coverage:** Round-the-clock or high-volume operations require sufficient approver coverage and escalation paths, or the fail-closed default will stall legitimate work.
* **Standing Approval in Everyday Tooling:** Much of the agent tooling already in use across an institution grants approval ahead of time by default rather than per action, and users will disable prompting for anything that interrupts routine work. The practical task is usually not introducing a gate where none exists, but bounding grants that are already in place: establishing which action classes may carry them, in which environments, under whose authority, and how they are recorded, so pre-approval becomes a deliberate risk acceptance rather than a client default.
* **Classification Accuracy:** The control is only as good as the policy that decides what to gate. Misclassification either lets material actions through or floods approvers; policy needs ownership and periodic review.
* **Correct Execution Semantics:** Durable suspend/resume across failures is easy to get subtly wrong, and double execution of an approved financial action is itself a serious incident. The resume path, the idempotency of downstream calls, and crash-recovery behaviour warrant explicit testing.
* **Relationship to Least Privilege:** `mi-18` requires human approval in several scenarios; this control defines the mechanism those requirements depend on. Assessing one without the other leaves either the boundary or the release protocol unexamined.

---

## Importance and Benefits

* **Prevents Unauthorized High-Impact Actions:** Stops materially consequential actions from being committed by an agent alone, even when the agent is operating inside its granted privileges (mitigates `ri-24`, and the subset of `ri-18` scope expansion that culminates in a mediated external action).
* **Supports Human-Oversight Obligations:** Provides a concrete, demonstrable technical measure that can form part of the human-oversight arrangements required for AI systems classified as high-risk under the EU AI Act (Article 14) and analogous supervisory expectations (`ri-22`). Statutory high-risk classification is distinct from an institution's own high-impact action designations; the gate serves both.
* **Enforces Segregation of Duties:** Ensures a distinct, authenticated principal authorizes actions that regulation or internal control requires not be fully automated, supporting applicable internal controls, including ICFR controls where the workflow is in scope.
* **Produces Audit-Ready Evidence:** Yields a tamper-evident, correlated record of what was proposed, who decided, and what executed, feeding the audit and explainability capabilities of `mi-21`.
* **Preserves Autonomy Where Safe:** Because it gates specific actions rather than whole agents, it lets institutions adopt autonomous agents for routine work while keeping a human decision on the small set of actions that truly need one.

---

## Additional Resources

* [Regulation (EU) 2024/1689 (EU AI Act), Article 14: Human Oversight](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
* [OWASP LLM06:2025 - Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
* [NIST SP 800-53 Rev. 5 - AC-5 Separation of Duties](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#!/control?version=5.1&number=AC-5)
* [NIST SP 800-53 Rev. 5 - AU-10 Non-repudiation](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#!/control?version=5.1&number=AU-10)
