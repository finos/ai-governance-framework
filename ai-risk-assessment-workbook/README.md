# AI Governance Risk Register & Scoring Methodology

*Based on the FINOS AI Governance Framework (AIGF)*

This document explains the methodology behind the accompanying workbook (`AIGF_Risk_Register.xlsx`). It is intended for AI governance practitioners, risk and compliance teams, and the wider community aligned with FINOS framework. It is vendor agnostic and free to adapt.

---

## 1. Why this register exists.

Most AI risk inventories are either too abstract ("AI might be biased") to act on, or too bespoke to share. This register takes a middle path: attempted mappings made to a **canonical FINOS AIGF risk ID**, so a finding raised in one organization implies the same thing in another, and stays traceable to an open, community-maintained source. The framework currently spans operational, security, and regulatory domains, including an agentic-AI risk set to cover autonomous systems that use tools.

The workbook attempts to turn the catalog into an operational asset comprising of a scored register, a deployment gate, lifecycle triggers, and a shared glossary.

---

## 2. The scoring approach

### Inherent risk = Likelihood × Impact

Each risk is scored on two independent axes levels 1-5, and the matrix creates a 1–25 inherent score. The anchors are intentionally behavioral rather than numeric so two assessors can land in the same place.

**Likelihood scores of 1-5:** Rare → Unlikely → Possible → Likely → High Probability (Certainty).
**Impact scores of 1-5:** Insignificant → Minor → Moderate → Major → Severe.

Full descriptor anchors are on the *Scoring Approach* tab and visualized on the *Scoring Matrix* tab. The scoring matrix is to be changed - the lookup table will use the CVSS severty bands to align with industry available methodology

### Rating bands

| Range | Rating | Governance consideration |
|------|--------|--------------------|
| 1–4 | Low | Acceptable with baseline controls and routine oversight |
| 5–9 | Moderate | Acceptable with standard guardrails, monitoring, periodic review |
| 10–15 | High | Deploy only with mandatory controls, approval gates, active monitoring |
| 16–25 | Critical | Do not deploy as-is; redesign to reduce exposure or require human-in-the-loop Go-no-go. (if deployed - Kill)|

### Control effectiveness → residual risk

Rate the effectiveness of existing controls on a 1-5 scale (1 = Ineffective through 5 = Fully effective). reduces exposure. 	
Residual Score = Inherent Score × Mitigation Factor, where the increase in controls recudce exposure.	
Governance forum reviews and escalates/makes decision on residual risk.	

| Level | Effectiveness Level Rating | Implication | Factor |
|---------------|---------|--------|
| 1 | Ineffective | Controls absent or untested | ×1.00 |
| 2 | Limited | Partial / ad-hoc | ×0.80 |
| 3 | Moderate | Standard, some gaps | ×0.60 |
| 4 | Strong | Robust, tested | ×0.40 |
| 5 | Fully effective | Comprehensive, continuously assured | ×0.25 |

**Residual Score = Inherent Score × Mitigation Factor**, then re-banded against the same table. The workbook computes this automatically.

### Risk Tolerance Deployment Gate (go-no-go)

Residual rating drives a go/no-go decision and the sign-off it requires:

| Residual rating | Tolerance Stance | Rating | Gate | Sign-off |
|-----------------|--------|------|----------|
| Low | Accept | PASS | Product / risk owner |
| Moderate | Accept w/ monitoring | PASS| with conditions | AI governance lead |
| High | Mitigate before deploy | CONDITIONAL | controls needed | Governance forum / CRO delegate |
| Critical | Avoid / redesign | FAIL | block / Kill | Governance forum + accountable executive |

Tolerance bands are a starting point — calibrate them to your own risk appetite.

---

## 3. What's in the register

31 risks across four core domains, plus seven added by stack-coverage validation (see 6c) — 38 in total — each carrying its FINOS reference, description, potential impact, inherent and residual scoring, existing controls, **addressing the risk**, **FINOS coverage**, **stack layer**, owner, and status.

Possible categorization
- **Operational (11):** hallucination, model versioning, non-determinism, availability, alignment, bias, explainability, overreach, data drift, reputational risk, multi-agent trust boundaries.
- **Security (10):** leakage to hosted models and vector stores, model tampering, data poisoning, prompt injection, and the agentic set — authorization bypass, tool-chain injection, MCP supply-chain compromise, state-persistence poisoning, credential harvesting.
- **Regulatory (3):** regulatory compliance & oversight, IP & copyright, data-protection & privacy compliance.
- **Agent Operations (7):** the agent-specific and connected-agent risks — see section 3a.

Input cells (Likelihood, Impact, Control Effectiveness, Treatment, Status) are shaded; every score, rating, and rollup is a live formula. Color-coded conditional formatting flags ratings automatically.

## 3a. Agent Operations risks

These cover behaviors that emerge once models act autonomously and depend on each other:

- **R-25 Autonomous Decision-Making Beyond Mandate** — agent decides/acts outside its approved decision rights.
- **R-26 Outcome Deviation & Detection Gap** — outputs drift from expected outcomes and detection lags (especially when the agent self-reports success).
- **R-27 Pattern-Shift Rejected as Anomaly** — a genuine new-normal data shift is rejected as an anomaly, so the agent fails to adapt and acts on stale normalized values.
- **R-28 Fabricated Outcome Under Inability to Respond** — when the agent can't produce a valid answer it guesses/fabricates instead of failing safe (rated Critical).
- **R-29 Cascading Deviation in Connected Agents (No Rollback)** — a dependent agent ingests corrupt/skewed/fabricated input and propagates a hard-to-detect sequence of deviations with no rollback path. Requires mandatory pre-release review.
- **R-30 Result Skew from Upstream Agent Non-Response** — upstream agent times out / returns empty; the dependent agent proceeds on incomplete input and skews its result.
- **R-31 Corrupt-Input Propagation Across Agent Trust Boundary** — a dependent agent implicitly trusts an upstream agent and lets corruption cross the trust boundary.

Connected-agent chains and autonomous-decision capabilities both trigger an enhanced **pre-deployment review** (see the Lifecycle Triggers tab).

## 3b. Risk treatment, acceptance & removal, and the kill-switch

The **Risk Treatment** tab defines four treatment options set per risk in the register — **Mitigate / Reduce, Transfer, Avoid / Remove, Accept** — and the explicit criteria for each:

- **Acceptance criteria** (all must hold): residual within tolerance; mitigations applied or consciously deferred; named owner and required sign-off; monitoring and triggers defined; a time-bound review/expiry date; documented in the register.
- **Removal / avoidance criteria** (any one triggers): residual stays Critical after mitigation and human-in-the-loop can't reduce it; the risk can't be detected or rolled back reliably; mitigation cost outweighs value; a legal/regulatory/ethical bar; or no owner will accept it.

The **kill-switch / complete termination** is documented as a control of last resort — a pre-defined, tested mechanism to immediately halt an agent, break a connected-agent chain, or fully terminate a deployment and fail to a safe state. It is required for any High/Critical residual system, all autonomous-action agents, and all connected-agent chains, with defined invocation triggers (out-of-mandate action, outcome-deviation threshold breach, repeated fabrication, cascading deviation, corrupt input crossing a trust boundary, security incident, or regulatory direction to stop). It must default to fail-safe, sit outside the agent's own decision loop, log every invocation, and be tested before release.

---

## 4. Lifecycle triggers

A register is only useful if it is re-run at the right moments. The *Lifecycle Triggers* tab maps concrete events to the action required and the risks each event most affects, across seven stages: **Onboarding/Intake → Design/Build → Pre-Deployment Gate → Production/Operate → Incident-Triggered Review → Periodic Review → Decommission.**

Examples: introducing agentic capability or MCP servers triggers the full agentic risk set; a connected/multi-agent chain or an autonomous-decision capability triggers a mandatory enhanced pre-release review; model-drift detection, observed incorrect outcomes, and a new dataset introduction each trigger a targeted re-assessment; an AI incident, near-miss/guardrail bypass, or external signal (vendor breach, disclosed vulnerability) triggers an incident review; a regulatory change triggers a use-case-to-regulation re-mapping; model retirement triggers data-deletion and access-revocation checks.

---

## 5. Terminology mapping

The *Terminology Mapping* tab reconciles everyday governance language with FINOS / NIST AI RMF / EU AI Act / OWASP terms — so "gross risk," "inherent risk," and "pre-control risk" are understood as one concept, and terms like *excessive agency*, *MCP*, *FRIA*, and *model drift* carry a plain-language definition plus their framework reference. Use it to align stakeholders who come from security, privacy, model-risk, and compliance backgrounds.

---

## 6. Assessment summary

The *Assessment Summary* tab is a live rollup: counts and average inherent/residual scores by domain, a distribution by residual rating, and key indicators (highest residual score, count of High/Critical residual risks, count mitigated to Low). It recalculates as register scores change, giving a governance forum a one-glance posture.

---

## 6a. Benchmarks — define, measure, reassess

A score is a point-in-time reading; a **benchmark** is the target you hold it against. The *Benchmarks* tab introduces benchmarks at two levels:

- **Section benchmarks (per domain):** e.g. *average residual score ≤ 8* for Operational, Security, and Agent Operations, *≤ 7* for Regulatory. The "current" value is pulled live from the register, and the status auto-flags **Met** or **GAP**. A coverage benchmark also tracks *open FINOS gaps not yet reviewed = 0*.
- **Stage benchmarks (per lifecycle stage):** e.g. *gate pass-rate at first submission ≥ 90%*, *% connected-agent chains with rollback + kill-switch tested = 100%*, *mean time to detect outcome deviation ≤ 24h*, *% retirements with data deletion verified = 100%*. Targets and measured values are entered from your process metrics.

Each benchmark carries a **reassessment cadence** and owner. Benchmarks are versioned by baseline date so that drift in the benchmark itself stays visible — reassess them on cadence and whenever a lifecycle trigger fires (two new triggers, *benchmark reassessment due* and *coverage gap identified*, are in the Lifecycle Triggers tab).

## 6b. Gap identification — when FINOS doesn't cover it

FINOS is comprehensive but not exhaustive, and your use cases will surface exposures it doesn't yet name. The workbook makes that explicit:

- Every register row now carries a **FINOS Coverage** flag: **FINOS** (directly mapped to an AIR risk), **FINOS-adjacent** (extends/derives from one or more AIR risks), or **GAP** (no matching FINOS risk — a local addition). GAP rows are highlighted in magenta.
- The **Gap Register** tab logs each identified gap: how it was surfaced (benchmark, lifecycle trigger, incident, assessment), why no existing FINOS AIR risk covers it, its disposition, and the register ID it became. Three current gaps are recorded — pattern-shift-rejected-as-anomaly (R-27), fabricated-outcome-under-inability (R-28), and corrupt-input-propagation-across-trust-boundary (R-31) — plus a template row for the next one.

The intended loop: a benchmark or trigger surfaces an exposure → log it in the Gap Register → add a register row flagged `GAP` → disposition and treat it → feed material gaps back to the FINOS community so the open framework improves.

## 6c. Stack coverage validation — register vs business / technology architecture

The register can be validated against an enterprise AI architecture, not just the FINOS catalogue. Every risk now carries a **Stack Layer** tag (L1–L10) mapping it to the ten-layer AI stack — from hardware (L1) through serving, orchestration, and application up to the end user (L10) — and its parallel business architecture. The *Stack Coverage Validation* tab lays the register against that stack: for each layer it shows the business function, the technology layer, the layer-level risk the architecture asserts, the register risks that cover it, and a coverage verdict (**Covered / Partial → Closed / Gap → Closed**).

This surfaced a clear pattern: FINOS is strong at the model, data, orchestration, and agent layers (L4–L9) but thin or silent at the **infrastructure and supply layers (L1–L3)** and at **business-outcome / ROI (L10)**, and only partial on **data-pipeline specifics (L5)**. Seven risks were added to close those gaps, in three new domains:

- **Infrastructure & Supply:** R-32 Compute Supply Chain & Concentration (L1), R-33 Infrastructure Resilience & DR Gap (L2), R-34 Cloud Cost Overrun & FinOps / Denial-of-Wallet (L3), R-35 Vendor Lock-in & Concentration (L3).
- **Data Pipeline:** R-36 Training-Serving Skew & Feature Drift (L5), R-37 Data Lineage & Provenance Gap (L5).
- **Business Outcome:** R-38 Strategic Misalignment & Failed ROI (L10).

Each is flagged `GAP` (or `FINOS-adjacent`) in the FINOS Coverage column and logged in the Gap Register (G-04 to G-07). With these added, all ten stack layers carry at least one mapped risk. The data-risk layers (L4–L5) are highlighted in red on the validation tab, mirroring the architecture's elevated data-risk zone — consistent with the principle that data risk is upstream, invisible at the moment of harm, and expensive to remediate.

## 7. Adapting this for your organization

- **Tolerance is yours to set.** The gate thresholds above reflect a moderately conservative stance; adjust them.
- **Scope before you score.** Not every risk applies to every use case — select the relevant subset based on data classes, autonomy level, and external exposure.
- **Keep it traceable.** When you add a risk, map it to a FINOS ID where one exists; if none does, flag it `GAP`, log it in the Gap Register, and consider contributing it back to FINOS.
- **Pair risks with controls.** FINOS publishes a parallel mitigation catalogue (`AIR-PREV-*`, `AIR-DET-*`); link your chosen controls back to it.

---

*Source: FINOS AI Governance Framework v2, air-governance-framework.finos.org (October 2025). This edition is a community resource and is not a substitute for legal or regulatory advice.*
