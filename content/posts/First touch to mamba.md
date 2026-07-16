---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HUDRZXW%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T131456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIQDkMv7fbgF0IpMXtBIs2B29tNptjww2%2BqEOtJoImKAfLAIgFTGH7oSNn9JP241BtxOl0TFV1MtsS93qBfLZJeR8dVAq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDJrfN0o1jDDi6jiyoyrcA6lrJs%2FRsusqJ2hNmsBcm5Mmz39TVkvZ7TJ97u2%2FzyZhlZqNGoZG2MUm8jHd%2FdYnOBSMc3QQpktmYe5fD8vrYYBlL5Wivj%2B%2FsCaxoBFhNWsi9sCPz0CzxRMvHB3GsJ7VYb4Byzr8avwSf4LINRttFC5Vph3dC0J2iy8mAFze%2BjkU4mbCNbRN1RJCXGd3drgcLur8UB2EuU9Yw%2Bt%2F9l5xWFDLnglnrcTStxzhXJy7jRQyfncrFiP%2Fy1lobaaoyJ2ymVmuyCRkFctB1%2B4CaDP0chUMLpEsUzXkq2WunevhLo00PIx2JkKzSCXABz7YzthRmho1G9MfZ9BLbus57swo8a5%2BqMwu3pS%2F1XfqMN0T%2BScuqF6wCr7ANNyuLZgepqcggpH2rlZjRv5A4QqNCw%2FFUGHFm%2FVw1nQc9IEB33bh3ncT%2BDdN5DlYC4qvovM9IBImbPOgJvIcfdWgt01v4xr3B0Z0gL7uxckrOoz60LRlmmCuwPmspMqH45plxwTtLC7mpRQGgjprsEtq8O1Hgd4zq6utZd7Avw33drnOEPOeI5XHz6eUGDc8uRk1hIYamqoi4uxAfGQZkgzbPXaaUrncCjuRIVO3srAhPDLBK3MIjv5CoHPasBm2RgUlCpt%2FML%2BN49IGOqUBRvorDiB1F0Hq9Yc2wAliCupJU2r4Je77r%2F6qLMwM112la%2FBkJochIxjGE%2BftV1FdmLcRtBS9cj6GAvgEL7PW0m7wGcGlD9PFxB6JQej3rSIxHmCTtYdgy2PEghVKd49ogrymheNDKDoYJxEtJxm3v5DY3dWMLtoZVA6tkGtN39jhwSq5WjJCF%2FrkBeq5W4zDCUXb192w6f26LgCxpOpbPSkK%2BC74&X-Amz-Signature=8fea91008f065926c55aae28456c6da4370859be615be4e3327f5ed76c6ee75f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
