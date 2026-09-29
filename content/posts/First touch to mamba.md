---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466742LAWX2%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T073727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCrZJ4RUj19ed%2B53%2FdUKUEOWcyQzFr4h0yhuPbr0EPaYQIhALe0yZaqAZuXzCYQgTlx8vzGLWewZaLg3BmVTefsnXagKv8DCEgQABoMNjM3NDIzMTgzODA1IgzJP05PPAicySepfBoq3AMK6bxcQ7LtmrCHirZCMzOwsT1RROGimiMgkt9bCS9tuGCY%2BEy6X3XRjYb35CNELqRxKScxGi%2FbTF5PYl5iLpWAoxtIxWjulyrfUFoFul0KUms6KaT1MXmtpGvSL4dVWsqZHJdkpfwrV7DNAsPq7amgNGcqRLYm9LkiblTAWx45p6JDQ1TNWGHNkMQQK4dmYnvpp5DM9%2BnodKPNXoyRHzJyE3IN6eB9C7GydwP%2Bnty9BrllQZ6QGLmEgjV7kMqcK3kjAgp42FzS1BtBr%2FoNu1nuxM2%2BA%2F6dZCK007R97rutfUza4RocG8GKRgyxyCijRxc10QxAJ%2F8XzEBY8Y4ZWzciH%2BVvFvOc1lTsfRT3Q%2BkrxzpTpInyiIXeNA1mmyagAQC0C%2F71OCqAqTWA7nhPneOPBi%2FLFSYGuB8mGz%2Bwz3ECD3vvpfNbwn5Gce2VVBDh5X%2BP62%2Fz%2BicV8pkmTQr2I2edXDUriuDdNnKigzm%2BWBQfSxvzx6EiLlQ79QlcfPseOsSAxI1Q27g3B0urxYr6jqqFTPd2CanwHECbbR4BrlHAZa7noKX4MLlqyqPcAl7HR8fznlT3zK4xsK%2B%2BKRZPicQzp%2BvwXOpALEVE3nILcu3goCNK2zqa48%2BQ6FWlcjC4x%2B3VBjqkAW9guEFwRxuzknUN%2FEZr59agGAs%2Fr2IIguucafzRMJgN5%2Fh986%2B4BHdY0JkkPgiBlYVxjsusH13G4MeJofG6v%2F2xTQG2%2FqgmK2rOpNzwUjF0s7caNx%2ByxhOXUf3HPxixM793MGxCkYW%2BFiiIyIg1KRvivNeEK%2FO4gZajHky3DXWyD9%2B0rKzKCRMkNEd6KKoA6ZFf3zoIDHMFor3X%2BCZs6rXj397L&X-Amz-Signature=9f69014580678fdd78d710cabbc943b06fca83f0337747ac987fa746441e9e49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
