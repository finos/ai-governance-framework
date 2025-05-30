---
sequence: 23
title: Intellectual Property (IP) and Copyright
layout: risk
doc-status: Pre-Draft
type: RC
external_risks:
  - NIST-600_2024_2-10  # NIST 600.1: Intellectual Property
  - OWASP-LLM_2025_LLM02  # OWASP LLM: Sensitive Information Disclosure
  - OWASP-LLM_2025_LLM03  # OWASP LLM: Supply Chain
  - OWASP-LLM_2025_LLM10  # OWASP LLM: Sensitive Information Disclosure
  - OWASP-ML_2023_ML05    # OWASP Unbounded Consumption
ffiec_references:
  - ffiec_mgt_i-governance
  - ffiec_mgt_ii-risk-management
  - ffiec_ots_risk-management
  - ffiec_dam_vi-acquisition
eu-ai_references:
  - eu-ai_c3-s2-a10  # III.S2.A10 Data and Data Governance
  - eu-ai_c3-s2-a11  # III.S2.A11 Technical Documentation
  - eu-ai_c5-s2-a53  # V.S2.A53 Obligations for Providers of General-Purpose AI Models
---

The increasing adoption of Generative AI technologies within financial institutions introduces complex Intellectual Property (IP) and copyright risks. These risks stem from both the data on which AI models are trained and the content these models generate, as well as how proprietary institutional data is handled when interacting with such AI systems.

A fundamental concern arises from the training methodologies of many large language models (LLMs) and other generative AI systems, which often involve processing vast internet-scale datasets. These datasets may inadvertently include copyrighted material—such as text, images, code, and audio—ingested without the explicit consent of the rights holders. This can lead to several IP-related challenges for financial institutions:

* **Copyright Infringement through AI-Generated Content:** AI models may generate outputs that are substantially similar to, or derivative of, copyrighted works present in their training data. Financial institutions could face legal liability for copyright infringement if they use or distribute such AI-generated content. This could manifest, for example, if AI-generated marketing copy closely resembles a competitor's copyrighted materials, if code produced by an AI assistant for internal financial modelling tools replicates snippets from licensed or proprietary software, or if AI-generated research reports inadvertently include passages from copyrighted financial analyses. Ensuring that AI-generated content provided to customers or used in operations is original, accurate, and legally compliant is therefore a critical concern.

* **Loss of Proprietary Information and Trade Secrets:** A significant risk involves the potential leakage of a financial institution's own valuable IP when employees interact with AI models, particularly public or third-party hosted tools. Inputting confidential information—such as proprietary trading algorithms, sensitive client data analyses, M&A strategies, unreleased financial product details, or internal operational know-how—into these AI systems can lead to the irretrievable loss of trade secrets. There have been instances where firms have accidentally leaked sensitive internal code or confidential business strategies through the use of AI tools. This risk is heightened if the AI provider's terms allow them to use input data for future model training or if their data security and confidentiality practices are inadequate.

* **Licensing and Usage Rights for AI Models and Platforms:** Financial institutions must ensure that the AI models, platforms, and APIs they utilize are properly licensed for commercial purposes. The terms of service for AI tools can vary widely, and failure to adhere to licensing conditions could result in contractual breaches or loss of access to critical AI capabilities.

The consequences of inadequately managing these IP and copyright risks can be severe for financial institutions:

* **Legal Action and Financial Penalties:** This includes copyright infringement lawsuits, claims of trade secret misappropriation, and potential court-ordered injunctions, leading to substantial legal costs, damages, and fines.
* **Loss of Competitive Advantage:** The inadvertent disclosure of proprietary algorithms, unique business processes, or confidential strategic information can significantly erode an institution's competitive edge.
* **Reputational Damage:** Being publicly associated with IP infringement or the careless handling of confidential business information can severely damage an institution's brand and stakeholder trust.
* **Contractual Breaches:** Misappropriating third-party IP or leaking client-confidential information through AI systems can lead to breaches of contracts with clients, partners, or software vendors.

Effectively mitigating these risks requires financial institutions to implement robust IP governance frameworks, conduct thorough due diligence on AI vendors and their data handling practices, provide clear policies and training to employees on the acceptable use of AI tools (especially concerning proprietary data), and potentially utilize AI systems that offer strong data protection and IP indemnification clauses.
