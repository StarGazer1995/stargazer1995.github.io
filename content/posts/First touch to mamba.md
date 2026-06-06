---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKBGA7ZT%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T205404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDanqPz5Vw045XVaM5zDcxPq6yn0vxt43DbgOZ3L%2BGrwAIgFr8HWCJ58aSbvGhrP%2F5JjJdA0RRIq8O%2B4LK9Z2keiMUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLaaB23mdZmJfqCtSSrcA77GbdWX8cxQqnO%2BE1tYHd9F4f0DjR5mWQeyhVjKjOY0jTVUYhLH2d433yys3g1bwziqXltArqlwjTr7bOYrt1KREM5%2Fu07AuN3TW5OKR5MHWB1uPiYRUZXLTgBk4F7aJLVSUVek2Uu0nazCsOCMt4veYaYmvLHlWkTAKAGFrbmVwayT0jiapokWBbHsTzIzZrDhRyj%2FJFZkb3oHKYnaQeMzNE7KAtEMFxCHikfB0fZk2Jg3mY5s0CBGJ0%2Fz2tgH%2Bio%2FO85ChZfDmkALpu3KVUKHOY8F5kAufY3gEr%2FbWGOcj0wkAPnfWNDojZ5zQfdqzl%2BsLPDG51%2BDX4CvtYg6BAoGKNPyaVV7q0EKH4ZeWKmWN%2Bms5ma7n2y1f2BsGzEDUeo15%2FaApffqxECH%2FdeARcuJ3jMZgU4o8QczUdRyq1o6H4tRwEunaWcNAmIzfh%2B3WvPjYxG5OiC5JIfYpAP6MjolRG8HwdTQ1qW%2FlA1LSPmYwxNGpEaAqObbtSJEt3oLO4PGJ5I4L9KTqr2ImSBQDCPySWltzTCDkdET4pizQkYjbsZ9PnO4%2FdUAqauKoplPqrk%2FtKBbiAje9sTqsNT5poVyW9oMROSmqoXADIiQJ6AkKM246hlcs9TgqgJ2MJj0kdEGOqUBJQI0vR8L%2B%2BHFjV1OawRbcEG8ytS6iEZwZetY3K42tt3nUM7t9ZRe1ghG2Bzxn0%2BHqteQrgrfFxHbFOFG4OPYkLzoYI3RgCwKHxingtgDSr1yuqYEih%2BSI2JorGQBScO8i4tXuNH%2F35T4vkL%2BK1mVpP%2BVLxfoa5kaV%2Ft78AWur4DFB6ngm%2BMp1%2FpfXq4Eqku9i7YWNqwkisIkkqmYTP6upYzDOIcP&X-Amz-Signature=ba2637c26b797f22b01f01446cd36349f0644489fd59bc46657f9c983f8d98c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
