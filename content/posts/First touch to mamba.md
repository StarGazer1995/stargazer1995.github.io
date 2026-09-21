---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWAUPPTW%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T211921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlL%2FjnE8xJyurN3nrliie6fdCUZxhwWPUuoFszzgX4zQIgIMeZkz%2Bcd64CqWa1blVF7aXOHgP0g9QcvMvd8FBekBAqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKWMc0NsQ8jX4jO1oCrcAyup%2B0IBbFO0sBXcicPh0EQ%2Bx51sUaq9Kg8Hv6JWsvRCDM%2BZ4UhBVK1AW7P89BMKw%2F4lrYS0tfRnSKaApl9MvwmG3TYeEFXKoCgsuAkQx9CZckBpNwE%2BwNl8q8gMBBhh3L0dWUZ%2F%2BjzN5IKDQmHeffX9Yk4GGsB6Wdct%2BgVxCLFp8KVHSFAJm9U%2FtgVZLbxzhRW%2Fku62aow61KXz7Dq9clkZXr0%2FYupIJN3aeB%2FualwFsW26f%2BRprZhV6qMiFMvcI5SLM9Su5Qh7liItPh2te5%2F9LnhRQn%2FHNWhgsFlEPQsm%2FUsccj2PExcz954UcMLm6aB1f8VQgfM6%2Bm0%2FeIt8NS1L7p%2B0zJzgFqNaYKPhjbRT%2F6NrhIG0%2B4P57TIAtqa51nvyMpvMTbAruviEwRpx3Pu3Vm54QiOe%2FOvDAj%2FZAN0u127rxMw%2FrjU5mu6vbKvYqXnpL25pD45MjV4PGoOQJT%2BIHiZ5wa2Z7XO%2FD32T%2BXwjZCBFP4uILwrFHLRdTdp3nzFNTXL4UkcgMho%2BnfL4QVomAx%2FH401Iy0dlk86nFJK6ZKpUscAnyKHNpEsnID%2BIWWEGrxuWhMriTmEpoF8%2BR9M%2F1uTls43SIcA%2BuQC8bX5zvB7bqhoKZyXnQcueMMO9xtUGOqUBAyW2V8E0qdF8ooanM0vCImCY7c2C%2F7OOjgXNmFYa5R7O3Z71S3QVEvuvPUY5cwmDRte8SW31g0pWwXx2roYRL6FBrZrfwYyqv7pbC3o8TN3qWfr8QDfnpaO8T64wolKPCjcFKE%2BTzFq%2BhzJmzcuFyHXibuW1ls8c1iXCyl2qVIpp%2FKrbtcS5sonLp5MMBYsmFvw%2Fs1tS3CrBbQaXZ7y5NbEJ5gLX&X-Amz-Signature=bb6e8a5d3f319ce59c035e976a5ee91d9a48a282e15d7cca6120b6713cb8ca88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
