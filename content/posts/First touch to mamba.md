---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2RGFQHQ%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T105004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCA6lfjuhyYq27DYzbgJEQ5GAl1g0iljWKXp%2Fym%2Bb34%2BQIhAJeEXOJBtDX%2BygEJA0WvqzONH6tSud5Gq6vM1UnwemNSKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2Bli%2FRLAolXxoQ6Fgq3AOZ2O5FVML9VgquxiM3qTK0SKw%2BHI%2FR4pGqCYld2tdF2yn7PyRKa%2F%2Bk3MUo%2FkxRq2dYXH6yNGe1burCPfa24tc6J%2Flr3y%2FD3ZfLkFmoAJZwLq2TGdhtCr6aCG5CpLqFX3znEZldHTkEED5NyCA31oB1wsRXyO4vTiSRr1XcmA4IIbQjanQ14YMif5l9k0j6BScFB1BXfCuOjWFLvanirtfrGLOV7RY0LIWN%2Bq4oKSVX5%2BVdAn0pOZSsMDODbOXQVD4dse8C9bj34yGNVgtzs68FuVJPgPdVZAbPccVxwttJzSok4idrlLyXArilqCj82OLRz8Gm7zKlPPidi0XeWtCWPD4bWNaWKM8iKhGD1ELjg2xZZyCIyJlx1p%2FZ0Nnwxr%2B%2ByrNLeZmmWY%2FU2U6vrjsIbvD5lWLOOWTHMkcftWQPvYeokGW%2FwM1SU%2FKP6CYGQkkzNhGlOOMuXqpNr9gP29Pjw77jACZoJmLH2mr6wrGApxn0KBCXIH9VlC7k0oGGMux5d%2FROlJEKIsuiAACkii3RTNKcdgYqx%2BbB4Tpb%2F%2BYLyWlIb9Y2HRVXnzXFSg7BM%2BbfDr12NTs6vGSFERTjk6ZyPp1H7RdmjjMyH0y3tErkmQKg0ZM9GbpkLfYV9DCzm%2FHTBjqkAVLYOrQThYzTRZqcM3QNao2V6Q4CWxi5%2FD97yXCX%2BdoyPnOn3KBb3DVl2HYrof7rku1BBY%2FNOO3%2BQUbVFUNGPocw6zl0AdztBDUjTlNR4kMdmb9USw8oGFAS65U46R%2BfnBFxZ9wHEOUqEQOYf6yg5uRmZjPOaA6v6NO0964mksiQ08XDeoiWrqguTrCqoSg2F%2FvABdELiYgyVHPFDqUeHwfqoDQZ&X-Amz-Signature=def15586366a490c92bf6691eccfee6f2e458f3805896d59115ece5a2b73a72e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
