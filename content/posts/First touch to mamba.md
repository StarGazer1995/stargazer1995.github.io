---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LPIYIPS%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T184422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDeODNvMg1Bve5LqO6eSBy2URe8oidjHo%2FlvMCUPiBADAIgU%2FCKF8tvuiONyQMUb4Vy7gLNS1yxLY8A3TjCLLUxU54q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDClVePO7EcwYkXggrSrcAwdGF835lY2fSNIx4rRbMg1kSpGJ%2FNLDYPMcbj%2FNxU00rvHUOJPvfgWt%2BxsQSMR1RHXUUc%2BODcZJ96l0%2FYViH7zVhHkbKPOcriogXrYCqj6kk3CgLRO%2FcEL3ROCwH9rXhC7XKslWDYoeYjrOkkWnN1obyMIy6NwoV8mXN6aAPeab4%2FDsbTIlPrdeJFhvEhnk87BglT32Jrna%2FrXgIsOqrNe1KcxAmXIsxQAEkn9h5i4M7UFL0LzmIjFPdOK5q8e8m%2FPmudIJGY8GbYEnyDF49vm4EB97eNwmZsLBr4mRtPKewtgznDbrDb5m1U7JL6o26Dn4XofJUk%2F9pzQa112%2BUE9ZOvAlwVw3MUfSMTOgQgNnfbt56ZzBT3sEl9U6202e4NV6KFy%2BeCYpSYyLGEmrN5cMfDE6H5nw3swz3dDSzYrWcJpj4EF1wakZx5AsTTqG9nHPgKHCiGzbTzaVmPWLLP36Qpg%2BPh9cGWbVXGbO991d4v73f%2FcCu7QCEmUHbJfkPBs6lVFpVCmrZXerZ5cydt5nUE5%2FhyYFHMn%2FoU%2FKoLOqssqZAb4JkxZFmYhnWQEUSja5enM9Zbno6RX6b%2BJTk8%2B3GtsXVveJRa4YT7QNrLriTECFSTlaFxAbTjffMJWP79IGOqUBjNV9bA0CNG06D%2BdWdz0ReW3nEfjXiNqyEKyVC31F3kA8xU25%2FAzQk8aoMctYPK9BsseyeLnCfqEb4dpFWNu115z0JNcryEXtQCGzoSv1w4Fvz7kZBEtH3nlb6fqE6dasfHAJ5RTcL8joAoKi9x5Rp6uBsCfLpMWKrbAoEgLFBJe4C53yAxRbe1GYe4tMcPblM%2BqG6CU%2Bl0CMncGvt3UIeRtRAjR7&X-Amz-Signature=0bccbd098d513789b233b96847f1457aaaaee369ba8ea49f99b47bf5dd9a8771&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
