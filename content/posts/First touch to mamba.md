---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TM6EH2KF%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T150520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEQjZ6ndTDdkDvnww0KeW%2BduArd0EO4ZiqsPQxVstJtRAiEAv7janSz%2BELcYC5khRYKBIwQ399y%2BmfosIfh0fatm9rcqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO7%2BEDCrZdZlJqElZCrcA94UGuqc6nLS%2FaWXSdqaKiwXA5ylMNh%2B7NSTSxPGuQc8fmI1t6O5lfxVDq3U3cl7LNigtU5s7aEjvqcd7ePiol7qtSMhL8fhnlL%2BCdRIoNBgljZjSypWu5dxKzr%2BdgL%2FrIpGXKSc%2B%2BrJMKr2ptNhpxQKbHKYv1tPCXkPYdF9MFVyM%2BzibK6pAi38fEdGRWNGRnzyBCpU1mYEvvRNI%2FEwMBnVBjgvNroXkot8iSpsWS%2BDHNuqS2JAlKjLb5Fz2DSRTMexsuciOUy55cwyOzD2w1YRbG6d9%2B0B54rRyiakCnRfXkyPxoLOn%2BBd9o5uXcd4Jy1p2mJ0IukTruPRJENckyDGcFlPKHkGiJXIAXRN68NA%2FW%2BVX1s0AmrW7vwzjdDwYUQqn0c3HuZFNL%2BfwR0Vqn7YPCH%2FsIO6QjKi8yle2vQANmTzkbfQEF6RdvLwepqpWbLp2w40CNOsLY%2BBBMi8q6Txroycz%2BR9fJMl8uyJEOC%2Fxmh2rq6iWkZnDWUMx2Mir%2Flfxq0Nx3mYcd%2FHHK0hOex7V5GuQ1hmzYtkQUF4PIatwO%2BI1hZ5CfC8UNervh4hxDxknIAtHYw9Bfak96D2DggdTK7XH0Pv9IjOBxp8FJnUgViXMH%2F1eWKDtwm0MKGKkNEGOqUBuTWch%2FZAvctypnZmwih6jiJ4mj3mz0SSwtDSF8vU834aGUEap%2BmNOPfvLiqx%2BFyeN49PM%2F1RROcj0%2BqwJ%2FWcpES0vMpkH5zgRBkUPr85r8niiIBlWaaVW1ipTVCRowNoNibCCiAPhtUws53UadcdYkiqAHR2QSdpcXYRg%2FgNCGzHXr0zjanV8Jx7haO76k6WFq7tGN%2BnQXcSbACjZxdw2VKc89w5&X-Amz-Signature=1315fa1b299b1315697387d2b6adb4dd1f44104067051681ac03b4c58f2d00e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
