---
sequence: 9
title: Data Poisoning
layout: risk
doc-status: Approved-Specification
type: SEC
owasp-llm_references:
  - llm03-2025  # LLM03:2025 Supply Chain
  - llm04-2025  # LLM04: Data and Model Poisoning
  - llm05-2025  # LLM05:2025 Improper Output Handling
  - llm06-2025  # LLM06:2025 Excessive Agency
ffiec-itbooklets_references:
  - sec-3  # SEC: III Security Operations
  - dam-3  # DAM: III Risk Management of Development, Acquisition, and Maintenance
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c3-s2-a10  # III.S2.A10: Data and Data Governance
  - c3-s2-a15  # III.S2.A15: Accuracy, Robustness and Cybersecurity
  - c5-s2-a53  # V.S2.A53: Obligations for Providers of General-Purpose AI Models
related_risks:
  - ri-8   # Tampering With the Foundational Model
  - ri-19  # Data Quality and Drift
---
## Summary

Data poisoning occurs when adversaries tamper with training or fine-tuning data to manipulate an AI model’s behaviour, often by injecting misleading or malicious patterns. This can lead to biased decision-making, such as incorrectly approving fraudulent transactions or degrading model performance in subtle ways. The risk is heightened in systems that continuously learn from unvalidated or third-party data, with impacts that may remain hidden until a major failure occurs.

## Description

Data poisoning involves adversaries deliberately tampering with training or fine-tuning data to corrupt the learning process and manipulate subsequent model behavior. In financial services, this presents several attack vectors:

**Training Data Manipulation**: Adversaries alter datasets by changing labels (marking fraudulent transactions as legitimate) or injecting crafted data points with hidden patterns exploitable later.

**Continuous Learning Exploitation**: Systems that continuously learn from new data are vulnerable if validation mechanisms are inadequate. Fraudsters can systematically feed misleading information to skew decision-making in credit scoring or trading models.

**Third-Party Data Compromise**: Financial institutions rely on external data feeds (market data, credit references, KYC/AML watchlists). If these sources are compromised, poisoned data can unknowingly introduce biases or vulnerabilities.

**Bias Introduction**: Data poisoning can amplify biases in credit scoring or loan approval models, leading to discriminatory outcomes and regulatory non-compliance.

The effects are often subtle and difficult to detect, potentially remaining hidden until major failures, financial losses, or regulatory interventions occur.

## Links

* [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733) – Early research demonstrating how poisoned data can introduce backdoors.
* [How to Poison the Data That Teach AI](https://www.scientificamerican.com/article/how-to-poison-the-data-that-teach-ai/) – Popular science article explaining data poisoning for general audiences.
* [MITRE ATLAS – Training Data Poisoning](https://atlas.mitre.org/techniques/T0021) – Official MITRE page detailing poisoning techniques in adversarial AI scenarios.
* [Poisoning Attacks Against Machine Learning – CSET](https://cset.georgetown.edu/publication/poisoning-attacks-against-machine-learning/) – Policy-focused report exploring implications of poisoning on national security and critical infrastructure.
* [Clean-Label Backdoor Attacks](https://arxiv.org/abs/2008.04333) – Describes attacks where poisoned data looks legitimate to human reviewers but still misleads models.

