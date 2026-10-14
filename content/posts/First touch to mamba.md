---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BRFN7EE%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T224733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEHuRBwTkStAEviR5TXdX5cBgB5xvs3fi8N072%2BQQwKQIgC%2FxVU%2F4iJ8hsJLBb7kdvizOSr8vhmByVa4et2V%2BPtZEqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJfenl4NweAc9FthpCrcAxq0RlHpTJC82Iz4Wo%2BE8xV%2BSACGKjyUrLK6%2BXH5gpBzoCkeGbOeXIBlhVzVuMks0KjpWfkoBGHlFewityvJkzHdCuV9HCw%2F4UlmG6vRfrNXnop0XZXTJ8yN%2F5MWWY47y%2Bc9Ul4OeVaA2qZmj8yPb1bW1E1u4awQLezE1G2pbnQHV0BdF5VpP1trBystgCTcc2o9wJDk5bFeQ6WB7%2B%2BxAd1%2FNogqKF5GW7hD3rqU4SCfqhcxh0H4MQVb8plC0wtzTJn9CW%2Fe3%2FUWMzhomGJwJ4LFO3YvWZ%2FAT%2BXSY8qptn1Fsizw1NHnHELK2ruRKdUPsZVIxiBQao5aWsG3VgxOe0qWxdqNI7NbTaV7nJYJuwyZIaYnbvhkfwxmFQJuRl79SwUKltcEjJ0DBoNKUcYVbIn9lLggSBYrRstlvuvTCTrFKSpjB5nYGAP1rXPmJxXN4wnMLuySl%2BEueQ%2F4FwN2fXUASltD7PI3QgRCx4VLQclw0P6%2FYHas1rFNM9W4LednaTT40oJWi7MTAuGLhTN1fQw1ti%2B2p7hBXJt%2BxLLUic4cO4UTmrdR1hVMnQ63cOYKr8oDnCKb99S0DlysVyuWRCXxzDYL%2BhyuZzal%2FQFqheM9ofSTacStUbfLQBsbMKLWv9YGOqUBug1zmiZRVa4hm%2BZ%2BvYSLpqAE1%2F%2Br06faieOCeB8kAxEP35rTjTS9W8lckyzVoylcCiuog6PPybQrnPrhA%2B0xUez3B%2BGqSU4bo9myw1QXaf7LfNa4%2BIi3jwtSVBOS0HQFRj4BwSZ6h60vDc8iN4ATppBZ89Y4e0ou0q0M7kVrNriJNGyCwB7N8c5aco91cB0hqTxC%2FaXm%2FaIh%2BLVNNCWTmJRhFnPH&X-Amz-Signature=aa1cf5711ae505b0d3d38679807f12f7f02238e3cd6c07688b7c0be874c3694e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
