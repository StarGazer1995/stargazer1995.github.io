---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675ZAKM2J%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T135217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA9GHMc7mPWjIh4oHKN%2BahpK0RRrAyUFKa19xqbAVK5EAiEA%2FUtUp6aHgBCkOBjEOFTGx8R5tJ78x80zAIVF94lHBQ4qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLy6%2Feu8uhvqnyRoZSrcAw722dCoBIbmeArKcfq4QobRECOverMwMEAFPCkLsIyXeRF3QQyHVCh3Tnx6gzrsLmKSFZC4I3%2FM7lzzAi3bT6cqpd3yQWtS%2Fw%2BdHJFQb4rJ0UA1E5EezFXeqcJVlmRK6PyxDZwXGjlf7pSE1jh%2B7o3wlY6v2KeHZkK9tVDrlL30L1v4tgxCOa7jqnzT0b7YAI9Px7TzSb7IxW2cjL3X3BlsnrNdRbBIgsFG7Fbuy1tjXDiA5yXETP2jTQRuRYE%2FNi1TpsUHuZljm0Sbn08pcCOMNK9hlDFQhaZpqRjKgS2Qq0oOp%2FAkyoG39kanpqnvjV7aXB4ELy5BQopJNoCumVNPltxmjKljKeOfo93IT8ezfrF3%2F4vzMMaM%2BHQ6Ouf4J2IoE%2FoxKoJSzzH4tZzbpFY%2FcVU8GMPTTB%2Fae1FFmSJM8lPCvJnojfiaFS2P6xfkErcD8BHXRqeLd84Or60hiSvA9Vvs6qb1Z7JBOHhW3E924YUpZwgf6plFTHX8aR%2FbOqobBHrCY6QxTb%2Bf%2Bl42bN8y7YHgX%2FvuyULAI8WunNehHCVYhAX7gikU5So9%2Bqh6d10ESCW0A%2F3M2DT5lC8e2KiKhxob50WeGVkvp75OItqAt2sav5K5OXMAhpYkMI64jtIGOqUBNei8BOI%2BDJxBDh5KMUeN%2B2TvMSuplrFNAA7SFzptde58K0dqGPtHz%2FC4wVY9YK1aehVzV5DddRl7yxiDbgOC8YAXCEydro34%2Btg5xvuy6g6bOSptJTr1FKa3j4d%2FFSJ5sort1ir5b9qbcyHvIcV1TJZbJgYvX3ksbM%2BF%2BurFed4OBbgx12l8ASLseIV4ojc4pqQhyIAPTbL7XRVrdzxwWmz7Z05h&X-Amz-Signature=b111e6d698b3feb007d8b7dcdd0b37d181ec435311c76391448ece5410c42c27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
