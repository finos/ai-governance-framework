---
sequence: 9
title: Data Poisoning
layout: risk
doc-status: Draft
type: SEC
external_risks:
  - OWASP-LLM_2025_LLM03  # OWASP LLM: Supply Chain Vulnerabilities
  - OWASP-LLM_2025_LLM04  # OWASP LLM: Data and Model Poisoning
  - OWASP-LLM_2025_LLM05  # OWASP LLM: Improper Output Handling
  - OWASP-LLM_2025_LLM06  # OWASP LLM: Excessive Agency
ffiec_references:
  - ffiec_sec_iii-security-operations
  - ffiec_dam_iii-risk-management-of-development-acquisition-and-maintenance
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai-act_references:
  - c3-s2-a10  # III.S2.A10 Data and Data Governance
  - c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - c5-s2-a53  # V.S2.A53 Obligations for Providers of General-Purpose AI Models
---
## Summary

Data poisoning occurs when adversaries tamper with training or fine-tuning data to manipulate an AI model’s behaviour, often by injecting misleading or malicious patterns. This can lead to biased decision-making, such as incorrectly approving fraudulent transactions or degrading model performance in subtle ways. The risk is heightened in systems that continuously learn from unvalidated or third-party data, with impacts that may remain hidden until a major failure occurs.

## Description

Data poisoning refers to the deliberate manipulation of training or fine-tuning datasets with the goal of influencing or corrupting the behaviour of an AI model. Adversaries may introduce subtle patterns or maliciously crafted examples into the training data, which remain hidden during validation but activate under specific conditions. For example, fraudsters might inject fake records into transaction logs that mislabel fraudulent activity as legitimate, leading the model to internalize incorrect associations and reduce its ability to detect real fraud.

Poisoning can also introduce systematic biases into models. In a credit scoring system, adversaries may bias training data to favour certain fraudulent profiles or unfairly disadvantage legitimate applicants, causing inaccurate or discriminatory outcomes. This risk is particularly acute in systems that support continuous or online learning, where models ingest and adapt to new data in real time without rigorous human review or validation.

The use of third-party or crowd-sourced datasets further increases exposure, as these sources may be compromised or manipulated before ingestion. Poisoned inputs from such sources can propagate unnoticed through the training pipeline, embedding vulnerabilities or performance degradation into production models. Critically, the effects of data poisoning are often difficult to detect and may only surface during high-impact incidents—such as regulatory failures, financial loss, or safety-critical system errors.

## Links

* [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733) – Early research demonstrating how poisoned data can introduce backdoors.
* [How to Poison the Data That Teach AI](https://www.scientificamerican.com/article/how-to-poison-the-data-that-teach-ai/) – Popular science article explaining data poisoning for general audiences.
* [MITRE ATLAS – Training Data Poisoning](https://atlas.mitre.org/techniques/T0021) – Official MITRE page detailing poisoning techniques in adversarial AI scenarios.
* [Poisoning Attacks Against Machine Learning – CSET](https://cset.georgetown.edu/publication/poisoning-attacks-against-machine-learning/) – Policy-focused report exploring implications of poisoning on national security and critical infrastructure.
* [Clean-Label Backdoor Attacks](https://arxiv.org/abs/2008.04333) – Describes attacks where poisoned data looks legitimate to human reviewers but still misleads models.

