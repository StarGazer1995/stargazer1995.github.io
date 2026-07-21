---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIW73PD7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T170603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA195NaHlyznZeIrit3uXhqISZtE81pGnti4RtDhKNBPAiB4E0Ffe4vO83BhiSAt4%2FIFiDYoBUSJNoyttGykHxFdtyqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtmtUEq3RrFIGqE6cKtwDDJMSxxjWWDcvexTUZcSyOnI5Wtyacaa5WLvzItZAx4XZwNmDk%2BKDNugwqKFkcfZZxeqBu%2BxH%2F8Ebdk4ENRtvTyFwx6%2BaZpx%2BLgGTZ5zf8SNrOE835DPIm9kMJDfiKi9TM3mGanGvIOq%2FYh%2BU4ZMkMytI5oE%2Br6l9CQaeok8wiWnzGZyqD8zOW710hysCD8oXF0wo%2BN0Sa8uyfRN4Rvq8qqOzKdZZqDoWYgXas%2FUN8zjaJ%2BoQHaCunHuFCcWJw9cEIgY96Ylr0S2JZrndAPcWS3v%2FGWJRu%2BrrhXuBxERMfcexuerKgW8kQSQc1MQ8HscXL0tTn7dBmHFsvfR4GEWypgRtBgAcdDuE8MbGTHkBYg3E5dJTLdgWfC8%2BOdaFCJR5eIaYRASuLhJXeGcuf%2BGtpD6OG5HbT3MhHB2KwLRgX1Ktg9eVVThRoo9L1sBetET3%2F9GkH9550D3bUdw7ge1y9Wm7pLBeQW2qOZ9nSYfgnKtAEhhHYg29RO%2FkmiXuR9c5X7xqnKheqALG5iK0qgJacbEM%2FrWYyj8K7Gh82Gx7pP5PWtlyuTyj6tg9lhFWpX3YQzo0LrUUrbIDcNU8UgWRbZ3kQHk3stkTX%2FQSOmW01etHifylXzl4k3nzwPEwgK3%2B0gY6pgFAQuTreecfHtMKna80KPasvpvv5rDoDs%2Fi6zIAYslgcfHgTlVn1Y4rVzzY8%2BqF1cb%2F1NFnGRX%2BM39NNOOpe00wiyybhuLkdCQgo%2BaSkswr4Ilsa0Br5Vl6XPlxw9u0%2Be%2Btvj764Bd%2FB2D8a4xQ4zlbcvGoNvF1N55JWwMTZSW8Iaar77%2BFeV2ZC536lcze%2BF0lCgChTCuHDbGGwPOzKu2FnZWeou93&X-Amz-Signature=eb82f94590ac9c1614dfa6b14bb02d26648087846c7e2d67a4621910f0af7a2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
