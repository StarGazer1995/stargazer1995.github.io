---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBGUD2DL%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T135812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJHMEUCIQC%2BP4MCGj1PRdr%2FntzuPMQdHPfkA06BHwi7kIQwFDvBbAIgWkentrERXuKaoMAnfAmQx6Lt%2BrlHRrAd4MoCQiAmDLYq%2FwMIDhAAGgw2Mzc0MjMxODM4MDUiDMnPoo2XCV8kX7zKnircA8%2Bs8FSwcrg4q19c5Sk3Xc0W2nR8KIGcANlDMJp%2Bab6FDTlbIM9zmsHrJ4GOdlZyNXiw0JktKlu69CJ0xhlH%2Fidx6NfD8wjmXEywPlQ5oXpiJ5bGPW5M5O3ews6GF%2BH46wKIM2dH2Fj73b4TE6wAcKdh4dFj0nYfprkxbTwVQWAJL5gm4pfjwOjaJ8OORLNszcbWOdebkPN%2FxgsR1EEmAPlyLtrMHKAGVGbJCqLhU3NkGK8dC%2FYbGkJ8xtkgOgjN4sbG5JPcCWreNnGUACPb5yi4lkTTjFYGtSwcjZFK2SQRE7WyH4QhLHpZKxWVfJuwantmS8r9crW1MOLdjGD9NCN22pVPYUJwPlb25fvWFjkwjhYH0V5%2BJHep32xjpOPCI7AOvGzmreR2k23rNamDAp0y0tjx7BfoFWy0y0bdSqnNla8a0zVvP4KMyMAU0jMuwiR7gpGR28fGAcyZ8QzQDuLLHlLVCXpuvASXtg0oMRY3XYSpugLVE3qzXM8O%2FLJwVu0vei6sjLGN0M3p6Uf0f%2BwMF96IhDHGQeMn5f0GBp4z%2BVKwruKqvhKst%2FD5Wge6kCYbuoLExDmt4NM6Sh4jJlO8YuBoPBhXJuQHrgenDI0IzvJBCeiXE3ZHxXfTMJLVntIGOqUBO5raGOKkUUNZBzhLNiplnRlsTujETDB6ZTZOOyAtlaQsXONaaW0OctnV1kWqMWLPoOui4TjNwU4%2FenEX%2Ft7VwzaVNvlRhF73OcynvgS3A%2BK7mWnF9OPFqcZZJuDbbh8C4L61%2BIq9b4O%2BY3d2P%2BUMHmqtPLr2yfIvzpVcpNY3yBVDL%2FDMwbuNy6VmwrBMUgBYShCXxgyOVMuB0%2BLlGueUeYeQnL5t&X-Amz-Signature=f057a07e4e71f52b0a9092a6721639045669277ddb1b3aa16229b66e0735287c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
