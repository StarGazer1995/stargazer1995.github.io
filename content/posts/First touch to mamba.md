---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MEVDS4J%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T210128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICmky8DB3wrK4mvSCFC2YOKKT7EcT4HhQ%2Fs%2F54YpV0c%2FAiBUaI8vvEXViptRYHnyTPBsqZMdUzL%2F5l7eYBfQ%2FSexYSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML9eMnd%2FDdL7%2B7mm7KtwDL6iXL6H%2BVRH6jvswX3l4ZDQ0Ohd0jIHUrr4MtHmAVFfTUOCDA8khYl76XZ%2BCuI1oowthaAaQc9Esr8AQUMn2Y%2B23RHFOP9HHZIUiXRnkXNSMQS7j%2FB0hW44mrxva1p1dOh%2F8f7zVD1krE0hryimAHD6GzHe6KxAP0WtOyGKkjsanvqoMyIgcmOBTBcwGGtqFpzSsQGu3QtmDhcSLo7UiBR6Qc6ZJ3wZW6uZ9ZdzreZWMh8wq4zzTSxSRXMym3IdNpGFCCWZrroN8QhRePjdRN2OItjji%2B3FgtqmQXQ3OMmGu6XUoDV30Qs90Qh7b0vem9K5Vl8Ge932DRTWz6CEXSPdyuLivlGK%2FHIDw%2FPDCJjvY6f%2FMR%2Fr6W%2BhbT4BMVh3b27xsJDQPE1KRzserwX%2FGiR4MezHDm7gu4caJS83LyvPo09drqC02%2Bamv6JE0Imi9s1JbkyV%2FmppBfvCLB2kLB84nzHu%2B5XqKe5aI6jGPfuisLzzjPtMt7KPVVkAwHvFKgh%2FXObX6yZPAbVE98ueGDvi1cJ8i5GSA7BH9GbXuuDAYfqPtMMy0NOqeKfv2uOOrrgqJ4vV2X6yx4PdJmlzALEkenOwuaRLyQQ6xdMZcOyGb9qvLySPpxD9CcOgw9eCt0AY6pgEJ6R7qdKltFaKVyZwz3JrcrfzwUqcP1Zftx6enHM0ycmYw%2BcRZxeHTYW6VON9nIiq6sxQKxQPG9tHnXDqQLOR1etDVQAKOuhhpzFRpFOycrXVIUEsA0UhlXN1ZmR%2FpvChm6qPZG%2B0ycU8xdebTpxotuTqVThiNbSf1zptfEe14txB8uF7AI9NrJW75ZTH%2FaYG%2BsVGn0%2FQAfqomBbYqHSSzwtXhqShb&X-Amz-Signature=ac50d2b175522bf88c5b131c057a69ce09e25c8dd59bf8396fcc873747922d7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
