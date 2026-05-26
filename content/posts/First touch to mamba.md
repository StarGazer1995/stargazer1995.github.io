---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAFNDZFE%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T143526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3K6tJHlSWAYleZld2fSX9uJhG5JxkB%2BX1MnahWQHhtAiEAwWHoRbQUt9%2BATyDOZ5bADmc%2FVhxR7hJ6%2BSo0h4B3HzIq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDHpJD63sosAB9dnrmyrcA1eaXYByYbJoJS99WTxALWzlxeOQ6XEbghPMLqWRnengBK4XJImks0GUZwVLkM8rlg1GB4U8l1UlIQ85%2BjHFvApyVWJ2RSZGI5FICBPOkp%2BjqnQ9o0rLQV1nfI1WiIsshi3KT9arsoGAVnaGIFhs8p1yOG7fRs5Q4aiMT4B8zrfc60Cyl58aGdlFeHgxudO2M%2BWaMjJ%2FSXy7B6uJWL9oD4vdrbA%2BpnKYTgeH4x5u4y1r2dnZF1wezKbmbUxaeLPpmh6HSmIVOnO6z54XeiYs9m08rtGAq3snefgKuBq7dJE2NywspmR1Ti8YohF1xYurE8F6D5vlaMEzn3LB9nhXAMYSRhoiHFV0%2BVove9fOk0da4w%2B9HDM%2FDgh%2FC3fsVP%2FLOBQMvvxTMu1Y1K0JNdRFEdP1mYt8PXrjudw0Gnr9eGAK%2Fd5mn6fTkkCgkalNyMd5i769GIhtfT9MXlJWZiL0WjSb%2FLUeMO83knGfjcTRgzelt%2F2%2BymoqErixLdQwscHO8ettgkXT%2ByV3fkx7Z8eDaoeXTbMdqZZw%2BOqbN1DjmgB5G15Wy0VVjJiSpiZW13WomkQYHJbVRYRvBA%2FTFXHVdE1cZOJj3YoyiFePoh0qI0%2FdYJMhptZE%2BEr4MPxUMKLW1dAGOqUBduf6gR35ksmAUXTDJp4X4xlHm0zinTCRGVtQrZXamwwsKsYHavf2szAyYG72LKNayYLbJZtwqlKaX6eiMo%2FyYwppjDmZdGW5gtNgOt1iSDyhlkh2LPRSE8ysvQHo588SQ4m1Lni9jKKjLSQ3MT3dOZ%2BiPkKwzoBVk5PexaexuN%2BIs3AnDS07OO2sSm6yNBXFSA0mrlTEMkHe1Jv71rM3k8yKUgKp&X-Amz-Signature=1cd1f789c387bb7167ff71911f3b3b13f59313c9e44da6ec2c1d622e9e2b6621&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
