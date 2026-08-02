---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCSYGYVL%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T164454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCICZ3Lk20I6g%2FAawiwuasFLmC%2Fcbv58sZpxSj76e4RN5ZAiEA%2BO%2BNYJDFrJEQluTThfwMrfPUl8GCKhgikRHE6LbDoWcqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO2bv9BfiRyeiNKVWircA1bdaHyfHodJoK6tFfl4L%2BXLzQuvSn2EstqZI4Ytr0NzA3IP4Zdw7H6Yb2v6ksmY%2BQRF%2BCDw97q4i1X%2B0STWvgmLf3J9N4CAQJwaVALvvimEXMmoAwcG43dqMWJSyHsuIfHaVHYefu%2FS9VbgfI6LjavcvvNw%2FL5T4LIINiolUUkX8ySGlvODOABarf1Tli9jYCAmWr22ByDMlL39ydHvPVpu4pz0RBRwCcFsU0h6Rnk6%2BUTPlL%2FmL6YbV4TQCTy56QLHhlpV1weRzNrCeWI912hl9tUi75UxrNfvvKKEF6YnqqS0UKL6oLQrxOFf60kDN%2FOCtotTTsQ4hGtc%2Frg65sbVB%2FcoeSE95W2hGK6f1mirVexVnioEPrwXa7FbZ57R4MweNN4Y7JvDTY3z9TNTD0iscF76xAzibgXoJJlyQUDeD6po0pQAu3pBH%2BnRBVLOSK1ymQKyStvOPdE0zWkC0Rigcua3KxG9jR5D2G%2BDXa%2FDhxvoQdNcxhJINLw4WzN75%2BVlSjZhtMfcXkndLWRScGWuR7Osc4lrFCpPiMsbZGS4wLDx4Rs%2B0IzKZPgBCHfSJxwPfIvkhtMy8%2FFmhDKYkUY%2FiQ6I2JdG9Fub9j50xowO3Hdms57LO9RDkGWzMOPfvdMGOqUB%2BFHPgrWcEAfqOaRGMfUNLIj9%2B%2F7ZGQrnSxE08ZFSK%2BmFC1PP6Lj17Arl2zhca9PPhnpnnzwfdEcpEyhZkz7sSz3mbnBqXXibOPAJz7t3dEjLhKECLIRuCmaNpnZXu3RfBy3BO%2F9GqGbhOvFXlffKMt7TThSFqFm5M4iJr2DK9zRCb%2F%2BviIQaR8uX4DnwbH9xNAXr4%2Fxk%2BeF5QFNSCVUVhOFjvQgv&X-Amz-Signature=ad241a08e47484549a9caf04f0bbb7d3ff0e3ef10167dd548a51369d9b902530&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
