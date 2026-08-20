---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMYXGKSK%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T182110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSrmT7i07GxQRH67Ac1NNRrgE3XdpATRMxG%2B7FtyG5LAIgeIJNCGz8Vg%2BLiIU0JwucHx1dFGchC7RGQzuaQRuP%2FckqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2PTPqAE8xqXxjMOSrcA5C4H9CHgf%2B5xFJd4655Xcbmfy3GNCepJ1lvmnjDfZw6pGbDgzyK4Vxw7jc4UufJ3BNWIvNM88Rs49zKyS5SUArA6Fn6RPkTZJxmLbFzdHXte5pRJYUpEtuBndpTPZZP7zLwWrFwnICA0jU8mWyxAIlxejgglFwJ6SLguKbNm86BQW%2BYhzQ42HGfu%2Bf7eo1WYb6C6Do9bvRoGfgXTT2eEm%2BMTfZdTxdRgY%2BOdmTNTUjvISN8Vh8EGqCMsRhmJLlcHLpwMJ3ymkA8Y3je77u7niJ1yPAUvKbod1qbaB2arLIw8BwHReQ3CmzPI%2BEGSqrs6h%2BoBaDC0sgbMN%2F5pA50lmsdJCqYvR09y77m8i36D9TqZozW8csOIT9y%2BMfCdT5nN0rkhUs41SXZupAXtSB7CRYDScIDeVF038A0bTm9YD3sn1ZxIBj0tXA7dEna0NXB%2FCjsemFObvzyMz443YuczLbXAO8pzy9IesHfvM%2Bw02Xw%2BCTg54c%2B1WaJaoDVNan1uZEDdRv8nubEwOGfyBDB98eNIZFo%2FKNwPKO%2F7gahaPDBeapsVA6dXqhT%2FLI%2FVjMvWrWb8mzLWRcLBJXSR%2Fu0HvXfLmy0vXvWoLp0cJ4kDrPK6K1BV0bX5kGyeRILMMHknNQGOqUBierMaaFyFP1z0JsVHRuDf38bIzHVWWAxyj%2B%2B4qha6cLxGliUFgcTjgvcwzxpdH71QH3UFkAsSW%2B4AMfoz1ezH%2BYKwOMv8MlsC4IC%2BrGUBDNcbuPgc4PJPAEwxBYbZ4lfEQFlk64ky%2ByfCixiBkJlFJ6RZt7g5wc8PMm2ORy8Xjju2N9z8RUJunWobnLKkGqOVkHd25E%2F1cGscvJNPgUmTj%2Bt4lEW&X-Amz-Signature=0f849e285586bd040968b11a0bbbc8ed9a03caf14e736c4bd07b4b09fb8c4722&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
