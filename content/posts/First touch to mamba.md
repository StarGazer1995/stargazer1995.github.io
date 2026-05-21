---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663B4XL7RJ%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T175036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIHE3JisJ4q6kE7GRLzlwqtXQ9qje9YaHasghhbZSUpmgAiEAiR5QCb6On1bwgllP7zgJFntx4TslAsR9S24cH%2FjeO%2BQq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDI893wJqZHF5B1PpISrcA8OwULjpIhn2jQwXqacDVFUzSY81aNKCZRQu2o3L9HYOHe0AWem6XHaEryBuVOez0JzE5P9Lq7xecfaBvvAskftnYC%2BRuofWxo4XFdt7QHculaKxKeDG9oCfy51Qn2li09yn7JoBBmqhvnO75rMXbi%2F21GiGJNABNFFIaTR21yo6UwpFwY3Gy%2FTNlgFar7%2FGP1lZsrJ4zx1LJH5ZlmUrNZDNzt5MCxJ1pvGEjGiIkTPeYoVWreioh3Q3F0Xju2UgIlxaE2SOMTRPKrpVR2Ktrs0hydohdXXi6MH5IEqx9EQOptgkyidNiXZUOXP0XwVxJJUbpwjYKnxCMcRjUILNXN3Y5OO1ZlrpZvNQgu3R9fTT5RdP2HWz1TEkjv%2Bu5MFSpiDiZfeQf%2FXEZ1pAujiWUtc7wffgH%2FiYjPEH1T1SbcaFmy8ekSO%2F3CjkZQ34FHohvxj0KqanS6oCIVgB2iew%2Bc%2BOh8ICerPBvp3gy14bYAMdaMvOikuLu8Y%2BPbhIwi%2BE%2BBW0u%2F0T9cept85grDRsYmdUTYJYZRALBdZmqJbSWmcbvYXkK%2F5cCC%2FobemjB3q6G%2FhDUpQnel9XXJBoTS9rXqmy4AxC900Q5aSih4xP4%2BDD7wqIb%2FdgdVGdbPphMOyBvdAGOqUBshoTdRmH40DYv%2BInhShQmxcnDGscE9yy1S1ygxMrPyHDx8tpGaahjzyvPqsizSTkJ9Qmf576V1%2B7jnNtYSXldfSCKQ%2Ffhpz%2F3rBUjQwsajofghYxyQNheO6T8yhEs8hKSJ0NtswGjZ6Z8Vs%2B4zHFEsvWAGzqySZhUYZuuLPCnjCnFSeQW1HQESKnFxfi5x%2BTm%2B4ApjNICyAm3sp3dzG0gfuXRaxA&X-Amz-Signature=081a61f4bee88053e9793ee09c92e8e6a19213ec0f6b46c27b59dda44800238c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
