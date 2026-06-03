---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF2QLJLN%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T023558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCB6qE9kU0k07ubYwH2%2FlKRBKKouqU3b6tk7H2P3kD3BAIhAMZnp%2BptOnEeqYe9rtFQO2y3tT%2F1f%2FsYhMaG6wUW0JboKv8DCDMQABoMNjM3NDIzMTgzODA1Igz%2Bp8U9Nkp754Rgg2kq3APfi9lRymIU7D2wUsEUz3o%2B1DyHhEFR3ZfUBwi4c%2FekJsatFiypzYRi1T9jMk0HYhfRh93ZwT7w6THPtClkW1FfjegjLoHnE5Srjvme8RGFQdx%2FS0SEMcF4zwrRKzRNMnDOoHzMNIX2QkwPfwR%2BKQb86QshK1Oe%2FbbBi55TJQ%2BnuxzDW6efUrb%2FqsxjO5glDTttuY55XSjcuKh6Aa4e7MDM1DX%2FKlWEIPildBFl5hj4ZtZ1g5RFOLWLlHqKYz10OTMUdEdksETOGjWb2zWdvZOiKTMskB9Ima5yV3AT4tNdYqPTXmK7nkE7v7szqzPWwbI%2BpWwaBqzvTUzseZxke1j1fOJ4gh3ZMyI1lhd8yds%2BV8Y9BcEoWPFZPmZwzkdy%2BkuHUJse9fATevcL8fvqtFkcMapAUJ%2BsSmPr6DBfmeJy5I6r7wvOMyPJllBSADxpylAC0iOArCI%2Brec9nADMwyx3oPdbQfB3RkKGM94mD6baPUh60EuioyTZ0lIvGUcKIKjFpYiM0vgXyb2sEyZtN8Jpxtuj5JRuim3unSN0DrQdhl3IwCSgDdQn1kposRxOqmEJe3HFnN4yUSpHjCyKdMT%2F8joJvlReQNPRDXJaE7PXandRX0%2FX25NClsrCpjCrm%2F7QBjqkAa536fFcsHuzrqhrHE5XMrPuFr0VFY0i%2FxBgnKvHu79Iqak6mrY2UI5KhEq9CeP%2BZQ92u8yvKVLhAUTDflYj99PeT8kvXeKqXr3N5mGUXqc1TwLku2ZfR7WyS5ayGVUGLvhdq5LwSIlj%2FRY9PoRAcYToa1mrgiIPVowEAJXC3kOKP1UX%2FTmr11aon%2F0M4jDwqA5KMX8IpxkGjRl42yVQTV11AxAa&X-Amz-Signature=d027c58774e545aa4bba5afc83ec8bd8b2f1b7ac886eb91173f77ec43c361961&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
