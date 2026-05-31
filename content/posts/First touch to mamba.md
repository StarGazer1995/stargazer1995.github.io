---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFNPIRVP%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T151035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCHJqrULqS6ibDp9yC7hRoHWN0RvAID01iBSnqYkgUEtgIhAPedcbkj1WwiOiYT%2BC05WckEAVtun3qfCgxKqTYdliadKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwymWJFzOlT24doqjcq3APvFD%2FElrb5cEcNwicpVfovMyUTZEq2RPUpD4VjrlqkRvDErzWwmQycq92P%2FeSksdmDBk5s74tO0HXOmhEZumEYAQ%2FyX7TyhHWmToyVlcbVZhgJQPiH6UeaBs1DdnPj5sEM3U17HYOOFpQU8dTCD51b3dzaEcDBx0rLcVko%2BX29D6YKsW7JdOrW5SpzbGoUq6%2FZtk5yGEeGBcBS7PHFfvxRmtxuH8L7TbKdN7lpZ9osZxrjjJBT6TssWiSJWBRY6GUtURKvHSoeIGDmEiUyc%2FBhHOpEqAws2L2YGTm0mGgOTFC%2FgynAePFc9WXYt%2F%2B8MBjIS0XI6fAm9T00Q02Gimd5ia2BCY4QC0Yxb6ePcO6X7LFaIvGU2iiKSBiZNsFqsYtm2281sJASG1%2Fp06wA4m5ULbCamZ7fSYcTSgTXW7%2B1ulyseOSho1zrCH3wrVRgx2KtPpg13EfM%2FwbrjpTfJ7x%2FRxX8VZAwkLqD%2B68mehi5uF%2BTOjMDKoNemSf5gdcr2qQZG%2BVpDJhtUn8P8s4OBuYgC0yLa1VIZEmnte%2BIbchyv893G%2F8wSPNmxk13dmhDlrSurNGfHar%2Bv4g1PndkAaV80HqVHwR2ZkFQHpbkBOMH%2F%2F2RdKRyJLWtdMBrsTDti%2FDQBjqkAfFtBA%2FwanbqZukjgBUtYIufGfU4xyok6Yl8M5CS6I73QWblqiOkppzvfFjv07H58GuBOeduIikss73h6zjKrdLifBX02MEhiXjBb4cKIiy3EwxCXxZ%2Fh6qUYaksMehyl%2F0ocnJRvxjpCm43KIlbCyNuFNZjLY9QS4a8tCbtoK55BLis725wdYUhDlm36V8r1DPMJSBaTX1lcnqbhkd5zq3SZREh&X-Amz-Signature=1010ffdd0da0ec3b99bb5c9e02337806dbab5f129e0f0dd9e3328201ff4f33f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
