---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MWYMNQH%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T203721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjiH7n%2BRURy4K4phVRDxmsqc7RP3N0ngs2jUey1C%2BLvwIgcEO0yD62cA0qOgiiqiaRbJ%2Fu4NJEm44siBbH0kWMaEgqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGz9rzno9%2FuKF6XGryrcA4y7P2oOmrdTJIR4VpnRTMFvtKd7Z8B3R8%2FtJ%2B%2BGItk4e4HDfwsQSv0uDLSFrUrbbHFinNTqnTbWBGVBFyGtf0qA7LajKNpxRR6X2b06y5MkNEd%2FOwBkV436g6cfB3JJ13WKlaBagJjDvaYeSqAmBdO2PGzre9bc6N1aXF9Nvnmk4RJqvzjaGcuwlwiFzbQ7HKIdXI%2F8GlRRyJ6Q8I5NGcx8W8UpdGojY6wF7AO6z2osDQvqyVqj9evsyN4asEyIeNDu0deuQJ68FtEEBmj0kbQ%2BToQwK1yyXCY%2Fycygxliyjs7%2BaFVTe3yTLN5W4y5roL3uCx12PXsWIg15bweMOW8aRPSB2cWFz8eJq0mqk%2Flxm6LKvroHbA5MAOx9Y0PT8TQmPBeBJ5aAF3iu%2F%2FbO4IvnEixPAaurpVCLmkp05%2Bor8QOctRVygx632Fcrt2Dej%2Ff%2FLJjy88N%2FniC5DceyCDhv8UulfkU5f%2BES6wkEDjF6IrBHdmA4ISPWXOrsaTyok1S%2BTpv1TOaj4gumiDdv7ohkZbA3pYwsrdXNRcDAbyoo5x2BaGI5d24YBEr6gU0Jk%2BiW0Y7Pu0%2FVc1ZJnAs93tLENMLwunSw3wj0IifTop6JS1DjRXxnteIj15KkMPjC9NIGOqUBSLKFbiWjgGLrtr5EendQbmgrtuHup4vlru1rUuHnEkD%2Fh9r8B%2B224oY4XEVgDxbn2g982ex1q%2FceogaS5SJjk5fAmEeZtN%2BEVWWDvewwEa%2FlmmCF5zLAevFlu9RO87PnsqjXyZwzWJCW6kgeNWpVGUmR4PHtNmvGCrzWKFYTqiq06PvjdrF2ENN4uxlka57cTJNPgcxunhjNEf9tFMcVgm%2Bq7GQS&X-Amz-Signature=a606b4d92e3cea22e714bd8c189acb3cdef9ed733218dc3b0173053864cd13ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
