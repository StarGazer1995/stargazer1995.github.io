---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB4YBPJN%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T115338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICDl7e%2BTCD7RPAFGQkotBLbgKpF3qrRv1j9zb3xxu%2BHCAiEAk%2Bk6zteZUx9yrHOBarfU8sBNRK5sy0KRQSCUxIIgiwYq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDEc9WCksnJET9xt7dSrcAyTXLVJNo1xpGF%2FyreB1%2F4reg5%2BYsyRVwEfFpJM1taDgVbZO0IVXhq2%2BCkgTL739n66DWo746YGyn5Rk92qVHnWDtqAAvXEo3KmrxXMhjG3CcToFwL0VjtdGRxRxdPxp0lsLLiqtZ1pgN3VRiYL7WuHUPiCtmOsH6y5G2EK4sS0sA%2F02B%2BED902vaPOUQSFqB9v2R77PkeIIRLgSENpHBIAv6unVx88xhel3xNYtoyVeAlnioAdIz2Ei1xOqBVQUO%2FCJHu%2FIEKNcXqEyKmGa7PXpIrxeiRnURGSExwqRAxk2LooCY%2BYCArYYngZJsMGp%2FENn1b%2FpiVPMTkMl5tRZJWGUbqL95UxWzY2ZTMTDY4wF%2BhkEZENlVuUYQNiphmer3bqITz802BvSTG%2F%2Bv5Q2i7huIkG1GtN159y9q57OFP71U%2Bk08D1bno%2BakaFBUu8WaXOuJOzxlpuk0DMiA2IXbWzFgtOE4u1POJEXrKNS0eDeLEHli2LO4AjLBljgBuaGIXDajIIfeAEUyXHEgQJK5zTiphsB7uj%2Fimd9wUJhuev%2F1fO1giNhMntMJ8F9iQc3jBaaK2Njx1YnnPNnBak4rdEAZ9amfX7itJxMXh1%2BGM%2BGuDu1o0pS3YyGGRUlMIL8ytQGOqUBqjunJzYxRjHAJeRRhulBuDa4MT5fdZ%2FOP0SnXEFuK%2FVNVtjUk4eQ1jRIEGfYO9Dwx%2BkE71ZT3YavSZkat8m4FpNf0dity%2Bh%2FX5QeJTFyMhIjojjLPW0rZ5s2t0x%2FouubmaoFIN7DmRcZVj0lI49vzX%2B2oaKs0%2BOOR3%2FeAxq6mUeI0kn7gxYOmaGEGlr2WBcByRE%2B%2B2se2Ht7egFyMIqndwm1jxEA&X-Amz-Signature=dbd09e629ccd9c01aa6022f8040d3de4ef465af0ea618ce6c1cfe6cce73b2af7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
