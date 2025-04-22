---
layout: mitigation
doc-status: Draft
sequence: 7
type:
  - Preventative
mitigates:
  - ri-1
title: Legal/contractual agreements
---

This control is about legal agreements between the SaaS inference provider and the organization. Those legal agreements not only have to exists, but have to be understood by the organization to make sure they comply with all requirements.

Requirements may include:
- Legal deparment would specify data governance, privacy and realted requiments.
- Guidance from your AI governance body and ethics committee.
- Explainability requirements
- Conforming to tools and test requirements for addressing responsible and complaint AI.

Legal agreement should explain these questions:
- Can the SaaS vendor provide information on what data was used to train the models.
  - Imdemnity protections: Does provider guarantees any imdemnity protections, for example if copyrighted materials were used to train the models.
- Understand contractually what the SaaS provider does with any data you send them. The following are questions to consider:
  - Does SaaS provider persist prompts/completions? If they do persist, for how much time?
  - How data is safeguarded in that case? How is its privacy preserved?
  - How are they used? Are they used to further train models?
  - Is this data being shared with others? In what ways?
  - Does the provider have the ability to honor data sovereignty requirements of different jurisdictions? For example, if EU client/user data should be stored in EU.
- Privacy policy: Legal contract should clearly state how in what form data sent and prompts are used by the provider.
  - Does the usage of data meet regulatory requirements, like GDPR? What kind of consent is required? How consent is obtained and stored from users?
- Legal contract should state the policy about model versioning and changes, and inform clients to ensure that foundational models don't drift or change in unexpected ways.
