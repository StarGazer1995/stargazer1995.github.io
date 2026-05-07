---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673MQZUHH%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T052219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA7CoSKUJ3UmBiBgJy2SjYm69gPgqohyoXHBK%2BJNyUa1AiEApH%2F%2Fxujk1ss%2BbxhPluEekkJUsO%2BBAElaS5v9QICZp6wqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRy1lNxNXouGYejTSrcA0Zi4HZKJ42b8cPx2MLxqW%2Fe%2FfIenlWAWmKnBdS%2BiR%2Fiont30Gzjr0radBceBhUIgYWkvedBKefdbBiwn1SmwHr%2FPY37Z%2F9uEYRbr3CJvFo2WVw%2F2vjEvs70JpvkvQgY2cexaAqRvIN%2BHx6FDrz2dCCIyJxOmr82Fhr9agay7CiSR89ZuixiAydoh8dBg8comqD497r7%2FD40pwTu%2BjjXX3ENgbineq01aRFs55q5YeAkwQkHNmb4mQB8%2BpJE8OA0F961jACPylw0T48bQtfuZoeNI5LL4XIOvm5f7wj4fB5BOBod7lWI8oRk2AhVN9eCI6Tb84q7xsmuNUMXuNdJt5yZ8vZTgcB1am6psCTzhZNj5i%2FgrlINf5QilTkRheLIk9kcdD6Mrq57UePbAgAHC%2B%2FdIAfvrZv%2FrL6a%2F81Kr0%2F8WL2kFl4kax6vPJMizUgqppHDx4wLSy5zjgOCaxLygkdJkTKzBNOc9wZfRZ%2FBCjszgnJjfM0r1wX5Qg8NbrZqGElhD8RieCfJRydYc66yxFjP8V2PFUpFHsmApuuiSE9FcQLn68ERqtjpWhM3RbLPTQxQKqW7na8gyfIH%2FHahFp6C3SinCwJSdgB9s6LN813tkDOQXws3iZt7H8IdMMOy8M8GOqUBmD2UZS3D6mXs9d2shUoAsBRZ6UNc3evvmWiG2Xp37qnCfEaOUiVKxJRZHSbyXKaODGkdhGQMMIhtjq3YvdXqHlfDYB7WkgyH5eUOYnwLHJv99IMkadK13gthzkZrJe3NtHBJdPwuOnSRxdkuGc2RLkQdrfJtpOQ2skp1VNNgisxBy7rDriGYzgG0RmzX%2Bz1tTR5g1R4GzALoMlO%2B1Z4Tyec42acR&X-Amz-Signature=d043833f4f77029973f85048d98eaaaf8d3251b00ac833108c514e26a5bba82d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
