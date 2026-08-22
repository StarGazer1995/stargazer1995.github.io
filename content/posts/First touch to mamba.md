---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIFAZYQP%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T161034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpGXHzRm68E1h1HxCfDhS%2BM7Iu0jA%2BHtMtu1KhCQ%2BWQAiEAjObqG2Wb03s2sSS0R5vX%2Fhc3nImUmYsxVVREEcSygLMqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZw90tiSI841g37EircA%2Fxl%2Ff1pd4Xpx%2B1eB2XUQVweL9bo8tkVWdL2RHVFgEe7RSMhQ0%2BIb7aqfBraF9YsKB7iJQFcr6xA0aY83o5nnRITopz2Bu9ktwazDCsCZkIbdVGE7B4qpT921vznYvTG1Ode201jsepbTwnLxinmepxhJrA0jZ7S2ymy7uyO4o7mfI87GPInGQg1PiSoFbe9BZGWsVzCsG83sfxlOfbzfvXuE3ZTLbktv2%2BOFmXQt%2FT5uPbT3w5Zk%2BoupUy43%2BwaNPtuDnol4yqeunoZbQeC1vCc2WYoFdIBnmRsUOP64S8cP5NGqKB%2FCQ6cCLPfuLvZP7%2BxIOzRwYpt%2FzwxtvcpWAXI68pygK06C3WWTMfZjvYGf1z8Ru6CittDPDTjEmbcVTDGahao0XNmGxBCoX0w7IPBwAXoiXUrYEUwM%2B9jm8I9chdR8t%2BJb2rL5mwcsKU7Lka%2BCQBEsgJrgf9P8okzxHwuVxdCpXhc3j%2BzdCE5pwhh87suksgMnHWlDud0seHKEcq2I4ocEkuCjVtjKe85F3fGfXURy54WJGI8ckwCE3Fo62eOQ13MkDpQXBAlqT%2BVtTvzknG2y8hk4Se0LwvCirs2NuGRceREA9pwPDI2bnKmftwIhNtHZV4OKki3MLb2ptQGOqUBdFLRonAV2b43JqsRF0ZznGfM59k7n%2B5J3G6kfOXNY%2BeCzEUlXFsbtt0Im0NCS1AjAx3zJz%2BpaShJzidDNddcwoZ5QLVQwZXvS5pRCHSqNS7rV%2BmA%2BEUhHu09chH9VJiX%2BpcWFXqeuMqEDLaWrN%2FkICJL5USpyiDQK19HBVoJyndlxtx8gft3bfPNMbyvnBHVzTNnbStRouPaicKM2liYlHMa1eRT&X-Amz-Signature=0b89ef811404db7c92abf8b9af66c7c37a75d5780d1dd121430ca86ebf0435ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
