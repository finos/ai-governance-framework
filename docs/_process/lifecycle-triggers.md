# Lifecycle Triggers — When to (Re)assess

| Lifecycle Stage | Trigger / Event | Required Action | Risks Most Affected |
|---|---|---|---|
| Onboarding / Intake | New AI use case proposed or new model/vendor introduced | Run full register assessment, classify data & autonomy, set initial tolerance | All — establishes baseline |
| Onboarding / Intake | Use case involves PII/PHI or confidential data | Trigger DPIA, score privacy & leakage risks, legal review | R-12, R-13, R-24, R-23 |
| Design / Build | Architecture adds RAG, vector store, or external knowledge base | Assess embedding leakage & data-filtering controls | R-13, R-05, R-09 |
| Design / Build | Agentic capability, tool use, or MCP servers introduced | Score full agentic risk set, define scoped permissions & approval gates | R-11, R-17, R-18, R-19, R-20, R-21 |
| Pre-Deployment Gate | Readiness for production sign-off | System-acceptance testing, residual scoring, gate decision vs tolerance | All applicable |
| Pre-Deployment Gate | High-risk classification under EU AI Act (e.g. credit, fraud) | Fundamental Rights Impact Assessment, enhanced documentation | R-06, R-07, R-22, R-24 |
| Production / Operate | Foundation model version change or silent provider update | Regression test; re-validate; update version pin | R-02, R-03, R-05 |
| Production / Operate | Data drift / accuracy decay detected by monitoring | Re-score accuracy & drift; schedule retraining/refresh | R-01, R-09, R-05 |
| Production / Operate | Scope expansion — model used beyond validated purpose | Re-assess overreach & alignment; re-baseline use case | R-08, R-05 | 
| Production / Operate | Security event: prompt injection, poisoning, or agent anomaly | Invoke incident response; re-score affected security risks | R-16, R-15, R-17, R-18, R-20, R-21 |
| Periodic Review | Scheduled quarterly / annual governance review | Refresh all scores; verify control effectiveness; re-confirm owners | All | 
| Periodic Review | Regulatory change (new law, guidance, or enforcement) | Re-map use cases to regulation; reassess compliance posture | R-22, R-23, R-24, R-07 | 
| Decommission | Model retirement or replacement | Confirm data deletion, access revocation, dependency removal | R-12, R-13, R-21, R-24 | 
| Production / Operate | Model drift detection — monitoring flags statistical drift in inputs, outputs, or feature distributions | Re-score drift & accuracy; investigate root cause; schedule retraining / refresh; re-validate against current data | R-09, R-01, R-05, R-03 | 
| Production / Operate | Incorrect outcomes — material wrong decisions, customer complaints, or failed back-testing observed | Quarantine affected outputs; re-score accuracy & alignment; root-cause analysis; corrective action before resuming | R-01, R-05, R-06, R-10 | 
| Production / Operate | New dataset introduced — new training, fine-tuning, retrieval, or third-party data source added | Assess data quality, classification, lineage & poisoning exposure; DPIA if PII/PHI; re-baseline affected risks | R-09, R-13, R-15, R-24, R-23 | 
| Incident-Triggered Review | AI incident raised — safety, security, privacy, fairness, or availability event involving the system | Invoke incident response; classify severity; re-score impacted risks; capture lessons; feed control improvements | All impacted — scope to incident type | 
| Incident-Triggered Review | Near-miss or guardrail bypass — control caught an unsafe action, or an attempted injection/jailbreak detected | Log near-miss; test guardrail efficacy; re-score affected security risks; strengthen controls | R-16, R-17, R-18, R-20 | 
| Incident-Triggered Review | External signal — vendor breach, disclosed model vulnerability, or sector-wide incident affecting your stack | Assess exposure to disclosed issue; re-score supply-chain & dependency risks; apply patches / mitigations | R-14, R-15, R-19, R-04, R-12 |
| Incident-Triggered Review | Post-incident closure — remediation completed after any of the above | Verify residual risk reduced; confirm control effectiveness re-rated; update register & owner sign-off | All previously impacted | 
| Pre-Deployment Gate | Connected / multi-agent chain — one agent depends on another's outcome | MANDATORY enhanced pre-release review: validate inter-agent contracts, corrupt-input handling, rollback/checkpoint plan, chain kill-switch, and cascade detection | R-29, R-30, R-31, R-11, R-25 | 
| Pre-Deployment Gate | Autonomous decision-making capability proposed | Review decision-rights matrix, autonomy tier, fail-safe/abstain path, and kill-switch before sign-off | R-25, R-26, R-28 | 
| Periodic Review | Benchmark reassessment due (per section / per stage cadence) | Recompute section & stage benchmarks; investigate any GAP status; recalibrate targets if the benchmark itself is stale | All — via Benchmarks tab | 
| Periodic Review | Coverage gap identified — exposure with no matching FINOS AIR risk | Log in Gap Register; add new register row with Coverage=GAP; disposition; feed material gaps back to FINOS community | New / emerging risks | 
| Incident-Triggered Review | New vulnerability discovered — CVE, red-team finding, or disclosed model/agent/dependency weakness against a deployed system | Score with CVSS v4.0; classify Critical/High/Medium/Low; apply interim control (isolate/kill-switch if Critical); remediate within SLA; re-score affected register risks | R-14, R-16, R-17, R-19, R-32, R-33 | 