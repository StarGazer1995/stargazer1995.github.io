---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUDR7XSN%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQDje1nqVea7ZtCGB40Ia1MDhPdehzZfRxnV6aY35L2L5gIgUEXNNHgaUShINm1uGTFM1jSj%2F8jK6%2FXBV1VQ93W4tIcq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDOgMNyWPkqqnOJYPnSrcAxoZ%2BHIyPe8U%2Fc%2BAiC955LnnO%2FBzgQH8HrFEdEI0PfEptukt0AMMehVL66pZd%2BzyLtatrRzyZQwPsTEiTP8bcwBt1qfgCHFgZ8ttSk2n2PLHEi9rhGL3Zm8ujcIE8zA2fE6KLE2qyETDR2IvoYUkNBh8x%2Bqxbi5Q9Urk9MF%2FA2lgwDMuB7EKBO0D5EVslCD93z8oepSia34JU6doFN2bGWl52T8zrGnSAerCFQRmxazuPw0TcAiqvhlK01LqQ%2BUNpX8vGHknVLiYy%2Bv6nfV9%2BRx46NCQNu2PyJhtoFTfxginWzFdUG6R5ITivumWbVRGNgsddDiepCXD7cyt2AOBfMRcdAsjWPB3RjF5uiQ%2FYWtQQrmM8MFm3I4Yt1Xn7PhF1WVgQTg1vjip5PAk6HtS5HshNyHHr%2BNARGYDnGumZUWb4wu4CWYJ9VRFxq1AI3fgx2aCHCNG9YTc8fXkzWkuHzJFJMW1ah%2BW3SCR8IcAq%2FfIMr6YvCXt9RA2oVnO4zey5yblGrW0OuqzhKdvis1%2BiOlwPDhnPw%2BObPndVaSUxef8bdGWt%2B2vaCNDyUsBVZJ93r0HDu6S23nIJcofvE2QnTO%2F86WVKKyMNy%2BZTyrou7gvSs29fWUL16LVDE7RMJiot9EGOqUB8h%2BG3gQE8XwURIw3flXTjoGVu2uFjblqrEf5cExizNVtNPBmGZ8oGfP3bH1OICBGQh%2FRKXI%2FZdftGA4A1vAUgI0C15FHwADPe%2BV04%2BHPvZMXlfzLZmNCOC%2FtlgB2dZTbxai7Zok29m9hqcRgKVquXaDcUW4VvXZN0EugIPpBVWX4EF1M%2Famb5nhDRZ7myAN1bC5nxoJj0GByZXBZGX5NZKPmV%2BJ8&X-Amz-Signature=0869a88e23cf9877dd8157134e9dd47f75cc72adde13ff62db09db92bdc32d18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
