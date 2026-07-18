---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQLPCONI%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T105549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlSC%2FFO%2BVC1N9aw2ulf6Qe9w9D1yng0mFb91vlhdcGAwIgfPZhVQhxo6VnXjQQYvw6cupxTfK0RqhshJmXSa4lPTEq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDNGNtLEFsJv08aqv5SrcA5SPsIx5fbL28Ll8hWuT1twtZ8auyIC0yFUxPQi5WMhSTptFfZ8FZXBwySgDoTObWbgUlP5vrxKrDbwpn7630bHCy%2BvfjJQimdWeBUp6t5lSv%2BLw9jICBRodw1ngUApBI59BjLzTtxz8dHds%2BIIlxLld3gpYeyPgbUra0nQh2N5JdC9y9Kk5BD01DX0nW2IAQQJ3dK6%2BoFH3koetP7EaRIL1LO1zVvqGHsmR7e%2FcuZwN%2FOvLk6gNdYhd3XJp27bdkKnfWDb%2FEP1uHGt%2BEIGnw4Hc5ag0GBiKHhSikU9G7W5M5c8Gmxu5x%2FCOVj7xlV7gQTJmI6qt3PR8w0AKku%2B3tf8QQexc9Xm5PhmGuOOaIy0768fXDgphUxAPRHoyD5ecsi9yD%2BhJNhU89bNstIVpcoIEj3FAPxy7BXip8UPrHsXs0Zb%2BSmRu96J5ZRqjefwYp%2BD2k4bC9au%2BoGp3D1VI9xsWaUwBH%2FhISUECa4KV97kCB3cSBRJEW0pQqdjUwb%2BbVLRws5cP1WoUxDEIgSliCw0o4mPzDPBOlL9%2B74UUbDD5K74dJaVHJiCdhCecCU1DCU2mDUkKl3gO8yCZNNL3QfEhwcGgBGG0VgS%2B6rl3OMYEEFtVDULxRfuKXwK5MNeh7dIGOqUBSfvz%2Fiq0XS%2BPTeFGYBzEDHhzSSAVEZ%2Fck6Gd7hZHzRqjQD8M7N5%2BI%2BPoCf%2FzO0NTcSWoxIbntMZSQwFi2fXOensGzxMzaF8Z1emR%2BHxQxeZ%2FqXJiT17oXMaDNu%2F%2FA%2F8FmPJSAIucJowJm2m0ax60NycygDuSPZq%2F9s5nHZiMcxpuA9sHaVs1pcYA9tjsa0ucmfckolTQHCuLhz2iYc5NjiE47W7b&X-Amz-Signature=e43fcd5f43799b876fa3c54975e4768b76be6bacd25664bbabb9ae96a3c399da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
