---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZQ4LMUT%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T085814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHNUuY5fprcSgHGrAgadJ4XfpAHMz49vnoryLcTg0RSQIgXlOcN7JbjjUHWml%2Fftj2Fw2nd0UIVxGZh6Cm5gCI8b4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIm5n7vtFA%2FcxSHnAircA5auC3FuULBbZmQt4c0OMNDQiLhGBtTbzQM5fC4S1ySwsspsfkJUAYGxo1%2BaYmMBc6%2BgYFXGuwcDISBlZbh2qhwryUPfm3naHPv9qMxzJPGqdYy%2BmhnPLr9h6BhfL1oBw0GZB7cACL55Xw6P2Ohvj1uVxhTUvvH3ZTHQKgzlhVn14OHX8fanmSiCHTMbXkiAIv3wK%2BKpkQqkCc%2BCZaf6a5z68npxjMS77YhPeZVQVaUEN5vV33mjWsg%2Bvc8MVUebyjteT7x3CaFTsnMjwUd2fJQIloB1XMPvrUphtN5SnWaXu5hq1CMXo8ANWM8QnzInHsRaVnu4pmoczu9WiUmnxFBVfQWEvWGTWA1YYr%2BdWtK1hJ8JoD2vOrwRhL0eGt4Czkpp8WaAetpzHwyuXpVWwYdBBdKX8rRDSsww3%2FIq2G4Byl3eG8t1K0Wz4GfYMltd%2Fd1rGAFkbEdG7PDcK3c40EbJbBPYqlhvujRWFGmeWzSVWY0j2RNDxgCssUtmTVX3xu5JFKfumGB9%2BW4fDLfVgxkr4suVB91cIbWcB8dG8%2BVuWymL3KNkxcYJ3yo7XjGt6hcTBstvL%2F1V4OZtJH1MMx2Fj2z3VjhaO1eerH0uusrtL71oTwFgCspTqWDWMPLHwtIGOqUBPlpmhRO5F0bN3cHa2ckaFLwF4fYAKgyTFcDRCL2BEBHJtaqYRdaj5D89m9QVP6q7JgAmbLV19CDt%2FxbNIpQzYqRe4lXvkWATCLonm7BJ4Gai4KO5RkLxZ%2FSCkLYgqQh%2By%2Bglks1ch%2Bu17KguPIgz29ojpj2UlNiZyeI8f3Clud%2FmD%2FGm7fzcTJ16QyPyV7kqrY9xhmb5Q0fZqjzkPiHsfbS9cBk2&X-Amz-Signature=84de1e67232af2b7ea4bdaba7c43e84d5b44aef058cc2cb5a7ff5bdb9636489d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
