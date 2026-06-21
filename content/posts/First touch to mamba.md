---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ULCKNGA%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T171710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDsmrr3nvJL0W9eNBBOjI15PSJbRQ8ZSkWhcqWKPNQcgQIgQcY6DDcIJpkwVrQUQe86u5TfOMj3qRhuc%2FSrK47l9CoqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0%2FrI2RpUAmiRZ%2FZCrcA%2F%2B9neDgqwmiP5Q29PMBb983kc%2B1FPR6cpHuOdlv6LakvlbT49VM13%2BId44XuGukHRz%2FLS2RTb2Ew02%2BEwtgfLOXk8Nr2w%2F5VFx06C8FbWgsWf0OeZuv1%2BAtkkjzzYS28cj0a6%2B7p0x8L5jCHekL%2BQXz2vNeJp3xTFPgc4%2F4db5Yh58SmHOwE3TYdZRpZcYawWzgd9kbZKWkTesnP%2FA20vHwDfFRnr7E0qzrP3uKUiF9amSPcwp%2Fmjz3BBhPV%2FKmn%2Bg7OOHiYjdL91FvpBmcJNn5cWeSHkWi530MYuc8QR2hBFm1eQ8o%2FDUFFvIlXVW6m00%2FcbA6wp8tJDys1Be3PZzOCLi%2FD8I4kyF2Bo0YmkDtUlDyZZf3U%2Fx37xQhbKwgIxsZRll8%2FpAUKkN7DIIx05fuBQpUvgaz%2FwMLh9rS19ccvzp9TMNvIo4AuKtaLAMaOhn8fJrqoHWAU1mElk%2FehOo79a5Zy36bAJTjGH%2BlC1UAM7rOH5gftRemoPtAEnyTERoYeDJiamV9QMvITFetfav9gv1b0wFUhxSVuLxuFQfvprwSm6UvDpxGXpc5%2F6wQvMbLzUOqKG0VcpVtwkAT7C4utG%2Bs2kVN%2BYuUCp5yI2Hu6upl2wjPPEY4NiLEMNOl4NEGOqUBE%2BQVAlI9kBrbBDLCQVC%2BikGnpjhVCfuaFVL4Yrw%2FodZn3du%2BXucf1wBZJtJKWkqU%2Bjm6%2FdlEe9VkcRWx61UbLe0BB%2Fnn9VI5o9rTTFv7P079B9nOqW8NkhKqmpwIx7rNDgWnxhxLN7bl39mVXb74VKskSymPM0wHAw28J4TBJRn6YuJW4KevcnUPv3G4WqOpHJLCQC3Mxab2uxiDIjHpXVKNFmPm&X-Amz-Signature=81d0faf4722b25b771e51fe8bb5340a8db61a0b485d79a272cbe83095ea0cd3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
