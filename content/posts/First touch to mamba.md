---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBXPRKX5%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T145431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQD6s9psE3e3%2FFhwkKGkzuzog7ZBv1aHTrg13wCKA5dgoAIgHK6Eps6WGbNYRG3iHbnzAMA3IiII%2BFBVAJmpHwLB4nwq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDNCIuD5Ndj4Wktmc4SrcAwUGV1YgRGzYRfluZKNYvKsPVz2d3lbKa8YkABakpMHABgNx%2Fhw%2FZb0pXnhtvYJ3YLZKoFZcmgXoZdC8vWsM2M4j74WTO0UoPQv%2BQ%2Ff72T4uLouJQg%2BimsiHj7RTvF15C%2B0YFy3JyaGdR7yyBjUebPTOmQKHjARZhAkadnDppcCI%2Bn49%2FMGhMnrzalg%2Bhnzx2l%2FbmETDfks%2BZOX6KhHIrtu2FrmZQdZsnVTfsVSGYzyFbfEyfGA9HDvr6%2BtAcBAjK0xoLKErweR911b3Ysvzo530BBul8FTi5%2FDMpvMJ71E3z30lAsp4mpHYTx5czGThuKs8wVs6qNoHou4vL3wA4SC3RpifUG5xpY0HgyAaJkQM1kPtNYRRt761Kq1HmqpEauHGqOy9uTRoZnkVxgnF449XOHTog7%2BBGW2z0VcQnW6M36EVd8Tl9%2F4tJ2qQMESHOX1ihhOvVzTbqgcltyHEwULQPTvSNgkGJhHYV6bHktTWE0IRZTTr50YCPksmM9i2gvtSti9GDyT2IFzqTO%2FBmZ0ihu%2BVdrmY74jtGafFRU3dkziBNqFc20wFO%2BVAVz38Ys8ozTytPbwzq6a6aDdLyPAXW%2F9kMlqwreY12CZlOUlKqpCRp0Cp6RsfrcbyMJ%2F3xtAGOqUBxVnizpK%2FNYV%2B%2FEGr1SVF8DOFFjmghOCTvEjMZ4RrZvyT67rl2b%2BNpDn2mRyj31lta6AwUwo9s0wgHC9KhpU7aLw3Q4WRLP6ac1vsgvStBFJ1yYV9HJJ6vyA%2F0Os0J3Ve1HuH2j7XUsrUWPu2UNuxNyK1ZgqBKS04hAYhGArz%2Fby6EDH79fG1kXxnT84pO%2Fwxpgk5foD8O%2BObb27PPHlgBIvIEkdp&X-Amz-Signature=b5f19cc442c19809b1848895c3192833cb823001c5d3439916d41ccd66de28b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
