---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQQ2XWMZ%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T061308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJGMEQCIGQa2bCTe785rNtaMMqLduGGGXDbJAQA60XM3hgv8MbyAiAWthXhTjQZtjK53PmAIOGoW80pHp3qBsIIZC4V2A5dWiqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSz7TqbBVBhwyAH52KtwDugFyOPRvXSIJl5zMmOWZCQ3DSi9t1ULIQL2ghBioNjPKy%2FnaaCvibyeTOijgraWkFa9hnhukk8A2cfCMfrzbpX3H4UoiSBLP5GGw6%2B8JJtyN8LgzQiOMJJ90fm8HjaIKDfM9lMIT6Si0RGB1PXxqjNQqvpIWlXi32d772z5NJPMerI1pMYTq0bbtvHCVvvPBSIZTn8rxmfb8oZWRqTRoqyC9mEASPTE0md%2Ftm38gw7PACtx1KvZU%2FsX9AczSSRoVAfr73HMgF%2BUwXoT8MsLM7bSBnMcb1203nIYdCq88PzmISmp%2FUT5Bv1aW1ySVe3oXZk85iBOTTGbBEXEOqzlEi17EQJj2fA9AYTExOu7XyYhSSqY63I99%2FuELKPyu9Fcp8%2BsqaxGxX0EuQ0DcP49NDunO06%2BKv%2FjNHgi42H9xI1DMfEg%2FDJClw3Sd12zHd1OU3mz1iNuorH4%2BJg%2FbFXeCVwupOl%2BWSjofuS5dS%2B7zbX7MbhQOlSOxHUHrIEaTz47TspLrgGgjuFx89Ac2nsF%2B6m%2Br41yPn4Xqytx5q3FxZ0w4f5RiAJo85n3s1j05lroZ1rcUQakI3l%2FO6R9DU%2BhN0RDsBrVt6HhWpNKzKytv%2BtPXO3e5wwvYtb4HpQ4wyLG60AY6pgGK4zi6j9BYECfzA0Vdqia56B3YGZ%2Fjfk5Es9qo4fke8nmkipWrNwm%2FcrjEm6uqiw9rzGaC2GHS18nxulmUYFGUGa%2B3vZqw3QmQLN%2BNgjI5NZdkvi16s2ao9mEDdi1TTI%2FXNsC%2BDaYEGaq22ylepDTmuLGNJr8ktBnJWkmC05X3Opg7bpfjT3l%2FBW%2B4aIXSsNsJU8VywkvNtjBOSk2CaQjN4RGnoXax&X-Amz-Signature=c5be14d6142d119f59d7f1bbc8ccb056b25f08d7d6284fb5aac04ab322a2eae4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
