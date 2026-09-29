---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JAOKHJ5%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T000317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDrwBH3914b3YNrLSsV3RwSOlqDem%2BEyO6RCnN19r3oJAIhAIokgFg%2BlQZkXm0euIgP4ucVElkbuLpC7Zmv4fFbdEqkKv8DCEEQABoMNjM3NDIzMTgzODA1Igyuu3ouFCeGD1Rj0dUq3AMmnvrfms2YyTMzMFL6zKSS1knyF3kMWx3lTu2F9sLUL%2Feam0dNGaB7uyrNdyEIlnTxNHBhxhFIV%2Bs1dowCs0RkyQQXR%2FRywDOUkmrQZtbHT7O2%2BG81SZZatO6qn%2FeWyiO9M8c6S77xWHLQRxPMJAH86Aw5lDGWHYdziiLKE1%2FKMp0i5FlL8IKGE6dMk7PfDIJd8r9venUACZZb5iO%2FBoMAIKe7Q7NY7x%2FHiMcDD9%2FcDVnTGuFheZEHd0q8277X9pUa%2BI6Duqchf1ItYiaN1wXUbGtPmfaiUCxH2ZOZBeCNtCjlHiyJr%2FA4vY9%2BPXUBMikRCA5ndZwNM30hS231c9LqXajTFc6EYKdzRMejhVQsWVH8rg2wlcHeScz1lVrwvopUe%2BkNLetfVFk9SEzjmkzhe3OdIpD7yaxOsZB0HC%2Bc0WLBueFBFMpeJRJvPKILeLLuhB3sdsA%2F1Bc3KABWvTuTMll2oUiJOH0O22Z65zT4HGKjPoyx%2FtHl3Yh%2BF7sxmV2I6igRA3zgpz%2FRSXraPD2PPsMavM5RAUcYitBBkAT5s7uZZvh8tnwgk10jIZ3jLQUr1mkdIKgDyHnx26sQ1PzZojEsrnBXHOKpEhPKTivAHWbfKKMbGIRs2Cg1hTDQ8uvVBjqkAa99tXPnEvoGWh4IXImjfGT%2FP3NJRaWgUt9ELPrD9Ypj4fmx5wtmkC22ZNB3Ru2xMk%2Fppvxua2J8sa3fmiDon%2FbkoXGnDPonevyW16Y7jlyfAAHy3%2BVI3bZaVVUjhTK%2FeP2Ru9M59zbrgPGKZau9k4%2FslWpT17rVPqAdjm5bRPIkClXiVtjYuPapTLa8kpgmgBdYzNBJt%2FnsTz8%2FOGgxBwZSPlWO&X-Amz-Signature=4133e1c479dc38a124c8a6ee401feba365ba9f145fd30cd41311afaaa6bbb33c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
