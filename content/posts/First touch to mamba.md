---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKYEBIQL%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T052834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJGMEQCIHxkApbBbzzF51pJCLR5Z49Bdp4XhbjMIlaNSdeNTj5xAiASJEJ8IB2C%2BDWGMD092DS67Uisld01hjVz7HPsLImoSyqIBAj2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW8dEfGj6pl3lJ5aBKtwDbQDiVa2EyogsxfY49djnjawzmjPmyU4jIsIabUCo34MY21%2BHGzmPA7p05m%2FJlwZ7ZsAEdwIyGmBqwd%2BGRbgaD81eiNfsEonBZqAWMiWX7whJxA%2BnXd%2BxA%2BM5qV2lwzo2M0qXaeqBmkr8wX5mNo5Osrfq8lxdlKykW8r2YvKhK3X2WKsIK%2BXP8ELhyqrfX2F98OWBTeiSpqP%2FAHttOoZmFYrQ4HNz1obVi3BlP1YS4m55VtlYI2ooF1Ta9T5VlJSvyBHjL0K%2FIPwClfDeNFp%2BfovgZrazpoOrMGzv%2BotarKVudrf4c0qwMMY8MYF3pSRjDlwlacOspEDsrD2Z9mknG6egYN0Tc%2FXb9QUBWi4iZnRmPdp6jMtvpeW7VkFatLQnkELf7%2Beyqucj6AFTbBC8vk8iyrZwwhiScP%2FzoBbgvebsVJUoQ%2BJki4N9bHqQuNeHxYmG3EYweYfYxD7Qxrh4XHZDy%2BWUSHFDQeZnu%2F0647UjT%2FvjbSFb8ygfRGl2Kh4eeA3eVuJlLCRRM4y0jGTGbImE9Y%2BOnDNkU3UyFsshf44ZbNFVbB6RBvh7l2%2B%2FAQULiBZFHqDfMEtGhzDRlXZ7Op9zkGrEQAmVfBxmAfk%2FER3NyRAQ1%2BAph5Os9Hww9JKA0AY6pgGH%2BsTi6FnxbUllXxhVYcicXd11vUI3%2FNEzhv7jKH5%2F%2FUtPPb1uhv%2Fnwg6MjPgRJywHgsS8KeYQVHLupLRIJklO%2BBnu50ho138v2dKG7YjTrANlC85E0PbZH%2Fp%2BhgegCL4Ma0%2Bc9DFacmHawy61Mqt4ixLwGv88v48GiquAGTas0FdmorCHzF%2FVpYD%2F9Sz32KBUPyWR8xST7E9HM0wL0BrRwpsy2XNl&X-Amz-Signature=73c851ee03ebbf1a4e84ee418bb3f98dfb54a3623a814803dca4eb6ce0c30069&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
