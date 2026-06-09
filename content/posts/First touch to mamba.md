---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZFGJABB%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T093956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDDE2BjrZ%2Bdos7CFXz0XoLX589F%2Baf8qvcFCOb2wTbVTQIgHZEsjUPPjCOd8AlSLKqa1i0nLC4YcQlYQ2OcSnk6SzsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJneD3iXxF0ShrUdDyrcA%2F7BJ5uYrVqh0pDjSsb2ut3cWJh2k4UnZNOCtzoTHmwyc%2BT2UnSaHabF8CNuOPnFDLxUR1UXCjCxvQJx3rWgB7NAYs3%2BwFo2HyCiDgaSTnjgC5%2FSGl%2FVvSjV1XOyCcJNaveNXAVaT%2F4rEVxQEbqTHQOdJzex9oV0fNUKV90psD8Jy5bx2JGpm1D6J1TdjbV559X7kzh1VHk83LE80qL2FjGrfQhUY1yCIR7FLRygQLKdV0HUefUuAWJuJrBQ3M2KWyROr%2FkzdYWvVFWXfAe7%2BxkvWgGznSSZH7htsxgRjzj7I5D0gp07xDyarfhtiWmCCjwW%2B7kW97Q9CuLgJUkO4Tmaa%2BgfAMXYzYDUFOFYBKKC3ZgYDtMjxrZcQtpQWaJhfl7ZA9ptSkxD0Uj0bY9a%2FtRe8BBzGJCt460bTIp37w4XXUIsgnymxjD2eBasgpFVWgjxLfvlK0agE9niAdQ0JFzn3uv8JzxRzVI8rBXlWU0edv5x%2BgJaeyfgoJQpRl5E6PnM7c6gln%2F6D8iECHi0uX7PMQmmTwDyaij%2F3YwR1QvEk6e7Cim9%2FYko972jStoPFz6oj%2BZvvu9hhXPnlQC45BT7%2F5hy%2F3txWs%2FKisheh9A%2BI2BTnADhlWeiWahGMNK6n9EGOqUBvUUjpPCmfjOFUnY2tZ8R76Zoe8lM0O2Lu%2FZk6D63B2f9X4IcpHI%2BoTmft7HbKPtTHsClhuqiasaPfEPmwMqjTZiAbcFHNnbEopFdq8K37MVA8dF1RG9w3dgBzh%2B0Rob9aWx7u2GgcHrYFtrHg2Mzo5kTIp4TMdOflaoHkE4uP7p4tcADI76ybo4naK9wSoWjIL0vYBNc0jUP2FRZTmw1u1XHOxvz&X-Amz-Signature=6efc06bec3de35042c4802fe45cc9a408e0356c1eaa35c2db77185bb21a45ada&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
