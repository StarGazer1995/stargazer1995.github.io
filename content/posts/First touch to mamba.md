---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCZ2F56F%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T114541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcHG%2BSW7%2BL12H8el4cR1w58CmNOPtw14IahaxoSJwtZgIhAL9BqYUNLZk1zNUq%2BsoVbjFr6Kuj%2BrJMk%2BNyVwPt9DTZKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2WRAIcSKjXiSZAT8q3AMNAaBEQEy2awLasGSY9KvkUp%2FH39u54N7UE2cXWcuh8baN%2BAt9o4zID6ZSrgMFngNwPaUXHsvRfHrr87J%2BJRNe5yr2hUYhzRnc1iSEHiVDVrjTAL6U2E7U1MRUJiH4bM7khffUOCbdGzhwbCu67oghov%2BV8mt7i2jvYjBLlbD6IjYL99fUkJYXIIiJCN7pJoWVd46TLq7M69M7JSOR3IMAZ5mAmkiagNfFauj4RWpc1ljRjDbtn9H5VggRU7W4xIkCabDfJzykeBYNWyv%2BBgS6yV3%2B6eyO6fotgW8F14Wva8KA5pygp9wyYVLvUX2On2J0JCN70goGdSisblX9K8B%2FPCGnb0wswdtpNU898k6RN5Dw8jWJtE0Ctw%2BB%2BR3gV5TfPPBtPI2KZFONxvJ0%2FWNCfmu4wZrbTBk6PaGG1cenA%2BBcxUtGkU3zL3h6qCiT0Z0Yr8Yu4%2Bgek%2F%2FbqSF619YjR405eLWvVwdYi7PWPPN6HWs8rViZiYgB80YV9pviu1ZCdp5uIWFvp20TGQ0jS7a1mlYxdGPCzTEQsbhjgTo8zyAK%2BSQEfpm%2BK3Wm1ICJ7NuGJU8Dj139p46KsJ5yfGvGkn0TXzFDwZIcfKxnPWlkbFy1c7exCp0POtZ%2F7DCa1azTBjqkAZqtdV4yUeLlh4EMbFmrVSTBv%2FSzRrW1kMlplw6g9CfExLCCVGHOfmhb8LFgPWmt483BpHpbdtIX64TW8WiQZOdFWivePjgaISt6eo%2Fp%2FrBW3rkkDHY0e2bjjx6cI0cspv9BgRYtDUXdRiaaVUtwPItqDyV2c87QMpRcLWQFkjz0xgOA9UnMW4kJt5VKloEoayBEqIPvOEfuUi9Te3FIOxThCcGW&X-Amz-Signature=34056db6118c4c45c502085763e08a13b76f4440f67314eb6038a9335464de33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
