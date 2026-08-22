---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RURCPE5X%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T221006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYFQj0agFjV89uDLAMQ0rnH9k8v5thzcRQXSSVurXfIAiEA5hcRg2TgwZbSGqqr2airrHdhc6PbAcSZuDD9D219vc0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPBgEUpCjOjH99GSCircA1VSRZYMR1sMLsVV2ebckmzIzFHrlczx0ew9zUjCt66CTu%2BiFuixQe0YTWU%2FDAPo3zl8gmCJkWg%2FEp8RPUw0Yff1PtoMClQshM6mYOvPCPkdBKwmO8oaeaIJwR79qJ4g05H51o7XRi7WNXe5jP68xCCtd52kRlxp8PiHE4wLMAVIE4IkKQCfASsZg6JSsacZytoBJ%2Bg8410%2BXswLKFrG6Fu3OPRZkw7bh717MJC2kh3ekJQ0l2oTKI%2Fy4OAiFkqFueaNpQi%2Fwx0YAKcWvWQ%2Fmy9M4tHolhPvcwDxEo3%2BNsq8tFbmvwHJ%2BQxtYJDu4CTL46fF%2F%2FALN85L2IHdFYa1XHDTrr6thE5FLLAdlcBVsJBfmwMNV%2B5QcDZ4Y37nESnpej3lI9a38MXHGwZxvrvX%2Bg58hZDEf1M%2BaOW3Tuk%2Bc%2FMvVODqJcbnMCVj%2BfqomMm%2BgWwYC67QuY5MPhl9vC4Ac5sFCZLxwavdkq5MMeeCHZNS%2Fc%2Bm9gcbE0B8QEbmlnpYxJ6zztbn1HeyC%2FuRt%2BM5ClKKlB2ftb7OGOj4gxGXgc18t9efIJz%2FiFPDligv4Adfm6QxjDOc%2BLglDzi4IN8OlgChipTqjU539JIwGLVBb6%2Bi21YYC%2Bq7VMgbbZzsMPCfqNQGOqUBzUHMrUNt8eZlkdi6moDBkP9VjXqINVuc9Xwk37PWWSoK5zwBq98gdoLpZiRxXmy5E2IwXX0p8sGEHJwHmRLNV2t4E6d%2Bbp%2BFlwSXU7TGBV5thX21Ny1sA6j7ZhqNAn4qDygsJ6rXxqy3BIhPvyO43ReKl1KrJBnHK0SRKjjnujIIOyEkvs4s3qmFFSRW23fD7PUNwfCmeEobknmvsLWhovL9Um3a&X-Amz-Signature=bdd1fb09b949ed2a95a0b97089e5fcfbac75ad3269044fad26809581b6152915&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
