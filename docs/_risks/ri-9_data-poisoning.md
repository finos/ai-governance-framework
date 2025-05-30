---
sequence: 9
title: Data Poisoning
layout: risk
doc-status: Pre-Draft
type: SEC
external_risks:
  - OWASP-LLM_2025_LLM03  # OWASP LLM: Supply Chain Vulnerabilities
  - OWASP-LLM_2025_LLM04  # OWASP LLM: Data and Model Poisoning
  - OWASP-ML_2023_ML02    # OWASP ML: Data Poisoning Attack 
ffiec_references:
  - ffiec_sec_iii-security-operations
  - ffiec_dam_iii-risk-management-of-development-acquisition-and-maintenance
  - ffiec_aud_risk-assessment-and-risk-based-auditing
eu-ai_references:
  - eu-ai_c3-s2-a10  # III.S2.A10 Data and Data Governance
  - eu-ai_c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - eu-ai_c5-s2-a53  # V.S2.A53 Obligations for Providers of General-Purpose AI Models
---

Data poisoning is a malicious attack technique where adversaries deliberately tamper with the data used to train or fine-tune AI and machine learning models. The objective is to corrupt the learning process, thereby manipulating the model's subsequent behaviour, introducing biases, creating backdoors, or degrading its overall performance to achieve the attacker's aims. For financial institutions that increasingly rely on AI for critical functions, data poisoning presents a significant and insidious threat.

The attack can manifest in several ways within a financial services context:

* **Manipulation of Training or Fine-Tuning Data:** Adversaries may gain access to and alter datasets used in the initial training or subsequent fine-tuning of models. This could involve subtly changing labels (e.g., marking fraudulent transactions as legitimate to train a fraud detection model incorrectly) or injecting crafted data points that introduce hidden patterns or vulnerabilities exploitable at a later stage.
* **Exploitation of Continuous Learning Systems:** AI models that continuously learn from new, incoming data are particularly vulnerable if robust validation mechanisms are not in place. Fraudsters, for example, could systematically feed misleading information into such systems over time, gradually skewing decision-making processes like AI-driven credit scoring to favor fraudulent profiles or to approve otherwise unacceptable risks.
* **Compromise of Third-Party Data Sources:** Financial institutions often rely on a multitude of external data feeds for model training and operation, including market data, credit reference information, KYC/AML watchlists, and threat intelligence. If these third-party data sources are compromised, poisoned data can be unknowingly ingested, introducing hidden biases, vulnerabilities, or specific triggers into the institution's AI models.
* **Introduction of Biases:** Beyond enabling direct fraud, data poisoning can be used to introduce or amplify biases in AI models. For example, credit scoring or loan approval models could be skewed to unfairly disadvantage certain demographics or, conversely, to unfairly favor others, leading to discriminatory outcomes and regulatory non-compliance.

The impact of data poisoning on financial institutions can be severe and multifaceted:

* **Flawed Decision-Making:** Poisoned models can lead to erroneous automated decisions, such as incorrectly approving fraudulent applications, denying credit to creditworthy individuals, or making flawed investment choices.
* **Direct Financial Losses:** Successful manipulation of AI systems, like those used for fraud detection or algorithmic trading, can result in immediate and substantial financial losses.
* **Regulatory Non-Compliance and Legal Penalties:** Biased or discriminatory outcomes resulting from data poisoning can lead to breaches of financial regulations (e.g., fair lending laws) and significant legal repercussions.
* **Erosion of Trust and Reputational Damage:** The discovery of manipulated or unreliable AI systems can severely damage an institution's reputation among customers, regulators, and the wider market.
* **Operational Disruption:** Identifying, mitigating, and remediating the effects of data poisoning can be time-consuming and resource-intensive, potentially disrupting critical business operations.

One of the most challenging aspects of data poisoning is its often stealthy nature. The malicious alterations to data can be subtle and difficult to detect using standard validation techniques. Consequently, the detrimental effects of data poisoning may go unnoticed for extended periods, potentially accumulating and only becoming apparent after a major failure, significant financial loss, or regulatory intervention. This underscores the need for robust data governance, stringent input validation processes, anomaly detection mechanisms for data and model behaviour, data provenance tracking, and specific defences designed to detect and mitigate poisoning attempts.
