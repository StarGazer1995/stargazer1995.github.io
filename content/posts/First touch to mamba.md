---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDHBJBCO%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T074325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCf%2B%2FrvD27LQU%2BaPUb%2F8Fqm8BfLXoJBGoS%2BPDyjvXXneAIgUXj8oUqk3akAENp4K2LX9lykRsRtZGJJlJoJyuO7WYoqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDImAfcNNsSVBhMXULyrcA0tnaG1EcrIa6FK4QUBhRLUA1NhcVIRWWYt7Qp3xAszAoluHpERTAOo6tnWK%2Fc6LGyR%2FEauyrTPYXsv%2BIYG6qmau4mSc9Zwt7LnwWVZ0weA8ualMrGWHMq%2B0gcj5m%2FLu83eGsi4MmrnjuBfVPtBEjqsBZH6ykNKI9NJQtzovcpZk27XXxug9k8WKN4cN7s6Zilli20NUPfqQ%2F3ROh%2B0CQgVtNd7P2iLQUf%2FhFs3%2FzMQdf5JmkUuDoogE94cCuXZTb3UkzHYt4avevSlW2ixrO25FeB8pAJqRqqjfF1KmhRaFdB1SavV4J6eNjAI%2FxT%2F2fI3SI33X7KbN2qozyzzk%2FanfXCnST6U80PmzSS9t0rAOlelFkIQ22ib%2BmidMwPzvCsdRnnwFvtBvrGVBXDQLFTlE%2FzZnpNwKrxWEpxbVzi8f4aX4CWbxouKxAUh7ZdHzXUjYeQFMpQDvL85HoeU1xng464hnmqHSa3w6ziP8hQxpkTWWgin5XY%2FsOwQqyl6bycn1t8tr7jNG3ii1L%2BeJ3Rq1zF%2BxeXHKf7yWiMS%2BOiBBZHMHLHEGHrHSdPmdS1JYNjQZEej2JK80OYvgCtDYfIWmz95N6wKe2GZskQI8su%2B7qtdcrzGf1LBNOX8pMIPtgtIGOqUBKARHHe%2BtuRuz8mUvDieyOhkPXLTG2J45ufe9yvRD9KgzMaPnwPByA5Xiv34T3FP0THtUZsmqLCGhNWU2Ujbcec4G1vzQ6SgJ07hZuQeye79dGTPyJuNHDjCqZTxAodppxrqi4z%2FpNetA6cmAmeEdWka78TmH%2Bjklm1NX0Pybbl5Oxkl7qgwrDxbCD6SEPiiwud%2F7bQ68x8rcjrTdeE3bK7I1sPLh&X-Amz-Signature=cb9375753f85825034782bc96ddb1c2248ac9297d2536b121872a2d854ee52eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
