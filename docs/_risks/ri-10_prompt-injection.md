---
sequence: 10
title: Prompt Injection
layout: risk
doc-status: Draft
type: SEC
external_risks:
  - OWASP-LLM_2025_LLM01  # OWASP LLM: Prompt Injection
  - OWASP-ML_2023_ML01    # OWASP ML: Input Manipulation Attack
ffiec_references:
  - ffiec_sec_iii-security-operations
  - ffiec_dam_iv-common-development-acquisition-and-maintenance-risk-topics
  - ffiec_dam_v-development
eu-ai_references:
  - eu-ai_c2-a5  # II.A5 Prohibited AI Practices
  - eu-ai_c3-s2-a15  # III.S2.A15 Accuracy, Robustness and Cybersecurity
  - eu-ai_c3-s2-a14  # III.S2.A14 Human Oversight
---

Prompt injection is a critical security vulnerability where malicious actors craft inputs (prompts) to manipulate a Large Language Model (LLM) into performing unintended actions or generating harmful outputs. This attack vector is particularly concerning as it often requires minimal privileges and can have a wide scope of impact, extending beyond simple incorrect answers to include toxic responses, sensitive information disclosure, denial of service, and the generation of unethical or biased content. The DPD chatbot incident, where a customer successfully manipulated the AI into inappropriate behaviour, serves as a notable public example of this risk [^3].

For financial institutions leveraging LLMs, especially in customer-facing applications or integrated into decision-making processes, prompt injection poses a substantial threat. There are two primary approaches:

1.  **Direct Prompt Injection (Jailbreaking):** In this scenario, a user or internal agent directly interacts with the LLM and crafts prompts designed to bypass its safety protocols, override its original instructions, or coax it into revealing restricted information or performing unauthorized actions.
    * **Financial Services Examples:** An attacker might "jailbreak" an AI-powered financial advisory chatbot to make it disclose proprietary investment algorithms, generate fake transaction histories, provide advice that violates regulatory compliance (e.g., bypassing suitability checks), or access underlying data stores containing customer information.

2.  **Indirect Prompt Injection:** This more insidious form involves an attacker injecting malicious prompts into data sources that the LLM will later consume and process. The LLM might then execute the hidden commands without the direct knowledge of the current user or system operator.
    * **Financial Services Examples:** A malicious prompt could be embedded within an email, a customer feedback form, a third-party market report, or a document uploaded for analysis. When the LLM processes this contaminated data (e.g., for summarization, sentiment analysis, or integration into a workflow), the injected prompt could trigger actions like exfiltrating the data being processed, manipulating summaries provided to financial analysts, executing unauthorized commands in connected systems, or biasing critical automated decisions in areas like loan processing or fraud assessment.

The objectives and potential consequences of successful prompt injection attacks within a financial institution are diverse and severe:

* **Unauthorized Data Access and Exfiltration:** Attackers can craft prompts to trick the LLM into revealing sensitive customer data (e.g., account numbers, balances, personal identifiable information), confidential institutional data (such as trading strategies, internal risk assessments, M&A plans), or the contents of its Retrieval Augmented Generation (RAG) data sources.
* **Execution of Unauthorized Actions:** In systems where LLMs are integrated with other backend functionalities, prompt injection could potentially lead to unauthorized financial transactions, modification of account details, or the initiation of other damaging processes.
* **Generation of Misleading or Harmful Content:** The LLM could be manipulated to produce inaccurate financial advice, generate fake news impacting market sentiment, create defamatory statements about competitors, or produce responses that are biased, unethical, or violate regulatory standards.
* **System Manipulation and Profiling:** Attackers may use prompt injection to probe the LLM's defences, understand its underlying system prompts and configurations, or attempt model inversion techniques to infer details about its training data or architecture, potentially leading to model theft or the discovery of further exploits.
* **Reputational Damage and Loss of Trust:** Incidents of prompt injection leading to public disclosure of sensitive information or visibly errant AI behaviour can severely damage a financial institution's reputation and erode customer confidence.
* **Privilege Escalation:** Indirect prompt injection, particularly in complex integrated systems, could lead to privilege escalation if the LLM operates with, or can influence components that operate with, higher privileges.

This risk is particularly acute in automated systems where there is no "human in the loop" to scrutinize the LLM's output before action is taken, making such attacks potentially invisible until significant harm occurs. While distinct from inherent model hallucinations (covered in ri-4), prompt injection can deliberately induce outputs that appear as hallucinations but are, in fact, attacker-controlled. Defending against prompt injection is an ongoing challenge due to the creativity of attackers and the inherent flexibility of LLM input processing.

References
* [^1] OWASP Top 10 for LLM Applications - https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf
* [^2] Mitre Prompt Injection - https://attack.mitre.org/techniques/T1055/
* [^3] DPD Chatbot Swears at Customer - BBC - https://www.bbc.co.uk/news/technology-68025677
