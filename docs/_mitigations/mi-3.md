---
layout: mitigation
doc-status: Draft
sequence: 3
type:
  - Preventative
mitigates:
  - ri-7
  - ri-10
title: User/app/model firewalling/filtering
---

As in any information system component, you can monitor and filter interactions between the model, inputs from the user, queries to RAG databases or other sources of information, and outputs.

A simple analogy is a Web Access Firewall detecting URLs trying to exploit known vulnerabilities in specific server versions, and detecting and filtering from the output malicious Javascript code embedded in the returned web page.

Not only user input and LLM output should be considered. To populate the RAG database with custom information, it has to use the same tokenizer that follows the exact same embeddings format (converting words to vectors) that the LLM uses. This means that for an LLM in a SaaS where the tokenizer is available as an endpoint, you have to send the full information to the embeddings endpoint to convert it to vectors, and store the returned data into your RAG database.

#### Things to monitor/filter

Monitoring This would make possible to potentially detect and block undesired behavior, like:

* RAG data ingestion
  * Before you send the full custom information to the embeddings endpoint of a SaaS LLM, you should carefully filter any potential private information that shouldn't be disclosed.
* User input
  * Detecting and blocking abuse from the user to the LLM, like [prompt Injection](#ri-10)
  * Detecting disclosing potentially private information to an LLM hosted externally to the organization as SaaS, and filtering it out or anonymizing.
* LLM output
  * Detecting an answer that is too long, maybe because a user has tricked the LLM to do so, to cause a [denial of service] or make the LLM behave erratically, potentially disclosing private information.
  * Detecting if the answer is not in the right format, for example if you always expect a formatted JSON output, or when it's in a different language than the LLM use case, a known attack technique.
  * Detecting the LLM is giving known answers for when it is resisting abuse, that may not have been blocked on input, and could add up to constitute an attack in progress looking for vulnerabilities in guardrails.
  * Detecting private information being disclosed, coming from the RAG database, or the data used to pre-train the model.
  * Detecting and blocking possible foul language that the LLM has been forced to use by the user, avoiding reputational loss for the organization.
  * Repopulating in the answer an anonymized question, for example if the user included his email, it was first replaced by a generic one, then repopulated after the LLM answered.

A tool like this could combine with detecting queries or responses that go beyond certain size, as described in [CT-8	- QoS/Firewall/DDoS prevention](#CT-8), which could be part of a [denial of wallet](#ri-7) attack, or trying to destabilize the LLM so it provides possible private information contained in the training data.

Ideally if possible, not only user and LLM but all interactions in components for the AI system should be monitored, logged and include safety block mechanism.
When deciding where to focus, when information crosses boundaries is when filtering should happen.

#### Challenges

##### RAG database

It's more practical to pre-process the data for RAG previously to send it to the embeddings endpoint, which can run more complex filtering for a long time. But you could add some in-line filters.

When data is stored as embeddings, a vector search is done converting the user query as vectors using the embeddings endpoint that may be external to you. That means the information in the vector database is more or less opaque, and you can't easily analyze it, add filters in or out of it, or specify different access levels for the information stored.
  
##### Filtering 

Applying static filters is easy for known patterns computer-related, as emails or domains, and well known terms like company names. Picking up more generic things, as names of people that may be common knowledge, or private information, is not. Same happens for detecting [prompt injections](#ri-10), which by its very nature are designed to bypass security, or foul language. That is why a popular technique is using "LLM as a judge", that we describe later in this document.

##### Streaming

When users send interactive requests to an LLM, streaming allows them to progressively receive the result word by word. This is a great improvement to usability, as users can see progress, read the answer while it's being generated, and act before it's complete, just taking the first part if it's all they need, or canceling the generation if it's not in the right direction. 

But when any kind of filtering has to be applied, you need to disconnect streaming as you need the full answer to process it, or risk exposing the information to the user before you know it's safe. For a complex slow system that can take long to answer that has a huge impact on usability.

An alternative approach can be to start providing a streamed answer to the user while detection is done on the fly, and revert to cancel the answer and remove all shown text when a problem is detected. But the risk of exposing the wrong information to the user has to be weighted depending on the criticality of the information and the final user that receives it.

#### Remediation techniques

As mentioned, you could just implement static checks for blocklists and regular expressions, that would just detect the most simple situations.

Adding a system prompt with instructions of what to block is not recommended, as it's easy to not only bypass it, but expose the prompt and see exactly what is the logic for things that the system shouldn't show.

A common technique is **LLM as a judge**, when a secondary LLM analyzes the query and the response, trained not to give proper answers to users, but on categorization of different situations (prompt injection, abuse, foul language). You could use this also as a SaaS product, or a local instance that would have a non-trivial computational cost, as for each query (no matter if the main LLM is SaaS), you would also run an LLM evaluation.

For private information disclosure, when in a critical situation you may want to train your own LLM Judge to be able to categorize that information in a bespoke way to your organization.

Having humans provide feedback voluntarily on responses when on production, where there is an easy way to warn if the system is failing into any of the behaviors described, is a complementary control that would allow verifying these guardrails are working as expected.

#### Additional considerations

A full API monitoring solution will put in place observability and security benefits not only for AI security, but general system security. For example, a security proxy setup could also ensure all communications between different components are encrypted using TLS.

Logging would allow not only to understand better how users and the system are behaving, but also detect situations that can only be understood when looking at data at a statistical level, for example a coordinated denial of service on the AI system.

#### Links

* Tooling
  * [LLM Guard](https://github.com/protectai/llm-guard): Open source LLM filter for sanitization, detection of harmful language, prevention of data leakage, and resistance against prompt injection attacks.
  * [deberta-v3-base-prompt-injection-v2](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2): Open source LLM model, a fine-tuned version of microsoft/deberta-v3-base specifically developed to detect and classify prompt injection attacks which can manipulate language models into producing unintended outputs.
  * [ShieldLM](https://github.com/thu-coai/ShieldLM): open source bilingual (Chinese and English) safety detector that mainly aims to help to detect safety issues in LLMs' generations.
