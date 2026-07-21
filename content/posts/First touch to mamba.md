---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MHOVVVN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T045734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGODZvP5Bq3wPal8AbGo2OGWThf60xTuWQ12m89jQlY6AiEAlfVgSrPszk8PaJmfpLuSHpeh31kR7vl1DzwER9BCkjUqiAQItv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbZcP6Hc0h7XoROPSrcA9oSxZ93QCFg19eJ0swMkx8KzJGzoLq4kebKEiFu0MybYsXMP%2BxyJlWJ%2BS8uxTcPxRXSotuZrDDGneXi11l33gxMDF4cMQR6%2BWVz8DyfwBk1ys%2FubJvSP%2F%2BlCdKF1xv7QL1pHWQ4%2FAA0J3%2Bs5nWwZKxaAqXUbT5SZAkNT76tZrPMpZi%2B8sOtWovH3GZrypDEZv%2F7zha5mgsOtSNXIv4KiGK5KX3YInJ7ErGTeaAoGF8%2FSehCxNQyTJbFFJ1O8m28rsezHPKaEKdH49VtYZyTrH5Dxwo1ld6gnCC39a2%2BT856%2FkilXGrpzwdNvEX4K3zhL10EXWOni5Xndfq4lle8Fs3HsETc75snoBRtOaa0836X6mlxbztdrTapPJy%2BHlPBJLGlRmotclu6L4B4RvNS%2B04F6oFLOxLuC%2Fr31Pmi7eGCBq4hpYeHg6%2Bstt1KN22MNTHPaqmCi9vj3jIB9%2FdEm2tAkjrnvRQxVUAVCWu8N1LjQWQgmoBnysvncN478oYPxeZK0FMRXW7xdmCvbxHDOABe1VKLI3vdXwG0Ti9iVGVyYCpBM9xk8oTJooE1v2AsDzDHX9nD03kmkkN1R4K2xN88jA%2BF6WkBkoOhIdP1pYEh1%2B01V1kjt0bMA9xFMLvy%2B9IGOqUBV2Rd8sTtxYvX%2FmmGSsh0mUAaCoffsqkmQ7cAoH1AM4AvS2%2FI8r%2BcQsm2vuLVKRfi8EoUbEu3V91hYsJjvhal%2FhBnXPaiEQsw9qTbLYXZ5R54Jyo2TqfTx5ELVN1orAIdCsYYZexto9ezatx3%2FmgBTuDYpk8FK8Y7tHBBAjmDHMcIB0oJs%2FcqnKqvl1S6DgHEh547RgQz6fUd2oqItoQGKzr6j7a7&X-Amz-Signature=07886333157502f82d23047e059b6c3a76aa2bbe4d48188ebc83c1d962d80699&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
