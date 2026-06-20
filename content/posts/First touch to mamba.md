---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YLLNQKL%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T102527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCID0UJlKyG4X5EpBq%2FUDA%2FNKLEkX17gCrIRNy89z9tOILAiB5qVjuKd%2B%2BWDjNAWBZp8z6Oln6nD1UQmdvruijg2C6UCqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuSDcv2SqNmYaiPxFKtwD4MUXMuZSwM5kQxQPpC%2BzkLeFSbma92PM1c6kQUQmTL9dxUr0y47bjVnVUkj0XERiJYcKVu8DMcLd7WMxebnwhPRxJC1C3AQClMc2G8%2FoO8trx3WDpRvlC8dgbs9GToAXJ2BJwIKIkdLpslaqVpX6TOQb1GosTBNSGZmsmr094%2BbedyOxjg8S0Dv7BotodG33T1SrAPQj3S2j665x%2FZCMegKOQXDx8%2BcfnuoT5Wu6BtK8nO2V9TaoOGkabfaAwXbcsnJhVHyUoC%2FDbyCT%2Fn5xkQW1yehvIGaWWvg4Zj%2B%2Bk2q8bFtTVo%2B3SIyv8yGBB7AFrFkVFfE5SdIGBq0Pb0isKoPcsgY0F75vNERenDopTNH6odXr6khd4vH0u1zxuj%2F3q6KDe7Dw%2F4g8GkH2zaWp8KqV%2B6eMXXA%2FkTrpCJRTDUf1xtMlsJAbD5CnmOItfsV%2FKQMSXEofGCY%2Fx4nbMab5Si%2FK0PvYUT8HgFnwnm18lsZ2Q4HTVIOun4m0VqwF%2BXJb7ZoU7sm%2BZ%2FziQr0ifoIpkiVQ%2Blbj3ucJxQG66SM%2FS4HnZebayFqs6Qj0YTwMxhW20YanP6rOGgQ5gTPNv5ZVYcpIpVxh2ncIM%2F6SAx4YqHVWRS7OeBaj37Z8QacwusPZ0QY6pgGIOIE63%2Bgog%2BG4X5K7E7U1qfL4q%2Fp0x8mSqu0aetm7W4QS8R8TvANAXpT8QlOs2K1WFWqhYIksvezL3koDjJCzU7QMdSuRtCm4lg8fxIpOFSYVKDfb9rqSxkmIv0sJmEEkSkGoJWtrlgZXnm5R9jk6XwegTgmQua9ebF5a6MwXm7HqRvOmXvh9ZFmoMrAWCRoFFn28Z6h4d02eXA9OuYYh6pXxAMci&X-Amz-Signature=5880096a18f5b242feb66581f494237a04ec0a1b0063c687b8e0b436b42abded&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
