---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REVKJPMV%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T140316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDd8dQxQvd%2BuumH5Tlckz%2BEbn9VIHzQEI0ue4lVLPYtXwIhAPuTQ1j8ohd7p9BjY0tcFHa%2BXbom0UXBxDGzIwTgmK7PKv8DCEcQABoMNjM3NDIzMTgzODA1IgzKkMkRrNwNw3VQjzMq3AMjYPAJSZEPEB79Z0RZh04RZzbPPbqA%2BEaCqap1ZPscmJJAtpc5G2cosC8VEuKn7xVIQtaA1JZe5rCSseRlu1khitTQAjNHj%2FwkkzvYjJLYh%2F%2BJksugZC2Lmcpw4%2BV1gdL5xIQBH9fD71O%2Bnn5NwV4BvdcxZxe%2Bb4O%2FUezxiZ8G8w1bvM7FWPnC9%2BhAwz0btPntJRTeuA7SC7BAI%2FHhezfNBCR3OWcm%2BPF7sp%2FhdV%2BeVez%2BrGlbUeGCqlxA3D%2BUQzHsQEGK3qfp5Kd%2FNOhldCO95x2jNOhwmkfZvXdOIQe1%2B2JI6XYAmx4%2FYYwqdBVfj9OMYoguOZIdqwdhFon%2Fy8D8%2F7hL7QfvMmh1wzd2tRNIv8O7Tlkm2JOTRvBeRuBddCUSNPx%2F1h8umdcFLlkP7HpOt4Yf1Igzkk9b3VaTy28loK9KKBHh4OHHOw9AV4jqLqawUPUEySQloWAq4hMrZIA%2FF3RQCIUbkwX%2B4oYAz5eufL72f7agQo%2FN%2F9B%2Byeh1bpeB3iHjzfBbuSOOlbCJ2V09qtsPCAM59VVfPUSGqJJ8pc%2FV8DFbRtYftKAcRIBnw24OaSnNvF7c3blMM5rlPuay6sunvCXAivhyrRDRhaS2kkxKAvmwiCpU%2Ft50sTCk%2BpHQBjqkASHn4BAfXabbXMcf1NqY7CD0GMq4rMGjKrQnFQsGc35GW%2F8froWAZxjjNEGL7tt51N1%2BdSZmUxfQEYUGOkYdIxLBK7asCbYtLa4v5S5hbzjTV2mC34OmhqSljy4sHI%2FAtKc5yt2O1T0Ph3jPbMKOrxSDKdUM1dGmtlfbj1KbTp2UNrAVvzYfvQHABP2IEE83U5PfhUwdc%2F9szdKg7CnDKofs0Fn3&X-Amz-Signature=7857a136eb8256f188cc701208b27afa1e387d13d55ad12ba256e4bcfaa51b07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
