---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663MGRVIV%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T000138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCKs5rkjc1LSq2p%2BBan7tZ%2BKs5%2Bz8bKjvJee6aD4q3wTgIhANOhT%2B8vPHwBvRu%2BJzSnAgUA2IvfEZUDoeTdF9t%2FQ9DfKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVZICHHEXys5AJ%2FWQq3AMtEQ0RV3me8ac5syXXdgCyK6UxEk4gGU0bRwgOXaMmDNwdWezHOWTMnJiR7%2FR7mEBLvtFiMtlpH9svk5zmw%2BlDbMrdJsWzyXmDhnRypY7gjX7bT0mVUPiROFfJ2UxHb%2F1KbBfjFDcNMko%2B%2FSzDs%2BXLynuRI9zvQtZYqZlrUtsNJwxSySXaK96u4Yv%2BivEdqBEHGFtJRKggljeMHG0lWq9L7qEUXnvqife%2B48v6Uk9wKCZ%2B2EXE15n63o1czCkh4m2ueYYliG6eoCHYAHft6YHGMC9vh70UTfD6nl9G%2BYIIhK7OuPtu02qArT2W3PCUap5jLtRDpjaNhSBdE58IjixuoUO%2Fxasgd%2ByYJHaBAyAqhA9S7ING6p%2FM00WeZh7gp1FaGnyqmuwkMJrjt5%2BnH5MiDU50j9zCUN3DG%2FPOi4gWYdQ%2FmlmnpqDIxEF4wjGVCtkTJLqU3I%2BhbOC1KpvOH5MVI7uLiH3EkYI6Nj2t5mzWvXTnkff3MDDvIZxYW6IvsCNeZHnnOUWYealL66xxeRyCplyRin13U1XjxbGo%2BYMYyN5uTFNfLGIf6giBYS46NXq30ykZx5%2FCAkg7gAToh82XhNFrUbCbMbinGpfK9JtCrE9zHPUZeJOYSTR6tzDBu8rWBjqkAZDkJA%2FEMzryInnfidwr%2FdqwvS4OlWdcVORlzUSJXec4G%2FiN1BcgJTrGHDX5O7lD4irAKaKMub23zc7rmvhMaRMX8jKs770C0A6Lsdlcsm9OOtkwBgVsyCJs4N0xZcG9mEe5W%2BXEoubl0nGix7BxIPu0zXrRtX3oN9KBKGTuHGzCrqa6guRG7q6QgAXdZwIclT5TD%2BHlQdZA74EmXqIw2CZNafdB&X-Amz-Signature=b1ff4aa7cd5cbb4dbb4124ce6d9d4d7855cae97e399cf66fb39c10dd9b57af0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
