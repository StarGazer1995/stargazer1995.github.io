---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JITM3JD%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T020951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIAmFAeRnD7oX5itcoyCBDo%2FoEqjH5GLvWvWM4AJBbNtkAiEA0EjiFzRxCpWNq1lkK3z8oHpbFQbTXdOVRFkBB8buwRsqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOsX1DCxKEU5KdvOCrcAyJ3BfUpbKKEjFAx6GlEsfnKIFjP%2BLWPNzccmFlfa2tknJvCIfS8whhDT%2BDv3%2F6IfXja48zFgDNdHArTAd0%2F%2FHzvc3oL03mDx2DZyLUb47PO0ysY%2B6Hnyza7%2F5pJCj%2FyZwWesVvJEsDo4ZOu4EkorPj11ba563%2FJzJ9pfCNxI3%2BSZ6333Q5PcX2PM3decHnz%2FoMkYVNkbe6AAQpQHLIRLP4gM3qIuG5v8fjwKNGoF3zF89lascqfduAF8ZixV%2BYUiLNz10rPe8VQLgvI9ycKlmhhWZyB1LVCDhVsK1VZzPYO4oENBcmFFh3IUvNWT3UAXVAH%2FSCTn1imL%2BB0uBX3NwC%2BmJNhJYArMmvXtwqpu%2FMA5Xu0yUbtgNSFjNkWZNjGLCaNL%2BQdxqnl1tLJaYHJCYSmoVMlLexXx4otB6S3NZa1lpshyqoeDK2092yAiAT1nrJkHmJ7KIaiSGhKUUSa3o0QptyoQ1180m4BRAUub13IzkISawIaIkxkDs%2B7o8Ei8YDjGKbaQ63Oc3mwbSmOY5wzWxJlE5%2F9e7bWQIMVcMd4HDu7O6HRyJOgbeE%2FxqyujjYQq%2BZUuGSMl0cvkj7TvWTQkt1j4NYiXgFoIhco0DNUm%2Fcxu5YAUnEqZ8NNMPCE7tAGOqUBnWsDSPri6jagQ5IRqz4oOTRsFZKMu%2FjoFzyIE8TaUXxJkLPUqgwkvmoPpi8AecryzoKaNx8lijZF1a73Fpz3juF4hiSmfpka7kQcKFttc%2BO0NpNPVKjg24gAvkwLRgbTNGEzX0BtNuJWJe4Xkoxup0IrzXKk5i6NcxneWU9I5opjpISeyLiswROudq%2BNkNYzwNZ%2Fhy6T8OPwMLWqo1mwLwrgMjLG&X-Amz-Signature=66d009ef117fc3362cb73ab6c39e5e36bd6b55e6145e58981e94b2e4399cd66a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
