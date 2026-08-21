---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZR7GT5W%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T062407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKy8MTFldO2dPa%2BUimi6vjuaY8%2BrJym8ywWiNKAGpKsAIgMnw5tJ05X%2FcjbXy0D4nLR41yoAD6m74csLkAyzzAVTEqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwbb2%2BGIYJ4bomypircA5sZlbzofBI6cf%2BxDJ4aaC5nm1fa7AtBFypb4Vgg7NhZYBhcaQi%2B1za%2F6MARod1S6fxJ98cNlNO%2BzWPyv%2FHDHmx3GDpdrEhNlEnQsH7SHf0LqjPA0aAeOZtT8cRdhrtewgS50aTCTyGxKRvKDlVNvK0M98SY1TwcBkVqhp%2FN189b7CG4vt1YG%2FqnTGGEY9pMX3jpSdn7CUodkdYKGJlLt19HomBY50%2Bj%2BQTeyrVPUUKgzREo5TAFSznkfINYLvNmcRAVf3vOKQ1tmegACL%2BS5q4sCrXK4jb%2BrQ1ylXV%2FyYv947F6vj%2Fjpwr6k1NQ4wHcBKm9AYA6VOS3ef19rlilbQVOs%2BcT%2B6mJ%2B2y8sbS%2F7ESTGirnEpmc4ex5AVsxmqWv50Ors%2B%2FNJdu7SzZFYul9jMl3Bk0G7fIiiLkO13kTTRVBuARKgaXfUsXv4yWWDDvBFrjS2vwaXHPYyoX5kFlSfam8XEm73%2Fbn6PZq6FRFChqMM2A%2FBHNPg%2Bw5igmWeBL0eFFh4KFIDSP1SHYveAs9MJviVrZosfr1O6sOvKhv26sZx1QyFitQwFj3SKaOs5bImlBrjmkvrMG7R8IIZgfdro6DreyutkUDjNm4dc3TQ7NbB4K00CRCavyjA5QMMKqpn9QGOqUBScM3jFdPwqpxSS8GYH%2BzZjOeHdyiIDbcem8GWEaUn7DuYI%2BIqyfe%2B4cGwiXXjKbXp2MzPp39V1wsaUhkOliBDC76Hy6%2FvVg1pkMlgDeqVnw7mDHjRaP%2B%2FwMuKbWdb4F3zxq7OHs6xCpa4dU90ZzFKgDkL6goLZtiGbkzru%2FwG5H7wsApm1SBqNKvm2%2BmJG724HivF1K173re9SHlKCVZes%2F4aFQv&X-Amz-Signature=89bb994ad4fe7859c0605a07e206d395e780fc31aaa4832112d3ca880d9c942f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
