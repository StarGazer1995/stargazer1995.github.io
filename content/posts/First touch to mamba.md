---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662B4NZPYO%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T161530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDSSAKVXCOK2UZXqqetoOsVSfCHZjWT%2BjKKIcjqVRLQmQIgcU2st32D2JXL4XtX%2BMR33iwkeI7aXNdUZGTGBSiwIwcqiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD1dGFABWc22ty%2BY1CrcA%2BOuRC5GZyeyyiPzui3z%2Bi6KehDaAHv%2BnRnlzyJDyKwd2HhwwWrU237d6hi4YeaPRYJ6eZd6A1xbW6%2B3E7FcwRO5zspOf7bRb1HodIKwLZFZcQmgY0kIe0Xf2c4LjFdTo4alcjpXotnq%2FFXhtG24Sh4QvdHwPOXbwjeBLjJs7cE7pWgieC1lSp3buJpT41iBLrq3TTK20v349m4W1lU60qHyMNXOLUh3awwdnKa%2FvVjKPveZMO7byX031cAKyyTIknJSHXoKBBxmiYlIXkHJYTMIxQ4qV8JbwCa0f72VvpRfxB3jeMwiIERMkUw0oe1eRsXBj%2FpVJzZd5BW%2BPGN%2FSvC48bn0UI3S5HXMlBDj6IpQKg3ytKr2boOQLFGAQoXNuIa5HQyfrfvs%2F%2BOe4Y%2FvyTRro6qdMfqg2fH4YMzCgZxHsa0SO7saIExyAxZ1kfl61Gnwjabnib8GxPcerGt%2Fh6CI2VB1nkQU%2BAje2jFEBqmeeHmlCuBCprgVV61HkuuugsRo12THnx6yGM%2B3MLVqrtoBl8EP1VBG1rfbHMZZNDhufyP2WS2fbU8vNmvn87Kjgp33WLPsk2c%2B0m9VO%2B5mZqod53XsVumphPgtAEmIa0yKecepWhwKebDcGU8cMJfHlNIGOqUB2EbnoLD9woXvM27uAmrveaCEMz2vEKieK5jc7GzUICkOlQH5dq7Wlr3%2Fnn%2FsPw%2FUAf7MBP%2FzP5KpP0txkdIuYY19w8X6VINnXhEVPpmbmroY9nPHfMyDNkL9KAZnLjXiPtb3ekjBJQ6%2FTDmcDSNI0Fw91j43CqgQufDbDSrdWUm1AHxxyAzOD1GAswzyf3mve%2F3c%2Bd5kEeFTYUmbbIr32%2FmeH24l&X-Amz-Signature=2b5da137ce5f53baddfa84bf7004b73160af738295e67bad736520d331c007fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
