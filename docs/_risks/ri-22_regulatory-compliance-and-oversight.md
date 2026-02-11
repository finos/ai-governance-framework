---
sequence: 22
title: Regulatory Compliance and Oversight
layout: risk
doc-status: Approved-Specification
type: RC
nist-ai-600-1_references:
  - 2-9  # 2.9. Information Security
ffiec-itbooklets_references:
  - mgt-1  # MGT: I   Governance
  - mgt-2  # MGT: II Risk Management
  - aud-3  # AUD: Internal Audit Program
  - aud-4  # AUD: Risk Assessment and Risk-Based Auditing
eu-ai-act_references:
  - c3-s2-a8   # III.S2.A8: Compliance with the Requirements
  - c3-s2-a10  # III.S2.A10: Data and Data Governance
  - c3-s3-a16  # III.S3.A16: Obligations of Providers of High-Risk AI Systems
  - c3-s3-a21  # III.S3.A21: Cooperation with Competent Authorities
  - c3-s3-a27  # III.S3.A27: Fundamental Rights Impact Assessment for High-Risk AI Systems
related_risks:
  - ri-16  # Bias and Discrimination
  - ri-17  # Lack of Explainability
  - ri-18  # Model Overreach / Expanded Use
---

## Summary

AI systems in financial services must comply with the same regulatory standards as human-driven processes, including those related to suitability, fairness, record-keeping, and marketing conduct. Failure to supervise or govern AI tools properly can lead to non-compliance, particularly in areas like financial advice, credit decisions, or trading. As regulations evolve—such as the upcoming EU AI Act—firms face increasing obligations to ensure AI transparency, accountability, and risk management, with non-compliance carrying potential fines or legal consequences.

## Description

The financial services sector is subject to extensive regulatory oversight, and the use of artificial intelligence does not exempt firms from these obligations. Regulators across jurisdictions have made it clear that AI-generated content and decisions must comply with the same standards as those made by human professionals. Whether AI is used for advice, marketing, decision-making, or communication, firms remain fully accountable for ensuring regulatory compliance.

Key regulatory obligations apply directly to AI-generated outputs:
* **Financial Advice**: Subject to KYC, suitability assessments, and accuracy requirements (MiFID II, SEC regulations)
* **Marketing Communications**: Must be fair, clear, accurate, and not misleading per consumer protection laws
* **Record-Keeping**: AI interactions, recommendations, and outputs must be retained per MiFID II, SEC Rule 17a-4, and FINRA guidelines

Beyond the application of existing rules, financial regulators (such as the PRA and FCA in the UK, the OCC and FRB in the US, and the EBA in the EU) explicitly mandate robust AI-specific governance, risk management, and validation frameworks. This includes:
* **Model Risk Management**: AI models, particularly those informing critical decisions in areas such as credit underwriting, capital adequacy calculations, algorithmic trading, fraud detection, and AML/CFT monitoring, must be subject to rigorous model governance. This involves comprehensive validation, ongoing performance monitoring, clear documentation, and effective human oversight, consistent with established model risk management principles.
* **Supervision and Accountability**: Firms bear the responsibility for adequately supervising their AI systems. A failure to implement effective oversight mechanisms, define clear lines of accountability for AI-driven decisions, and ensure that staff understand the capabilities and limitations of these systems can lead directly to non-compliance.

The regulatory landscape is also evolving. New legislation such as the EU AI Act classifies certain financial AI applications (e.g., credit scoring, fraud detection) as high-risk, which will impose additional obligations related to transparency, fairness, robustness, and human oversight. For high-risk AI systems, Article 27 of the EU AI Act requires deployers (including financial institutions) to conduct Fundamental Rights Impact Assessments before deployment, evaluating potential impacts on individuals' rights and freedoms. Firms that fail to adequately supervise and document their AI systems risk not only operational failure but also regulatory fines, restrictions, or legal action.

Responsible AI considerations—such as fairness, transparency, accountability, and human oversight—are increasingly codified in regulation rather than remaining solely ethical aspirations. Financial institutions should address these concerns to the extent required by applicable regulations and supervisory expectations in their jurisdictions.

As regulatory expectations grow, firms must ensure that their deployment of AI aligns with existing rules while preparing for future compliance obligations. Proactive governance, auditability, and cross-functional collaboration between compliance, technology, and legal teams are essential.

## Links

* [FCA – Artificial Intelligence and Machine Learning in Financial Services](https://www.fca.org.uk/publication/research/research-note-on-ai-and-ml-in-financial-services.pdf)
* [SEC Rule 17a-4 – Electronic Recordkeeping Requirements](https://www.sec.gov/rules/final/34-38245.txt)
* [MiFID II Overview – European Commission](https://finance.ec.europa.eu/capital-markets-union-and-financial-markets/overview/mifid-ii-and-mifir_en)
* [EU AI Act – European Parliament Fact Sheet](https://www.europarl.europa.eu/factsheets/en/sheet/212/artificial-intelligence-ai-)
* [Basel Committee – Principles for the Sound Management of Model Risk](https://www.bis.org/publ/d469.htm)
* [EBA – Guidelines on the Use of ML for AML/CFT](https://www.eba.europa.eu/eba-publishes-guidelines-use-ml-amlcft-context)
* [DORA (Digital Operational Resilience Act)](https://finance.ec.europa.eu/publications/digital-operational-resilience-act-dora_en) – Includes provisions relevant to the governance of AI systems as critical ICT services.
