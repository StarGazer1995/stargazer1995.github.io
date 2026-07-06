---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644K67LUN%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T145340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBw4rdu4WThHsBiJQCnryM8d1jOIQFkS1%2BJo9fQMxGNHAiAUYeDusoa42yc0CGRZSuBW1v%2FKN7Eio3rEAu2gpW4P2yr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMoa7XgNP43G8F1%2BReKtwDJxR%2FHCmoujQlxfc%2FyKuAIFrm%2FfjCMiH2i7YFDoXOXP6itFn7G%2BZi1OkgqesMlotGPP4qzSVDO2yJ6Vt5ZB3ZVBAA1G%2FJNkQV2bn2a7iLBaDWAzmph2%2BpyuLXFcGefDa1GXZrdnk8jY7SOjrt6rzwm%2BuSVqz0NJZgNiNd7d2dU2PTb4c5pV%2BBBOcNt35d%2Fk735H7DmhxRoXUyFVjiMUFdyCY4meDwUGAbhQMgCaj0vtE6o4PRYBHtpFlNp2vMufXytLBKrooj4nuEi5TY9aw7BapYp1jUwo334eTnKovSia%2B00XEtEbruyoWN1VQSXsavqSxFRLf8Bz0ejVzEGevzYIo%2Fwdfh9R9j05XwZ4CKBTMgCI0PqCwW59ZfbXUicuG92Kp8mVjEBTvM4IBMBYvxW5xZk9R7DSLHVqsfRnw%2BnUFavctVSGRCqsXLD9pqWaSY0Y6EbhN42L75DaILaqYwIY5iSYgSRAOgaU5agXLZ0%2BCptWpo0Jz36arzqx3WK8z%2BCHCNz7jMkzclZ0c9yvF%2ByjZiEThXTixA8uOp3ghxAnPpHRa36Z07o4ZgoPgT5FU0ljLPV17jh7KYFrESMa%2BeOZhhPEkWz%2FTLT0ukbx5hRUG5ksF1cIVcV8gmFvAwwveu0gY6pgGwkDl1c%2BFGds6JBQC6EyYenR2Raiyv4gIlokarV2B184mXKBH5TXS1HNyIu8tktA%2FBnKH8Xbj4BzTGHGKQT2gp%2BZbd2tVyFP4k8JoEl74f2xKm7HugfM9mg68pDjjVP8a4pBYm3W5pE2V7LfCCziEUb7bwiNTixjLUIx4QJokch3OblR%2BMz08xbqUTL5G%2Bvxmge2I47mwSR0VSpjcrsSeLJc9Nnbid&X-Amz-Signature=6188489e94972544b8b48c21a8b93f7aaa918906777bf06374fcdf13c8724904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
