---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEILKGNP%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T125224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDokM9sVs75IMGoe8PkGwckurkqbONs44zqYFw%2BUHudoQIgJUthPs7ap4W2RvKpcV6vxH2kEh%2F%2BwQgBn1T0jZFAGGIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCsfp%2FAPu0lt%2FbgPCrcA3f6l52YrBdBnQv%2FSfvJVeIKDL9zhcHMiBbT53UxLmHBDxTx5Uc3b7RqqjWz5M6xa7NByqZVLxtB01qb0EV6UzNPr4Fvu3%2BGiuUpfTPhYYQzP0NKnENgWbdJeSBn0u0VkR0tUL9RAWlJ95wcbnckZ9gmv%2Fd0ZfvVDdS4zHzC5CJ38F3ny8NF0LZ5jXww5D6yDK4YOTqgfR%2FZB%2BlWUEnu2Bn65gzMVuAbz4uiOecWAuM0%2FxVpGvMjLH%2BRJgUGQSD24gGUU3vBcSUz7M0OW6RX873qYLDNNRpst66uj4YAfryFNqSsuVFlaETKti6%2FavkKCT2T4ACOwUU3wtT2C1htaI9wIKEw2JPeStzXlQOA3Ad70o1WsdZLDisvINGXiOa98CiTgSGq4kHc7akF7d9WKDChvRDoMZgkPZu%2BqUEgb2mjqcRL9D7ybPHSRjbM%2Bnp46AkIRZiLIzMJd%2FekteT4waBkNGV9J5YR5bJBNk5PA%2By8W8erYw0%2FY%2F9xfp%2BocvcOn3t7LcEVBqU2wAyIEj69cjhtfEnmbVJh0GEbbkQGiidxFksTZ83Ej4GslCXAoC2Id1Ao2tO3CdCJKP8kR5OcJIcnk%2FWi9V5jbJDlDu7dthAUsOPmT%2FoOQn9yTfwfMPnfpdAGOqUBfBHMTpjk0mfAGlu2gUURXdSs8JY6Gf0znrwps6v%2BUJ8VIE1xz%2FJqhnRahx5hoZO1p7CBMKpZYGHB4ycXI6Ki%2BEN4JBbbEeVyQJoqIGj1i31C1s7edc705Xt2Ya1eom%2F%2BQkJ5gq7swC7fNfMbBrSUtZ5ZJYzmn77xXAchO0QzQ5ZrCfSA69Kalhw5uo3U8MLjqpdyiF1bwwyzBpQ2EidPgtVjl9cV&X-Amz-Signature=9919edf062c12003b12bf9650dd4bd1f9908b83af5e5b33bb6165d50d174b8b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
