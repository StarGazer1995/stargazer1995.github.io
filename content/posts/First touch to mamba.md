---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYW6MHEU%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T145041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIC%2BWRz6tsa4Uk2g09%2BI3Ymj9uAdn%2FsmtB58Ot61yxaT3AiB2GrGTBh7HvnWQsEkUjtdYF7idNfKlFsGM4n4XMrAtgCqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkFWulwgK1L6gnrosKtwDW92DCOkVsNb%2BRMtQe6yZvPmWe1gT2eDhYMrLhlUwpEZ5R7bYIXS6YLqdv9WWJCekC5dp8B%2FYYA72NTMIpv%2FXGNGh4OjYsKMis%2BWtenYBq6hgO0EpPKNgb9FN5pPJ3od%2Bu7szxuy7n7J%2B8%2FIvGWryYi58EEooADw7mZSKr76e4UtKW9%2FNECRyW0qJLXHiKbQKJI6blW2PCUiZFD0xbh%2FbNr%2F3eVucdHeixQFrV%2FgpBBsgzqPsiULyb4acVO8RSVY3KI5cPeCO7mxJFnV8%2BzaCY%2BRME%2FjleZfDMbvE8ZI32pttm1CrhdPrnDfWWyApfDTRhbz8Pv%2BvabYE675%2Ff41D%2BCpvbxv2M4nBifW4DUiq0wFQeBiWOjbxDkn0BGTMDZAnhvO%2BVEokDsEDi%2FFCPeElXH%2FiiaEcnFYhgb2FpPEAqx8ql76qxz9Ko6%2Bed17e2iO3Izjy38vs%2B79%2BuXxxDN440olGwzX4aIkplBaQLLzY0fbr2WfIyzQvFrQxdXIOH4X9sANor4Rq4uCRjhall7uYc6LMzbONTmxB1DW2FfkJcpxUZqzEQ1E%2FwnQT1q1PDTzcEHjETMFRfGMVrSRQj4F41YT3xnyfvXOG0iNKQreZHYy4cSssHViYno6TKS4w%2BOnZ1QY6pgHrvqfCHNd3ffq8NK1Yu%2BPF8txm5p5hx7LRsINYTxrEOLKiH2x7EojnnA3XUNX20WcOALUqPXPmvDVavjjhuF%2Fo%2BAHBdbc7ze%2FD0XCr22No9WHfYNNIYXmjEtzDT5oxN3Ju04a0kIqTXq7lxnqkyn2W4O0lNAB4Arg3hgf%2B6TM5OzTzV0kyaIqlD3c%2BiHmLboHSTKmBTnvxjU9yyUcsFc9gOEclsGUG&X-Amz-Signature=4fda516b91101cdee1a2cc7ab472e748bfda1e72aeb3392b7bc829016ae23c47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
