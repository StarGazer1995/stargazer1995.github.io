---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGMBLZJV%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T225153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDgqgnnYSjkIaMB2qXWC1lO%2FXzjagN2BuyjGEkZ%2FMe4KwIhAN3MwylUMIWdRj60DYtotjspocOKFAuX%2FX6Ve0hNLAuKKv8DCA8QABoMNjM3NDIzMTgzODA1IgwlhsiynbSs5pmh0wwq3AMc83Sb1F7lbWGC%2F3TwMwxmeN8LraStHSvmTgTl6Xy1ROkU3pD%2BkpSLJYZVamEwY0DF7%2F5gHSsF2C%2FaXeCEKNN9kvMXrdISjVI5vSnSHAR2UvjMa3DEnD43ACqJnFIzh0%2FInAd0FDgMTc2Bdm7lgaebevjkIROrMaStFPkVwwNv8C3TNFCFOSqmxC5L3n7%2FGKIg%2BTKIY21j16xgwwDz2bWNaArr3d%2F5LXEeuE11PTYsHhyhkUf3zcQSVkDsnwowxKCSe%2BdF79YWwq%2FzZkcjHpMUD9EkK7cVwS83SQ%2BJzPEK%2BHfY3nhkN3P%2BXI8ZuuAC3RG8Jd7Qy3%2B3H07ChURT9Qi0HB7aOAMPrI3BH7JUjQ6vfEygpTFTDo9WtuAQLpGqNO%2BlymsI7J4lm6%2FZvaddKu1Q%2B%2FH%2BXsBES3qjPISbWd%2B3mvCT9DyL38gVjpXi0S0N4a9u5RqM20I5zgG%2By0Ry3nY9mh4hKtM9XUBExMLxyJQxkUEcpNKPuBNUKlPiKq6piRAKcJ3BJlSKRM1hR3TxZE%2BXPOjwI4ql9lStzbBzA5QoZwb4%2BJsz47165F6VwGXHfbIXgYv%2FibeVQC4pnoA3BVql55a3yWMqKTnptBnJyp%2B23dUvG6%2FnzWcYJvRmbzCHuY%2FTBjqkAa57nfJImA3Ejnc13NPx97g5gbiOayMYJWiBCyUNQaaPrX9eWl5fv1hbLHxN28Iw0aCjhG8ZRmvvotaJcK%2Ba2GNvDlEsS28v15fkfG6SYGCpC79cU3Evbtyw3GO59AZSAXQ1MnFVDNUcX9bJd%2F2zXOyOEawXEPb%2FqyWYI2bAMLOdsif%2BG%2BfgTHLDrmyP5a196eqZX33Ub%2BxvhvNhFlVCqm%2FdQKJP&X-Amz-Signature=e4360c6cf7b0028aad3241f98e0699ad719af0a787e6d4e589a225b0068dbaa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
