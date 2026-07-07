---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH7NBWTK%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T193135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG6wPXXryHpwBTquGVQQfE6kcwz8d8XM4Dna7fSFE%2B5iAiBCNLUDCiCnXNrWQbKSfLp75kN1VosOOjDGExPC8upJkyr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMG1NiVjXAy1TX%2B4EzKtwDckq%2Bv6KZlGEgoWgdfRj0OhN6pyzfwkg%2Bo1jCaj1Fxj6%2F4gH%2BIKAI6MB35gF3UHusTiOhNLXg15MLW3rRIVERRKeVj9YWh0fQwzE3eHpNBc5EFvf2%2Bw6pXAxBnZYubqpnzFuCEpzWm03KT%2BbpiEM4iDweargPJoD8JxHuJODpgumHe52nKl2t3F8wlGlqSwVt%2FQife%2BnFRNfKX8%2FpG0ZIUdsgDdVypgG1vjvSK7JTwMnD4Jm2b1iZp245vICzeyd4OnYkLep0pXUKi43HEbHjP1qTT%2F7oAEvtE6cGBp7Ox585e97TGN3VZlJxgSeYG%2FWOC%2FQQTsKheAm77d%2FobPsS7JE%2FKBBFC%2BgREW1IHg2%2FSifrG4r7H%2FUpKKEdryi98L3CyY%2FNBivV%2Bc2%2Byw%2FLQjvYgaDnH4Nz1nTc4G%2BrmQVRAS3X14H%2BVLdFRzajaCY2QA56YyAzeOV%2B7u6vrG24utZe53DFRaUuOSUgH15PteSnVSV8lAzBRWraesdwFWW7BOlYeHL4ggeNsnqcGyBYBzQoQRDJM3rCL9s8iZgpN3S1xxFG8bkjXY%2FXwt9vzjdoak0bdby9zrn9qfpn1DYqtfncY1RhKB3uSnATuKDnByouoFKmxj7%2BkBYWOfpmsukw9Ze10gY6pgFB71YCYX940gkc4Oo8meTXg90rE6u4vGlY0V03OO5T%2BXwtkMnwPbIvZ05IVePF6zJ8U%2BigyWAhZBwbsb743%2BFFBNDFqFuDzi7Uh%2FaBN4Im3JhA9gY%2BFz43cRTi5bQyiK5GwljElvxFl0jwglIUDpFy5ASZhKigs7JI4ZAVWPYjnvPiHDbla8%2ByHLh1iCuL1qyufcAGE8ftPOpP0JB8mQlibEf7cA2b&X-Amz-Signature=51ae294bf2d520fe316bcadb5ba4d99c5fbe20d9fa9d877d12c04519c12eae9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
