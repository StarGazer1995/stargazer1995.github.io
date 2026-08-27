---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UX5W44E%2F20260827%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260827T170131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIQCycej5K%2B5sGO2tiLpAxhF3dnB6nqHghOOybRjsb19RJAIgF1WzCCw9ocbiXHDuA8ccnFz9WCpeUDUUkJurfZ68tKsq%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDLJcv2qG1gZ8NwX26ircA%2BOxiiV6sZSe7t4fmeIkZC3%2F4dnv2ZPLfgyW8ethbxbf7bizmgir%2FqoKe%2BTFcE4S1UrvKfAElyqPh%2F%2BRiAhQ7w5dzp9FMPiUwbqOxEa%2Fn8QFtbd2W0Pfft5MzVUv6Sbmajt7MNGwj4CelAoLmY2BytE0dzf9TX3uVyZJ4xL1IXdhrB%2BGs2OBDjOjs4TBK8cdHhVeNgLpFwX63iiNqsJO%2FTse1bUbSbCl4qoKvbvB9o2VQVFssb1LvUh5MLARC0yUMrgDmhrDM%2Fubxuq4yeiF8czz3jOjT7TVkWrX3RieMf7cjKhhvIsWay4GCmM2Ps508dvWOQ3f3rmLlgO8oWP4Q%2BWp3mvwloOoJPl2cxwgVnPbnv80G6s1HnBuC4ytFe3gZyTl9OWmr%2BHyvBIABWwZuER0GVg7RjnNQK%2F1iRAgi4M6W52bWieMCI0jx5GVcLxMn3kGcrqE%2FarSS5F6l%2BpREPlw5kMxJAcxzhBdWglVj9gvSA6wHxAqQuTsJng7g8W0eLk0Hgm0Rc5sTJ5w4W6ptNFbFqA38ft8RUV5TvqKEA7Puca%2FGqPWWqzGD%2B8FDhkCtRdJLOOEvUDsKajyRxzMC3zD%2BcJ%2B6fsJi%2FgdLJYdM3Tp%2F7c%2BmUiUygHOWqrsMOzPwdQGOqUB6tLiE6SdL5X3OgV8iTosJVp8M%2FG6rSsEyqPvkrPuDKR2zS6qTxqepdVBWecAWfnZY10WtJRaizj5XEAjoFZvtQ5iAoCbuQ%2Bpz8ldNLbHXbnv8Vbt%2BtY6bZjPDBwUpzANSNa45kin%2F99yINsH6mlRBdY6510dAjbNYU69SpSJGYjvIF%2FT%2FwP8TsKw7q2M%2Bhi4kUdS5q7lgYy25IHlxifO%2BoceMQ4s&X-Amz-Signature=562f22f905583c0f3f1c086288f7aeff5a59cfb6a4f64231d34c4d3b2e5c557c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
