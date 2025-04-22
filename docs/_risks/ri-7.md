---
layout: risk
doc-status: Draft
sequence: 7
type: OP
title: Availability of foundational model
external_risks:
  - LLM04
---

RAG systems are proliferating due to the low barrier of entry compared
to traditional chatbot technologies. RAG has applicability for
internal users as well as supporting customer-related use cases.

Many LLMs require GPU compute infrastructure to provide an acceptable
level of responsiveness. Furthermore, some of the best-performing LLMs
are proprietary. Therefore, the path of least resistance is to call
out to a Technology Service Provider (TSP).

#### Key Risks

- **Denial of Wallet (DoW)**: Over-usage that results in slowdowns,
  unexpected costs, or outages. Examples include:
    - Unexpectedly long prompts due to large chunk sizes or many
      chunks packed into the prompt.
        - This could be exacerbated by systems that work with
          multimedia content.
        - LLM attacks to exfiltrate training data may also generate
          the maximum number of tokens.
    - Scripts which repeatedly hit API endpoints without built-in
      throttling.
        - This may result from Strats searching for new sources of "signal".
    - Agentic systems which may generate additional LLM / search calls
      that were not taken into account in the initial design /
      capacity planning.

- **TSP Outages**:
    - Some LLM providers might not have sufficient technical maturity
      to provide uptime to meet target SLA.
    - Inability to fail over to an equivalent LLM back end due to
      proprietary model / lack of capacity at other TSPs. (FFIEC
      Appendix J).

- **VRAM Exhaustion**:
    - VRAM utilization can increase for a variety of reasons:
        - new release of LLM library has a memory leak
        - new caching techniques to improve throughput at the cost of
          VRAM
        - setting a longer context length
        - etc.

#### Links

- https://www.prompt.security/blog/denial-of-wallet-on-genai-apps-ddow
- https://ithandbook.ffiec.gov/
- https://www.ffiec.gov/%5C/press/PDF/FFIEC_Appendix_J.pdf
