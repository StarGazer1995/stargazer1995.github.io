---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCDNS47U%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T043104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDATzacjbqYnwcjhjaGP5DwnDx9E5wWfpqF7QIAk7TpRQIhAPWu%2BI8PXH6MmCHHYq4JFhubr0%2FIN5%2BTqDeR2T%2F3zVuIKv8DCD0QABoMNjM3NDIzMTgzODA1IgwyABVWLJd1uwRkqLsq3ANfw2IDilsr%2Bkxno4Uc5u69M7A4i5PUfwCeMguqCFKA23RqOCdD3UteNtkF5MVOtga1n7ZhLGU2tKjERxgnQ2FBU54ow%2B%2BLc1bPoPu5rRtHz1Ee7Ji6n72wDyWdzHnPfEMEp4LaDpYw%2FYWf9TyvNBLcrFDR6Qvaf4bUsJWPl%2FkFXWpulzRxWmdoYq9mP3iQHK9cZ0I0BLXa4I86dGysF3gPUHvv%2FejllbR5GA5oFexeVGHgbVR7%2Bew97gjxpSujEEX1EB17MmwxmPyJdL3wDD4y0DsZWGZhf%2FAitgTA4lrBSPwPCIQV11WuR%2F2GQ9fvhAe2EUq9bKBkqh8kAw6ppUpfr3%2F73%2FudCEpmwlROjSbT1kxBczd762xMc3768POdcoVFnuWBCaitfemgae3bISDhZA9pKr2vsg8AmVDsiBPq1hAxRTd6NquqEGgiotRHLmalaUjv0v1D0aW%2Fy3%2B%2BX6fkg2hlyXahWpGaYS1zuUuWE%2FIinL5PzgTxVJpVwePUSGWRKk3Utge54fYo6sRglbchu1EmRFhaQFRc4NwEaGw4fL0RszH3s09oHVSp0C%2B7AA24LCGz17TgIKPxxU7oONVq0u1jp%2BBrAjbDxZGuzlxQaM4fvPKY16RPcdoFrjCzlYrUBjqkAfojkzy95Nr7n2xm0yu8TiVQAOVKV1zBxEikR5zokUnWRj3Ue1%2Fm2hY8I1wdEAUv08oMnJT7OnrPgY3chSD1eNy3JDWNhj8RODpxRgZnaL%2FISPWAtdNrAD7WY%2BzKspeVF55IPLHHrbo0D0uCUoCnGBZ4BHF2cfTZfaWsjsQzIwcokqzYZZ3TV06RJn1fCLDxcAw0kVNNvK1spUTblVURWiYidCJz&X-Amz-Signature=bac908b436cefd129cc24daa490d70517e41a5fff1aaf6d1f92f8a13701b73f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
