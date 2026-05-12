---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RL2MMAE%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T192734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQC0zDBgepsljf77Ft2Z4cQ1Se26MbqWBVcVIelK9DqVJAIgCODb%2B5htDQdk71VOiJZHVcVbUMxiyk3ho9m0wcP%2F09cq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDDCCcwBKGw5aaTstOCrcA1vom4PFYPd3VKr%2F%2F9ycsq1HLocj5xy2kFBOlVFePUXOBc4TNfk2Y%2FQIFFwZgh%2BSsnjduqQAvQPWq%2B8WaxRepL4lhs0FyDn8iPXmaCGiqPVYo8pYxZSF0zZYlVzA6SgVHXYo8IYtTp8tV9GqBLI4Vp6i3HmL6uiA076ey8ByxtOmjRWUyT5TDA0MF5XHqGMRnbfELNiyVj7SgskJRhHbJJnl63BJzXWidzHI0Kq1iMnqSCTkICtLNwbGQKBDZcoh5VxnXL7kkv5uhF0B%2FGrsI7JgAjmfZ%2FXxIrsleNt18NBo%2BtyWDegfqh2%2FbBQmfUvwoEHYIZ8OIggrVJnhkuUbVRyV6FnN0xj4k0YK956Mz41b9YbA%2Fk6Yl%2BJ8R5k1AQafZpqYsY1CPh4n%2BUegqznfttvxT%2B5XO%2FfBR4brBm%2BAEVa57b7sx4OFCrieaOjWcDEBcyOG0%2Bs3mLw58yh%2FbnxcUNK5SzJXmYcdC7dDTmxpqC8ApWHkQ5EJ0BZjhqNSngatahPl0Z4TVZzrWKZkXBV%2B%2FE4FuMHIZbAgRuEC6SByLp1HmRLAlQFXw8nVu%2B0IFL%2BURFB0bwKEyH0f%2FvGwcbqv63xQakHKI0D6xUxgdMG2stX2AoKyQwQJUyKSQde9MK7xjdAGOqUB%2Fo%2FiCvjGPx%2BAYYUWiB0o2ozPntCCrxIRKDo5tzYZserZGchB6IrufcICFl8tjfW2nXJrxi5u41dl2NqvK5EDyscaUSKEdB5Iktz%2B4rKXaPfDUWSA36lk710izKN6aCbSperZHr21LAoVYJA6GIGzBVrqk9VM%2BznM%2BC5fWXn2uxR%2BOKuVpIaQ5yXILQ3clsSHvyHkjZlCKgdTihmu0v4phsCnHWEA&X-Amz-Signature=189dc62815d4a01a0fdc31e4556c5efb94ab546f7593937ec2367c2d7611557f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
