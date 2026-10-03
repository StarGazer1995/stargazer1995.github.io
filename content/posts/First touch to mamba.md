---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVOXRLNN%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T004909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZamuiq82v1%2F8W6f%2FGUkKE%2BApQojKbxHWpZPq%2BgmTe6QIhAJVfKQ5fdGu%2Fyb7JAT8r9z%2BkP1BYnbkNGoipdvX2RySSKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwkuf34p1n%2FOBcS9NEq3AP4%2FcCkJ5ktsdGZ2qUBQPxM%2FB8GZuCKuJ%2FY303sDuUyGo1DSr8KmJwOYAsnDsgILfPDn%2BZwvbzpe122I5IyFW0%2Bsr85NBoXPh15PtIOXrCoJvsffwPTkzQpvvXaDQLRAbYeikeRp16hEBi8VkUlKY5WNbbRrl9Jge0FVq4agv2GE6KpIe0tnvOsX9U2ABoozh90NliIQKq0NVwWTFFNmYj%2BcJ0qxkx49LD1U%2BwCNjRrd%2FcnmO4qZOa29d2QZCKyhdmN5gUP2lapFzaRAIVfhaeUFO4EDrzM4RP3%2B4Fyz94gr7rkflEguoLuoDhr0J0%2BVEWnpmKm0OGqp6GukMxP%2F9pZ0nFCDbj4o9BUpxRts3Tf5to82bimyfS%2Bli5i1e%2BcGSezsLmvoJaWLs5wkc7D3D%2BiPMJCTRiGE8aGdMpOijKOwCyrcbUKwk3%2Ff93AF%2BkmnSaI30fRWUdY679Ot9ECiT221mXs17Lx%2FJkfjsQS67TTJCR6w8GFKyMv%2F3422r3paXuV%2BFKajfRpaFODPZaYpFEeQI5xl8zPB6PfUDUjO%2FiTbUVMfgfEBhb1pzlgeWr21ugbkPgauHVhrD2rPW7fgtEfwBIconRsVc2rm4qbfjO%2BShOITC7FMmFfYq%2BT2jCY3IDWBjqkAWA9ZLJLzXUohB9Nuc%2FxyHL7hF2O4bjCCyomgd8tjwLqUIdTSySTA%2BAORdeOWw3UutAqVgbZEQ2b6NA2u84E7aVjfEeE4fXMKtOu08UK%2FreeYK2J%2FzKlE0sHHBjEwhmrSdcdb2plFnO63venrfDCKsyaz3IvfZDvCJF%2FBFh7K7N29PoLTBSdp77PTfCRhJoZMGcwi5L0z7AGR%2FJAufGGsoyp5CdI&X-Amz-Signature=442d44caf40bebb06652a1719e9204db0305e903d7b39037eb72a4ad1e979c1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
