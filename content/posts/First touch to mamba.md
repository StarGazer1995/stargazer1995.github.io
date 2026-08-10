---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUH6CI2E%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T090543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgkiIqnKGEgxHp8sxaZ6EoSIWbmJEVQx2qAfKiLPBHTAiBFH6PN%2FNuHsLRhRe8weQpD43WfMD1NuGdbZXcSbIVPWyqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FiGPlazeog2ZRJ8gKtwDZef3IfsUNxTBhMEQck4mWBDzH8o2bQE2g2qqDgxdw3PxooUp%2BXzFg%2FE12VQ2jiN%2BEtXLQn%2BQ5vAlEEvieaVL6CK96Me614l9lHlsdR%2FTOLMWt9az8nfhcWtifbA1YR%2BV7uNItapI9voTFCZ%2FO28G32YZ4GGZrQQT3IcLg5r%2FgCrGYIhddJZSZfVztTqidmCeOQi6fzcX0L4XnfVqai2FyAPtnxS04i26pxfxMhO6hFZX%2FIFBZyp9HU%2BbVT3llKevH4FjrKHNZ2BNSdlCJgzPfx%2BXFRJ8KCWrXtdoyZR9GbWaY7UCwAYtlUjUeu0U4%2FDm2uJ6CIar%2BGhu8TtNxGGpkiTuzLZshTMFcYhej2tqHO0VIp6JkIwhKk3TgpMyi2lX%2FfgPKmy%2BZHNnkgKYmpr0BwVA1beoh00db9A6%2B5JZffd0RKeq5X4ReImNC4Iyd7IMgmNuoU4Puruya1EJ6%2BtJbO5nNyryu0JX7VvvCaIbre4lkS8n8tqERxCux5dQD8NQLIjAfrKzmzVsLWlrS%2B0zGHfd2lZGtcQ6gJXEB57xj1AN4Wgu%2BziUJEKKV5Ha6b3G4%2Fgsik3vW2tR3riKoBMjWR%2FnlARypkK8nShBCFf1sPuv8drtBFLuwzRHOTQwgILm0wY6pgGr9q5GzGsv2ws4gTp9YMGW8JYUcVMwhJzj2WBBrf8hNFtaPRL7ytSAo1zanks%2FhxyCcgaUGLG4ndB5NM1ABWGjL0lSrFqR5bwXncqzSOXLHPdjY9jpnKKqqiZsT3%2BC%2F9TIO4qnM3bHT1GA6qJC0%2B5h4A5%2BIZw4Ojl8HOP5%2BxSq2XZnTdFiHSiQbH96z7OBl0joU2jfZAw7yxdj5%2F2cWTwnVSisM%2FAU&X-Amz-Signature=6d8e212374b405183e1868004d246edc35789d0645f2b2386fc2504c6cc2a9e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
