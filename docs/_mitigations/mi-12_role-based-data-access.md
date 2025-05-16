---
sequence: 12
title: Role-Based Data Access
layout: mitigation
doc-status: Pre-Draft
type: PREV
mitigates:
 - ri-2

---

- In order to mitigate the risk of unauthorized data access and data leakage, the principle of least privilege must be followed, i.e., end users must only be able to access data that they have permissions to.
- AI systems use data from one or more data sources. These data sources will define role based access which controls which users or user groups can access which data. However, AI systems do not use the raw source data, such as documents or structured data from relational databases. They pre-process the original data into a format called embeddings that AI models can unserstand. Embeddings are stored in a vector database. The AI System will then use a "retrieval" algorithm to retrieve the relevant data for any given prompt or user query and supply this data to an large language model to get the answer
- Users must be restricted to access the same data through an AI system that they are able to directly access via the golden source of that data. e.g.: if a user had access to some documents in sharepoint, they must be able to access the same set of documents via the AI system as well. To achieve this, the same set of entitlements need to be transferred to the embeddings. 
- Embeddings must have metadata tags that specify the roles which can access that data.
- When a model/user/system tries to retrieve the embeddings, the system must filter the embeddings based on the roles specified in the metadata tags of the embeddings.
- A user may have different roles on different knowledge bases, so all their roles must be considered when retrieving the embeddings
