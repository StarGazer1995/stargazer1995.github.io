---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7TZJILR%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T181756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDCi%2BwQF2exZjZGaCsCjUfHjNpJa%2F6v9H2aYdpNUVcNfAiEAipBsm5dPCEK2oaTwkXhEyHLd%2BnQl7FbNN8wPWdtq%2FE0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHu4pCb%2FhpmSUvSZdyrcAw3Jp5sJaa8p7nW54eW4BhgUjlYod2K1z3Pk5CTDRbJyfNepltJXiORFKkUIuA1NNytIVF1nH5kFl6yQq002%2BK7%2FiykUL7bkaxKP7dPislYmRWcnXRyf5D7gWHhgKSTmcxCpJ5JnYzefmIbmLiPU1WeUfv%2FNBwPn9HHLjzhRmej5cJ23OBEtRYM%2BbFOJV7Y5w1TU0ICEw0qanG%2FldkrKTCFaPc%2B10DYFZf%2BBqPKcSx24CG%2Fj4nxTSJG6PWn5waxRv4BYlDggzG4R5K3UyepU3m5jdJTrX5BSUoCBRhwEQpcY%2BCJ0v5BdtiJXqBZqGtmrip5JD87E3qThOy2N4bT9myzwYEZhsPZdKhrX4OEmKKv0P4oekLevBEXgm4yIAUzU2i0N0msOxx3qIZAqtDElf6d13Y5cgVtmmsFkVO6BZMLwgZMf7QxSWyz0bVIDYJ7uQopwRpfOAElkeyTu%2BbXX20cCGXDJOfiRbUtE2mzqOQMCoq9LsR3oBqUwa5Sf44XUz3lJaUK%2BN2Ji40Ons2bXHi0wu93gpk07VCuLHVz3%2BgMM9kf%2BFVncKmtsQVT%2BSxqqGwe7kihUMrgTD8RDZ0y3GTYDsIleZtIPGi3Xm2HcmlGhFG9z9htLl1c9fhr6MNzV3NAGOqUBvt58%2BMblpULKmWmUcrpyC9OL%2BKcNMe6SjNaT10nF0tyOwadU4clsVVhafELgfmVa9w2v52rMK0Nze0PqURacq%2BI2HWM5t3UxpXh%2BfWJZ%2B5vi99mJTJIggWTGzkSr%2FTXdlhch8zFYbB5EN18hYLTVYxa02F5VY1Ynf4MGYbxQKcxe6xZlVbohrzjYcPN0Zqx2OKqkhddsrNbMhRwAxb98d9XUxs59&X-Amz-Signature=c964f36141d9e71672bbd07e125bedbc146e30bcef5485d5903576d7bcf126f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
