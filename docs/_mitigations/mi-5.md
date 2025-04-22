---
layout: mitigation
doc-status: Draft
sequence: 5
type:
 - Preventative
mitigates:
 - ri-4
 - ri-5
 - ri-6
 - ri-12
title: System acceptance testing
---

System Acceptance Testing is the final phase of the software testing process where the complete system is tested against the specified requirements to ensure it meets the criteria for deployment. For non-AI systems, this will involve creating a number of test cases which are executed, with an expectation that when all tests pass the system is guaranteed to meet its requirements. 

With LLM applications System Acceptance Testing has a similar form, where the complete system is tested via a set of defined test cases. However, there are a couple of notable differences when compared to non-AI systems:

1. LLM-based applications exhibit variability in their output, where the same response could be phrased differently despite exactly the same preconditions. The acceptance criteria needs to accommodate this variability, using techniques to validate a given response contains (or excludes) certain information, rather than giving an exact match.
2. For non-AI systems often the goal is to achieve a 100% pass rate for test cases. Whereas for LLM-based applications, it is likely that lower pass rate is acceptable. The overall quality of the system is considered a sliding scale rather than a fixed bar.

For example, a test harness for a RAG-based chat application would likely require a test data store which contains known ‘facts’. The test suite would comprise a number of test cases covering a wide variety of questions and responses, where the test framework asserts the factual accuracy of the response from the system under test. The suite should also include test cases that explore the various failure modes of this system, exploring bias, prompt injection, hallucination and more.

System Acceptance Testing is a highly effective control for understanding the overall quality of an LLM-based application. While the system is under development it quantifies quality, allowing for more effective and efficient development. And when the system becomes ready for production it allows risks to be quantified.

#### Links

* [GitHub - openai/evals: Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks.](https://github.com/openai/evals)
* [Evaluation / 🦜️🔗 LangChain](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/)
* [Promptfoo](https://www.promptfoo.dev/)
* [Inspect](https://inspect.ai-safety-institute.org.uk/) 