---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJYOWMR%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T075635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCM3MmDKUYbUV5YOk87r4oVHXPbjy47G7%2BYG7ty3DBpBwIhANPxzJJMwjP3vpCaXrrw%2BmZmEtDduK3idMT8Aeu7pWUDKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJbHaHHM5knHbUeeQq3ANz0SHOUlX%2Bz5mV4MjJ7k2%2B%2FJ1nTRqXbv398PNi1wdRPg2ysrsCxH%2BjD%2BHEupXar1HjrlENB9AaEyW3f6gxawx4TfV6c%2Bq2c%2FIbdZIX0gnXdOiJMAAbzA24BioKZXnzkphUoip%2FmP1t%2B4cXbmwnWTZPO9HbDAM2BSpQrQkFtjaXMR8Hj%2BbhhxHU0CAqJtT5bx%2BOVShGA%2BXatqTmvWytqrEUfnuRy6iWZTMgvL43B2i2vozgHp%2Fwr6hgGbTeetB6K59FlBJQE4bkphcNhXcw4BrQfCYb0IjmDqV86UV6EBgTx0dOdMaGlceNDDChmm4%2B4BFSNLGaVSa2yo5LSHGgGJaGLpz9NkAKPqckIk1N5CnZmztnHLu1OOqAAGGFldAC2QM7Fl4Zx0UEodiK7zu4nKBzkZ%2F9spnzYqUBLqQiy%2BhXKBSWHqi0Mfq8FWRPdbVATbmdbttfrsiXFH2%2FZ66xoJMyHv6gpZpSw0dAcBBm7V7WKzZE6Q8JoTfTkCJgFQ2MHEvvcbkvidvQR3sfME3J47W%2Bk%2B8VJd9xPTaNKuWJC3HO9YRUSPH93uNSr64jCFH9sCmnqa9YCLG0G9XlTyZH0UE0elXInzxHRjQU62nXxEq52hC296qy25qwaT6ErDCJ6vHSBjqkAfjz43iTV6MYE4O%2FSslI3Vsxuqbwn9F7aOPV%2BIyu0ivXmqW9CeHMVzJtBWUoFdl07FRiHse%2F1mfFYjDLcjLhE4M%2FIYBJODk1CNXZNh4sactScdgzAsRcTKm%2FP01krRO16m96s6gPOYxhe3dZhEOMx%2Fa4Wh7ofp3ExHWmEU1HlTHeMQVeLNclepCzrpgORKxJmgpT%2BOawX3MrIsF%2BSj4d3pmIALFf&X-Amz-Signature=f7936d6d00cd1360dcc13e002348ea956f23a33fbf88a6976ef4c494a77326ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
