---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPKPSRH6%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T111545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6brPQ6AYewgbYBCTR2W03uD6aOD3XfXHR8k%2F%2FJAaIagIgfc9VtWFYDucem52l84qKjCbQoWnh2DKCulnxj36%2BwiQqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHZCETi9pLEEyUlrESrcA96FDHs276pa1idAvY05u1Q%2F%2FbxZE6cHB5Yx7LoFfrq2zh0UQyDMdq6hToXmiNdcaFV7%2F5BH%2BJVHSOn9GNK0yKlzTHWicBiJ8wLGLp1kZCavX7mcAlJ5K9%2BXPo8GlB3ZxPoqGqoY35fXY2UvDYRwHiWW2ZtIZITyqfuXCm3n%2Bdb1Qygm0CLjh2uQs1EVeY65Hs1FPSt4IETYS6Sh3zbTX%2BBTvb88CQp22zDAxb816Ox2xdKrAduFXAayk%2F%2BVdXCdlgL%2BrY1r0ZHqxW%2BJl%2BSbI53%2Fh5XD%2Fll8WWrLvZGYuC7uEHyunxNNRpaDeoEv7WDnm8HOBGnzgFjIEXhWMm0HwjAt88tOHVSlI7Nmuoz%2F%2BOAMX1v26DygCn5OdsImo02tyG79w5AOpR0FciBQOK5tla2uJ3b4HrWvkQNZCxkwLgKJ23c2P8EoZup7mPXvBOVyL%2FX5E7TOqX8gsxaMr8%2FcLr58rbo1ckVWWYrKp0pJTxsmMkVKM8fFYdX2PlRCfuHjntLzp%2FQOAwE9VxjVyHe8uBehcsJ30geyliLJ2jH3HAOrGl%2FMU0UJ%2FP3kukMb%2FnwLXEPzdBUs4T%2FSm36RjdTs4vW5X7GROH93WcrqIMoSDCTjOo2pLtTcpyUbEgENMNPgj9EGOqUBFxtKA0TDAD7Xu33L0PLCGsrjvtXIXN97YM%2B2hTnq79%2BS8MKXJqlzH60hVqpgghHVqh8L1CCe3DTbkFDImfXM%2FVb8v1I2jIu2Q32GFWuDJmwHLqpg1AuUGw5Y3xytpwYbP1Rv8vzXmCNC%2FkWwBZK%2B8AHrWI%2Bt4UDEV55GbZZ9Dy%2B3dhNysr7Zfe0tBlXk7GyM1VX1x7W1rVzrX3Ci80JaOv1TRT78&X-Amz-Signature=0124e46af1580897e4a20a4af3160892e3fdb83bccec41cd9ca352dc5019ec37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
