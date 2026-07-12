---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LBGFYHM%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T164332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQDz7lEKH764Ck8U%2FvxQIc06TXtMNWcmAj0izA1mLKMsMQIgQZ7MJOpUkrV95CGwFrtkQqnhnRnUmcmR22cw5LjcXvUqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzhKhzZDOxk6ao7IircA%2F6kSYq%2FdgVNiDkcTf8Gdo2EoTddVB47oUKedydNb26ALQmpm0%2BKCyk7Fxugk2mzUTpxVcDVgmY1NwcXS2wd2cqzaOphOafEXzJe72WUZkp4c5Kj9zvn7Ezl7MaPsXmu4KxIHX6wnnM4BrVwofy2H%2F8xpMeYiyRhwusp8DFGUPRi7tFPpNxvpkz3oU0ImKZBgTM9rNJSJinUTZt8GC%2FYJIFf33%2BH2i9qRcB%2FBaLJXY5ixMh4F56FuL3JLU3StwZw%2F3nmlLF4Hlx1MhGrYnyLbMNHrluKWkDqZ8eiw9GY5TLM8I37tffBTxPrnIp1KVGFqWIyr1BWELKSMiGe%2F%2Fpnpo%2BHhN1oSy5Fk5%2FsNX5I04n%2BJycwNH%2BSitI54y1dAKmkhqFaSNLV7I8yKZ2ggnh3I%2BfMCisyBBmx7LldwwJLuS6p0SYymA36MFLGelV0iHnH52267IxBJdJABLxsxEOLg8W8Y9JKJJxZ%2BrnP0Fn14xaUNILXFbONq3QN%2FOTjJaiiIReE%2BmuIOxPmypczdMrbwuVdNSTSxDIH3jnHEQRciCDiuKDt0InVrrkL155bp9BexDGkPJLtumQLjhDk%2F6v7b592pDsqCaYbiXLRMKhktlKO5dT7BcwZAlcPZu3bMK6CztIGOqUBm6%2FUQ6tmYN%2B3M84yXZtAAFkUyBhhwvK3OVNtdDLnBV1c16RfPr%2B0rsscNkwBkVuSKza8pKLZWuPMyrMEWFRyCE%2BYNoaJchGK%2BxcGw8sG%2FZSgRLPt1kZR3Grg%2BT6UM73hnkR%2FIGg8e1aR%2BCRxP2gZhp58NIGzWryMQ4QI9yeBXoyGS2XJgAcFKhdbcQgSHYqs%2FoEpqgwUXRIswZVnfNKqQkIvHiGT&X-Amz-Signature=84c89559e3029501a1ed03639de7b6e5d2aabb670f32438f2a6161d4f165aff3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
