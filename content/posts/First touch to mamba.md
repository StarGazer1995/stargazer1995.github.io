---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJZCXPGY%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T012158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQDTTmP6dCbnerfdlMDFdZVeQzPmAzg5AtQxiD2tWcU87AIgUOjCGp49gPheBzJMmb%2B4qZkQnQPqrllghSlLlt60VNQq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDKXf1UZtQXjc4IerVSrcA95Erl5s%2FSY1LUv5q1U2lcEax6SkNiHbPOCLWgS%2FbAesqYuxT2V%2BBobmLKGc8YRngtf19O4q2tHDyQQqfU3dE6%2BnSdaSQf1dfEVkXF611mK%2FzU4%2B%2F6yY4I0NjwBS2eZFnEnpU2sM7NVa%2FQFUk%2F3JmH41r%2BiXlkgCpEyE25loGaEW6mcpM%2Fc8RBKfbQcHgIQyc%2BAre%2BmYy%2FXlN9JbXu93zF%2FG6qXO4Nbwt1KqCp9522SW42B%2BakMIZhV4U3LAKSKrBGZ3XTEKzqeKfLKBTtTt792xJ8nMwWnq7Ds2xemPRgjMcYMoXbetIIb%2FKYrP01NfIzt0IS2YbUT%2BiIH8eeKAIqxehl3FOt2I%2FcJ7oDZ6CJSNvK%2BziUASQ7GzRUBvUN9AT8QgPSMb1z3RrUB0t49yNGA7EXzjlOxPcVT79CPCrw4KOlPdo9OlYVAiid8dX4A%2BG7bKlW11O3GFS%2FBNA3VW6X7RRrfwZuDNOt4vJjePdkVQGLJngmgL478U8QZNHnZAAlydrWZDtjmlO5XMC3uAk1EuGkL7SgPP08pSigTSZ87t5cal%2BFinqCOHx1ozAB9tAP9D%2FxnPJ0xlv1ZmKwgkETEcFi1SiTOHf2UsbBsWIbcpJXOpEi72HxT0vIVHMMWXytMGOqUBan%2F%2FLfYo9wJk%2BztDysHtTlrL7nKmhuXH6Y0rZdIqiIcrcBAGuyV0mqxwdwV%2FU%2BVZaTQQXqw0S8EfJ%2FqAFaa2Afa64xRpPmYlc7QFLpvwjCuoMU4asJgC2ZvEV0YcHLk3GTQvpwyAFDt53wryP9zHC9pPkCH%2FUtIjZnIQLRP1o0kz%2BXs5waFHkMw8G5IQfhF30UJr%2F3Ukz3raTv5IrGKXi6wKurJs&X-Amz-Signature=38fc4f6e17c9cc34f10e77de1a3623fc7d99dab292d680502718e124a2cfb499&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
