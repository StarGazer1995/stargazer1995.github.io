---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637LTBNYI%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T041925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIHji4O9ZnYzNrtK%2Fx9yGTC7fjZxvHYTbnfVFqekEIHceAiEAzXWJ5CzUoZ9bLg0UfsoH4UVRNKzXiQVlY%2FlcHxlwKbYq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDOrEi8TqVU1k6lFisCrcA9FsEeAaXCZbqbfB9xyMeqovbt8Exf7JrAuKucRMJ36QYEj8nOSuYBxdpDSdrB4fST3Pn9ifWyqXN7fDsFOM8rdOdAe6YmQSTwEdpu4GTLsPG0yeDZS85GBsJ32pfXpvEKhCm%2BP5sv56w4qJEyNNxLpZfYD2Bp8BEthurfxGzkuJsnrpVu9br1ajbp%2BCliPufQhufme8UFDpcXFOsaJnYU%2FeZpHpFhhMf4u7XEQDpd%2Bqn15%2F7HdnP5pUacr0cjZ71v33dcfhvVuxkwtBYuY5G%2BZE2CBizO%2B7CZaKcRRHQ8mJWmvFuJgkxvU%2BxrHFCKsZkAfis7c0DGiSw91GICsowfbHvS3OetwFLxdZ%2BaNz5qW2or3SaYMbbnaxEBCZgP3t7pgJdSNdM93LDHES4b2n0%2F0zIbZ%2FByjJl1LZMNBnuyHKkhdkzq9bTI9a%2BCKEeBrKtFMZnB4ad%2BlsBQFPi428FLYNSz5LMJ0KzF9Ld0Ds4%2BvbNu3z0qKlQUiXWPC%2F6QsSe6ANxCHPk1dfwVvjn6lPBdoMSQDLCyVwAbJ5XqwNwJFqrnC4ZAcQ9VQVmxsGAY%2BwANnMOXNSHkoQsjIxTe%2FpLTi8jx4Qk3lpb%2FrveL5V47K7AWpZZh6IXVAfac2vMMr9%2FtMGOqUBR77RIiZvg1VCTGd%2FGJaijLAF1tEWFAnOuir6nN816p05Rr8b%2FyY7%2FrC7F%2Bb6oKwXvylwy1fJGXksJn7Shegg%2BQm6f5acYMPCKBPscSL4lCGWWyIdUrfEvJGShxqvdRWrX6TuZr5hFiko909JDMMJmVKRaQYeJGDi%2BvvvAdRqtm9LSTd1hPXbklWK%2BAeZl3IFQ%2FQR6vnTI1QZKnieyGGhy0DL1Kgy&X-Amz-Signature=9ebef48a44937badfd9bbcdb9e1a8f0de9aa982c1545a8a028ec2ae045ff2a52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
