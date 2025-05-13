---
sequence: 12
title: Role-Based Data Access
layout: mitigation
doc-status: Pre-Draft
type: PREV
mitigates:
 - ri-9
---

- In order to mitigate the risk of unauthorized data access and data leakage, the principle of least privilege must be followed, i.e., end users must only be able to access data that they have permissions to.
- In AI systems, typically there are many data sources in which roles based access is defined. But AI systems do not use the source data, such as documents or structured databases directly. They convert the original data into embeddings and store them in a vector database typically.
- To ensure the same entitlements are adhered to, the embeddings must follow the same  entitlements as the source data.
- Embeddings must have metadata tags that specify the roles which can access that data.
- When a model/user/system tries to retrieve the embeddings, the system must filter the embeddings based on the roles specified in the metadata tags of the embeddings.
- A user may have different roles on different knowledge bases, so all their roles must be considered when retrieving the embeddings
