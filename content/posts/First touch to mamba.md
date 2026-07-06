---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL3JNUVW%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T225557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEVbR7Z9sFCm3nLm3TiU9TLUVmr48GoHSU4ija%2FTHPKAIgDhbXWWAue6WDhls3QSHYzUNFaRYd23%2BWB8%2Fi2p9zvrQq%2FwMIXhAAGgw2Mzc0MjMxODM4MDUiDBCaLYVWfNSTyy7qgSrcAxsfv6nu503Rvi2uK55VTG26HxIArZ1OIkQ9PTbceyEf4tKep%2BXdpQZDAgXr83nE%2BSPuniO0srBwTSWbdYmuRge7C7rT%2BpEBqdPLH00SZTouq5IyhPP%2BOp13dMeLo3aTEIlFbkKTkiyK9UFnvINkgra8%2BNSAZKE568lde71h8aM443BPbW9IzxjxRlmE%2Bpr27kvgMClVUZsELp%2Be7fXg9Zy42kdG0%2FtX6FVeQdrDrMJZlX6E1jv0iTfiNLFF2WG349dA5W2jszbW%2BCo5HCggFLRtYJOTHdq0az4bfK5rRtd6rgrCA4pAxix4eUo2a6u0Xn0yMiqTGIo1NSl043B0JwMgWwfjUHyqc6kUWzYYeZXzD5qCeTjZmkm1LtYFYMhVMclsWei7CCwRG%2FWkHacQGlPuPARX2rJOG5gT8knOKfpgjYsBikige3j9WEmYfEthJvp9W9lv%2FRDtemRViIe8bqnJHvi61iqbqKokpqimsAqGuWBFHV4r6yyjubxGhPxBse1INx8D4Fz60dNizGpFLWyldB913Se6uQctB9vcfYpWX24qQ3PQWcFUGR6yK4VzKFh%2BUHQ%2FdQEeFal3yRQr0ffGSV6jemCoMONU8JXS6lUuvrOI92aSJXG1NCSbMJiwsNIGOqUBg0%2FwuBPc%2B4jjqZVNsKOM%2Bc8%2Fwm%2BelooP81jtkKbpU6eW8%2FliOM1lHWouQYZGL0OjGUjtmzutcRJ5j9KhgpWZCQdbZrJYBFEelMYQ%2FnSpk%2BT6b26M4tfWTjcvfpK1W8d1wbQ5u2YWE66X6HgqJ3BM9%2FLPo8coIcTT1opxPPK89zo598%2BxhhYTz44kcx0fO4fMdnA9BJ5b1rlddHn6p4y2L%2Fc5tRoX&X-Amz-Signature=dbd6fc06180a48fd43806bbdbbce075dcf5603ff406a9fdb011223a324de7735&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
