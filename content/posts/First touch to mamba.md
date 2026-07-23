---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673UQN3GK%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T224557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQCl%2FHIVEtT%2B5QS1BG3ZBmKxVww9TVlKecEKQMx6VntUMAIgUwDaYfmSS4PwBLHAnW9mz4WUcVHvGQJZ71JHYZc1jMsqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJAjiMNnibHsgbQdQCrcA0e%2FCDhVM2qrYVGrO2upsr%2BPuNc9aykhPtp3rOq2OU76P9s4w%2FrrYAF%2FEA9qexy7WopiIJnrOPqP9WzE7iB4vMLglHv2Fwsg7c86ApVpy4OWTNH8SNXTJnegw5JeWoePYCTVxSX5d4IZRE8tyDKs657AXAdYNrisG8dXg9NJRyhyQdz1d%2BGRT%2FbuqTlL1wzGHCKg11Rtpz6PLkoshIc7YJgOz0EtvwJvJaqWq9ZQSf6bsztvwwndwpe%2FhkMTo2z1tJ8DSzlT5U6wbPAy8lEtBxPYxEQxMAbs4dOshrtW2ravhpwD9fx1hJCB97PDe0a8w63vJjIDDAlZBrBVl8UbFrnxv9FpWSM1Lsz50b8fht%2BxLvOUcxxrfoPqpQ%2FX4nu%2BqbZTh7fWdvqYfWLEePILFoej6shUtPLWkFjB6EWemcUIP4K50%2FeqypC2dKQ2hUYP5lDbyryq2f86CiFNsDq2xOAaGm7i6bwCHneBYsmhTrB11xIwsHQ6L0AeYPcj3QZsffU3Vl1%2FTK98ZC%2FxZFkB8OY823d27hAu%2BKcplxKWUXNSiK0Z20NxJoBMFaz%2BNit6E97SMZEC0CSeDMHYguW7LNVdVd9AXor4ATXNna%2FHCXJacSeqtYXiAsP3pw5dMMmUitMGOqUBNd2qQGldDAuZT3sbH4JWmLj1lyzwLW6y32gV0JiLu4K2ZMtsvYMvj6ryo2ssQPVqe3c9Zf1RSqFHncpZjn%2FD5aMi8JAhnjcLxGNROSDb8NjLDlPEqheJW6OFRrbHkF9UnQ0H4j9tpRdJbuJ%2FrnyzrdFx%2BlQIXl49KEhR9cHt33h5KgexlOsFMo7rn21AJd11Pv5Dh4ngWEvxdggzrxB05GBGEBz5&X-Amz-Signature=7b1be6d94111de6a1b312729f184dcdff1dfd59a3f2316c9960179a06ceb9af9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
