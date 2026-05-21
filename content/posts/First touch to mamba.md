---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QTYJXIE%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T020130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDfX%2BOmb5dB7q4ajAwTUYGooIduqUMQU66ZGMx%2BviyV9wIhAJNTo5YYmgDXO6z%2F9obotHVrBHsvvNbDmoXPYkoQ%2BGLLKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKhLwyJjGjpBqvdXUq3APd9jFGMyFknw8gHKNfrqXrwQeHIb8dAbGnnduCPmlHmanWVqIN%2BO6RQ7Ac%2BZhAzR9yJEpK%2BIi1NWefF9Bsk%2FrG0K%2Bocf6ehiizjjMNchymYZaGy4miQbW%2ByREqs58MjlZOKJMkD1LcWD6vwmolNfUFjXNTwWpCuXBgan3UKoKdKG9JawosSBLM0lghDff9z2GBTrS5nNUnKMWGyckrVRyLtcWhN30GWxTJZKz4ipOUeGNvg7W1ZWkID6%2BrVioS%2FmKOwjzuwyxz45HhMeND7tLqVOW8fXVxTSf6IFhBXeU1nLucD9lsQ3u5UkYAWQi%2Bw8rSy1dUYhPfu3PX%2BQ3yfBYJyRwqoEV9YVrUhRdmgGLoMqAYaovtfV0%2FCdcVz2RKhUHHIe8GhGxokhH2Xu3bzYZe%2BaKEOkjx4U7YquxlqoKx4UibGpnk4fSCUaeb6E%2F57mZ7EpOOE6Rsm1cPjnbWyo%2BGaLjtX%2FLxywL59O%2FLlpTkK6r7qnXhG%2FPhfrKhn1ClWk%2Bh65XXyiFzY%2FyYnSP9GknmfOFRF553zbdD6xHbWIbn9HKoTDIwF599Wwy4gk591KeX16%2BW93yQ47uIYfy2wPWTobNyPS%2By3mPRqFOEWXcX7vJ%2B%2FOTeBmQGLe5pQDCEvbnQBjqkAeB5d%2B9B8vXn%2FNq8Kt0skOmlJhAJJ0mcwemje0IzlBMpOGfm92AlMnbb4bvm4nJgXevorFAbMd0DlyIuYviBiqsahKSQ6ckB8NxEyLBzm0VlhtrLMBMfbtg9aSkrvqiuGnrAmiVUNHj2xGviiF2Rj%2FDSxN4dSq7y%2Fds9yNBiVc6NiNubFSHQ%2Bpdsj5NzsZwFOR%2B8%2F5UkzovkgrOhDFcDe3PjQuwN&X-Amz-Signature=ec338cf247b1ad0213c132dd9ea0ab4c922b1127cd09e5334b3dccbee80ac05c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
