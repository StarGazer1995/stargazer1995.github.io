---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXBEFEZ5%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T215841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDNANjeiR%2Bvotx6savcUpXgWwIOoYLo%2BLsxrSu4snXilAiEAhHOEiR%2BssHHIPG%2BFEZEPmgfit2ZZSScfGsY0DcVmkT8qiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJaRzAN8uRC6WXR2byrcA%2B75ORS6JDj8BNCwQSNZ3%2Fbd8nFWL63Bj1bAVWVcu3Pj53EwUaNic%2BUvvxeeC1e1dtqxn1P9lvhqg3WgnJ6s4j%2BMoPt%2FWI6vDBm5JhhAfK8LITNygrObrXVeJI4TDFH4G2jBEHKkpRL32zYApAQevPrhmlZC4H08GXEWPT7Sro%2B9ouH1lrARgc8f%2BmxV0SKtxNYS3F8igPxcuwzf1XNALOE1VFnF2yZrsHNop7R8RdIp2GiplTkUEYqQd5InMe2blpD%2BmP%2BNqGoYYORQiEShCmnjpW%2BwZcm4gru5BdKfvPH48nbGnT1fKjruCW9lgXu2HfrN7klIG7G3ILSYWmLNxDksNEEjqvtyvOFnfsHJ0o6Ozy3CAt%2BIHBXEkQAK9tFWPtiJAHR7RUQIg3dSbUKgx8YQ9Od7up2Mnt7eQCzjDAQPt8JJt5oLrl4sX970a2Z0f2HrxIS5s49M3U%2FSfSL5wtu5amQCweJ7uDy%2FT5RXflMN%2F4DkZcSLa5o995Ylwc7M9iI3crEaY1M%2ByAmc7vnVw4OCje7S%2FVOEZR0Jd0ysIsxb2m8fDvDOABXfnRODn%2F9bkXqU9lEiaZihcWLcasjk2jpCV3qlKOcEBYH8nCkXEsT3RY7pC3KE4KcEkaiWMLzilNYGOqUBHcBzplDUW3mZwB%2BywthJNKc3hyHP%2BG23FdA06kHWWxHMKZnYFL7doZ5qRvO4ZDM6pD9RyeSqAdns6B55tH8q55%2Bf8PPAZtXFk0vyqFiHEEb120UwDhkZrtEmD%2Fm1rCgf4IhxcwkBfYLeuHyuMPLwdGUhsFfUoz4Ll%2FlleqI%2BNwhxyoQCpnGQQkwvb185GrReu6p8QhqBYzFLy75a9ucxu%2BMkyHR6&X-Amz-Signature=4af761ab5848bde0cf46a470775f822721f49a632643c43ca7e0b0c26f314417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
