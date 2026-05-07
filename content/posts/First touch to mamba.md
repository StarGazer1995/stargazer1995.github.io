---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N6QX6ED%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T192426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGx7VmurxMbvxc3AslCysF8Eaaew5CNOZns71H3PtvV1AiEA0KqYVSi21VinjkXk7h6eS26K6zM7twt2U%2FiJTTBc8gMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPmFuYSydrhTKCkGHyrcA71h%2FREEUwkLWL3yHiYdrapgVlMcI%2Bg54qteOEpEtQFkzO7aYZC60X6EXmAd8fNdNd1GarY5E205%2Fsgga9zTzoSicIWCuhRE3niGHwfU%2Bw1hPhFVGDv1vkZLmGHSQrUtlAaImHdYD44H717O%2B24EoFZ%2FRoj8f0pWqdHQdB5ocGMluZUXVhxouhHifujTywEFD3zmPRR4wVOhXjXiXsjtwMjO%2F%2F7C0y3AWD5Hm4YhY2nkhMjuACKQAwXOQiKnX4z2YWCxzhrNsd8gGQ%2F3TpWZZHwMPTCIEL3B6HvwFpcywBcARP%2FlnCRVX7KzeCilKCFheIQ30y%2FJHn9YkuIIlpVVQBtaKiy7LBcPfS%2FAiiSf9IaxZ8NmLBWXwmTnmNQDjPbUgE0upcrW912Jm5mUDnIThiMx%2Fu9npjsFJzM4wIl1ZtPFRl%2B5XOd1JxxlYYD%2FVxjcf2qC8PQywZL6BTGo7s%2BSftW44%2FmkiWCVRauYw6tkjcbBel8giF30DOVslmqhMOAPIhGyQJbsWg7EQ9f046Uv5QKD0p5kigeZGBKjFMBowmlQYsyjccSey2FMPzr0qbb7fn1QFy%2FtXg8KwTBvrNgC7ZbtiDN2z9PBwEJ2MwLLR6o966qkFCe6pHOfjuz9MLSu888GOqUBYFIOWB9wxYkag%2Bf06IUeueiB7Wg40O3sH8zYs3ZvLkm36b4QCjFGhyW0foiNpqkugAdcLoXeLr8KQ7Jf12I5dSjHzld7l86qRdfcR2Nj1Qq%2BP4sPI1zJBJ3SqhNUhwCMVk12feE1tBXfbtcfxqf8yJlzrED%2FMDnY2NHEwpsYpqYGOTBTIX%2FIuzN8qnOxzsgYm9MMLHiDPbhHhYy0vfQQ0VXx81Kq&X-Amz-Signature=726c3eab0d4476ca8be23fa44050eb9c0accbaffbdd6634d4331e0c4d1906599&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
