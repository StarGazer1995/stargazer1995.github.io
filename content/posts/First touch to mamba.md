---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPGZXXMQ%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T172001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCPrqrQMRsig3%2Fl9EY43aH1M0KrUrhEuhwzbS0V33BkoQIgdJeAHcJOKT6eOdBrvmvuEd%2BQe1eddLthV3%2Bgn45Q00sq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDB%2FwO5xbGMi%2FL7Fi2SrcA%2BRc%2FEGbYxXMsy67bxEvP0fxN42KKG1AE8ACGQ9HsjT%2BQMm8e%2FFrQs%2B0IMJH%2B5tbnmuUvSuxvtz%2B2NRvNct3xGYCkbfD9bB2ZxkThWzYSe62w5m7cpWmyMQ08V7ce1SlOccjMKyLwCY1FR7haA4kSVAB2BIWd2%2BpxQ0OkuDcJ7nTc7TmOTqS2U5xEjAnGwXdddQBLlupFqCCVHPhT8jU3mTXSzGQK3ucBh2NSTBRSa52kBiIBMELKYFPv69JJuC11uVUhPyqk2lEU%2BYXTXO2GCFSJrRXTbhmHbCthfkC1kkhVUfDd5Sf%2FhdbqQeYm%2FOewGmgqpiEQtYqhfutY8SCCmaK2mjIE%2Fuo84e8%2FZ6ALgjtJU%2F0lyl8D0g6GtNwN1rza%2FXtUdp%2BPGhFZNIf%2Bgt9mrxfLCwBXmW7BZ133WkEFiN2d2qA7LuFatL6sH0T04tYW1%2BRbqqCnpA6lTj49aKUdfXMbyPCx82ImG2yrbmMLyBxAKWhGbkuKUz08aXQCJ%2BfAHvO%2FgzMnewV6I%2F0g6osZTyoP%2FmDRcuNNrwbA9jJQBvAIFTPuNY2DRcoBAwNN1E0R9FtRbc1MGSXMWZPGg1tn3uHTaFCKjfftgbeRA68O%2FZ5x%2B3aW4Z2JsNL8si4MNStjtMGOqUBuUJ%2FoVlvrxehVnCqy%2B1G5og99Eex6HK%2BpYrX1jDbh%2BYg0gICKurdXo2T%2BHNH1G0ppDflUDs9VjGXZwWaOPCUL6V4i48v%2FPU6iYKErCSwkUlDQyjubuSDm11TOiasQp4V6szh9HkPt1rk3zTLQJ%2FA273gtMAZ3FGE%2FsnV70EB60b3CT0idpSS%2Bd9z53PP8okRQGdRg9fVgpSQgtqOrEBzQPndaDgv&X-Amz-Signature=62a823896504807c33d8c85f314053739904f764f5fa815770d5e689962698c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
