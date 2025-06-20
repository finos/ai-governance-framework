---
sequence: 14
title: Inadequate System Alignment
layout: risk
doc-status: Approved-Specification
type: OP
ffiec-itbooklets_references:
  - dam-3  # DAM: III Risk Management of Development, Acquisition, and Maintenance
  - dam-5  # DAM: V Development
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c2-a5      # II.A5 Prohibited AI Practices
  - c3-s2-a9   # III.S2.A9: Risk Management System
  - c3-s2-a14  # III.S2.A14: Human Oversight
nist-sp-800-53r5_references:
  - sa-11  # SA-11 Developer Testing And Evaluation
  - ra-3   # RA-3 Risk Assessment
  - ca-6   # CA-6 Authorization
related_risks:
  - ri-4  # Hallucination and Inaccurate Outputs
  - ri-6  # Non-Deterministic Behaviour
owasp-llm_references:
  - llm07-2025  # LLM07:2025 System Prompt Leakage
owasp-ml_references:
  - ml08-2023  # ML08:2023 Model Skewing
---

## Summary

LLM-powered RAG systems may generate responses that diverge from their intended business purpose, producing outputs that appear relevant but contain inaccurate financial advice, biased recommendations, or inappropriate tone for the financial context. Misalignment often occurs when the LLM prioritizes response fluency over accuracy, fails to respect financial compliance constraints, or draws inappropriate conclusions from retrieved documents. This risk is particularly acute in financial services where confident-sounding but incorrect responses can lead to regulatory violations or customer harm.

## Description

Large Language Models in Retrieval-Augmented Generation (RAG) systems for financial services are designed to provide accurate, compliant, and contextually appropriate responses by combining retrieved institutional knowledge with the LLM's language capabilities. However, response misalignment occurs when the LLM's output diverges from the intended business purpose, regulatory requirements, or institutional policies, despite appearing coherent and relevant.

Unlike simpler AI systems with clearly defined inputs and outputs, LLMs in RAG systems must navigate complex interactions between retrieved documents, system prompts, user queries, and financial domain constraints. This complexity creates multiple vectors for misalignment:

### Key Misalignment Patterns in Financial RAG Systems

**Retrieval-Response Disconnect**: The LLM generates confident responses that contradict or misinterpret the retrieved financial documents. For example, when asked about loan eligibility criteria, the LLM might provide a simplified answer that omits critical regulatory exceptions documented in the retrieved policy, potentially leading to compliance violations.

**Context Window Limitations**: Important regulatory caveats, disclaimers, or conditional statements get truncated or deprioritized when documents exceed the LLM's context window. This can result in incomplete financial guidance that appears authoritative but lacks essential compliance information.

**Domain Knowledge Gaps**: When retrieved documents don't fully address a financial query, the LLM may fill gaps with plausible-sounding but incorrect financial information from its training data, creating responses that blend accurate institutional knowledge with inaccurate general knowledge.

**Scope Boundary Violations**: The LLM provides advice or recommendations that exceed its authorized scope. For instance, a customer service RAG system might inadvertently provide investment advice when only licensed for general account information, creating potential regulatory liability.

**Prompt Injection via Retrieved Content**: Malicious or poorly formatted content in the knowledge base can manipulate the LLM's responses through indirect prompt injection, causing the system to ignore safety guidelines or provide inappropriate responses.

**Tone and Compliance Mismatches**: The LLM adopts an inappropriate tone or level of certainty for financial communications, such as being overly definitive about complex regulatory matters or using casual language for formal compliance communications.

### Impact on Financial Operations

The consequences of LLM response misalignment in RAG systems can be severe for financial institutions:

* **Regulatory Compliance Violations**: Misaligned responses may provide incomplete or incorrect regulatory guidance, leading to compliance failures. For example, a RAG system might omit required disclosures for investment products or provide outdated regulatory information that exposes the institution to penalties.

* **Customer Harm and Liability**: Incorrect financial advice or product recommendations can result in customer financial losses, creating legal liability and reputational damage. This is particularly problematic when responses appear authoritative due to the LLM's confident tone and institutional branding.

* **Operational Risk Amplification**: Misaligned responses in internal-facing RAG systems can lead to incorrect policy interpretations by staff, resulting in procedural errors that scale across the organization. Risk assessment tools that provide misaligned guidance can compound decision-making errors.

* **Trust Erosion**: Inconsistent or contradictory responses from RAG systems undermine confidence in AI-assisted financial services, potentially impacting customer retention and staff adoption of AI tools.

### Alignment Drift in RAG Systems

RAG systems can experience alignment drift over time due to several factors specific to their architecture:

* **Knowledge Base Evolution**: As institutional documents are updated, added, or removed, the retrieval patterns change, potentially exposing the LLM to conflicting information or creating gaps that trigger inappropriate response generation.

* **Foundation Model Updates**: Changes to the underlying LLM (ri-5) can alter response patterns even with identical retrieved content, potentially breaking carefully calibrated prompt engineering and safety measures.

* **Context Contamination**: Poor document hygiene in the knowledge base can introduce biased, outdated, or incorrect information that the LLM incorporates into responses without proper validation.

* **Query Evolution**: As users discover new ways to interact with the system, edge cases emerge that weren't addressed in initial alignment testing, revealing previously unknown misalignment patterns.

Maintaining alignment in financial RAG systems requires continuous monitoring of response quality, regular validation against regulatory requirements, and systematic testing of new query patterns and document combinations.


## Links

  * [AWS - Responsible AI](https://aws.amazon.com/machine-learning/responsible-ai/)
  * [Microsoft - Responsible AI with Azure](https://azure.microsoft.com/en-us/solutions/ai/responsible-ai-with-azure)
  * [Google - Responsibility and Safety](https://deepmind.google/about/responsibility-safety/)
  * [OpenAI - A hazard analysis framework for code synthesis large language models](https://openai.com/research/a-hazard-analysis-framework-for-code-synthesis-large-language-models) 
* Research
  * [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://arxiv.org/abs/2402.18540)
  * [SoFA: Shielded On-the-fly Alignment via Priority Rule Following](https://arxiv.org/abs/2402.17358)
