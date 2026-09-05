---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ACTDHHT%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T174709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIGI15qKQbMFdm47nENhyb9LBQtwRF1K0Q5SbM3VdlLkJAiB14wNth2PhCignZqWP36ny%2BlZgba4JYLI4ZhoFQE1S6ir%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMzTPoW6rhYrljXW5DKtwDLDiap9x7Nj%2FhmcAFu4%2Bh7k6ghwKEwO%2BHwEt82nMbNrvHC2cg9uOVwGzvgzmpHROEJOSNLG%2BeBhaMpwg74BOeUoN7f33nVpXQlNP9zv4gBO3CjvyX5M8VexEZsIXO%2BpRVeIT1EgyVL4wsQaAAU3IQUelTpRm%2F5iwQQs9jVL9fRLLDNxbWQvN8DWlgRLXoVC010qjdtM5hwztlh1MaJPnQ%2FzAvE83yGzrY%2BuMC5%2BmNzbspZo0hV7bkY%2Bzv8rsacyfybciyS2YrMj3gQv3I%2FQ6VMxHOKVLaFY%2BOXN5%2BLrEHGnNMvPHCY0a4fFup0P%2FcGfD6BoDuypK3ME4%2BB6fVwxgNdWV6dgp3oHtiHi2Gt8dE5dD%2FX5pBz01e1qUHAbzpN08piQlFU21Pa0Ne2%2BipkOBYfz705BcV%2BQoTKKdLIWTnNA04BLpssZYMQAT6mRfjluBa%2Fzr4kvt92BEvBLQ03GYmQgbrTq64jOHolRjg8DJkPqo%2Fes8XT9ni18IK6Ky1yqTQmFD7eY5YjH4ZdtqBVX3qBTMajknsy2OT97%2F2JwQYoGp4XbYRs9W4ouRC9%2Bj1dEgAsCsNm5%2Fp7P7UAAGGzdvcmvoiQdtqSkDWjP%2FaRTgoo79LifyIGPAcVeF%2FpZIwo%2BPw1AY6pgEXGrfq3FHVDnP31aMW8TnNsXw9SMPr2Yk3S64QgT2pw%2B2nSjO4lzEbTklYGJJ9tllenVWmHkkwE7HJGlbjuZ2P7H2jlUKiIxp7oLr%2BqGNoiiSMasidJ%2Bv4mulW8aoN9WPiPnrNF5oq7t8t43Fu%2BK7NpSw%2FPwKtVJk8IzBIWlNS0pIorbkYQM6AF4PlWvODYGwUQdyyHEIIfa8bvnpHwXaFZu2Sjv1E&X-Amz-Signature=bcb11c8b277f2eeed16dcb054404c7ff38c10973b5cd762f97dcc3c8aa5de4b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
