---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PQE5OS3%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T054335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAdJ7o3KCnhR1kLdM1eL4zDjQCIpLXR5vQYnD9Etvg9cAiEAzr6bxW%2B8vUnvBc712JUgqmi%2ByX5U%2BpJGVEiJW2KeWboq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDDvl%2BldR9kayRQFYNSrcA9CAF06O%2FZB1utY%2Fb%2B%2FraYV78gw8CHDLFXZYZsvBEjsgmW4c%2Bb4Z1vylXHNCqm95xBYnsrL5LExJzud%2BiSxHh7%2BvIskGQYKp6ocjUr8eG7%2FPbsy3XmKfChW%2B633fwAlUNEwCvFRLziCoBQYrp%2F%2FbSS3joWUwsTMf6ZjPy3oO25pPCvMKBV%2BqXsxPVJglqSa2dDkwNT2bBcWdkj6N7S9I2hDg8r2kkQNyVmGMGoAP730ZsNPJKqVIiis9OsUFFuG6qG7h6gZT8Vy%2FQQdcR2cS3O%2FgnOCD5vOe1P6uVCsv44yd8WqyzxPxn3F6bx79ONFJtBrTmkRK1wT5DNlS0TY4ZS9IPbDS%2Fao27vnJnC0MIcmF9zJSUliGNaws6XT2%2FvFfceXX2kDlyopElCGrvfbbVMVlg4PYSrJIjVlWgD38%2FPtI4RusCcnoHfBgaU51ZAmTsycRh9dQ3sPU9PNH4xlTJ4y6Y4gfC%2Bt%2BmCu3VU3OAUnbv%2FqNsTdh0eD52hfOPJLA369m1JhzJEfyFbbDJ%2ByS5J%2BlChrjaL3j2r45MOGSiYWQKU1IPqv1P3u4KecvstDvoPq6pZkfrbRcU9%2Fcei0fO%2BQKNXHFVi2Ob%2F11aLG24UCBi1RZ5jfnGSaopjKkMM6rldAGOqUBPSYyNwB%2FQwXgbnQUipifZia%2BvgFtppSsE7VglUQmVchGYNDQBDRzC%2F3DuY%2F7bzFSHtSjkce5Y%2FagUIjBZaF2UGG18pgDLlwK39RN05Ytx9Ayk0y3iSiR8zh4wO0seCMbYtewmN25JvgNxiNtCoMHRcIzd7hFO9IlpCIxjkKeddWJfVj0bbwEwh952m8f%2FptbWzd5OJFIlzgMCPjt6Ei1xgj8kgR%2F&X-Amz-Signature=59a8d95ccd8fa2e56460cebeb872540484a3b06130b10f76115ef3a41589ebf6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
