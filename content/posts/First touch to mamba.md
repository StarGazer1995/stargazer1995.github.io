---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIEOTSYV%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T135752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMZjeqLv5tIX5qk%2Ftcnm0DTmK3KDm3Ca5XlfPUcNdhqAIgIAoi7sTdmtUI7cIQK2TtgDVYxnRX1Q56KRakeEu63lYq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDGXAVD%2FperiDGFBBpyrcA64N97VJEzU4mw6qm3%2FVhnFWtBg23cGWck2fp0c3vKQMv29szVDnvCRz4AywrMWAsKAgNf%2FUib%2Fefaj8qmM%2BetRuQColmSEMQavAaRaXaBjgZAcpctM3YBsq7I9flyoPyo10ueHQySkJBmaWeeVvSqcivvwf6GwsuZIU4fxYltlFDACqnr5sElkmmvqG9FYGef9UbQOZ7jETYDs76N%2FqhIYu%2BUAz77IiPcCuJqD8R3NyUEPhN8Gr9m1K8BwAYNW26p2VzwwKLWB4eHL412VuUWvVe23bKb7x1ijdjdkm%2FVvonVqbQLLGsqaV7wA4ZLLFencv0MOmi%2BV1PIzK4sj1UjEHIqUa7Ys9qSIFgpHMUVLKydKjdJC5xsQbsTC0h0V%2Fl6bEl3Hl0UpGUodbphzv0FgMojQRlWRpDNtikTFaan06NgtRxoOW3Uwpc0bkzU1RQWVwdIacLLZ55h3GVTmU5D6%2Ff9nE5QxeymzBKdOo%2B4qFVEqciYDAc9ciUv4es2%2FRW%2F%2BXMRVtYdU9GVeMOde%2B73AAVe0Yky%2BOEW4JWI0Uv9pD7BP1lGL0zOinI9te%2BUdn5gbN2jXbix9OipOiOcMd1d%2FK67KEVWUAEb%2F0TFebpmfIGMpis7gtrJciuoeqMNTm%2BdEGOqUBbH5RQSPe%2BbBtGHtRh45dDuSwJ9FWH4JZT6J%2B7ZCctCLfkkqNfW2U8d%2FVmPcBXt3sw3ID9eRRSoj7v4UCjbxkqssa6nd8Yf%2F99OaW3KFurZd690HDjk1IljCND%2F9tbj4cs8faZL0kp7NbLg7cCAyKEsce9bjI8yZk4dmhPSomdcwIz8FdTrjBezJHWo%2FM7iMYbnDdMg5t2wF7uQfRs8jaUHXlTB28&X-Amz-Signature=d8bbada2086a7cc30eadd68246b4fada6de7d648965f127f20200b30d8fb0a0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
