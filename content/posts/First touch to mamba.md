---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRWVSA2K%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T200856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQDOXcilAIAj2fn%2Fddq1dotxMwpvnu%2FY2M0DD5DYkrrv4AIhAO2Wno7xyY%2BSmR69Okwwih0cOiHc0W09ycD8CA%2FOMCeeKv8DCAUQABoMNjM3NDIzMTgzODA1IgyhgRTQ0yDeO44KYv8q3AN7US9ZbTlIciaSDGkTUBez3MK9VkQoFoEoZNa7n4unRawX0mGVb4ZMwU6%2FYC9SJ%2BTR71ZHA2mmNd3d8p8z3FxbwaQZabV0yYIw9PotB0N%2BYXwhjd8wYykPU%2B5xwMUT%2Bq4LzHBSO5r7Mvn%2FzoUD%2B8tbNHSIlUci6dhnNZ6d2f3xIkPVL0b6OnSajOsLjtZ531E%2BWMqM%2FGu7ulWp113Vu0oZGldHowVxOB631C9BygxZGhvm8qXpSIkqYasnV5umOJPWzx9mJeD9c64Sod952BhR3LpHoVprAj6Cnn1h3siYZUWKy%2Bt%2FaL5NNmSYbFzXNDgxksqjcum99iLtgu9bM%2Bs3hCsWT5YURcH9zx%2FA%2BeHimd%2FcjAkfEotiDMrioW52mR2R49KOjDk4q2U9lQe69XlOPZwuSjCOCbKmklSIOp9avIF2pg%2FOsakxfhPcPsEwCg8hUSz7oxdFknDTgAb0bFgeBTasDU77T%2FxJaOiKdgtQSyYH5jHfJPyGCayg1v%2BW8mN33AdIlZpgq9W82HNccDon9ufV%2BmagF%2BCq3meCtWC2hsuF%2BKAjftP9EAT4mWwvx8ZIBJn%2F78XCeqKncp6Jir6SyEVsa5M67sU5fRNszQcXHmIcQsy2JaVEwnK9bzCPqqzRBjqkAYCEAvB8ar%2F9O35AaBCvUE4c%2F0xJ9MZ73Yi%2FQRXTMD4%2B9iKY1uBXOzvyqnof0MkcxfTT6EZXHZPBx4L5S6Z00Uf6B2L74MobFZoc9daBzIZVJp%2BPF3MfhOATsFGz1J8WDEjBlJFUVMOU6lUakvY6cSQyf2njlBc7bVmkiaAGJyg6%2FJHJNP03oV9KJoISsJh%2FFjSEnfnNwkw%2BFXLodBjSEti%2B2%2B02&X-Amz-Signature=26a51e9d2f3d1d2ed9400732e62175442c2991253c2d0dbfc0c8fbeda1ac3151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
