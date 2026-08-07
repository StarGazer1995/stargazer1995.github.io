---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOZOO4NC%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T144451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCR0VTEByA7P6f676y5Gm9b2oS1qWlJGlzu5L%2BncxjW5gIhAJZVhe4c7B7RtUuuESNQDXr4t1rM2vXQrDweefsHjpcuKv8DCFYQABoMNjM3NDIzMTgzODA1IgwLppjoTfv40krfYrAq3AMpCuir%2FaJGi1eEKzo2LRQSNlYhQ8ipMPjuQHLulVx3iPf0gH6NR05Dqv%2FJpaeyqziauUvC5YTn8RF0647jyjtIxZ%2FBsaCQPkFtkvkhtRQ1RZjQlo%2FI0Ozrqp8246M4L6QldiSnGoCJ1VvorsFdFW0fV4XmwjamHMn5aLpxi1lU%2FcSu%2BEpnAv7wlBEHZWS9acia6Q0%2Ff6AacN4NUoRcsrLjl0grRZspmf6rgdB4ykJ10SvymAkD4qEXav4XPUlB0iBfWBb6StREjd3hMVcOAKukzoKWNL3nnrVDqVkZQBIENUjUlyXxCPxvPnfeL1%2BXxJvQb9Hq8Y7Mau%2B9VqHlK3j47rf%2BGG89tfJNs4Dl1t0HXXCnWTaaoHRsIoDqaF9d8KJr3vTiXC7%2FUG8r55mimHj3tjc%2BACzex8mhNjXuR%2F193zzQLeg9fwz0%2B3FfKXZIlIi5NA%2F9qQZslL0m6Lx4%2Ftf%2Fhp4BByyUvAAq4lKrvWspoO56OXgrpc9mQspjAzwNd0SZ6%2BtQXyJirhOrtoSa1heLoinCTLwNGwukB31m7sSi13dPWr1gWkO7fybd3xxBknetfCOAB4KZX%2FRZxuuNv1ycEiwuMPynan3r4yIePks%2BXGFQn91dG81c0vkHljDbrdfTBjqkAdKxmQ5LC2dM%2B%2BpJK3GiJY1VwIzgzHEgLFWnie9YTPbwoQs2eaRiyKQJVaZ8kirKIjlsy%2BAC3mrjUH7Ej86fi%2FSk37xZn0tGbZeLLkWf4PELpbQR6tMFjhQM40tWTeqgJ8EjRuJ5bx%2BgPiU4OjahKBDTRTxS6JwP%2B%2FFYv8CGbUkhFfRHfXkWU8iyeaXMXy5Jsu%2F%2F1Az1fuKmy0U%2BtbuZ6vBa6w7%2F&X-Amz-Signature=87532e958c8b6b1b138b6b9abb074f83756137c37942e289cf2679ef6cfe4d23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
