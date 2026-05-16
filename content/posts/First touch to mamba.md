---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFSSRX6Q%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T051910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCitYWwSWH2Lcyv9PZsV63bjYBqkv%2BA13BWEG1kfT6R%2BAIgI7OIP47CHpecRCuGxv%2FXQl82YgHdb1gNkajHoPLoWEwqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIjPzOF%2Fz8%2Flbi8S6ircA676Gqalxo28LYtZ0wN%2BNDHrOlMBLJwn6mU%2BO%2BZGK9dWeUVtwHYEFBvBskIaCc5npM1TmGdIcGKx8Q%2FsQU7MXqaILOGD3oOlRhkVNIfxk6X55J0JODBilvisvnFweoVIXW3ZxI7XwHGIQuuxQTQXggRP2Ys13DxxLCSIgUdShn8Cka%2FbgCxBcv%2BonE5SsZBrQeMOH67ccCdIXpkGOjKk08c7KaMiF8iwL71JO3nI4BIhy7cQqnTbRLKDcC%2Bee92fenZEbhOvk%2FLf%2FaT0g7AEL%2B64UbCOWfs6NkO%2BbhnKANytERvkc3I6gx6LiV3u6wpx9nXfnVmKuP81JgdubMuA6dc1%2FKNz0hoVvviWsgo6t0lUrTzG4VN7ps2SD7sahz%2FFFfMoveX4kTSECEkzZBNJDDON3WlndlIRHtmXeA4L90loD2sDPDR9BSBGPZWJBURpJ0ebfQqCNxk0ZwXn0AptfPiVAXxwgoy41yiLNtnRqpwlYno8hURfsb0R2XN9Zy6E2Xpv8HTy%2FO4CaVva%2FFNER4ldWZt3VgNVIVT2LUKQmbZ06NCQdMzJi3Mu5DuQnj4Jjq%2BEBr8TShckCtva1gUzqeF%2BPQ%2FMAaEJ5hEatIrf2aDQSMU7sEMn0VhwopFLMLTkn9AGOqUB0Q1PQUEHoDilxgRg4mcxHan2A6vB%2B%2BKThVbuaNKD5d%2FG%2B3tL0HLVkLZ2BVkWQjbJ73e1YB3m0vohHBU5JAtiSu92TMYjjRzTBxQXyTYinzi0JIE4%2BlqkrjCQa8rWFl5f7XFUG1%2F1ZR4okfZEnH%2FaTutkm67tvmeAVvVwsvfe8BPY9xTWpCtmgnL7zjKNKKzog2fRXLm%2F987xFrA5vTleVXWF4YvS&X-Amz-Signature=252ed7aac505d560d241d5f168def8cebae820c6d5b5e1db74dfbead19a73025&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
