---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY3IS7BO%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T225009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCL1RuJ80GJdoo22qzzY9Q4O8rqAX5AKjWsOAJZPtw%2BuwIgQukLARrFM0o5EZQi5TYHLpvmAz7APhhfek64ausbi8cq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOMUR1bOB%2BN465uDiyrcA1NNViAggSaZNshlxSWazXqlg%2BaloSx88xS%2FL%2FQiOTTpx%2B5yiRGt04ke2oErf%2Fm9Y2djQNufFTvkz9K52OvNUrQ5YiGdKszG8gUZ6%2F2xEqnu3mmfncDLKJEAJN6%2ByMUvkafA2oouyYURw2wS8Uw2AwOdd06Zx4w4yQjTEKgTohvel6NRp6GJR4tEqI98hFYo7YtlHnfcj4Dx44aZCDUnYviiHkxkzJQ1T8UrgAfgpi063KqLOi8qOzUEyGXMK3nKnkPjMqfHWtWwavSeL6npqJ00yZCe2B%2Fk9NEsdGDPFSW7R5Puo%2BbAqydAA25ueTiTmqezDNHUez3HLs43vVFVGuqYDOpZSJeIUG9%2B4SD%2BvoZeRrBJ0YopglkbwN2eqjSWEpXcau8nv7TqBlXjYfibLbSA7hJSKdjAZkKCzMiiTOlgO6BLxlBL%2BrcFBPMviG8ljWT%2BZG%2BPsqT8RA2Nz771hEA1jDMW3bDfli6Z7XpQiG7LbNbAjJcmacbBI5udMCuyQagJDfSBZ7AUetlfzDdQLnGMSxVyBrw4GH8KM%2FtMk7jLrcLYGLAVPb3fX4bS%2FqO5EYtxpMhuACQu3HCuwanO3QyCnhkMfQVloynmOCs7DVLZKJVrnt637%2BDCA6RBMLSsw9AGOqUBt7AY04zPyvAXPlA0wteWaxCk%2FCGjTN2DOr4RaCCW6pBkZ0s8s0wuhgn7CoUgc9hdBkflHQPFUyzI6bp4c56NnECG%2BPspKNFsGAGN6mCGK4os4STXyopu1xgKO5aR3NL6OZ%2BDmmuaQGpjlbgWhU%2BmZdhJ40dHdIpYVSS2BMmmZSHBxSyi3nnvcjs%2BVKOtnaK8wIxmFFQuj8fDriHw47gfbpCKFFga&X-Amz-Signature=4969ac36acd3019f43ea83d21a68094344948adf846897833b77d9b9ee1b62fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
