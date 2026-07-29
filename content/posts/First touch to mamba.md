---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USM5MZEX%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T224651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGvGmL9yGT6vCg27LQqzn8lLF%2BG6NeJPSETfVztzzKhAiEA8n3eIkXxDKcU6MULIBn5t1V6NjqrtyI3dfDje2x9%2BEYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAEgUZjpxUMLQb6tDSrcA7jb0TWUhuXi89KINmOgLkXmQA78NYbB%2FFuGkVQuyOTugudlAmCu%2FGWDDD6%2FhRg5S7ZYfI6yIqJYAKesBhXYkSUujK6YcRFPKy3jP0zJTzs1xEcVyt4m%2F6oOGdVIb0F4GIR5fOZIeiHBbGAZbRCvfODVcVwJwgynr153rJzGcVBglJ1dfmo0CwBmX%2BmmEhw2FBQwiT%2FeGlDMmRunxgicNYZD3HgzHLLhSP0oKEi2XzFLNt%2FgIIQIN28l1BvI7%2FbNi70e%2BoPvr1fsO1A0LQrcFjbIweOyw3lMZNy5eaZWRAS3OYonaamqRZeUuhJGTWwaLDNs7C7OZt8T513OnFhHnLIyiGWKgrDfg%2FWYepAOT3ztPA2BawuT4BaRsRckxqckR4yfPhreweU1I9j2rmpiXHfO6%2BDDVQaKbdoAfBavJz1GkGgwcufR8%2Fphd%2BYor2AjRuGvM%2FlcGbvBBRLqHrAFGCY7gMkgvzjOixvHxdMpw%2Bsg1VQMB0zZHeyD8yTyYIU7yXIH2wcAleVlL2dvHExCZMqR4on0dCDRqYY4Wne%2BYiEYPMVjW6aZcA6LsloCOs12%2B7p%2FphnUzbK6XQi2u1%2FNKwS3z3sockKwcRcjhQ46MhqNq%2F1su2rBleXebPy6MNP7qdMGOqUBJNVpCufXFv4YvhfHwRfdDxyzKYMmrjs7cPFddJ6r3Qwtvp9dH806zlOw4W509fxSaZQEIqoXemQ0mGdYEYcIqPVcT%2Ff0mREnAaNqGnNa3mNXtBxjRX9Xcy7Nv0hBKRMptoV%2BlcPUH7NDBDPPNCNBxKGW2rOLpo7CYB779u0D5dTKIci0p1%2B3Goo9HTbhDk77WVVNidicBLJap4jhLexf52J7nw0y&X-Amz-Signature=514aa901e9ae1eb6e465272721ea09e20f5826f6f248e8944d1a86b25c28d7f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
