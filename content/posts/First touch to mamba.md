---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XWTF4GT%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T183025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiJ8DGSjvVgXH7vYXGy%2FTquZ1%2B3sQCB4gC3CMl7SDkqwIgL3tgzKy3k%2FJF4F68KTM1FSFfi9aeUFwtZnjggXyUq3QqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDItt3C5dnoz9jazgSircA7qibqttXz9WuzcOHrOD5L2a%2BaelaUwwawUXjwrkfdmnOI5okp6ZUt4%2FWH4iK10bhrDsfvtcXve3MK3AygM%2BMm7mIS3f3VLvv7yA5k6bi2sHGDP503E1QkrHPlJrWkyeBPjFwU1SN9jSdC6piDWt0qdHZNUkPrva%2F9K2U9fPwQnyr5%2BITVRv5Ca7zqiL90O0yy06bvRt2dmBQPnH9GbGyDjyFmodI1P5cIFW2FMoukRtUDlvdqdSbWaragv%2Fb4RSCwyN%2BuaDpP2b%2Bu3R5mIMjT6iq2gKbZuPiIDg%2Bgz6QdEz6e2y9XPq2wj6UXOvKXKOculF2dYyENypDuoWThfsuWKcwf7TIS6jtRYMTpQYUPDV0TcQjnEP5pyVZ49gNLBHc5wFV57Gj5I3K3fJA%2FgIm7G6KyyXQe%2FTZj5yvOdzkZ9yy5lbxsh3Myntgv2bhqVepZbdWosJJ6%2Foo0Bl9OAMeIMgcq6dd1QYbUUtgu2aWjrK7fzjbAIrRIfQBRqjVvSAFcJkLXuA%2BNIXNOPaEiSA2kuZsFPR8t4n3cPYAjtuN%2BrQQq7vbW38kHoU2%2B2eaaqiwN%2FhOTdxmQNR2OIof9B67u1la6fYcLcl9jgT%2FyxCyUgIIlNEZvp7X2hqfDsCMNeH4tAGOqUBX2ds50Ct%2BJ2cstphzd2rV1r2jV3lVFa3DT6%2F4p%2BYIlqZRku3Sm9oSMZbbJI7colGTdaIMgiuN5ueyz4%2F7u40iM8dk0b6c2Hu%2FNQpA113pAjv96LksACp0wX00JAsphoimTvcAT691xFlFbNNj4nQKrb8l9mWOqAUtndPmxZwJf7JDlzwvunTFjL8pTpwF9V1dEHpsS4f8nvSs76jfKwjrQ9NUIfW&X-Amz-Signature=cb3e4a73f9f74eca2668ca2a7daf17cf55041bef88ca0ebb60ee9947304af98d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
