---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDAXEWC%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T205843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEQCU4IYnhb5%2Fv7AFLEa%2BintSIbU9HvnS4jlrPyLVfXzAiEAjIwLj6MV%2By%2F7EPJqfggb%2FH69H3K4NioW7mepFfnZGf4q%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDKZIfCQbL3bdVhuYzSrcA%2F%2BwFo2RRIFnbLr%2BxJPL0EvmVCwQNADIt5BJd2GOC7CcE5R99wfoRAokJ5Z1%2Bw5lDxLDm75n3akpEQbeFDkbvwh1fvnGwCcsY%2B46EPUkcDXpWxYBL%2B7dw8vRnZRrxxtV%2FNTxERBt7y%2BRAhQasXcmOEtkrGzcmGoaeg%2FqYHyOXQouXekehs51eJ2nQnZqE3cdqdjOyqdXjdTIijA5y%2FyOeBf8zA344rEfFkN2XCf9UfmEFKw9zncKcAxBSt3lmcvJqMu91HdgQP2fE23UftkwQ%2FU1uo93nxkHGI3x53uDrDe5%2BhS8j2b8c3FbWySrY2QM0Q%2BimjW29K8AQZPoW%2BTBS%2BMyojRkktMZLkvpPE1%2FAS8qxv7T0WngqInFw0oBN7eOFKSi1q9nvvh3unJgN0tyVol04X6J9cfxnwzkDzuhlijxmJxUw3%2BwAeAqtzSs04UwSVBZRbGGF5fHU6W5Zr6%2By61JjnevjnMGcMLttvFeJCCrQnmQEHAB0Hyw7va0CJC4oRLG3QJDv3g6WFQ%2F6mTscvNjODoaWIIx%2B%2BrQpnukZYPrZOVjCV%2BO9UYyal6sNwMcsTMOGJycNO%2FyOlpGgAKWrq9EwosYqXwd%2FoHGELNb2%2B7n%2BP5qAaKC6q5Du9IJMKaXvNEGOqUB97I3tgJjOQ9xUdnP7%2BQi3zBfyou08odbql3b3kW5%2BxTLhvjoRnWVu3HSdGwBD%2Fo4cRlO8sdLPp8J8ImJegnDZ6cHeAkHaOBqqqRtmPnDgZGpGJYRRZUJ%2BwDdTFnvlAsB7Qr6l4FMD%2B25q%2B%2BZVF6xYTMHNUz6KlFNxsywa1xnbNKUonfViooBcX5OsulZdQv2JHkQGALbMLzHUIZj47OT0PGqAlmf&X-Amz-Signature=3078040389a6788c2f811ec293e87ca562068e3ef94f79101698def5b6a79b5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
