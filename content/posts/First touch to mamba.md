---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZUUPBOT%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T020158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2BxaHORm6JAKyhn%2FtqLdfScyWUuSEiGA%2BI%2FzVKwdr0YAiBYZMaNYkF1G7mNCj4J1jrm320hJhLMZFW6S2ujiTH7Eir9AwhKEAAaDDYzNzQyMzE4MzgwNSIMvGuj8%2FQdOQZQTtPzKtoDpEtFy19VzcwaikIpJ%2Bw95sbQ3HGwJpoYnbRY8qWM4T8XO6sTp0nQ%2BVX21z55x%2BI77GDwLLfJqiHhwwpLgMjhaVERbYQ61CUFmPhJ4%2FsFW7s%2BI2Q%2Fix3egXJxEfR3fqgw8tl1OIVbcVUj2ttW6Hrbs5ES70YuJ4w1sYxDtK8RKjFT0%2F2gcQGDYzxq2eoYawh8gN3cnNw8AKcCPsluae%2BvTC1BecLg1ez2nl69ct1hRUWre3b8r2x4nsxUHREY%2Brva%2BRc7QfWUqa6RJWf%2FjT%2F2%2Fb9fYoy%2BAPQc0AmvU06kRETM3Oi44PoLVQQ2jSbVW6j8Jdir%2BBebjiVEn%2FddSrqHdPCnGkxebzO0LlklI5b1KYoYKa%2B8tZ0BPet1P9zxpVMspJKJiJ0Cc5O%2BxFdeNnsfUTJQxrkMvjBhAg3pntslWPM%2BSSN6%2FLjts2mpo3BKYTDR%2F8OW3btonFm4PdjeKO2L%2FFmxQdg%2B5TuzQV70it6JP%2BTcequz1SoM7MpDMSJA9ufEsf6VZKRTiL6NLC7%2FVifoSiSt%2Bttygj%2BW12Gy1ozdlXcnR0wuwpc%2FwQYNxvyEwA31WhbNsQblQoiU7VOS7Cia7Mc5R4mwVDVu%2FUtdKmrz7q5tFTE%2FGHipQZOfMNzV1NMGOqYBCb8a4aF3Tx3yP1F0FdyCWpdt535UD5dN2tUK1wI8tXCFUCniGk11ZMpzZjloe108M%2BQ5dlQqGCagSBN7UKOTfJVHusZ88t9M6ufZZR1NCTle4%2BTVw%2FQI53xMHImrKdD%2Bdh7NMBOQaDi2UpXMng9m%2B15ZRc%2BezazYuRFJX1EAsyWrdet2qiNX5%2B1mKD%2BB9En6VVAzf7xz10Ldz3KtSTVFjFAn4OH%2B0w%3D%3D&X-Amz-Signature=40aad977ff5d553160135991f5fa41ca11774a56faa053ec37f3c828a2d0852a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
