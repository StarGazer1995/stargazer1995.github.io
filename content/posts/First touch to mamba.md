---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXONV33H%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T052349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQC7abkLEcqwZ9rBCfEqvk04dwBpaRLeCez9MbrPUdwHOQIhAMmeK%2B4jZeNNa4fSPi2e7oMNi3Vjz5aeTThP%2B7QjAInTKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyC%2B%2Fjji5mypwBN4hUq3AOoxNB7SjGARMfvgPirj5MSZv%2FmsEg69RlhiwVR7saoK9rNcaddqoFBb0kNk45%2ByDTsUG3JrXZKtMxOgFy5QmQbmCsd0QCdXsHngyg9SWYxfwUoIL0Il5xoGJkoZMrkJ18x5HWdlwpRe9lLKhtwig7tK%2BjTVKlZQrd41zlNsGHwKen3LyTSMDHsHBgthDnJoBlC7cRis4ZSsZpDhH%2FY2FcjjpNGd7cx%2B%2BxwJpb6U3d%2BCNVUo0Y7lGUs0ERUoOkjPMkQ%2B7DVVE89ZbRK99wDn%2BIYB3c7Hv72gCmYg2OX5kjMoIgdGHa2zsciP5wtswNNVvY4qSkK9W8qtmGKZpSx1KYAeI310LhbzwGxcQ4cHog%2FMfY1%2FTQagM0XD109dFrKM7beBZqvd5WgGSMNHozfOd4HGDEc95nLoB3ZOo1DeJR0vPyuEjUlxWoBITOiRzjfxbya7H%2Bg8MpHtEH3XAH4%2BdaX5uTltcHHB6FICmJMcBEOU4A7Ep%2BAJAEIFJvBN0OFn2tmDhk1qGwfYC7ctOBYhSBzKP76kPm%2FbhdDM9D6KLLGdTfZmbYSvZojKWk6Zwqu%2BfXCmvT07UKrjQdXyYF7D3WZARWJUihS%2BP7pF4pLdZaDKoTB2tyPWacw3QaJOzD%2ButHSBjqkAWzPugeJiw13eIgul3jj5aKsxkbWpHmxq6QWR0irJxuzt7COQ%2BiRM%2BNQuZ1seAWQFKQF8nQpcLXZPYNXbDMARLgCVO8ogCZPVU6HI%2B1G1GvAXIr5R33eOKjdor9WfhkEFtz%2BlQMeQg0W%2BTq2hH%2Bf8dTWLoPG8%2FQhS%2BYwH%2BePJ8kdXcpdweANmaju0RJorqyHbd2e74%2FmMe25svXwFIfKK2Lo4NR6&X-Amz-Signature=1fe86ae22c99db84e38acb1b464abdb7e786de6bac0dd30d40ec6007c0772757&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
