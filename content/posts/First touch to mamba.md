---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPSPMCHI%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T063952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDelk9mUbB1xP9QhY2yLiSuijX%2FZsvWU8X%2BqLi84u1%2B6QIgSqqwC8WOhjBrldrPx6ryzUKDyprCxoHFgVdou3RpmQ8qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEnqA7IHINt1FfB9LircAxKHLVwPbRcJ5fSkFuoQVJqSpAwHEmKmJvgbUt%2FSUe2Hvt1PguO5BJ85WeeNdxPvpnMu%2F%2FlI%2FH5IE8l0qlLDZpTPmrKApPyPOjjyVmtYB10wcCqAe3yFtUbsbDHzObRmj%2B%2FsSpC6geaoacREGVFLQNNx9lmvE95KfWdCZe8O3jZac1YuwQ2Gecp96uv9qimLskiDSSmi6ZC5as0yiGVvOcdgvmIywE%2F3Uu6X7CbEhWo8jJjRg15aJojSfWCEkgIfbKjGCFua5hZjabjyMCbHJZ7Y7F%2Bna%2F2He%2BaZnf0%2FkD6uZf5cCbml4S4HuUs7hpjZBDufnWO5anwldbda9nlbdykjiaoa6TWOouIaxtmc9phy0Ixv%2BCVPoYBrg35eYwCFXoy9teXTVCLGTfsYQDo0eUYigm7JC9po9UNH5WCUMtdYIySTqOyT51CIku25zx95PjPDjMlWyZlCuRPKVp20s2Me1dUsfoDUUKZ7mym0TnvIoGL3RPFP3sHtvrXxL%2BAsJi%2Bups%2FFz7TG%2BXt%2Firqyh3oG2sUfwTNVUiz4GTDUx%2BL6HpwCVKE6x20TJBuFFJ4ZmGpwKWgwXgf1zmUMIV4UXTS24fz5TYHB2WMj8toROByyxZyRs6zXye%2BL4KE8MK2w6dQGOqUBlLGOBkcI57AkP1i6qw%2Fq%2FyrJIS6ZW3ahcxYlSM8ugZDkIOX%2FofI3sr0BPY7fU9q3L7TdvQ3gFKqjwq0hNDQuKOUR4rOtgrLz3JSGQEL0hHoHYQ5%2BmxCcQ2lPozBn8aS5XIUbXyA58pf0oUsC9dD5gLGgZByIwDU2upZR47bPwdcMBft4xFMOTgaCC7B3b2n2CtxJkNUXui2pNF2q6AMGOJG523jm&X-Amz-Signature=1c9817bfe9d31ef64f85707e0d2702c906290b19c57fcdd42ebcb8661e95d648&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
