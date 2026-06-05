---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GLPZS2N%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T192944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKVJZFHG0Wx6bIUWzzXntg1Ye9PL7Rqp%2BTkUIHhj1KxAIgV5sQ0o7vf4UFShhTPS%2FfHwAnHMN3CTF2UmBvf%2Byu1EUq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDAKYASX4614U0WmHrSrcA8zSnSAGI8miopsNRbQ80zNa4TwNtQJ15g9JJrJ33u3qTHkfSiGSi82bRtoU%2FiGZws3%2F%2BO9vTjZwG50kbwTm5M7276sf%2BMpXSv820Ks6QtNNq2pw4yf2YVA0RSz1rvubRilIqemuwTzkKxrXJWj3T0yWkr1wLl47C%2B%2FIycy3D%2BwXyBjL653fNPLStVZi6T1MS5LY9MU%2FheioHs4U%2F9JnH67YMPgwm6eAKtEccRZ5S8sjZW9KyEIVS8AnfF%2BLfXxGfIH2VBEjj9x3eOjh%2B2S1g9MGtJ8lj9pJlH6rAjPbIkP6BN2puCIlbYaCu8DKVOnYTMKepk%2FTebBqdxbKXtYvbJZqCgkWM1ZNkjOIN2srpcUIgXPPwxN6aJ2QyDl9FOn4EbQDzCUumveaAFjxa930d3N4dxmLawWwskTTBG4PD6hzEeTEyKUGeDuiwGxL6wuFZIhpMDrbR%2Bza00ktwJAYjC1mmLzy9szCLoHy1PGC%2FbnWQTXnu1I8XMK0TsW5Er1bbMvfc7lcFbdandDB8%2BwQ%2FewdhdKauUy015onWjWqXc6Sm4PyxBrIAb1IX3T0IT%2By2Mcd5YAWO6rkXOgOmB4yAJUnX9zlltu2jZIGXVw7%2F2Qdz%2BlmEp66bMJX7EQwMI2hjNEGOqUBvtwSUz%2FJhvjoUib2g4lc1WHpxAxot5TGzoiS0BE6g%2FsbT0zs1h8GlnLrTxm9vTxp5%2FPACjn6smomBHIxIvq2cXVYz%2FTqW4fLSKUOU1dYQAJVtcNZFX3xOfF3srQ6VpewAuNEKsSN1nvrZeXCiLjcmXQJ4%2FERtQ1rzPr5Hsw8QIIZLLubToZoNY8eLETbC7PlvbU83bodecSX9%2FbyETEEhYqOvwGG&X-Amz-Signature=8d90c6d285a2ce067391918694d496d9bbb8675f33958987148a8dfe9a053d53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
