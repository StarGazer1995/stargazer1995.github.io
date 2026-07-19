---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657EFP3OE%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T124736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7wYUoRJ4Cr%2FGg41f67PgMZjIN%2B4O2iL1m3wkP%2BfrcwAiANcBR5iSRcXmdF83w0cIK4Zm3iy%2BrnFglGfA3DQNw2biqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVAndzt2tfVUb5IwbKtwDesz2sPEa9I9oYDyAZwat6g%2BaTvRRtADKsYbGjErwZ7j1CdJ%2FXeYIRMs7ugUW9tlRG%2F7rc6xYNP%2B7vOREgdD6Rooayzv3s1NMpZr3wugwX4GKdJh2%2BEUmKv9CztawxcakGtJONUcyiLkKrEPCEAOm0qwIlNOQ8USwOPQfSviql36Vr%2B04mRR%2F3XnmnPM4%2B4fCpioBOrZQZFhRhbQTM7bTjHyI9y15gA59MmTgNjLF9EzwEimnYlnc0oKuKVy7TuvUlr96tRPl1xUHBAnDeFIsFfpcaTOXQkRLKUJGYgDOCgWfbzGtHbY7ZkzX%2BBusGy5Roc3m8X0S%2Fyv4wmbPLujidLC0IK5d6ieWhdpBwg7IfnBFpKnABUVcy1OQtfcRoQK0QIQdsJQpMTu09cJJQRhP0Is9XUnHnE7YPlxaCuG96Yy0%2FA07zqgmH3v4EzH%2FiAPHJbs%2FcuPbUVBxfTRfWlYzFXsz7M4r2HpnMzhPqZQEWzQEfzOO10PwFUi%2FHP4eUX5FFIx502lAwaQy9tB1M60eyvDO7udwBXL3ObwGCdLXHDsJB8vu6xHcBJZUiMRR4JVp%2BAqPq%2BovPH4fAUbX%2BuYJQnCUymTrq0tpcMuB8IVpwLBumw5wdm4RDPFxK%2FUwt6ny0gY6pgFBE%2Bnp3knP28f21dCJFOSzXCcSLngpQlSHkh3q72eEEL2o5ED4KmVVa5OvrYFikF7kvpPQ0ow4aNridSurB0fW%2BIA7ZnsB03V28O501kNBsD6a2pJwPGDsUENIl0IuM%2Fzaj2DdwzAynAu%2B4Y%2BkhnZijJt3%2FyuiLoS5b72ou95b9dXpI1fOLLARuhAIKXUCNKAOx7IUSLzPcQsyG%2FDuBhC83126zNKG&X-Amz-Signature=b43f02bc5fe7e8b96b9528a359dacf55c8da362b45c60a15c85b3d2d87604982&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
