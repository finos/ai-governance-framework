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
canada-regulations_references:
  # AI-specific guidance
  - csa-sn-11-348          # CSA SN 11-348: AI in Capital Markets — interpretive anchor
  - ciro-acr-2026          # CIRO 2026 Compliance Report — AI section, FinOps posture
  # Registration / conduct / suitability (NI 31-103 provisions)
  - ni-31-103-s11-1        # s. 11.1 Compliance System — compliance/outsourcing accountability
  - ni-31-103-s13-2        # s. 13.2 KYC
  - ni-31-103-s13-2-1      # s. 13.2.1 KYP
  - ni-31-103-s13-3        # s. 13.3 Suitability determination
  - ni-31-103-s13-4        # s. 13.4 Material conflicts of interest
  - ni-31-103cp            # CP Part 11 — outsourcing framework: due diligence, accountability
  - csa-ciro-sn-31-363     # Joint CFR review — conflicts of interest
  - csa-ciro-sn-31-368     # Joint CFR review — KYC/KYP/suitability
  - csa-sn-31-342          # Online advice — AR must remain decision-maker; AI cannot substitute
  - ni-33-109-f5           # Form 33-109F5 — material business change notification
  # Investment funds
  - ni-81-102              # s. 5.1(1)(c) fundamental change trigger; Part 15 sales communications; AI washing
  - ni-81-107              # IRC referral for AI-related conflicts (proprietary models, vendor incentives)
  - ni-81-106              # Material change reporting for AI adoption in fund operations
  # CIRO rules and outsourcing
  - ciro-idpc-rule-3100-3600  # Business conduct (operative IDPC Rules)
  - ciro-idpc-rule-3800       # Recordkeeping and client reporting
  - ciro-idpc-rule-3900       # Supervision
  - ciro-rules-phase-4        # Proposed Rule 3900 — supervision of automated tasks
  - ciro-gn-2300-21-003       # Outsourcing Arrangements — due diligence, SLAs, monitoring, exit
  # Tier 3 benchmarks
  - osfi-e23-2027          # OSFI E-23 Model Risk Management (FRFIs, eff. 2027)
  - osfi-b-10              # OSFI B-10 Third-Party Risk Management (FRFIs) — concentration risk
  - qc-amf-ai-guideline    # AMF AI Guideline (QC-regulated FIs, eff. 2027)
  - iosco-fr-02-2026       # IOSCO Supervisory Toolkit for AI in Capital Markets
  # Tier 4 adjacent compliance obligations
  - pipeda                 # Privacy compliance for AI deployment — SN 11-348 flags privacy intersection
  - qc-p39-s12-1           # Quebec Law 25 s. 12.1 — ADM transparency obligation
  - qc-p39-s3-3-s17        # Quebec Law 25 ss. 3.3, 17 — mandatory PIAs, cross-border transfer adequacy
related_risks:
  - ri-16  # Bias and Discrimination
  - ri-17  # Lack of Explainability
  - ri-18  # Model Overreach / Expanded Use
iosco-supervisory-toolkit_references:
  - t2-governance  # Table 2: AI Governance & Oversight
  - t3-1           # Table 3.1: Oversight from Board or Governing Body
  - t3-2           # Table 3.2: Senior Management Responsibilities
  - t3-3           # Table 3.3: AI Risk Management Systems, Policies and Procedures
  - t6-6           # Table 6.6: Reporting
---

## Summary

AI systems in financial services must comply with the same regulatory standards as human-driven processes, including those related to suitability, fairness, record-keeping, and marketing conduct. Failure to supervise or govern AI tools properly can lead to non-compliance, particularly in areas like financial advice, credit decisions, or trading. As regulations evolve—such as the upcoming EU AI Act—firms face increasing obligations to ensure AI transparency, accountability, and risk management, with non-compliance carrying potential fines or legal consequences.

## Description

The financial services sector is subject to extensive regulatory oversight, and the use of artificial intelligence does not exempt firms from these obligations. Regulators across jurisdictions have made it clear that AI-generated content and decisions must comply with the same standards as those made by human professionals. Whether AI is used for advice, marketing, decision-making, or communication, firms remain fully accountable for ensuring regulatory compliance.

Key regulatory obligations apply directly to AI-generated outputs:
* **Financial Advice**: Subject to KYC, suitability assessments, and accuracy requirements (MiFID II, SEC regulations)
* **Marketing Communications**: Must be fair, clear, accurate, and not misleading per consumer protection laws
* **Record-Keeping**: AI interactions, recommendations, and outputs must be retained per MiFID II, SEC Rule 17a-4, and FINRA guidelines

Beyond the application of existing rules, financial regulators have published AI-specific governance, risk management, and validation expectations. The relevant regimes have diverged materially across jurisdictions and practitioners need to map their systems to the correct frame:

* **Model Risk Management (UK and EU)**: In the UK, the PRA's SS1/23 treats in-scope AI systems — including generative and agentic AI — as falling within model risk management, with the four pillars of development, validation, governance, and ongoing monitoring applying. The EBA's guidelines on the use of ML for AML/CFT remain in force in the EU. AI models informing critical decisions such as credit underwriting, capital adequacy calculations, algorithmic trading, fraud detection, and AML/CFT monitoring are subject to rigorous model governance, requiring comprehensive validation, ongoing performance monitoring, clear documentation, and effective human oversight.
* **Model Risk Management (US)**: As of 17 April 2026, the OCC, Federal Reserve and FDIC jointly revised their interagency MRM guidance (SR 11-7 / OCC Bulletin 2011-12, reissued as OCC Bulletin 2026-13) to **explicitly exclude generative and agentic AI from scope**. The same package rescinded OCC Bulletin 1997-24 (credit scoring) and the 2021 interagency statement on MRM for BSA/AML, and clarified that the guidance is "most relevant" to banks above approximately $30bn in assets. SR 11-7 continues to apply to traditional quantitative models (VaR, IRB PD, logistic regression credit scoring, and similar). It no longer applies to GenAI or agentic systems, pending a forthcoming Request for Information on what should replace MRM coverage in this area.
* **Supervision and Accountability**: Firms bear the responsibility for adequately supervising their AI systems regardless of which regulatory peg is in scope. A failure to implement effective oversight mechanisms, define clear lines of accountability for AI-driven decisions, and ensure that staff understand the capabilities and limitations of these systems can lead directly to non-compliance.

The US carve-out does not create an unregulated zone for GenAI or agentic systems. It removes the MRM peg, but the underlying obligations have shifted to a wider set of authorities: fair-lending law (ECOA/Reg B), the FCRA adverse-action regime, third-party risk management expectations under FFIEC, the SEC's anti-fraud authority over AI-related disclosures, NYDFS Part 500, and state-level AI legislation such as the Colorado AI Act and California DFPI activity. Firms running parallel UK and US operations should expect transatlantic divergence to widen until the US RFI process concludes.

The regulatory landscape is also evolving. New legislation such as the EU AI Act classifies certain financial AI applications (e.g., credit scoring, fraud detection) as high-risk, which will impose additional obligations related to transparency, fairness, robustness, and human oversight. For high-risk AI systems, Article 27 of the EU AI Act requires deployers (including financial institutions) to conduct Fundamental Rights Impact Assessments before deployment, evaluating potential impacts on individuals' rights and freedoms. Firms that fail to adequately supervise and document their AI systems risk not only operational failure but also regulatory fines, restrictions, or legal action.

Responsible AI considerations—such as fairness, transparency, accountability, and human oversight—are increasingly codified in regulation rather than remaining solely ethical aspirations. Financial institutions should address these concerns to the extent required by applicable regulations and supervisory expectations in their jurisdictions.

As regulatory expectations grow, firms must ensure that their deployment of AI aligns with existing rules while preparing for future compliance obligations. Proactive governance, auditability, and cross-functional collaboration between compliance, technology, and legal teams are essential.

## Links

* [FCA – Artificial Intelligence and Machine Learning in Financial Services](https://www.fca.org.uk/publication/research/research-note-on-ai-and-ml-in-financial-services.pdf)
* [PRA SS1/23 – Model Risk Management Principles for Banks](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss)
* [OCC Bulletin 2026-13 – Interagency Guidance on Model Risk Management (revised)](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html)
* [SEC Rule 17a-4 – Electronic Recordkeeping Requirements](https://www.sec.gov/rules/final/34-38245.txt)
* [MiFID II Overview – European Commission](https://finance.ec.europa.eu/capital-markets-union-and-financial-markets/overview/mifid-ii-and-mifir_en)
* [EU AI Act – European Parliament Fact Sheet](https://www.europarl.europa.eu/factsheets/en/sheet/212/artificial-intelligence-ai-)
* [Basel Committee – Principles for the Sound Management of Model Risk](https://www.bis.org/publ/d469.htm)
* [EBA – Guidelines on the Use of ML for AML/CFT](https://www.eba.europa.eu/eba-publishes-guidelines-use-ml-amlcft-context)
* [DORA (Digital Operational Resilience Act)](https://finance.ec.europa.eu/publications/digital-operational-resilience-act-dora_en) – Includes provisions relevant to the governance of AI systems as critical ICT services.
