---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6QBZGEV%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T020627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0phH06KWiUKUFqJ9%2FfJBvgKyshB%2FV0lPkMtNdqh1gMQIgR1EHekXWSDf2amaSnWkzgkq9ClaJ7MHfyf5cEX5svLYq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDG6XmUUPObJ6flerwircAwR%2FpX38yvSEyKFmmLge4Gns8uLISgHYeXmoOiLwIoR3pJrp5z6goi3hApf3oURqPKQMu6Jl4WHahbVCUaGt2bcmAyRtiaKUtCPbhM0IG35pjhkHd8PahZADvIlLZbSMMkobafsDWJOYIspnGYTB52OZEQ%2Bk76ohTmH%2BPpUVus3zV5tQ6UwOqV2MKcAwnxQ9U8V4MI2JvQNMfWfke1tQO2FREiKPxP2bXvvBBg10gaUwAsvCjrJrB3QfmcpnWNNMkpfUCHtME1U5xYr5Ae8QeCFD76X2cFXJo2rzsPTQ7wM3PxiR9D8vt9QJSvLgpXnX8onBudDc4dOhMe%2B8p87ucrewj5mF%2BE%2BEw25AQ2Z9YLY6%2FLHu1ZxmnnS8cCHKsqSf1RyH2Ce%2BkHqLqsJiIgqDoDJaHP71KWgFT%2B45U%2FB4qECdV2xwUlovYTbSXMdaqpMt5LpjiNrm3bu1gPULKTbZzshfxqLZ2xjNYqCLKR8uqrAcnYPg72U7U2Vzh%2BNYAbRrswVzFQ%2B%2BiHh3%2BbWWJTZoTjeJXqNFYM%2FSUnxWNtcSAvZD8KO5XKsFge9RJAxqGYtwO2wfU%2F6MHsoHcwDxZ95kS%2FSLGTr%2FEIENBbO3RvRxeYsEecFCwHkfRQ3bFIYZMOnLiNEGOqUBDrNwS08S9o1HlvbQ0GKuKGk9s36NP4cpQOUfkv6qfeWLGsLX3JAVX4aL2yFJ70dfk3G1Pb6H1i2v75C0JMdyQ2HnvGvOe2ZbUc%2FyxDZUIudBW7g4wkj5Syk68quhzHDrWekrBzYzKlqHK2%2BHXRHWix9nI9Xo%2BzR%2BlsCG5l8%2B3vwKVuh9plbgb1KxJgM7ZNo90pHmV0Oh2Pr5HUMC1nJCwPV8TBYh&X-Amz-Signature=87dca9fa9a38af9e9b32cbd3313f990ae795db9e4e04ee970236cc2f93b6c808&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
