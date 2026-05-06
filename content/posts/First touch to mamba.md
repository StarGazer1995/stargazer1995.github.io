---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D4O6AF3%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T155842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCqbAsMJ4hLHUiq9ZEXF5QfLMAEZxN%2BWeXNqJRE7yLSawIfB%2FLA6EUjaJE4ht398eKqybn5fKqfUsjYpzBKQz5Q3CqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BzxlctIDA6G0mBMPKtwDK4Dd0SNIl%2FE53IIgXgBA5%2FaEciuKXWq8yKngdW9iqa8Jc7OKBqfGhGcDHxVFX4qZeHI7K%2F6SYiPgzBsGlBJPc4%2FTKe4JXh95QDzuiLUsIUN25nf%2BTXUvq55yCFHVgDutPTuz2NuCYT0u%2FddPLylvOXfxo7AMxiLKw3QRcM38PJUI658o%2BGKwIsfUOBLxqRkqUeELmJf5izXMblSFNK2SwfUMUcO36ofXPchEGV%2BtO2twrrXAx4HjipDUJVr2%2BcCQ5LandNUFD9%2FIrKqMOtOjmAE71OcxecATXHQEJcl9Paqqxvwav5FAcbKpGgQG8bCvnD71oCpvE7RJi4%2Fp6e7YetKhzNs2RDsEfIfu66s5ty0aVxNiLWq0e1TSbAyxbcJilSa%2BCg2qvwVJBW10o1ZTgDWasJW6fSsnBhLhjz%2FOLRARbbKt6pSEPrf8J5ovWgkz%2FGonawTm1nF3Pg3KwGzpS8w4g4Bls0iMdryGnV7Asy0cIPwS6MjoGLvQTmb6pY8HL8qFG3f29Z00tuVVVqf50H2JJMEjwa44WBCoceAWap%2BJotBmUXH6KkifQCm3jVcAHnU2nULve7bOp9oKMc%2BKV%2FKZegmW%2FHhl3%2B0IP4VXRtK4gqeXcUAcpx2qe4MwhLPtzwY6pgGqR7BdtRwo7Kn%2FR77G72WC1bR4w1zqwCqBg0NGuzwt4wYEyn7ZW%2BYhnI0DbWEud%2BDOabqQPmnDI2%2BRvO9rNrxdqK7sCR005dFKATRq9mQGFDH0sQ1nYmbcoIGqhJz9z7F8%2BEDkMfNli2Ybj65UZaDOQGwr%2FSQWLnqfSyd%2BVe2w%2BFcGfitfxhvYq6u7uvmV3ZUCT09uf69kZQ9cur2sqG707ztKBVy6&X-Amz-Signature=cd47bcca4c096c5e49350794dc8891276fc0606f9099a5ee4fca547d013a916a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
