---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75TVJWW%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T161150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIFgtYQJDK6M9Bqxs%2FdFzSUzXLxDEYDN9hDoDVo3U6wltAiAiMG7veCsL3vfVLTu483TmdPkG1pMWO26JY9B7MQla4iqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXd3a0HzHdOSAoD7oKtwDQCS0kAuwxo%2BEesxXHGHpKBNcUgqDsWPoMi8FLbQhKG6HkCR%2FAyYObBiYN08iHBQrHWR1jxzwfdp3lcmcc%2FIbACWwsUE12FfHdCw734d8Z3ZUtKLxuPzvBz1eo2oN865nEypbJVOAbuhcqlsscx0rYL7orw2hxO1A%2FxUcYPgRn6WQkf8IdTVrtVRHD8Os%2BlCzA9GAZoO168DWSyHvIKOwtyvq5WyI2ZUSDNZkT8NaZTPJU6%2B492bMSuufLQyPzLkQsem96n9mpyEpzlPSCwr5970xv%2FC2s5mqKF7NzPBMHX%2BtTAV3s0wLiS43N3W4x7YMYjCFhBtnJh98y96LyyDdwph1FM0M4336PJvFQvvMn2auJLb9SNj1OUJSfTdE3WXDlk2lvMDL3cej2arc03C9q9C8nJ7zuwcqhcSxXd3GgfL%2FcM%2Ff%2Fx%2Fqitit2zugfbtlbJ5R4p26gZjBG9R%2F92S1WR3HuHTlvGtdEBdbqoMLNrA57ylNmwFAAyqvD4ZcFkLvKXhfLQ5oBQ8OvfkJ53uFoXaHqv0fH4ohXuzB2Ny5ICEL6Zqnn%2FNuLaQf1y%2BHAw5U7LNXTg1klz9BO3o2qpZAgs1wAnmxhnreeXOSlffIzuC23O1cJNoFZWy0LN8w3%2Fqr1AY6pgFPkVsniCkZLgywAxXc633RpJrZZXdbMOdv855MXNR5D7TbU0YubSEuQV7OiUW3YofmDl%2FL8dljkCVM6EZvr9IXHZc5tSfFrQq%2F09YLFbV%2BepDjeJ2pAb9NEK8gyT1c2PF0EnRAMsNyVBFdplFJuTmQ46WlPiDP9vtR6RCpvrKsnlJ%2BVxiftm3KkBP2dB4dLqlkCeh1G0QrTMORB55Xv6QBLnjADmV1&X-Amz-Signature=e71185db69b9c86892f0d747fe202d970e22f0c2fc6efe3d149a0ff8f9ca8ce4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
