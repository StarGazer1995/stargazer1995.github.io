---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUPZ456Q%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T214855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG0%2BFp2pxhlqH0zOOhcn7GJF3u%2FMBHsCuMuBoHEGDVUzAiEAoV7yby7dgyLJi9PrIa4aHFmIuDI92MZcLuoRmsgIMpMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqVs3Ef%2BsZPH79vvSrcA%2F%2FLbQ1WLAR0Nk5w2SO461nfZ%2BV%2FfmWxjO0Difn66mycFE%2B4gSMH6hvGw7jZbOyoy9VpG9B9yGfpk%2BOIolAGNJpvRv%2FKSI6Oh4bOZKNefwEdISpjR7IWkp%2Btb4%2B21RhsMVSQE0vlAY7s%2FeBkNhb%2Bjz9alSGLeu96nnKb5Cho2dfUTSIT8suwgUBh8PJ71LQpWvXRlKwURlri3fLmTj%2FEidVeT%2FZiKBLN7kid4vV%2FiMvPCHyV2jaTm5xk1eJeJ3fRD21N2%2BvP%2ByW29AdFxyaL7P9j87rjzXi625zq4lVEm8nJj3glSa5MV%2BRouBUOp5rxzbZhgAHMmncU8MUPKCd1KviLFdn%2BpppQsdk0QSFcSiEfJzBwDE30%2Fwo6jGuiEALDvLIeFjJ7BaAXOIEgurE8XDTi3xmCHsQBovHkTsx3cHjQ30c%2FTIF6TKv5%2BulNJ7gL%2BADZQkcNBy5JTjXzypjgiWvccEaem8bT91IDtHVlouS80Hb0IcY1QpzXkplWHzixEvB3Q7mOro6bhIWuVZ57ojNxCqQMwCGcuMOLSAm1EmYw1VCrHjmI%2FTH6COD7JbllaUQTsE3NZCTgY%2FcrYf0GaLVTsLo4exjZ01%2F8L40ZIwxKClY1G1KCVvIBxQipMNX5m9EGOqUBW4Z71UjNDEBfzZdUU3UzJ89MSdmmkDv05L57sS9ftjpoWPxywrsxsFvwDtWiKI2KSYKbAxy7AMFD676rTcse5E3NSTNcb4D%2F1VnnXKwr8zpkP9mZeJv7WaSD2It73pnCugtjlSD%2FYoemLmarQ%2FqWszBr9Rd3P6HKIKPoPoYPydct1vN4N8mXgDMi7btwNSJX%2BbGvM96f5V4W5OTdH%2Bt4NTSZ5Gw%2F&X-Amz-Signature=f98bbade6383048f7312c1143167b5e8a7af9017af5426c56946f121c967bd47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
