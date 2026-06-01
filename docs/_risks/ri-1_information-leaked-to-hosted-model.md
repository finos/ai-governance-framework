---
sequence: 1
title: Information Leaked To Hosted Model
layout: risk
doc-status: Approved-Specification
type: RC
owasp-llm_references:
  - llm02-2025  # LLM02:2025 Sensitive Information Disclosure
nist-ai-600-1_references:
  - 2-4  # 2.4. Data Privacy
  - 2-9  # 2.9. Information Security
ffiec-itbooklets_references:
  - sec-2  # SEC: II Information Security Program Management
  - sec-3  # SEC: III Security Operations
  - ots-2  # OTS: Risk Management
eu-ai-act_references:
  - c3-s2-a10  # III.S2.A10: Data and Data Governance
  - c3-s2-a13  # III.S2.A13: Transparency and Provision of Information to Deployers
  - c5-s2-a53  # V.S2.A53: Obligations for Providers of General-Purpose AI Models
csa-ciro-canada_references:
  # Securities cyber and outsourcing
  - csa-sn-11-348        # Explicitly flags privacy law implications of inputting client info into third-party AI
  - csa-sn-11-326         # CSA Cyber Security (2013) — first cross-sectoral cyber guidance
  - csa-sn-11-332         # CSA Cyber Security (2016) — follow-up cyber risk expectations
  - csa-sn-33-321         # CSA Cyber Security and Social Media (2017) — IFMs, PMs, EMDs
  - ni-31-103             # s. 11.1 (compliance system), s. 11.5 (records confidentiality), outsourcing
  - ni-31-103cp           # CP Part 11 — outsourcing accountability for client info transferred to AI provider
  - ciro-idpc-rules       # Rule 3800 (recordkeeping/confidentiality) — client info in AI-enabled workflows
  - ciro-gn-2300-21-003   # Outsourcing Arrangements — confidentiality, cross-border due diligence
  # Tier 3 benchmarks
  - osfi-b-13             # OSFI B-13 Technology and Cyber Risk Management — data confidentiality (FRFIs)
  - iosco-fr-02-2026      # Toolkit Section 3.2 — third-party data security considerations
  # Tier 4 — primary privacy framework
  - pipeda                # PIPEDA 4.1.3 (third-party accountability), 4.7 (safeguards), s. 10.1 (breach notification)
  - qc-p39-s12-1          # Quebec Law 25 s. 12.1 — ADM transparency includes disclosing personal info used
  - qc-p39-s3-3-s17       # Quebec Law 25 ss. 3.3, 17 — PIAs for AI processing, cross-border adequacy
related_risks:
  - ri-2   # Information Leaked to Vector Store
  - ri-23  # Intellectual Property and Copyright
---
## Summary

Using third-party hosted LLMs creates a **two-way trust boundary** where neither inputs nor outputs can be fully trusted. Sensitive financial data sent for inference may be memorized by models, leaked through prompt attacks, or exposed via inadequate provider controls. This risks exposing customer PII, proprietary algorithms, and confidential business information, particularly with free or poorly-governed LLM services.

## Description

A core challenge arises from the nature of interactions with external LLMs, which can be conceptualized as a **two-way trust boundary**. Neither the data inputted into the LLM nor the output received can be fully trusted by default. Inputs containing sensitive financial information may be retained or processed insecurely by the provider, while outputs may inadvertently reveal previously processed sensitive data, even if the immediate input prompt appears benign.

Several mechanisms unique to or amplified by LLMs contribute to this risk:

*   **Model Memorization**: LLMs can [memorize](https://arxiv.org/pdf/2310.18362) sensitive data from training or user interactions, later disclosing customer details, loan terms, or trading strategies in unrelated sessions—even to different users. This includes potential cross-user leakage, where one user's sensitive data might be disclosed to another.

*   **Prompt-Based Attacks**: Adversaries can craft prompts to extract memorized sensitive information (see ri-10).

*   **Inadequate Data Controls**: Insufficient sanitization, encryption, or access controls by providers or institutions increases disclosure risk. Hosted models may not provide transparent mechanisms for how input data is processed, retained, or sanitized, increasing the risk of persistent exposure of proprietary data.

The risk profile can be further influenced by the provider's data handling practices and the specific services utilized:

*   **Provider Data Practices**: Without clear contracts ensuring encryption, retention limits, and secure deletion, institutions lose control over sensitive data. Providers may lack transparency about data processing and retention.

*   **Fine-Tuning Risks**: Using proprietary data for fine-tuning embeds sensitive information in models, potentially accessible to unauthorized users if access controls are inadequate.

Enterprise LLMs typically offer better protections (private endpoints, no training data usage, encryption) than free services, which often use input data for model improvements. Thorough due diligence on provider practices is essential.

This risk is aligned with OWASP’s [LLM02:2025 Sensitive Information Disclosure](https://genai.owasp.org/llmrisk/llm02-sensitive-information-disclosure/), which highlights the dangers of exposing proprietary or personally identifiable information (PII) through large-scale, externally hosted AI systems.

### Consequences

The consequences of such information leakage for a financial institution can be severe:
* **Breach of Data Privacy Regulations:** Unauthorized disclosure of PII can lead to significant fines under regulations like GDPR, CCPA, and others, alongside mandated customer notifications.
* **Violation of Financial Regulations:** Leakage of confidential customer information or market-sensitive data can breach specific financial industry regulations concerning data security and confidentiality (e.g., GLBA in the US).
* **Loss of Competitive Advantage:** Exposure of proprietary algorithms, trading strategies, or confidential business plans can erode a firm's competitive edge.
* **Reputational Damage:** Public disclosure of sensitive data leakage incidents can lead to a substantial loss of customer trust and damage to the institution's brand.
* **Legal Liabilities:** Beyond regulatory fines, institutions may face lawsuits from affected customers or partners.

## Links

- [FFIEC IT Handbook](https://ithandbook.ffiec.gov/)
- [Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035)
