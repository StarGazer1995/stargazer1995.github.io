---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YARDO7I4%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T045733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbBbSQrvV%2BelZe3HwP%2FDk7lV8CilOfwu0vqOLpAWXa7AIhAMycTTgOfTzdI3JAGviyhkR3gzmBaoWdIdCxqlBC3xeeKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhwCxrVS0d8OKAuysq3APXlqVQth6SMj3jwIZ1CeSkqaltq9cUvEkxQCwwFRyKju2e8qraxnqlSKMLIbf6GCzwhvxysUqg%2F4sxz%2BNGuDsnCVAa1K39%2Bh%2Fxel9bFOPTcEarXkoqRikPttg81XzuMp%2Bs3e2acEiVGXiMOHmV3FaP364OPEw%2FwMiySRPdyZFtQ4iG2MQBdMuB%2FJ4TzqiJwq7jhKHZwNgzIWmFdT8Gq13jDC%2Bn7qdFNSBdKSPQYTwnvZy0R28bQHZdQZ5Ckesoq%2FnuXIaYLUbhzYghchXjnaO4GSZbkeVVPAOnxu9%2BjRGhxKeIcuXimQyKey9gtSXgAW6xDcgCf0CdrxZ6mid9VK4uZcq7nTB7fHg%2F6kXe2yWh1J2MaSTYiQYK3rtar9KGJw7%2FlOeXm%2BVf2KPGAouiTGFhlxRk46MtJopLPsfAaBGm7M1MxSdqEaUuymOMStlKoQMrmBhxDYAh1IRUt4j9AS6uGqMtvkO73kp3shjR6kdfbV0lis%2FvbzaohtIjoqJsVoff1R0K9u%2FBBWKyiQcyiLYa9MQvv6%2B4sqmgenB6WNnMv8TU%2Fd2oXM%2BTalmkrDV4XSUcHqqRsBN1%2Fg6qIqFIhoY2uUgGXMJQI2HFdidRusn9ZUd2NXuGQlbxS95O%2BDCW0%2BrTBjqkAXVR0OdR7j4BbgoHCKc94390rdG11Y15uuYTE65cYXfvmmXBejH75YrsPv61GpDa%2F8rmGRdXbD8VfNg33lfUvNm4xWOnUSE61m1RNmfIS8C4joYg1Wnn7%2BIBLO9aJKh%2BkqN59hI0aS0x6%2FkClJUxEU59Wk4id5Yo5keSRnOOfCzK3pUQrPRcphGkkfifAO8%2FVzMBtioot0tkKh%2BZS1TdlVL2QE1t&X-Amz-Signature=15e52d637c970bfadc160d0a2429985664558aef98f25d821a5bae62a7c4f1e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
