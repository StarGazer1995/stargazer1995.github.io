---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF67CJA7%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T172450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHGWOx857cR5vJZenylUMiVU5RAVTNR5%2BZHAN7DqI%2BVAAiAk%2FWxKJNvkKTUVk9ZamjgXSeGIpEQODQuZu%2Bt%2Fr11SQir%2FAwhyEAAaDDYzNzQyMzE4MzgwNSIMf2rCwtMSuuMKgBteKtwD0iZ5wIDBy5MSpBRh5l51Uvs1iUCg92aQ9j5gC9lUF1AJuXWNmcERZ36DbVP0Cv5iLDQU%2BvPNbr0vf1Gf%2BhDIs7mTWeIM6KUTVUeedW6kVu51h%2BRb4eQl7IQh6G%2FhnrQKi7xCQs8LgKTBBHwM6CcCmTUczQCRmH8H7JtvVWJY%2BXOHHVbtMqh6iyBAogVK81H8M0sv4oBiXUJPS6PAw6XFfV3%2B6YKV2fcUeACD2WePhbwomqARo7Lye3IYwaOTY4IKtrWRmZbL5vLWTuEY97aMFQzew1Wi8lllAdh%2BpXgqt370wwFpBJBvYeBz6Ohh%2F%2FICDj0POYpCIugr%2FdtiAyQjh%2BpU3qxSW92pCI%2BmML%2FzwmvdGpvuPW0SpCDS8Hqjl%2FyriqNFPhdgHg5gIaC3DfD3km6aHFpLHO8VXM0NvaY%2FGHKcjouOAhRRESyQT05S5IUBIgizR1sU81CnNvIslCyeN%2FUtRfanRW%2FXZEyf93FonlgDRbrnytlqrhbjCORS7vNcU2JhlYfiDlW1JfO2t81nBXRmvz7%2Fzj08uoJO8kGpkzqzeofTf5B3mlLjmWQCD%2FwfZJAZkUxDGnueSfIjvHqvLHJ03%2BjebihaW8Xw2wRQk3rvhCww3fPzA4FKGFIwkKaG1QY6pgFPekGGyVaTPrRW8ONecmVkII6ThetlGYbu%2BkZtP6KRE1xlW0p%2FwBW%2Bow7HcCHTFRbjn1m6CdDQs8elf2RopKea9Uhma4ETaNg9dMABnWXZk60554d8jQL28u5g8VHrdIQd%2BpMI2iRCixVxKVWLNXPNpJXhmbs6GQgWTVXznU%2BlU%2FxrZtVwwuQkomQ0OJvJ9eMNvEsBHNwM2Gj1HcqkdYRroBD95qDq&X-Amz-Signature=6fb7c463078fccf9d668c37b776d29c5f123e8e1e2b47a38360ab7cf7adbf804&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
