---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKCS7OC6%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T162054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICe0%2BiWV9hvvbi0RoKAQOKHnM5%2FJaK%2FlR6uhbodkMhsVAiEApLMJqh1YIOzAxoLR9lMD7jucB7DtI1nmhmZVwAem588qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDTSjfKfCe%2FrX%2FwmECrcA4QOW%2FNPYMWgL4yREvQjlTSJJeC01cI91dNxQAFlpXNxoKX%2FdAJkNgZumS64BvG9fko%2BAArabDfFbGCdAINT7S%2FNv6VF7xJsvJI013Nyn4CXo2seSLvrSvt4BI4qim%2FAbXMbzYyvhc5dOIRCSq1oskap%2FPt%2B4FsADGaWW6022%2BqxB9W%2BNDNPyzZcRkQzoDP9DBXtvVOosJl6av9Sirybs0iu12tBMw5GBUfalKxt7LwCYtibC7CU0sFmmXQ8rvjjqmJX4%2FqvLkovVlqty8Cx9tsj44A76HmTAXJGf8WF6wYKkGIYTnTp%2BnntKNZ8zSCCiTXRV8MpslwO18ApsBZJQTXx5OBhR7PXK1iM1%2Bsrm3COQeJM3EiEsCoePILQl9sUoFtXVEPanVmUGTF75ReV8ng9AO9e6E3KvBY%2BYLODPOGFDM%2B9267u9WydL%2BVKtua2rqpbxkHtZRhXI2UpxxeIv08MW9PZQig7HFR9B1qxvzf8ZqLax5NunUp%2FIkueGQConA0WsGyPrkpm%2BuLvPostzutReJsqiJ4%2FwUwili8HxkKltaucGgDes9Awl1Ax%2FqvPBg6q5a0FeTb%2Bu9RBXNbwg9kVmVy7MEOJAzVwGve56UW7doynNglHpK4UqkqEMMzB4tMGOqUBoCVHAah9jAX%2F82EPPJGSajIXzwArq1cgIt11595tz8k5g1ZAYmPAZGMCAm%2BDd30rlRriwt15nLyWLAfQZX3a2Axkdar3bXTbdwZ%2BSOBqqreMRGMxQuKdsK1PE%2FNlRKUXfwbZvMfuKo7vawZFQegHyLZZa9msMviYr5Nbq0KPD2qT%2BR2NRBoyHmEvy%2Fde%2BJ1F8KA0FeS3wEDxUWB3vzrqvTsJXvjX&X-Amz-Signature=4b5f718c5ad61cf1b1b1e11424150c6ac14601454e88c3d153efc2095843b11e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
