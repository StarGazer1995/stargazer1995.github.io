---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KQW5NDD%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T062336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHw06bP8QCYCuU%2BuJGSuC%2BPIyM9Ey%2B8q97UACYa%2Fmt2dAiBhEaAjwdmS2hoy1mZbwNijQJmVV9cc3e3uDnA5Sp5FQiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkNWo3mOql3SVHuK%2BKtwDG3vVnWTA0AmlQPO7ZOFxYeNW2tcKrbcvfwTkOQeIFhGm1zMYzvgdvn%2BmOduOZ5NblDzZR2zZsvyDW3MvdxVTT3ly2%2F5sj2f7mZ4np4vPuhEh81iNKjwOpAwRITL7uMwJ4GymhfMuCQ0fNW%2BgNWiHDh93m1n7E1lBcAi22ZFXD5zCPqrqnIT2ynja0fEg75vdOHMChsvoIhblNmA%2FVtQvpUQDqa8K4KeCLyzA%2Bdr535utLbMl%2Ba2tV4wi5fInT9lc%2FiH83XE6dpiiWASfGNfd7Ogce87c4qi3gU%2B788m9Xs67%2F9nT%2BG61AGSD4Xyf5w8yej30m8k4qqdkfxg%2BStAokOxKSswAxg0IAv2ozBOw6fmBCiwPzrqbRWoTMipMk2F1bpX3QCUYjCB%2BEAjMPoOJZyqGN9NvNNSMGyyoZ%2B%2FVebgLbVKhrahzkcy8IY9mLDMuQ2z9ZtbrHA%2BTtSkx1cpkZ%2BcsXbMZNTyoHW0%2F1bZRdICo4k1i3SZ0BkXhgxaQ8AgKU22%2BzyzNwRHh1XF2XgNFcJrIRMbzNd2jrfbKVBLSvlMAcB%2Bho7%2FtEywSTrCNj6fSytjNoFUmWH6QEu6rdBdm1eDCuYGguR5bkTxJ1rp0%2FwfW6qyXUqZEQXFkUJYw1qqa1AY6pgH8Kx5bi%2FJE%2B7ruOLJceSgH%2BaPNPIYLC17PwaGpNPV5gaK9be8vDgwPZp6U8M3wdHpCwear13ukTdchGT3klxI7PbE2lniHVvshMVC7RjhZ6xapYcpFyy%2BgNXCdzFjzXN2SNQc%2Fx0YiiH46XIBDqJoBjOX0GQiUAwoCjfWfmkYN7OArX%2FeZQv7N5I4hRdq42Y0uZzi7%2BrILXmTqA%2BL1KqOrYTXuZc53&X-Amz-Signature=1d94cb1c1f2117da2cb27df35fa02a7023b92ff2c6724e2ca2d490e0eea1d0e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
