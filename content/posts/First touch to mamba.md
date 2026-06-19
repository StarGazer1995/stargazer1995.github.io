---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BOVM4KA%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T085755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmInQPqhrTHIiDg6Bi7lETv3CPcz4sFOrBvAAN4mdwGAiEAk7WQh8HdjsGGHavlIDWPOE95Ro%2FT6Qr%2FtSGf582yh%2FgqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLt7%2Ff6KqE%2F%2BBTnoqCrcA6BsoiA7VrKgez%2BuG2hA%2F8eG2%2B43745RB32w755lCOdjVGJvQdwrLniLs3epBFf5Zujv7PZb42U%2FWhzMw21W545%2BztXRtYQxApADlG08LKwZp4eYiMAHwFeqsSmv618ucZBYg8GVVeBNrb3dZZknLAC1qcKfk2cf8ZdznlgLl4cCGE7dfO%2BBncdJIb0hNDFCYE7WCWAz12bQ6bcmpOlnN%2Bu6RjNj4GQenwimw%2FjZMZuiA05zjjesEElmAZgb8l4vqJqvJr07AvSr2qKRL4VzxPezdwfqF73Hv%2F9cbwylSt54%2BR%2FgN5BfMVTWvoxXYmWFDc3KdFgHqezOxAcXL6raudKdKexNHfKi3WDyHWpNiuIwMKgHNjIyYPQ28YzQpOSPPzhImg9uBgyNI1EMY7UOd4BdRaftDIoGkZXUi0nLUr1HGwj7yyjHHyEveCJB2LXRVw2cR5RvTsF8tpePAcJMOhmqI92vO7uvI54o99wbSpcTfgCvj46v%2BDAVsKo4gMmmHjZIYzdqZCoY5%2BLDvlqHBuDocho8IdVitThjLDzqCEJXXGQhlD4SLA%2BPV%2BuGk9fHtQzxPQP8JvdDA9tT4fP%2BJ3BcnxIo%2BAOdGpBj3vgrzcsKHpYMEpyjoiO0BKcGMKT409EGOqUBG%2FCrWs7qatOUQ%2BCzD%2FPRRbglHEIhe41AqEdrcShYx7fF25D3z0CUldxyAyaIGTFIRm1Rls0TErCcZuBBDAIUouUHPwrvx3OykYYYGNuNJpDE5tf%2FLG2u4bwzpX5GUDgvC6oUOVnQ6CQgmJSem1cOAKjXuzkWnfWrPaYWv0WTZM%2FlTit2iMmSOSmj8R5pEqTvowmsz27%2BJKJGPqWQ6Wzdg7dDEGsO&X-Amz-Signature=516d62393f6783ed7b7fdb0970e99f4e3b0c46f6a5cfaf8e0d3d904365ea2df0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
