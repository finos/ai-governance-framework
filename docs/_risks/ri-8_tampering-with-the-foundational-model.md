---
sequence: 8
title: Tampering With the Foundational Model
layout: risk
doc-status: Draft
type: SEC
external_risks:
  - OWASP-LLM_2025_LLM03  # OWASP LLM: Supply Chain Vulnerabilities
  - OWASP-LLM_2025_LLM05  # OWASP LLM: Improper Output Handling
ffiec_references:
  - ffiec_sec_iii-security-operations
  - ffiec_ots_risk-management
  - ffiec_dam_iii-risk-management-of-development-acquisition-and-maintenance
  - ffiec_dam_vi-acquisition
eu-ai_references:
  - eu-ai_c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - eu-ai_c3-s3-a16  # III.S3.A16 Obligations of Providers of High-Risk AI Systems
  - eu-ai_c5-s2-a53  # V.S2.A53 Obligations for Providers of General-Purpose AI Models
---

The SaaS-based LLM provider is a 3rd party supplier and as such is subject to all typical supply chain, insider, and software integrity
threats. Supply chain attacks on infrastructure and OSS are covered in other frameworks, however supply chains for
foundational models, training data, model updates, and model retraining are all potential targets for attackers. 
The underlying firmware of GPUs, the operating system, and the machine learning libraries should be considered as part
of the supply chain too.

Whilst fine tuning is out of scope of this framework; it is worth noting that adversarial attacks can be built upon 
model weights for open source models. There could be a possibility of malicious actors using this information to induce unsafe
behaviour in the model.

Similarly, back doors engineered into the model can be triggered through malicious means. This could result in unsafe behaviour
or such tampering could result in removing safe guards around the model.
