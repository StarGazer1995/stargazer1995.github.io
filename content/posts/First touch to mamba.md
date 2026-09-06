---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AKTHF7K%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T063628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIAgBBcZ%2FWs%2FSRTxL4A8yUqxAbukY7dHGxyHbNtbt6%2F4BAiAPZA4oegYkDzW2s9fGJjShDbFXNngCprDO1e5vIWB%2FKyr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMb7EE6rkNnFc8%2FMQBKtwDfCEl4JjDblxjbX5ibXWXM%2BbwujQ%2F87vYczDx6GWuBLK3NcFsiVnn%2BGrZnwJKqufD5NXYNgssUoUY81ID26rsWQJVgY%2BVd0hA1xZcvwdy%2Fo40o3R%2BigPmJfGnBW6B5beeG2UmSyxNpS1MpOgpu0oCWaZ9Ex6F5q4aHEKNSEL2ca5flUVmc0SK4GinA3XjDsmgSTbL6wU7lzJz420fXLqz3sU8G0UGpAgBYqwSZeLQDKenP%2BZacEF2NcyjH7am1QEWIBJ7hNZQNi8M1cXZumhhCdnvak06YFeJsJ2fpbzG3S5LPBKiEF%2B8KOuRu9eMiVcXuZmHqJq14XfiY1LxS0vZduchOtks8eZnvRhMd2CaWsIb6TjRs53zkGXOMXdTzHR9XeBIBZ2LiPnu6kMSxB0nINtw4PxrpuDx0C2W8H3ssDTVLxRUBiyeqat495dC0RastGP%2BPwM1Sp%2FAGm02IPhMhuuKH8pZXa%2FGMRDvXk7wLVxz1KjlXdICut5Kx3xb%2Fk%2BD9LGE7oIYshEJppdmwX4ceo1skbRUCVSm2%2FEn9M0sbF69ON%2Be%2FRt9tfkl7eJECg4GTdsl83PVg29RoOYDr9EEC%2B8SlD7qVi%2BB%2B%2BNGffgsq1jSpLoEvBfGmAgWeGwwtfHz1AY6pgEg%2FWOlvawYKCv8BzNiPnAc0qEgUMwIgnN8xVTg3ROAPnIR%2F4KKDtGLzKFKIF3TCBxsDzaL5RsjHLgoQuIriWY1i%2FtfwY28K7ewg1YGNRqZz6zH6pqLp6TBiiHjSJP3UeCM44dozFpBHgoczrV1DAMjodAPepHA1qe9D929sSly4S1iF0%2BJVe2YJaMqAsKoe3uK3cK125Ij7moZfPmIt3K7C8xmY9Ka&X-Amz-Signature=84deea909e24af5587cb145bec9f5bc887fc17aafaaaade050f7725c8deb935d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
