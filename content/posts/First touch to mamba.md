---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG6KDGVI%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T131056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPJbZCbTWvzd3jJuQHN3VdD8fPxJJPEKamuzHNiksgiAIgS3iSS33MoDxtA7iFogwh0isxFI6tJ5AUrmAPAiYVHZAqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIrFAOfY9S%2BaECGD%2FyrcAyl%2B7DkrxUgvRetYveyXrYe9LkGw626tY3%2Bq%2FMhqXA7G8vo%2FbPqDgdmOo9Vv8OUzoxIwmuqLPSJs04zG2jMHFlYtn29CtSeFXAoJHlHmiiOm5Tceo2xt5ZOylz%2Bpin2uC0PA0Ztlj5pbxJINQ3a3XvRhUx1LhH9vE6sDczBNLV%2BGCVR3AjH2wRSZC42WW71IdPbeagET96QoP4PhKnbsQJnpEZHs%2Bp%2F5A5qMGyAbOctMgJiDBCe5afZBMtp3wTtRy5DdsgUaGpBt4D%2F02Tg%2F3ws4BP%2FVNk22Zs%2Fwz%2BnTeCgD8BO6ibd3qZ8JIpfkenvMQnSsV%2FoaZ3AQSaNE3PF5qfBotTxgQCYqRdZRRewMVCayx0Om5CQW6c%2F14khOP7SeWXPITBuZNKK%2Fsws4VqnpTFv%2BNQoBKwrhD1JStjS3UmXQhWvTTZsEBJ3amOHbOIJ0EPdZgIZV5Ywgc25tK1zzMx4dWubEpbHzZT5%2FuHN6L2OeMyN5CnCYGeOVy7uW1Mlj7z1A0F5qDU4rVQCTdCVqTDv1I9Bi62zMDgUXqrebw82pdrlhZgzkUNyBj4VJA8U60bN5Zc%2Fs5uOUfcTPxTq6%2FzOmAB1LsGaVqOvg3YRKLIfRDMb9WH2TU%2FruNFE6MNLSg9IGOqUBm9mnYJYgDby%2BQRewwms0d2zTkvTsjDJ7%2FI76dhLNNZLh2BWzKgnRxU5CLwktY8UlplNRCj35UzdiryHaPEEqTKEHyGW7Mm4CP03uR58Q5fqGX%2BpsXLlNXfHUv6mBhCKXEs5fW4k6Knw3ONWZKerN3ORw2iqyARiK%2B6zYoEjMMQWRsmf7jFGsjDd1RQxsUURrXZ5BMGAneB0I9BnOWPq6tabpsnRg&X-Amz-Signature=53dbe8c3d39b05884bb451fe54fe9f8048410ab42075fa0cef266aa08706ae47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
