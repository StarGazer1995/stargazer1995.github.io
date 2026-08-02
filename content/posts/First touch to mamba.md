---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFJW4VAJ%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T111408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC0%2FBiX1eMTP0N0vPUQdvq9TWEx%2B8z5xs3kEh2Ua8TqSgIhAJ5rHRrjpdncYgY9qoqyUjKG95XMq3bGu%2FRnKVrJckzHKogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIDBqXn4lOVSANyKgq3APalF7yxC4fnEkyObU%2Fsl2fkM%2BVxuHT4o0c%2FC3aNfD6Y5wk88qBYwIcefefsQDV1W7LHht9xMjJ7JExis%2Fq%2FNxZOnjvJ1wOGXjBcUnavO8lVsG%2BcIxCQ4Pm%2B2r6pPEfqkgNgSwkqxK9S0EMfpE0i76L%2BDVlJ1RP6LIvZ20nVdTjHn%2BgYrHkDR1%2Fv%2BFK0NW3SYO29W0c7phT5tfUjCIEFt%2BU74fJGhvHyaHlXyA0kGy5ZzYuMXDdKm5vZsii5%2FGJdrp1c5U%2Bi3VVK1Xn16DE%2B3Jfv8b%2FTzgewBHrrrIPYjNHUJAIoT9DzZUGuQeW4KcNDZgF3PxMtmnYbsdSAdN%2FlrQ1ImI%2BXS6UcnC4YjB5S5IqLp0CP8byWskFROCLZ3HA5ZiAsKDzfXFOb0U76hR0MsVNRZkiTk7ON%2F51B%2FFIVwKof5bua%2BH5yspPX6rY6ofPeaFQkw5Zj%2F35PeRAs5E7OkP7NUW2HAVy3c7FyoFKGB6yOPW%2FJ9fH6HeQ%2BiyKreaHE4U2PrqakALIIym42OFD3CtWLRezAn4gwrH%2FYkNShlTd7NJN1nA8t7MqzoayrT%2FJD2I6eonwgoIjUKqOBDxf6TihxiiuyY0j5QD3%2FtDL5YPSklYd4APrbWXlDZkAVTDp8rvTBjqkAdKZ5f5BWAqypEiWGr7%2FN1l%2BvvHSZ3%2FSKHoSqG0m2VcFmUecTN650zAosxWAbGCage%2FusxhX49dotsTntb8aLF8FBz0qVkMRiBg4If71J4jtm%2B0q1MF0AWxIVAy3LQwKByWqUW17r9b%2Fmov51SN%2FiLm6STc0Kerttp0pSydxuhUz6sDrM3lRPncdp8WMKJWgYQMwupcuWF8JBQ%2FEQp9xBw3csxkk&X-Amz-Signature=dc1eec3cb79ea717909d25ce241e855f7cd25c4403fbf327ad93db064c14b75e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
