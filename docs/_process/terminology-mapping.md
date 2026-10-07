# Terminology Mapping

Shared glossary reconciling common governance terms with FINOS / NIST / EU AI Act / OWASP language.

| Common Term | Definition (plain language) | Equivalent / Related Terms | Framework Reference |
| --- | --- | --- | --- |
| Inherent Risk | Exposure before mitigating controls are credited. | Gross risk; pre-control risk | ISO 31000; NIST AI RMF (Map) |
| Residual Risk | Exposure remaining after controls are applied. | Net risk; managed risk | ISO 31000; NIST AI RMF (Manage) |
| Likelihood | Probability the risk event occurs in the assessment period. | Probability; frequency | 5×5 matrix (this register) |
| Impact | Severity of consequence if the event occurs. | Consequence; severity; magnitude | 5×5 matrix (this register) |
| Risk Rating | Band (Low/Moderate/High/Critical) derived from the score. | Risk level; severity tier | FINOS heuristic tiers |
| Risk Tolerance | Level of residual risk the organisation will accept. | Risk appetite; acceptance threshold | NIST AI RMF (Govern) |
| Deployment Gate | Go/no-go control point comparing residual risk to tolerance. | Release gate; approval gate; stage gate | FINOS adoption path |
| Hallucination | Confident but fabricated/incorrect model output. | Confabulation; ungrounded output | FINOS AIR-OP-004 |
| Model Drift | Decline in performance as data diverges from training. | Concept drift; data drift; model aging | FINOS AIR-OP-019 |
| Explainability | Ability to interpret and justify a model's decisions. | Interpretability; transparency | FINOS AIR-OP-017; EU AI Act Art.13 |
| Prompt Injection | Crafted input overriding intended model instructions. | Jailbreak (direct); indirect injection | FINOS AIR-SEC-010; OWASP LLM01 |
| Data Poisoning | Tampering with training/retrieval data to corrupt behaviour. | Training-data attack | FINOS AIR-SEC-009; MITRE ATLAS |
| Excessive Agency | Agent acting beyond intended authority or scope. | Authorization bypass; over-permissioning | FINOS AIR-SEC-024; OWASP LLM06 |
| Agentic AI | AI that plans, decides, and acts autonomously via tools. | Autonomous agent; tool-using agent | FINOS AIGF v2 agentic set |
| MCP | Model Context Protocol — standard for extending agent tools/data. | Tool server; context server | FINOS AIR-SEC-026 |
| Tool Chain | Sequence of tools/APIs an agent invokes to complete a task. | Action chain; tool orchestration | FINOS AIR-SEC-025 |
| Trust Boundary | Point where data/control crosses between trust zones. | Security boundary; isolation boundary | FINOS AIR-SEC / AIR-OP-028 |
| Human-in-the-Loop | Human review/approval inserted into the decision flow. | HITL; human oversight | EU AI Act Art.14; FINOS controls |
| DPIA | Data Protection Impact Assessment for privacy risk. | Privacy impact assessment (PIA) | GDPR Art.35; FINOS AIR-RC-001 |
| FRIA | Fundamental Rights Impact Assessment for high-risk AI. | Rights impact assessment | EU AI Act Art.27 |
| Model Risk Management | Governance of model development, validation, monitoring. | MRM; model governance | PRA SS1/23; SR 11-7 |
| Control Effectiveness | How well existing controls reduce the inherent risk. | Control maturity; mitigation strength | This register (residual logic) |
