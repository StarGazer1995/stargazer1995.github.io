---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KTSZRXN%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T194232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIDi9CGXO2YquetnNZ3IAfucoLQfAp9ZD5h5VCWld%2FG2vAiEApSRTYAtFxKYDiF8dk0a1urqtbdG4QEtk90y9J9C5P8Eq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDD8S%2Brj24%2BFmVG9pLSrcAw9HgmYrUY%2BBLBlm2yfxdfo06Sm%2FDl7nGJoTxuu2SmK3KNyVUpIRcZQ8kc2gWVKXTQe3FLje49SJfbH6ItXh5posc9jTlANeIJkwwykZZrlotb%2F1AvFj%2BOH50UGCHFjaEkZQ%2Bes254kaorvYlTzBsoX4KQX6f%2BhNdJ4q2SRf%2FvzmaXbOGm8ehLr%2FRWPegw3jEySUVVb2A08M78raUoKiJap95UDyKFGm5MHYtzlRZU%2F%2Bym2jClXWkrK1vIgO4tGu2aHoSPKXsly%2BXMDuWoLBKF9WTH6prR6xHNDKMqLKN14ILR3XAT%2F7R9ITojSGmUV%2FJWlmYagN3nwDrB%2Bwgfub6FjJgetGkgJa0uA9Zo%2BcubezcBEajOY5WwFGKFONh6aUiCTYkzsBuk91e8hZ3JARVwcGUcnFu5wwwoouInu3fz5%2FxR0HI4YUeh6LtNU5qVRUQ9rgsugafIxBjJwgHcoV%2Fp2f3tcYvLMga68UgYfVvQt%2BlftHG6MreIHfIU8P9N4s5K%2BA%2B6vRy0XQb2HswaFR%2FiyFIOuExsjSLKyU6kipHyX3LXpokxA2l%2FppnQHm5qhkcKeHidcN7RfHmbiyNHifr0civ0Jwb2yyYF3JxXUIUrWeF77mF5T4hHjCmVokMKyjvdAGOqUBInFnAbasRxcLrYRUOy2HNsD23M2rhdeIYLxdJCdKrKGrdqZnYt%2B9g9OJQGV85yOCvOyw0qUVzH2XQOVlgjTmySuaIGEIZiDSL9Dp2XP13WGDSsqfkxhv49WRcjrWOAQShr0Dg9ZKebn%2BWxxyuwPnh7gxdJLgnfGpt8mhicnSzg3HollngSbZLV1hfYa%2Flfqb0zpSNLW5J3wLOgR9HU0dSzhbXC%2Fw&X-Amz-Signature=24944c0555ba0168ff83dbec7532ff5e0bdcf490c4a3c3a3810f3f7be85cd64c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
