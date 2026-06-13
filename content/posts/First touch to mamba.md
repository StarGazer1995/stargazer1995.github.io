---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WAZI3EI%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T170820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQC8H1pprD%2FGJylI7xXVFy09rkYYF%2FFs2aY3v5DgIl5PJAIhAJwkqE%2BuDhB6%2F0lCh8ELYY9TU3Um3Q30V5DiHWyqY8W5Kv8DCDIQABoMNjM3NDIzMTgzODA1Igwp5cNRhQYkWMhzZJsq3APnuLLOITGsDoTXKGpecT7o5PgkuY0UGDo3Zpt234CPM8EUrBk6Y0P5AFz72RYs7e4GJJDldQu5b3HBwsWQWc7c%2FqNRc8Z%2FgO58X%2Bws23XRgrXcxOLGzBAo0mLd4JIVWreSjwgJD%2F8jZBIZB9T4Df6vFmXEV0MYQuWhgPLnKTmFB4O%2BybeNI0ISwNoBmGGzVs66%2BN12jD6MthzIv8SGE%2Ba4pe9alUL8QoRoIvCjMTZ9M5OCJRAPAmBcN%2ButDD%2Br%2BKe0EvIsxO1t6thSJBWIhBEIROxktKq1J9d%2FXAxwheluCoCe0ypEhR196Zmqf5FBTTWL7i0r%2Bt3UIrYWnDGYZ2WSqNp%2Bxt%2BkGVHm5mgtzA4R7d%2BgA0qGptCN2dQ5QnTCGZ8W3nKgrdZHwbVSSb5bR8X%2FTiOGoiR6D3eXnCspd3J9x%2FjV4r2OxmvJuaEfW8iqiV2ruoKuQhmJm5eWWKuZOijiZPf9LCUiAtpf5UGfy%2B1VI1iTcVorJihkdG429sHW%2BHUslmCySZiz5ACUb0CCr8Xf2MabSOm5mAKlIo0c7S0Owf1UDOOHgvBghV49JN4ntldrfIjVkPmYrwelLzsMJVyRnV1GCdf2JkrV2apzDs6p7ZXC8btXETNEEAry1zDll7bRBjqkAdppih6CB7nPH3j%2Fk%2BfI4RPMzopDHhmDySfowblfO8c7ppWUIh4xdtUgV1UbUaBXHU%2BCPLAOdRSqWTqLF9BDyLwEcJK1QdwPJetB3fVmTyfB%2FhSsQBE00HepgtSpf3H9oR08x%2FiFjgIB6%2BEwxASAZp7EjlBYTXtvQjRxR%2BW%2BdDIv5hS4MUeeUHNMdC%2BEulZ2syiiTOZhpP5Ikk0q6XkQl8xJ%2FJzF&X-Amz-Signature=24a2caac5d5e1b2073cdadc86e5516598d45b4b5f7c762445e9264201fb42f0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
