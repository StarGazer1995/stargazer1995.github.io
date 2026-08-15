---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466476QGXGH%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T161107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIAjFbcs2flL7uUvYMF3FgUmnofR0CrJbCexTIzj4dRKnAiEA8Y5rXft1BZx%2FdyxP%2FQIddJn7RNVKwXywui4rLkY92u0q%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDKvcf07DMqg5svJLxCrcA9eAbyB6T0cKD%2FW6uu6UuAnMHZNZ3g15YApOTDXE3JoYu32MheeHkX%2Bqp3FzoV5%2Fzr3jiy8Zt84iTssvXuyDwb9XRmPvxrJdhaX8VkqzdGWB%2B10m4hJFHfDVgnW0UxTpxFmhPZ7bqeV9%2Bu%2Ff8zffwcSMoZOW4x%2FpT352lTE4HSYuoJHky2srUvXR9uJ%2BSaVM5Y5T4fFgKF%2FeiQ31afTZ312MlOsSbPji2MhUxiCWSavpr7sr9IoXj0nkPPI3eLi%2B%2BYPhmTLbSrGDh1QStIKbviKW6TxMts5TtHsKo0dy%2Fj5%2FMSCTJhNr%2FXZEhYpE0c97vo8vNhOzpu%2B1GJxOKkKL7LTKFNwz7kGXogo%2BNAoxr%2FzEbmpR6ZzQGHh3TO8CIIAJ7ASTFdf29ECWUZ08ThlZxtaGjRGfBnLUNeuQAZEkmQEIdjA1UJ6fzNhgCdwhOnuXOgoldSY7mXeOYB63qaUaitZ33U6%2FmEHTLBGURf45RC4FV16efC8swHWjRY2g6QpneaTYmTC5bECK42ARX9XNW5cKFA1%2B2GAjPqcobjyDIIrh4PLMCV0BcvN1VZV03CJlxdK3LcZXyqTTcmTqI5MNX5OpAZ%2B0Ed%2BYCIeHXYDWBqXasB8859iHat12UrpKMLqdgdQGOqUBnISrVTsmgGoDDkgcTof4JgMw8Zoj0KUmnQMawt8TWxerg1mtN136ZESzPFYjJq09hI6s%2B87nnJsbZmSKYcpTNw0b0CGlNxAyEQFOMVjWsFfZjQSi0Cvu3PAEIRIlzUbT3LjqUBiuMrc3R4xTCXZwBZMnkogrPBqy3nL8mtyD1OkjWRr%2FiPc03Xjmn8B3gTtNoifX32qk8JmR3Z%2BJCLQMzrZJJWw9&X-Amz-Signature=502f00ade80af3255fd3ecd052b04edfa3cf0fb565756cddd512e9f5ace80b58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
