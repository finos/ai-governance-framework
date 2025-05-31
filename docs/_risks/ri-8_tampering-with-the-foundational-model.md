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
eu-ai-act_references:
  - c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - c3-s3-a16  # III.S3.A16 Obligations of Providers of High-Risk AI Systems
  - c5-s2-a53  # V.S2.A53 Obligations for Providers of General-Purpose AI Models
---

## Summary

Foundational models provided by third-party SaaS vendors are vulnerable to supply chain risks, including tampering with training data, model weights, or infrastructure components such as GPU firmware and ML libraries. Malicious actors may introduce backdoors or adversarial triggers during training or fine-tuning, leading to unsafe or unfiltered behaviour under specific conditions. Without transparency or control over model provenance and update processes, consumers of these models are exposed to upstream compromises that can undermine system integrity and safety.

## Description

The use of Software-as-a-Service (SaaS)-based LLM providers introduces foundational models as third-party components, subject to a range of well-known supply chain, insider, and software integrity threats. While traditional supply chain risks associated with infrastructure, operating systems, and open-source software (OSS) are covered in established security frameworks, the emerging supply chain for LLMs presents new and underexplored attack surfaces. These include the training data, pretrained model weights, fine-tuning datasets, model updates, and the processes used to retrain or adapt models. Attackers targeting any point in this pipeline may introduce subtle but dangerous manipulations.

The broader infrastructure supporting LLMs must also be considered part of the model supply chain. This includes GPU firmware, underlying operating systems, cloud orchestration layers, and machine learning libraries (e.g., TensorFlow, PyTorch, CUDA). Compromises in these components—such as malicious firmware, modified libraries, or vulnerabilities in execution environments—can enable tampering with the model or its runtime behaviour without detection.

Even though fine-tuning is out of scope for many frameworks, it introduces a powerful vector for adversarial manipulation. In open-source contexts, where model weights are accessible, attackers can craft subtle adversarial modifications that influence downstream behaviour. For example, embedding malicious data during fine-tuning could cause a model to exhibit unsafe responses or bypass content filters under specific conditions. These alterations are difficult to detect and may persist undetected until triggered.

An even more insidious risk involves backdoor attacks, where a model is intentionally engineered to behave maliciously when presented with a specific trigger phrase or input pattern. These triggers may activate offensive outputs, bypass ethical constraints, or reveal sensitive internal information. Such tampering may also be used to disable safety mechanisms—effectively neutralizing alignment or content moderation systems designed to enforce responsible model behaviour.

In a SaaS deployment context, organisations rely entirely on the integrity and transparency of the model provider. Without guarantees around model provenance, update controls, and tamper detection mechanisms, customers are exposed to the consequences of upstream compromises—even if they have robust controls in their own environments.

## Links

* [Trojaning Language Models with Hidden Triggers (Backdoor Attacks)](https://arxiv.org/abs/2008.00312) – arXiv paper detailing how backdoors can be inserted into NLP models.
* [Poisoning Language Models During Instruction Tuning](https://arxiv.org/abs/2305.11491) – Explores how attackers can poison open-source models via instruction tuning.
* [AI Supply Chain Security (CISA)](https://www.cisa.gov/resources-tools/resources/securing-artificial-intelligence-ai-supply-chain) – U.S. Cybersecurity & Infrastructure Security Agency guidance on securing the AI supply chain.
* [Invisible Poison: Backdoor Attacks on NLP Models via Data Poisoning](https://arxiv.org/abs/2106.09132) – Demonstrates how malicious training data can inject backdoors into language models.
* [Security Risks of ChatGPT and Other LLMs (MITRE ATLAS)](https://atlas.mitre.org/stories/llm-threats) – MITRE ATLAS write-up summarising threats and attack vectors related to LLMs.
* [PyTorch Security Advisories](https://github.com/pytorch/pytorch/security/advisories) – Example of OSS dependency risks in foundational model supply chains.


