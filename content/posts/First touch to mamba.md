---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YDOT7D7%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T102105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2Fil8GT9huEXJOeRWNrPCxR5LX0KrjW947HNv3gNmAhAiAX1gcjBoNgE6VbFhiYRxsYG%2BMYDOr0tq6Mh96BP%2BFubyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLzorotbT1QX7dyuxKtwDKZXJcY14w102mah64tD7khZtAKge2rt8Ig%2FPOcV4nYGez%2BfB%2FvOZTxLzgM8NbKS%2FM%2FYuRB8oyySNdSbEiB9nkeZt8IDe576nOCzosWH%2FHqukYB%2BF2vtGh4hrGuEx38eabnBLrOmZ4xLt4bGNoRUv8aTzUpJP7eVXQYCMp7GUAIyapLo30YnB%2FSEhFJREGC9HempyqUAxSrNf6272upPR3lZdFs2hpqzTDc7h7y0RMdHVgsgzl3d%2BkRQgkXl7j55MjM8cM%2BMNrVyYfQHT2BGQ2vekXsY5C8IzqJWQwP8Cw65Y2FItQEElGLedNaG8euSml34r4XMIOy%2F%2FZSFIF8xjLFS1dKeD4YY07SisgcQHuIVnY6YHjKhB9trr4rRBwRmahvd3%2FXSQ5zMJPi%2B2mB6iNkiMRX6dY4M%2BaDhn9wj%2F7bMvM9WqSkhpf3mXaZBIPGykaiyWu0rh5BVWUZ8Wo%2BPZoPyrSeedvri6A5WeakcM5fDAh1pRRwI67zaCtiwRx7Y8yB0f7AVrS1Vm7j56Fby%2FNqZ%2BDJ1uU9cBDZbB0Hs5YA5znaudyNl3nD5XT6LBULfDLBot5fqq8XxtIqP6F5AuojH7ZMCAAdxfSsmOgAf7mcKlYKbMdn8QtSD9%2BpswofqU0QY6pgEEk%2FNjBvJqvPGhYCq1KFv5StnRPUSMJeU0TQD7NPMRCabxiIb40O8fEP%2FDAjL8pY%2BQi3Z9pAhHa%2BJ2owKStZ%2FKpTqAY8%2FAFoAwyLD%2BvpEvMs9%2FkEwpuoJ47fXoe8%2B48M9jQa1nHh1XpbO9vC7JQ5oNHM2965K7GoCdPy3JzanhPsGA8TYhtvHUx77iHbNyhvuPXLOV%2F%2B9Tj8WMuAp%2FWxA6hlqFSjTH&X-Amz-Signature=baa974eaeda6a56e7ed4bebc663964fe08c46376f9331a877797291012d15c70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
