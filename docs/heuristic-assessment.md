---
layout: index
title: A heuristic approach to identifying GenAI risks
---

Before deploying any generative AI application, it’s crucial to perform a structured risk assessment of the specific use case. We propose a heuristic-based approach – essentially a guided set of questions and considerations – to identify the risk profile of a GenAI implementation. This approach ensures that stakeholders systematically evaluate how an AI will be used, what could go wrong, and the controls that should be applied. Below is a step-by-step heuristic framework that can be applied to various GenAI use cases (from customer chatbots and advisory tools to internal process automation):

 - [Define the Use Case and Context](#a-define-the-use-case-and-context)
 - [Identify Data Involved](#b-identify-data-involved)
 -  [Model and Technology](#c-model-and-technology)
 -  [Output and Decision Impact](#d-output-and-decision-impact)
 -  [Regulatory Mapping](#e-regulatory-mapping)
 -  [Security Considerations](#f-security-considerations)
 -  [Controls and Safeguards Identification](#g-controls-and-safeguards-identification)
 -  [Decision and Documentation](#h-decision-and-documentation)


### A. Define the Use Case and Context

Start by clearly articulating what the GenAI application will do, who/what it will affect, and the environment in which it operates. Key questions:
- *What is the intended function of the GenAI?* (e.g., Generate research reports, answer customer queries, assist in code generation, detect fraud patterns, etc.)
- *Who are the end-users or beneficiaries?* (Internal staff like analysts, or external users like customers? Are they tech-savvy or general public?)
- *What business process or decision does it impact?* (Is it making a recommendation, an automated decision, or just providing information?)
- *What is the criticality of this process?* (High impact like trading decisions, client advice or communications vs. low impact like internal brainstorming.)

Understanding the context will frame the risk tolerance. For instance, an AI assisting an internal developer has more leeway for error than one directly advising clients on investments.

**NOTE:** the above should be scope to just those use cases that utilise GenAI.

### B. Identify Data Involved

Evaluate the data inputs and outputs of the AI, as data is a major source of risk:

- *What data is the GenAI model trained on?* – Proprietary financial data, public internet data, client transaction data? Identify any sensitive or regulated data in the training set (PII, account numbers, etc.).
- *Will the AI output or expose any of that training data?* – Check if there’s risk of regurgitation of sensitive info. (For example, did training include confidential documents that the AI might quote from?)
- *What data will be provided in prompts or queries to the AI?* – List the fields or content an average query will contain. Mark any that are sensitive (customer names, balances, trade details). If yes, risk is higher.
- *Does the use case involve personal data or regulatory data (e.g., credit scores)?* – If yes, flag for privacy/GDPR and confidentiality risks. Determine if you have user consent or a legal basis to use that data with an AI tool.
- *How is output data used?* – Could the AI generate data that needs protection (e.g., generating a file with customer info)? Plan how that output is stored/protected.

This step often yields specific risks like “customer addresses are supplied to the GenAI model – privacy risk” or “the AI is trained on month-old market data – stale output risk.”

### C. Model and Technology

Assess the type of model and technical setup:

- *What type of GenAI model is it (language model, reasoning model), and who built it?* – A third-party hosted LLM, a self-hosted open source model or an in-house developed model? Third-party models may carry vendor and transparency risks, whereas in-house models carry development and validation burdens.
- *Is the model pre-trained (foundation model) or custom-trained for our data?* – Pre-trained models may have general knowledge (and biases) not specific to your domain; fine-tuned models on your data might perform better but could expose your data if not handled carefully.
- *How accurate or tested is the model for this use case?* – If available, review any benchmarks or test results. If the model is known to have a ~5% hallucination rate in general Q&A, that’s a red flag for a high-stakes use. 
- *Does the model support explainability or additional controls?* – Some platforms offer features like traceability of sources (e.g., citing which document influenced the answer), which are positive for risk mitigation. Lack of any control features means you’ll rely more on external mitigations.
- *How is the AI hosted and integrated?* – Is it an on-premises deployment or cloud API? Cloud introduces data transit and storage risks; on-prem needs strong internal security. Integration points (APIs, data feeds) should be identified to assess where vulnerabilities might be inserted.

This technical review will flag issues like “Using a black-box API from vendor X – need to address vendor risk and lack of explainability” or “Model hasn’t been validated on our type of data – model risk present.”

### D. Output and Decision Impact

Consider what the AI will produce and the potential consequences:

- *What form do outputs take?* – e.g., Free-form text answers, numerical predictions, classifications, images, etc. Free-form text (like an LLM response) has a broad range and could include inappropriate content, whereas a numeric score might be easier to validate but could still be wrong.
- *How will those outputs be used in decision-making?* – Are they advisory (human makes final decision) or automated (AI output directly triggers an action)? If automated, risk is higher and requires stronger controls.
- *What’s the worst-case scenario of a bad output?* – Play devil’s advocate: Could a hallucinated answer cause a major loss or compliance breach? For example, AI writes an incorrect regulatory filing – leads to compliance violation; or AI misclassifies a legitimate transaction as fraud – leads to customer account freeze unjustly. Enumerate possible failure modes and their severity.
- *Could the output offend or harm someone?* – Especially for customer-facing AI, consider misuse or harmful content: Could it inadvertently use foul language, biased language, or share sensitive info? If yes, content filtering is needed.
- *Is there a human fail-safe?* – Determine if, in the intended workflow, a human will review the AI output. If not, you need to treat the risk as if the AI is “in charge” (very high bar for accuracy and control). If yes, clarify the human’s role (do they have time and expertise to catch errors? or will they just rubber-stamp?).

Evaluating output impact helps categorize the use case’s criticality (e.g., informative vs. decision-making, internal vs. customer-facing) which correlates with risk level. 

### E. Regulatory Mapping

Cross-check the use case against relevant regulations and laws:

- *Which regulations or guidelines apply to this use case?* – For instance, a chatbot giving investment suggestions must align with securities advice regulations; using AI in credit underwriting invokes fair lending laws; generating marketing content triggers advertising rules.
- *Does the AI need to provide explanations or reasons due to regulations?* – E.g. if the AI helps make credit decisions, can we extract reason codes? If not, that’s a compliance gap.
- *Are there privacy consent requirements?* – If customer data is used, check if the privacy policy covers this use. For EU customers, determine if this use of AI could be considered automated profiling under GDPR that requires consent or disclosure.
- *Does the use case align with “acceptable AI uses” in regulators’ eyes?* – Regulators have hinted at disallowing some high-risk AI uses (for example, fully automated robo-advice without human option might concern some regulators). Review any recent regulatory statements or guidance. [FINRA’s notice on GenAI](https://www.finra.org/rules-guidance/notices/24-09) and the [UK FCA’s AI principles](https://www.fca.org.uk/publication/corporate/ai-update.pdf) could provide insight.
- *Will this likely be audited or require notification?* – For example, some regulators might expect notification if AI is used in fraud detection or capital models. Knowing this upfront helps in planning compliance documentation.

By mapping regulations, you’ll identify specific compliance risks (like “the system might generate unapproved marketing language – violate ad rules” or “We can’t explain denials – potential fair lending issue”). This step ensures no regulatory angle is overlooked.

### F. Security Considerations

Examine how the AI could be attacked or could fail from a security perspective:

- *What are the entry points for an attacker?* – If the AI is user-facing, could someone input malicious prompts (prompt injection)? If it’s internal, could an insider misuse it (e.g., ask it to divulge sensitive data)? 
- *Could the AI divulge sensitive info if prompted cleverly?* – Test some adversarial prompts on non-production environment. If it tends to reveal things it shouldn’t, note that.
- *Is the model protected from unauthorized access?* – Ensure only the intended application can query it. 
- *Any known vulnerabilities of the model or library?* – Check vendor documentation for known issues (some models had bugs where certain strings would dump system prompts, etc.). 
- *What’s the impact of model unavailability?* – If the AI service goes down, is it just inconvenience or does it stop a critical process? If critical, plan redundancy.
- *Could model outputs be used maliciously?* – e.g., If the AI writes code (like Copilot), could an attacker prompt it to write malware that bypasses checks? Or if it generates text, could it be tricked into creating social engineering content targeting your execs? Basically, consider if someone might use your AI against you or your customers.

This security analysis yields risks like “prompt injection could cause data leak” or “lack of monitoring could let misuse go undetected” which feed into needed controls.

### G. Controls and Safeguards Identification

At this point, you should be able to identify a comprehensive set of risks - using the FINOS AI Governance Framework as a guidance. One risks have been identified, list potential controls and see if they are in place:   

- For each risk noted, ask *“What controls do we have or need for this?”* – If a risk has no current mitigation, mark it clearly.
- Determine if additional tooling is required (maybe a content filter, or a bias detection tool, or an encryption module for data in transit).
- Evaluate if the risk level vs. control strength is acceptable. For example, if a use case is high risk (say automated trading) and you identified only moderate controls, you either need to bolster controls or rethink the design (maybe make it advisory instead of automatic).

This step effectively produces a risk control matrix for the use case. 

### H. Decision and Documentation

Finally, use the findings to make an informed decision and document it:

- *Assign a risk rating to the use case* (e.g., Low/Medium/High) based on the severity and likelihood of risks after controls. This can be subjective but should be justified (some firms use scoring models for this).
- *Decide whether to proceed, adjust, or abort the deployment.* High residual risk might mean you postpone launch until more controls or model improvements are in place. Medium risk might be acceptable with monitoring, etc.
- *Document the assessment.* Create a brief report or checklist output that records the Q&A above, identified risks, and chosen mitigations. This will be invaluable for internal audit or regulatory inquiries to show you did due diligence. It also helps future reviews if the use case changes or scales up.
- *Establish review intervals.* Given how fast AI evolves, set a timeline (say, 6 months) to revisit this use case and redo the risk assessment. New factors (like updated regulations or new model versions) may change the risk profile.
