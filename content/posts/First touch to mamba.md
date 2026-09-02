---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7FJO7JB%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T234035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIDqnXg8eS41cZm8SpqQRMuRlNYbKry7KFshJOy4aKZ%2F9AiBGSSI4mPnsV%2Ft%2F90WDE6EZt0qflI0EcVJDs%2FN%2BK639GCqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDLp%2BlrtQDu4AvnWLKtwDnHVHXNBfJX24yc7%2ByxOYLfJFUWt79%2B0%2BvMySCSROi76HpPOhj6vfc1m09diPr3B9qSHyYfnVge3Ds6QAlwKCKhNeffq4XUJ9RG6J67zRpnsX1XdZcQ%2Fvf7ckywTan%2BoAhkNnyHM6%2F1zuNXViDg8Oxg%2BZ440jPmE7ojWikpAxmzrTUIolWg7e%2FX%2FWtWma%2BPnWJGryohlaHLed3yaPJqubgJ%2FlkLE4hl7bzG9t%2F6DUButiaYO7WNZY%2BooLV5O3724W66L7pcVUQflyR%2BdL1vToU1ysWB8nRjrql0RPGRqCIPkUr3TRTVdzq3RY4YGr0uk0CPPalLP0Pb2rWKlztDuE73FHqtADvTCPDznGhfrcfJ4SrwdTuFBsHkrC%2BmuhfsVOypuyQiOtJI94KQC9s3m1v98y6%2Buh00%2FzZuUbYnNSlNc0oUm3icXrc4BOy9Sj4M2cn4zH6yfOndoZtyIjgY0zsl3vn5OyEb2r7nb02gTJwcfw566iUY2vXAT9lr6LqFBo4Q8q04neblpku7zbiNwcp5mbqaQexoeMqdiFHOHsPm7q%2ByOAE1R5G80nck3sTL6LpRWqFRqC8LRFqIkKm5%2F13O8SVfnLAU6qI9yl05EOTJkqIlfu5hwQ4QHWkNownsvi1AY6pgETnZFdpESTGvUfPMys6z1o9MKq8dGcRbDXO8Yw%2F3VSZMbf0Ptq6ISEP6uYwFNoCtK1NFHkh3vKiEIiJVv6GjPv7yNSW0tqmfqR6m3x3ksYSaQ3uDhx1CAZS4Apux6Vwqolu3WswrUNsGhCxRxZA3blfcnHPVG2edClIsSmVbnbLfiS%2B4LmXDszXEhDlaR6UXmzPwLa0XLyWn%2Fhz2YeQzjUxBaqzttB&X-Amz-Signature=a273a442debbe1f4a3d686e780cbab3d3f032f24968660eca4d4a95390f7aa5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
