---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUFMEY5%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T075619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQC8YZkZmIr8iJkdNfaBd9Ap7QsR%2FoVrA28MLA5hIBnjyQIgBUDsjKwPbxQyR4N5CfcU4reLjOCGTj%2BsiNiEpm5OJ2QqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGbLAO%2FsB50fPIWSdyrcAzHO8cY5fO5CP5nZUCA4lIyxXA3T%2FdNvgsBipYEHf7yUtZalomA4BfAeHtJ1NhYyXxVPf9sRjqQSOyvEtyN9iCXps9HkKJ8AzvNDXmtUeEp%2FSsQY9K4L8A%2BYzJD7faRuKgonjWo4rF3tQ%2Bl6wko9A3VXRBDvPCJZj2FMbDH2Np0zOIV2rXP0mIt1e41Ic9kTxyf%2Fg7lgg5Wcqc0iyx2kvF4b3%2FSRHHk0QYcEiFdILMz0y9X1CfXY%2FmPIdJnTJT8tmezNPXpcDhL90GC%2BShxultXkz6hHx27j75gtQdGlXkb4ttb4pl1%2F3UzuXSeD2LcLQR0f38FkQQll%2FTJjHUlN3x5UipQMdwxpG2qykVh0scLF0HpmLu0u1lwoq19ALa9N96jKHEM%2FzUXM1L9QWr9E6%2Bdo2ZiVX93bXlGqFaS4ttjNPi5fa0Hhte5AcWrpEEvQHFBJsMZ9eOF3sSiaoHcvX3Bg8IAlYoHKxfyvfl8lKpMlbHMKyEDwBcBRQh7dHAHkBM%2FvRwHWy2kZXsEMbExyd6aa3Lp2u7NruEjba7NoutDh14F4Hm2FtZVYNSwv8sBu4KwLaHskILJSSm7r311LuYKQtxqbhtTO3J7NngK9aIBQdmFDQupVHFGMhkOEMIWIzdIGOqUB7ZDWUbLQaE7cmulxuqn4tjzvXjs6aNuk%2Bxqv3PkTSPtC0%2BWZEei%2FTS%2F5LcpHCakPmTTjaUSblwz7xKfMFtPk3sGKfw%2BAR2PEmtMPuLm0TTVBtUJrEjFr5XPQYXqXhRcdXdhynGoYIJy627GCiEsTl46kCYCZxtZ91af8D8vqtuo9EjJyC6%2FaeI4QNwpMFXZitBAhlAQe0oUPqtUh%2Ba%2FDK6wQj5Y1&X-Amz-Signature=df1e52b701d23233502325b15bde2600b59ada05446342d22074e0424a6ca2bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
