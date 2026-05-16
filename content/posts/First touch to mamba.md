---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BEEVQ2R%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T105452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGlmI1n8iEqhf2t5mYDKSzXmgw%2BActfWQZTLUn1OEzYEAiEAvaUh39FNfM02swVxuCHnEsb%2FZJ6qOFbhWe6%2Fh56HV4sqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCFgz8zBvWfYW4nD6ircA0rXzKvGgFLUYA64%2Bob%2FPKIbE4aqyUyhg7sHO9lBtdPD8z%2F1ZGuFySq0rQs1QlC2nPR7%2BK1j%2B2ST37sY9JNor1VCfzyeayiW4ZNhm1M8A1%2FZT3LYOqyVbSajH99jzUltzUYMNX7lQtdbz57bKSO8zeRTf292ZhciMnhpVn6mhwwL0md5YQ%2FLJIsZZSaG6cnJx3f3N0X1fZVRkIpJWmBegJdngxHPGGeYh3%2BnXLHNKt9C%2FwvmfCkYLz8HaOrbVpHeKwVT5Yhu547xtsbCkqFWpVYNyEZ0EogkUzI0rpN0hKiojaLmYlSGavnD0F2zGcjrvhLr0w%2FeTvvTKTpt5vwPjCrlKD5n5RciCRYkqGbusu%2B33Jskrohn6zYitAMnBUVZjGFkJuxreK3Ls5oDHZhF4iF0z9VGKAULK1%2FJ7bLnirD09pw%2FpZ0C1brXrhDOllEpJolR9WkTr6jw3ZwhCq4FZ4aa6E63N9jXsJy7HOK42KWVkp6LnPy1JPfVMEaVxR5Qo6SAQKTuIyrmm9zpgJcICDrH%2F3o4EPIfDselDkloxg1mRQudIvPYpUxy2Adbb5QTXP25f6%2B%2FsKZt%2BRKtsUQiEta8z2JaIt1ol6lE2ZYBKqNbE8mTGOFytqAd89ijMNzroNAGOqUBLoWfP4icOWpfhOrkd%2BsMruTJEvkJhUfJOavALN%2BkSiBO7kQ%2BPhod%2F95MTTX4V0sYzkVQBd6WTZnVMw5zHQuMzFhyd3RsHW2wVRM%2B%2ByDGMbr2gGW51ZjqnNIZzzGhg9RhI54vTr7DZTIxrKKALd%2FzbxBSGBaO1qPrtIPlpZHzeqtJmJ5WANhAZT7Z9X7q6mW%2B9KArE4%2BMKxxDZvquBWnkh%2BYSnPPK&X-Amz-Signature=ac629909ce6e73806f4228407680eee624461f2a25f3d6c129f8227adb1ca8ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
