---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH5JHV2Q%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T231607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNJvA1FOyb2fHllXEWLoNcCWxk3HZdsmCubsMXafbgVgIhAM%2FZ48O8rKydsV2ZEkvedqHlIymlsyANGfAK%2BcOBwzobKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRn5LDklQ1X5mVg4Eq3AOdybNo6n%2BYxFk0bPZEYBF2nJT8a2wcBeDXADUXFGG5ED1pd4HC9OiLKJVBSbeq2GGIw4lqAGkIHBD5%2F2Qt89pBIfV6zspm9UUE2TYICu33sKgXPiQVlWQEC%2FPXaUbE%2F19Eu4hVV5%2B8uU%2F89L445itvhCkGjkiTI1xQRkAHX2A%2B4yiFTRCmCo1jyH3OxpL8g15ZXAgd3FyiZGwdwDkWAjFMlRKic93nBv0kv9vFBKdiOliqMSD6zbZ8bQ%2FQPSmvAr9suBVW5tHHfL11tDmkdT9mFSqtwOf4v4MQIBQud%2F8OIGg8jo6KbvWAWTwDSLS1q%2FhNVZ9espLyQT5eEHvrSSOsf1oGqCejl3NzWKRPzll4VDtzSVZ4W5Y5wzrHRXt73dTKA4hoMnNnbI%2FyA5UvyVBoh%2F6H%2BeN3jgED66S7ANQbSnjWdqU5I%2Bqn%2FtQstOMebwbOm04Sp2nagxYYRg0AD1dSw2uYSowzwzUXW1BbOBBQ3YQNM%2FfKXB%2BFF%2FZM%2FiMzW0LQdQSNUxwCHu5ZCb5z1TFZVEcgmxpifzltMxFg5m0lWbA%2BGhSzct24z%2BH99RCBm2c7LKHQrQ1vN4zY%2B0DJ61q2imvYvPdZ9L9g6kZlgn2MwCj33bBHZ1dqnGh6tDDyrMzRBjqkAfsZ%2BRz1Auvb%2FlI0F%2B0cUWSQCrolozqZqbDF%2Bj3bWBNz4m9cDjxCBRo1nKl%2FIFFP3CO1B5P2lMpfJvrOVmdlNQH53e6dEmR3huHvEVMwzt3%2FdGk9CruBNdLLd9xvbUlV2AMpOsz3bKYkcAHcQ9HigCgt04Yj08lCIWghmd6ZDDPvFIQCIPmgXC1sR2mdCY1gRhCJxfKcq%2FcbPLe6aSNJohPpxsX%2B&X-Amz-Signature=03a45d2f987fad4094395e5ea3fb9047bab55159b35c40972daf907ca1c03c86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
