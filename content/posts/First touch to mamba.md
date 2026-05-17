---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BOJ6VEU%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T145013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDjL6OkgfMMT8lHUaqModX99xtpHDP0jL61KaN6%2BPFmXAiArVVjMkQQirskfJUEez2Qn3739KjOw1RpGPY854uY0mCqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXMtLwotGltfdTNi%2BKtwDzX4DdiRbnTT1gjPu31m3Olv1YBndCQZjgWVRaRJ2C2%2FVgQQAOpW9EpMqvFe2fpYFNbTg04cHCWsAL8w4dVtS1cJxg0%2FZrP%2BASX7am%2ByvAPy9lr%2FgTz2codrWTnvTTy%2BKGnhJCdLRMbca83WGTEilGCX%2BYs%2FolpN5SoOU3ZpnDaeZs0mC9BwoLs7y7X6qkCyqWpBd5QO5tHDiTq2lD2jz2aMpgDDdq%2BUAbh91cNQD%2F9Np1rfYiNETTwrQTM%2BC6xQwfsfFJGIz8WsmZ724OgJFbrX2IRVdrQZmtWmRj4Oclwz5cwax9SDVC0yxhli%2F77gnAuk2JCIdsMO8hxDWrlCFDoTpilqqVJGpnS45aTRArc8DSO5Z1qcVdY47qyhnnoP3b5XHQUS%2FVy0d9JDUb%2BJ9kOAjq%2BQBHFRJxfME3W2zHvwqHUNN%2FylozuUhZwzyO8oep%2F1KXolRAilbMnRvBz1GsSucfuLASnP%2FVEIKdouQIumoY99TM%2FHqZQTFwGseYBNZm54KfDJm1voW4je2h%2Fbt0U05o683ERo2SuO%2BuQ3%2B5YwbyGNSPEsU4Pl7IIv%2BGk0pVETE%2BWjLnMiEpoGmwWy8RYYLCq9Sv%2BDbhIluhVwv%2BKeJBFgtCW64njRt2Rww6v6m0AY6pgGjF66noznOVVH%2FaR0N6oSN7LfXaCMNzFBsAy2zecV1uIeMljWqaVW6XfNt%2F3YZzeyW93U4okHL8ohDtJXNeoJt5iPWl3cvxue1mQ5XwSpYFkMnftBU93aicpALWo%2FGmUVyEIutBTEL6d92efza83FX93nv3yompSGQmFrohMarGC4EFiiUqvE0uDZNr9SsS9wM7OC%2FLPcjQCZyZjZuO8sUbWg9QET%2B&X-Amz-Signature=c0f38939d090a704a3ce5761f22032d57bb574f949b1eb018aaa4ac10786082d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
