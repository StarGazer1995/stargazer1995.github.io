---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBBAGB3%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T104724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD1zZeV7tayDHmlqP%2Fi%2FhfWPjZRvz0qxs2NmW7AH0OIPQIhANNpgLuzGbYUCH5gYv6Ea8MmAJuXU%2BncOEqtJnRsFY3hKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGaA9AkuZPriYkQKcq3ANw6H53lLOmSq1%2FSH5sR688pBmWz9iKUoWM7jaOBxahlYlXHt0xSW5428s5pUx3wQLGBu3GIgWKesihltRnFzR%2B%2Bx8L7qGP81WcSpcZXnG79BZer5Uu049pVW9kyTvAEzI40Nl43yVze46UollWMZA5e4lJCfuM%2F8IHhKjHxs1nbYCncPI%2BHtHHTx2ZZT2q8ihi5UVN2eODzYcWYf9XZFfkLC47CQ%2BfRVaBApq43Vn3Td09%2B9fKUplkgp0smppA7NblsgwIW5ely2%2Bq2VMtWegsQ0Inx8%2FKfVfuQUdyOwmVTObCt9BRg6SR3vxDj%2FIZ13kTGFQiBit8%2BYdegwW0ruINL0JaH%2FKIvZxKfYgviyjeNMvxLt6DdRdq1tPHPmknpd8YSFSBNhY7QRAA2J3v8O8dqlzIJb3e7W174UaqySMKrrynhjE%2FbjJIedFKkMNOuWp4CpWnVUGLJNkcnw9GTDGy5u9NXtFGCU9lFgBSxstw5OxbDZfBnADJrIiuus0ui6frKUo4%2BN%2BnCaC4AeX%2FNYMFhmzC1yhIlJOnzvXfAvv1S05SMMuz3I0jrrocgMU8XC0JYiXB%2FpCKMsywmujczTl%2F%2BgODUt%2F7azVqFbpzQIvH%2FsoAaRftf5V391LRQDCzxPvTBjqkAWqT%2BdeYslkZVDuUCaOLE9SyxfQNlxCsopwJEfhPl%2BCBJA6vJl2t%2F6S33CixNHSMaPgGgpGo4iQnQ9XByScdHUGAvQ5qSYbU5V%2BaBWeD%2FKerj3FMHtI%2FohLBNOxuazvKyXGhonSkpw58Aoe7Okew4coURABtj2g7pDjvqiWPv5Be%2B8JwkYCApVfxgSRyatjLdB7v%2F%2Bkj3CdXWBDeLbpdUoiCz3ye&X-Amz-Signature=2614360355ff74f99d75c7f2784527afd2c148bb1706ed352eba2ba4f8722f9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
