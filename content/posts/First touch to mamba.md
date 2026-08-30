---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOGB2TMF%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T221217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzzfq4t4FgsMpug%2BCx6wS9z11A1pA%2B%2FtD0x3RqCyNEBwIhAOV16G06ubo17yBAefsbVDm4TybgIz%2BZJbxU7esx7YQ9KogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxkTeuPgdOs9UQLPnUq3ANDOxZCwYJbV%2BTsKw%2BUWvpIFeGIACAj2H0BY4VmwrHp%2FywRr9He0%2BOmU85WI37gCkmy%2BA%2BDJBfwCwG70qDeceeNFarJkPPPgp0HdOPkhpApadv7ruZVGLew6mP%2BqFiO07I%2FCb5qtuUdG1hUFKeDdarhBi5rFa6oydw%2FLyk%2BZzgLASdWvbCKlRTkfnvmbiNThsL2Y8m67srouw2ozXLYyikRaIEdS7TgUJaeFY0P6dFcCnXr1HTUmIcUjqtmXor5jR8Pb0bWGdjUqwvAqhJ3bnJosDGCXLP7LZ8WuK61gf87b7NnwbCvl7GG9rYuR%2B02UR27uot3KC%2FMiqmfg%2F6kO%2FsTwZKRa3Q%2FDYEQ3y0bJY%2BSMaiPQyLIycPfIZJFZ2e5rkN5wCWkHoZaK43BFfCtKsufidioaEPkj6qv5DyFDx3hhuJSCbVc1W%2FY9CUgU3TDnEYAOg8PZGMu2EYK5GMnOfX2UXIrNjwGCk4pu205%2BH5YkGU82qzux%2FU9z0cUp04P%2FeErmUqX7GB4NMqy5oZ5kWDsz8DkzoLkRkhlO9MfzqCnt3PN0Hz8zxxJG0NjQIxy4M0IxNQGDP06fwJZ2vFSrNUyMTEPkcpZbr5j8U5TZr8iqHGLXx%2F54okui3XnLDCrxtLUBjqkAezuWAUnFWVHCwmQVuKNfH%2BjZl0fyuZsAuqHJtBJ%2Fm%2F22rBTgIFDvalQBbI7h7wgW4%2Bv5ixbHt%2B1O589bwB8XPes2PgslS31Vr7NXFV1Mg2ohxXkFMUrHmQ8ZSdGht5PWxpbCqZDOAYzGKqZ%2B7MDjJqtIF8Ty1I8iE%2BRdpj9xhWDBnm5ITVg6ELRLJLin6%2F9l7%2FLffxpf3VAylGhGNxCYRt24vYk&X-Amz-Signature=34ab9aaa83afbdfc7ffe4e198bfcc65481621d846a1bce3c922d162a483e4d9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
