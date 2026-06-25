---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLDAMKO2%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T073316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCvMf6KDcfvAEDSrAYLZcH%2FQLN75IccjO%2BV68JeYmWfoAIgAfWvPJ2xqJGW%2F0GFse348SX%2BHwaWMKF%2BQlyTVyyCZMIq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDBRZZzEsv0OjbwsMpircA3aOKbX5Bov9iwk2LbcK9e2E6hsP%2FC4UIo%2BLEdvK1iK%2BXi3fhJ5WZldvB08tN%2F82GR5TAUbpY5aUCTok0oKgQYztafQ14ddRNTYnlvMmqrLLM3rl5gHRICe%2BK6TOmdsoo91VJ599H83LtnUIDfn5NKT9RbR3%2B%2Bl8VN7ei7KroGrSbFvIjsnI%2Byky2gal7AlB%2F3PxU%2Fw%2B7VfVzcWZUZl6saCjzZ1PdTSY79N9h82vU1CmcyoEnwlOJUIj8g1Z2gFifVTpGKflz731sUhqrcolecZP26q%2F1JvRdK%2FRElO%2FczSip3eBdKnvD7Hk7zr93Ciyp9PsmYtBdSN0CPeDiOLE4l3nwrFZ687jaBwN25Jc%2Bnzqh2xWe9gbiNcZBzz8nXueRdSW0b3%2BM5z51sT7PLPC4%2BWIhGX3bij4owhW8wn7OQxSxn91elky43cyccUx7pVInnwuVjGWfpMjDgDSB9YzPgIOXT0vGlvMznzI6sJ0W7q2jTME1SzM5ka9wSXOMlDc6HJ%2BUWLwSnD4%2BGr2vs2hCjWASpunT%2BDIoQ4b6EOXT%2FkJLBKMUBHqRSnD9XMcARrXpSlI1Fnk7ooe%2BcIt9b6cetozzfwHtxjNzdiOyFyQlg4ru9x2ONRPbx%2FU8IdEMOGd89EGOqUB592ApeXdE33xMU2cEHmw3BsrlPN%2Fl%2FlaKG8ZC%2F2Typx6o3pO7yYi%2FYaAN81FuIJtAzThD5AlKAKPiT7c%2FvNSQetxaU6od5hMw%2Fu2WXW2x4ineiW%2BLZSzfa9WbCNMRDJyULnrZYDDM4tpBBzrwcy4PZAWI19vvk0aZr970BDpnnA026exJe5Fg1edN0r4c78SJhFdMwHelBpEf%2BB17C0ZaUIhzYMP&X-Amz-Signature=f6d29b75bc44ce3829a54e32bd8727f6ea915ef833704d9a33475db1db044d9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
