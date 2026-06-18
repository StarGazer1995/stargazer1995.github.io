---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7SLBXOC%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T232840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2Bp2M%2BFOLj8ljmqoY2msd3T7jp%2BauSdoph%2BB1qqI%2F%2BeAiAIO1Y0v75EedtZ3iD4cebV0ryjsQ7Uq5Tr5S4nDtdIcCqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvXYLorOumy5E4hH5KtwDRkLC3faVRozv3IEErfmcHtaxwS51u%2B5a9ASUYZlF2ZH5SgsWt4KLFeXjkpVvYHOEld44fbLBPp%2FXUSbJ1QwJl9M0mfLB7%2FvLNuuayKhgzsXD0icW0qn8TTR%2FuXifgSQw%2F2KDA6wrpRdgkHqqRUNrF4qVPXxobKCV5XU1iv7fo%2BfpV%2BQj5gQ39F3g5%2B%2FKP%2BNGW0C%2Fnv7lAoHNZSCAri3pjr32xjPTLmPIrl0z0cJG%2F8UIgxd7ATm4xxSemMR9XwH5epmmsinuItvBmfABwu%2BlXQfH4N2ylR%2FPQSYSR121R842v0McpRQBUBAXtigXczMZowZIsBYZTmLBWbHwOY3gWLHCcuL5In58j6W%2BIdvIpyYSaK2IRL32U2RDe8yC0EB%2B%2FCPYbQfENENhDTejbPkI5xyyniGS8W3iv8%2Br9KRoEbYe7e4KmfwZCErAxelQSRmk8acLQinlRoKHSDjdpkaZbbyHBonRtjREr2LGs8524sVrXc%2BekHQHa8yynRSL6xlJiZsv73hB9y71%2F1OJFzpNTg4I2jOWdcU%2B2X1Q%2Bj3puurubkSjqA2haUfmq3CpH8nI5XoXmBBFyXInaBH5l1lw3u1jRZFcu%2FEr0626Ek7MfkfoK%2BNMtqta9YBSd58wmtrR0QY6pgEjTjhIlFYsR2Jsq6XJIbT1Mn%2BPbEoupjNKYmKFBbqmybZxexuldqvGLx5cLy4PyAjktT6%2F4944kTWXW5y%2FZICkhmWuRJvJ6e3RUv9YXnBMyx6%2FabZzEuFysiMgR8JF%2Fz8OJOtLyVmve%2BXU%2F%2BXldaas4dquQHjwupjU30um%2F2lg0fSESLrqv4Wa9vZaUY70BJ57O6KVlowzq0MSQ78u%2B6AYXMll9GJ1&X-Amz-Signature=ef10c03273a8f7df68d0bcfd2802a7dd55ef17be1cf16e604d39fc79f6044c46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
