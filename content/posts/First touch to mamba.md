---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LGNPYVW%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T074956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIQCN1Rv5pxw0mXcjSoek3lkw190YNgyYnEPadQpPU82uZQIgCPU%2FK2b0V4SO2We2%2F%2FFffFEE%2FqgbJ%2FRDYouUz%2Bc%2FW18qiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNFmQ3qp02dx3mvlOircA4IuKi1%2F1UW4uMByKE%2BR8EPMxZaQlga6t7QGtC8fqQ61uduK7%2F8YS9OgmiXAlJctKxmERFiuhHP8X9Uho%2BfGVM9Dc%2FFruqErhZzHnSSMNTfn5ghD8lboaiFTd9g7ssVyU5TpEdYzqJWRJr4ZfVptWx32UWWzTxMIoQavruKxf%2FG3fcRXSP4kwxUp66HFd0b2yTUO%2FHP%2Ftwutxsu9c7Iujju5pMNCC08QMkQOidQet6QGvoX%2Fl3eXeNy9omngeNe02tMvvCjHImPTs%2BJRRYG%2BTZ%2FjUyUBokEyl8LwUOz4x%2BGsN6dPC%2Btsr9JOu7qUvYPkqrK4XqGYTP9jp10eyeKBRDw2avmt4W5mr2XRKiOTV1M1nFYybXR0mW%2BUftxSxnndMkC1%2Bsa3Xo8Zn6qAfcvCkACi7y7wISp1QR4gzOuPfUli3bL7KZVnzUE92hw7KSnTB6nzIrGDO4qdZYR5tOS8peAg3UXNn2mlzwzFARz665iZP5X3B%2BpGireZA30a23CRb8uPkrXKU%2FAgl4z7cH8DThfScnsEVVVtI84jCe5Eo2gcCeWrcrwvc3OESigeVMpEJ5I5BY6c6jFpwzJc%2Bd9ftHtJPesgVhoiicOi6Us%2FOw%2BKFyCJZBuEUWXUyAzBMP2bjdYGOqUBduUaBtXp%2BvZOKw0g%2BlW8rrwud5Ww5ufyuX70rl8knvKPKlkMeSVUKxfIxLd%2FRlT0huqbPg9SR2qmEHRiseFSqfuxINef9zl0T3YmaNqRILYqnAsxMMUU2dcV3J2XW7sP%2BtFDUSQ%2FW6W2IO8lt07Q7y3waLjjFPhGfSYApycfTplyPSxwDX3sLbU3SsPOnOlzwwv7ycmz82N9aITKc5hum209Zxof&X-Amz-Signature=3d25a6f83a77b5092695126c985cf9d9747d7d14a7e1682f8e96631fecfd7653&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
