---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MPU3Q5H%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T163207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDbv%2Fw%2BXnodOgHJSMTZ%2FnIJSfHSP1lXBmlGC9DrNDXO0wIhAOe1SP9UkDCWXP7ug0wd1YjM%2BdHn7t72549hduvYl8woKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYESx7u%2FPUaWe6sMMq3ANyZeG0ZazIQRoHvz2Nd4%2FQtOKAi96wJIAo9sy9FkEPozXVCE24BM8%2BrwEi6ccBnDnPKCk0rpDZGuYvICXbw1AnDtMWDp2NKberMqiTH7dmBa1dtetHPaiXOtAJmnLQh3xHI3DBHo3AiSb8mEry6fd9PHTlhB2fLwYIpzmjW6KcjppVO4G5Uy%2BeIy1BXfkD7wAvETOJ83iKSwRmG671eVCv6EH0sjk7tNKti1TIGgSykUbQDs5j0TfYb%2BQ1vLUpWMBBPq2WaUgBQZntJicYcdcn38qdZgGxFOFoUnYVwRuUxVp9bu0QysVBb%2FOgEu3h2wcHVpMsxZZ%2F9SudKokCVH6tKjFxtlofiVAHVxPcGdYbcCufXltt3m0k4QVYzGH8dBc0hrV8GeQf6WFpB3x1Jw6qNEe0798VTPhIo60z5XE5gGNCI7gEulkvF5jd8onwOKHnHYvohGlBCScgS3ISGhj2yo7%2BJbrO%2F3399qJmu%2F57eHN5LGIByqMYDkvwe0qhCX3o7snyBtACERfhmibmPd28JG%2FdLBrA0fOgpc3AOy%2BqjjUNCNXp2oz0fHSTBS88064zMvMCz89USxFo0gKoxCF6bt%2FcdIRxDaJZ4BfdXqDy9Rqe11h8k7MbsiZvkTCG9Y7WBjqkAXckoalWXobMV0fikaaKq7lOjGviu6Bx9RopONWTxY4%2FUSnptcEC4cKc60uvvvava17w7DvUBpFYjwwal5BVUsK6J%2B1ZmJVJygfd7d2cOLLxnH%2BGaPm523iE45OzHpX%2B29FaTTg%2FCD5VinXe%2BEwBxa3p6roHNBCaDyBEVoaFdh7HJpUx6Zs%2FtxEYFNHMoefX4%2FLKkPhlK3BO8yOq8JHGhBTnYDTP&X-Amz-Signature=4f4d50e27f15ca63e821e4c042be77a1cf4318d7ab228d9f82746e5170a5865c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
