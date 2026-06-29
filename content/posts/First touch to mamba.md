---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUCCGEXF%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T084804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8ISsXRyxf7FD2NNUkYQbPvTPl8fau%2FxqS4ZUEy%2Fn4EQIgdvH2iFDWGVKlW602adGQpXdDL%2B4V9Ec6QtRhWWGZDykqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCe3aH2M0K%2FzsNDiyrcA0eLmM676ZeGSH9xi%2BSKvvfGsZK5TZPgB3mJkmz3%2BhWRrOWVhAyoKbAre659g0qTL0F7RMyEYRQ2wsF3TTWNBhrU2XjdZj%2F2I50GsFanPbNm%2B6Hwv1Q5GVa83LMKhhCbi8GQh6jif0Ii8nrF6dJx1hI6%2FYIpNjp2vIDxCDpUoExnF4BKgjCcDoJuPNEzM0S7rmeGC6EeZNpeaEEaYMPe%2BYm4uVBgp3XbjgiCcxuVj0MfD%2Fi2Wkc9ujZ4pSFv3PEcY5PvA6nKmkFyCvOupGpGylQZZb9M6svfmu%2FxC0y4oF5doKNNwxtEMe9PZzsFo9IPgKv4DGJHy4O5pvZYBcP2dY62b6eAQXapnhqLLHFNxX3Dpmuh5MGPpUmmgdKww05%2BFAWJjMjpxoGIKKFmogZmHsm5iLKj%2BxqwD%2FLlY3ZEJVH%2BNjFedDcX4cMQu4G%2F5GeG7RvV7XAiBlaHESfroPODCnW2eW8EnImolpOMNi%2BEsOoeIzn27f6SeZZygQAS0XEJHRYve%2FIgAtq1lRBRsDLtgcCXRVmzXe0UAU5%2BDnBUtp4LNmE0Rkegju6lsfEKyFj72pva9aVOj3hI6vlGRIN1HCr%2B8qfq%2FFnreH1sbfb5vyTf7ihOoBm2%2BM%2FcS59lMO3aiNIGOqUBQm9Zs4HySp1ucVGOV3WL1B6SC7YYXFAWGVVP0PUkvAFEdrfbYohboeHkxQuSpOzySP1YYMoQsmt3qH4xM%2FFClg6G4LJDJMS%2B2Q0cTc5KBUqFI1Tm7vIByGmI0xs%2BGUL1%2FT3Kujgfl%2F2kmaTPmIehYbl7hAJJKoy%2FXSNnMZreuXezj%2FyhnoOa71W0LHPulhv%2BRS%2FutovnKQMZp86mcBFLuDY4mU8L&X-Amz-Signature=25193bf9e9727374752382b04651533c1abc8a7b1a6d5031bde46928db72daa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
