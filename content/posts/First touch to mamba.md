---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXF3QVY3%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T020246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIBkeKxU4T4xOHGBxZQigLQP8GTIzCDU3VtLxu6d%2Bm0EKAiAvhZreAmVrlg7tfSE5bsGZj37pm%2B6sxcEAxAyAZC%2Fi0yqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzx%2Bp7JrfFiIYANsRKtwDlQJ384PGSkMwZp4AbUFcTzR4k%2FKSARkpLjxgLC9lN6O2gmmlViO%2FNSi9O8cGbqVOAmTxRTtDlss%2Fa139HdEn0QEgQAWacyRg2eBZgWQsl4Aspintxdoo3CMlRBnOSEtTSxWFKoH5YGNdM%2BMeb2O3g6NmnOx%2BT6eo4i69WnZx0w%2Bvi7%2Ba1anhBvFNnXwnnltT0rwzPACGPLeHeyxX6ldnF968lYO%2F87xML4xDNYa6ZH9W0HsfSF5Hh9cu1XF4I8Sk%2BlHVyPq%2FzLqcl6%2B0t74WUGloOkrtljvZmEdKPYjHDT6gzgyGo%2FoU3VJ0kxh6nYZfkSO9rJvh85iii7AuD%2BXVyfq%2BncNS0l7x5k2IPv9cFxp%2FoDxPyuLtN9s9VpnilB5WwLbUZuMi74imfC8oiSrZ3gcyHkJ%2B%2B3hFqQK9X%2B6LK%2BK4VAbRCikRIeua9caAapCk8OhNww6mbjhafwUpaqbAOH0EXJUU0b0cTw1kM8lcetQAaQI7dWJT%2BY7ggsS%2FATZ%2B7b7tbQLrsF575252nBYFWj0%2F5OCyLaXou81gxZMX2HbXxaE7hUZQtQzBAfpq1mvG3%2BncxwZCZpP8ASbXSKDCRytKE3Yes%2BuWkUfLz4TPDw6yb740nsDOpszm2VgwmPKu0AY6pgHaLRhahJ%2FCl%2Fh%2B1d1JdRRkF2Z5XXvh9CwVqmSh7rXkhytSsDlEbIlAHL5vdrlm8BfTiM3SGR%2Fcvl0LMjVweykG%2B8F1VNYvUurJvDsNriifToHz%2FnbtT%2B4DUtYSChyCDaDvNqvbYA132GIetskdjUyPs0vRRQ17ets9i9jV5AsAl1kB9jAdaA5htYl4VYIOa7xHQzH795CID3hfCv2qMwUzpZ%2FioNTZ&X-Amz-Signature=c7e2368a22cf81f006158e6c2232599b793b480355f8e4a1fc42c943d63a8d04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
