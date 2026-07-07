---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDNDIVZ7%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T225048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYUHEzF6Daxr0sAvGu3GKR%2FpESOwCD%2BQNp%2FRDANJ1IVAiBNkgzWAxMPrq85of3EyLcf207g2JDtkIoyvqIkpDdrPir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMI8TxW0zjbfBVTdMJKtwDchvOFIiMjNwC8HMlI9%2B37L6rwlSpUozjYY74hIK20phRWukyYPNG7z6K9bWMlcxJYlyG2F48LPQxXXzesUBnwfU8vkVYjDca8C5osYzi%2BfwkGN0yiOy5Y7wwppMdJuwTc4k47kH%2FWYoWPPCuc1Z602sRLxnnuiE%2Bnnly%2F7omvQ%2B858aEu1UhtC6Z7z3d8Hjyg2Lfqx8IC8O7MvWVXxjRXZSzl7oCg9v7ZdSKfbYwsnn87Bd7maQdhLcZqmWhc%2Bp9SMWIC%2FatuZZpsskaXlLJkGLnK%2BQB7dIcKC2sYO1SKAY68cEnR81lzXOJ7A4sQRu%2BSHEcciNZhk%2FOcH9g%2F4tt8GMBpAUPiKyNLYqvDir2qwcU0de%2BOZqEWDokqRmKux%2B43W5KNA%2BUtpvG7JvxXSY4D9h%2FaXM3wy650jeeEE3skdNulrbT08SYkyZDS5Z1pzFLJG1d%2Beofj%2FgzMi3n6XepqzpqkqTVIa5ZBaq7j712id%2F1I4%2FtwUe3JSKWsB4hDE%2BTKjvR2BbaaWW4FiVWbD%2B94NnOYmJzoznydLGE0U5TkYZ1xpz9mW3boJ6u%2FbhWrKP6hAq5dxySuVaiSXz6Qk%2F6KEFoxIkQ0gsgyz0g9jxL304BvtPUDhPwCLIOo04w%2B8u10gY6pgG98LY87kCOUJVWK9%2FebHAPUFB0I3WB3bWeMAKSLjkV%2BwTQQ5XM6TnLzwOaPRx%2F3O0BZ%2FBO3v6FR26hEOPHxJn9dse3UytXRV4ZJhRvcu2lNkGC4tNyxuRIT1bALdSOrpxbgRkosJVDIHZda0Or8xcKGynbCkp5t6WdVlIBuDm2zsXaIZJnMnDOIOnmQs8W0fKpSdrFLJ2CE2Uv7tnVKnAm8ZgxLFpv&X-Amz-Signature=188983edf32ea99f2096be5d821198ef4d01f5680754e1f098d6067363a26f55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
