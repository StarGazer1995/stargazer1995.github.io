---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LGEXLVW%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T220021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICR6IjDeJM1nJ%2BgJrJD5fkR9zzBBtH7H3kKLpZehlBIbAiAp%2BKtQ%2BrrABdIvDKvD8hvPFJ2ywhUmkluQguIuNMZe8Sr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMZoPGveEDPxHScH0GKtwD4o4JVYiASSjqXScAY6uScjV41JL0Rtsaj%2FKTy4ll6ZDz1ziclFz0gZnJqnNqq2zHIjSxO7T0CcKKFAmt8kt4BOp%2Fn%2FmMUHdkEIpONQQfzJFNRJVSZqna2Sne%2FPODOqCAIQInFg%2BGRKUM7G6qNrGy2y%2FLzwlTR%2F8oRarqePbYgmjap4qVFB5yEkIDN%2Bijn0TfiRWeW0HgXESNFGpMHKKxrc52zRWd0GITDqlNKk%2Fk4fu0xEgzAYjRxxA9dZTOJ%2FKwpCX761yygP0POpibQwuxn6gJp2Z%2FuRKhdp0JczeJZ7YC0siiZH704FdkwToP%2Fm4JEdToMJ7%2Fg4mDgyEAfWzVzhQZwECZrsDt73CY0YRroderRcAFvP76sANu%2B17QNbmbp6mJCSqpByViKlYvZ1Quu7HVSNaCeUz96xgoAVpygSwPztWdSnOzBMIfnKBVlwu6sECsYJNg3LL6FC3Eozf258DYyCD8L3iCSxbNjrbswnaPWT1XN4my7nqD3y%2FXLCigQ%2BfdQe00NwOG%2F5nzYUx%2FHKzHv2WKCMGUTGiyZwI18C2rSnFifkUzg4cEzXrZ8WLInpptd9CS2scHXN9jkM6KqivlgN1Q0lnEAOz3CGktwCeje2JptaAWqoCgizUw0KvB1QY6pgEICvsjFDmrsFyIeTFPwO4eVlsMt3MfAHuKV%2FiifKZl0T7uyQnUEIL8h2AuweDklQK%2FGWmZDZLJZT8Z%2Bk9sUwNVjfisffl0%2BwiLcpEW4KGLscbrZWVPA6MXpnYEev0rap4cwHaXPdAFbqWIA%2Fe8gRp7%2FCtU2z6rzC01MAW3AukFkoGePnk9QTl1BCy3jDy2d7Rh1LilrsPJkjXJJIch%2BmV3qfp7GCLM&X-Amz-Signature=3f7b0a1433ebccb770f7576fdc924565230c4d10564b47bcb586d5f2a02518bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
