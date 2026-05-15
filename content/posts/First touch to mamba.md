---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BP2YMUC%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T224407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDlNwOo8%2BU7Q%2Bs574LWI3mCIDCv94AVtmB%2FSYrdPR%2BPJAiBK9E85Poqjbd8hZcJpQUnYTRXFDc77NiL1iNc26ZJUqyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMiwaNGBD%2F1ScAtJjMKtwDUwo4jK6C2qmAroOVo3hPo9wIOH%2Bowpg71PaFMruP5iRVzupU3E1X774USDbwut2M5ty7oRPmUA7%2BmV5zlHKwfvaAgoeqtJp7TQ%2BW1eg2f5b1afUfYNIaqw5divpOv6tuV87E4Qk%2B%2BFRtTIqeJEZy2FRg%2B9b%2BdqpdtqWvcLQHl3Qu%2Fd5%2BGY7eT5AN7jpDZC4QacUpAyRNtWjj7pTlPV%2B1%2BqxFrz9%2B2wfcNpGQuW401TJ2%2BECUI3RkfoFiPXnRQsNQwnoD7hIMgFjG467YP3jyQIZFzCCcMIZl%2BLAfE%2Fvc4R1sX8%2FJuUkGkhD3ILCFroNYIBrUTaXWDmac8IaveykR%2BTmjRMUcnZpAxJNhA81eh0LDtzayU1JjlYQVHAQ%2Fod49vsLg8yKGX7Xif2HsqFstKmMbBwc0SgBeZrVFn6ntV%2BuDgJUKXkgKic6dMad3lZmvlSK%2FeADBOlbJwu6z1louvJJoUkqz0qjugSLjP0OFp9MiVbf534tmTe6qQyvr1VDbXIMO9Opftx%2BXvF4hfKau%2Faa7W3wl4Kqb24O9cyve8pdl4TbqoLYmn3aoN9kZ8QIpqFclBZRAKjlYPLeI1qbo6yw5tW3MHTySP0X1h7XqIiMsWgs6Z6NihFrD6u8w9LCe0AY6pgGSKG4oZxl2F5Xv2bMirsovaWWa7d0fjMFML8sjN%2FmLZmMg0jWyktjHK%2FSqOVTwHrcr0CQrsTUwsXPHEs%2FEXv5dTCw1qGU8yuvzD8me1p45b7C7vvrttRC63rJKyEl7GgSdr8pMd%2BL1Gntqn8c7NadMtQlDejX%2BGu3f%2BMQ6B2t9T%2FCJUP88F9RMzfR1Vr8yM%2F5s%2FE1zRe19FdyQC%2FQHTAHxXkbd1rYf&X-Amz-Signature=10572e96f01979b7bd2a0e9dcd7b9580898fa8e8dedb2f7fc7110c377dcacc3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
