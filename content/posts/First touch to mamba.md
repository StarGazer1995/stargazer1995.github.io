---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCPXNCKX%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T082010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIECPrNyknCbLXJia3Dysa7COyct3EmwVS5sH7UvJSKM0AiBbsr8eTLApfnotE7dM6eeOail6xZSP7kcEddlkNnUbkSr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMwac1wVfghKKstQC5KtwDCGgArDMIj5grgvRPR4g9i6jgt0uSFWhd%2BMZpN1UmQdCg9504Si6xZJP8%2FDH7ge2x6kj4ODOLeYvMYkTdn94fu9kehKVn05qhakHSL0r%2FsVpamgubRkbj6LfWuPOlqn8o6oTaviO4DZ0lecgnCEpHCQGprYFA%2BIaaG8QGKYoSaxj%2FxpYojhnWQAtX5k9K8WdtulZe5f7nXimDsizkHv8wbSCADvMrMYpqvddMLtBqOA0GDo1ycCNs68XuG%2F9j%2FA0GDoWIOkT0rkcl0RfX4ZQa%2BcyzN8YRrgPvi5j7WtseY%2FT1c%2BQglTB6McgnMVCr90XRp5S%2F6bRQckeZRPcHXTFXL6cRhwjBaFtfyvipnOIIazQdr15o5dDv2b%2BBkhSxaU3m1Y2wctT7Dz9N8nhf4oAvK8m4U3%2FGWyHccKQiTuhqaFDB%2FhMvdLCzolEAw74Km0ZZQL7WybW7%2Baty5Ssw60VkzLwvdrwBUi%2FARHou6GmjKZGkHPCTRjZHNTMj%2FcQSUdgq3X1JGc7aTYRT8QtPwSPEdfvnYwnCTMsiR7EBv5yf6cfAopiLL3XuQcedkjsAyUxFIqZUxL6zvBOgZm8ek98cg8YYdIULZOGaR6DrRrBaHotJQL13uZ3rsOvnRB4w0%2Fai0gY6pgEBuUAwODpMPT5quE96%2F0%2BxTX2DQqF9LREhoRN6EJR21Q2FehY%2BAays9un7n1GuyfbVy3arzBM5s2a%2B%2F4vyt%2BiJ7bFpq5PDvR3h%2FR6iDccKD6Iqx%2BA2QE3ta5A%2F%2F8Ru2%2BMC72q41I0YsumGyWMv3QIUVx89vUOIrjp7694PvLeyvKK3fnKz%2B3l7UkMu9txR1F7P2tw5%2Foe2b6t6ixfzn%2FBJZ8iXgDJu&X-Amz-Signature=e6d1a667e6b39b979daf76d1d9085102af3275a0194ff17fd5a2b77527453df7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
