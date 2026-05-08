---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHE3RRST%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T044823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEyDskq5vsblYpOCDBUDzyXH692ur%2FMVqsMgWDqvVNGyAiEAp7VYhTzWu09r17XvlxN2g7zHTWoc6bV1dZgQUwMWlcgqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIahJfIEQToUz8NqpSrcA1kYUvoTN3w2gqotlk2BschVTeXHldEXzHTKcr8AA%2FwFDTqmHeHxT8ZCGNg6IE66bB%2FQN9lNMITshYjUg8AfY7OAzlah2fNAjQhISyCKHt1T3KHNwj60mGpy5dMedrOqeP%2B7bUOekjLipuMPL5AdNGyzsuJIR6%2F5Lbboc9zQFvYrTLgBospo8Uv7kiGcWlYJSuNFrSR7Pekogv824Vf6bNoiocFLvGBXCkAnj9S8UcXFVK9pfPlC7OXY%2BZNXqEXJ7GUauYFyhMwIhrWA8RdPWVPQtKEWUdO%2FqelPO5m8o8Xu5Jr0B3MiPxc3sBiVVh0U0Eu9Ru7Ld4uu1TWxz51bmOZ0LXJ%2BGFlV5F%2FEyanhw64Lny9JMhDsbsSxUzkQ1J26bpnaBY3BmN6%2BAyHg1bhMvXgGTCuJxlYMyOKEvQf%2FHE2nm%2BcBdMGUHudtn5Ob9DTMCndWiiLxoRhEOfB6%2Bvg1zOen9%2BvQTY2cQ1CCzRgyBAMLh1VRdDJv%2BMCklI0%2Fn5OuEXJLwLd1b64qMFUEjdSEj91SaZDdhnQYYFB%2FbaUAwp6Ux6l6WQS9e6bo9Bl2ff6iY4JZJIWy7A%2Fs0YoKXnC7w2TDIH3LWtn8URCgpX%2BlTl3cNyaPOy7U2JQTp8QaMO%2B99c8GOqUBhmJR57%2BwaZPMZAYj4z5hrT3MXrJsjlC3zczycPpd5HrhmGREwZBsaoL4HV2%2Bet9%2B9ymokrnzhyYUKgUH2WJqaUPRKsD0ULZsvoo%2Bv5ITo0hn6mhNvPp3zUufXDYEgDZLev3eFuFNa%2BTco5mBLM6MmaF43XK2Gif8N38jxydGpwvQ3P%2Feo8r3L1tySooNpAp1E0kRmnMXwISBHBVzzZDfnu9wGjeF&X-Amz-Signature=550a3658f3b7f631f2e950c9233dfb1374c8d1d8270d7987fef7206ae5f0d3ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
