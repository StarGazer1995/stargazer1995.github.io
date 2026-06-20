---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZE6AZ4X%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIBi6IFMb0hawl31K3gU%2FWpRzPGy33vk2EI%2B9ubrAksH2AiBx8C31eULW6qv0JAckXvqc8XS4ASrstT%2B4NoLeiADxuCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX9ujaSzbtjyz3NKFKtwDqraOmMA9vJD9LlTKwkL%2BdOSA8%2FgfqxlH0ihjo88LCO4c%2FMcfZuW6TvXOyghiLb2S3ki8qHXOixfPDd3j6BIzRBRqua09f73w4sAlVDeS0bIV%2FY5CKjFu%2BDvZggMW6XnrtD1m1k3ecZjLkpEabJr66m%2B79hwK2HMmNyntGLR4jYkwYofHMSy44JDFQkpinayE%2BuUzOuR9UV4ql918hifMj6RBaVizP69%2F49I42YyydoTGNccjEiDBAeVM3mGR9A2P7b5rCK%2Bvvox%2Fl%2BR6Tccm4iYIlN6EPjBV42HZk4gbqR88vZEZDTxkSUXrkpbliS9oAEqcvCJkpyQZ%2BZAuUCLbM27zUBb%2FBmfH6DDET6lD6vRA6ZUdskZ%2F%2FmT5C0%2BMizmtxp8HhnoR0lX27xg1Y%2Fi7mo6%2F2G82Hs6V7IFcgVN1MJFuBedeGspXu5gk0bMKBoSJmD5vbsB08YNuzb17QodflXS1fvRiMjML7D2KvuYrjGzm%2F%2F7w%2B8Zi7FCVS31gAuG5Qrjw6e%2BjSZDqPMr1Tq4RsGFo21DlQwPNLzNN0SlejawZf9gQQC0oVaXsrx2tB0v%2F%2FfrkUjvr6GfgSOs%2F98hTA1%2Fpoqw%2BitD8uFB%2F3OUbV8tFZOcUEOZK151JinowpOnZ0QY6pgEFrU%2BGZqBqGxEkSYRTSyzRSIKHPh2sP1cR%2FUOBvAG9BFYOxWdJRgIBFVZSwB3il6antKNYvodjjAYXR%2BtnHpfrVCKDYItlb2Kbd%2B7wYwDGUyJY3It9h95vlobqWEIhwmhmayhY8VYg8oc2c56CavvfxBbSEOt5ZyTmE5XvXLybUZegssQLb%2BcHTKMbgc0AKcCmE9bYXbteFcTiYzd14XhWSl5NYwMX&X-Amz-Signature=52803c321145b3e1c233f5261225ab046cac06ce1c29fb78bd8733e4445151b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
