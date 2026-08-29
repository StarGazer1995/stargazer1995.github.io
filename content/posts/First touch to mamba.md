---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBEIVQEP%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T043348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcacJyNnyX%2BT4TNPCvYRhjBWylsousCcHKydJXyn7OtwIgdS4KE6X125FiL4vZoL3tNX73xuUaSRWdxu3GW2MbGbEq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDYLwVxFI5AhpJ%2BU9CrcA1%2BaP%2F2H0k5iQsLGLoBiTnQjy7vKeXRUX%2FpnjJWT4XyI8xeI2QHwDqT%2FJqNlk21JgAzgaN0pmi5Gu2%2BIdYsVG15TXs8Byd2bRUmkZZG5EtngASIT9QT%2BjhD6wPTG%2Br%2Fz1CwzAWamDzZ0ujoZ8M1W2x%2BHQUURrLSj3iP2rDJNR83wPPsKYg1gCkoqhvNv0Gw4UEJp0vZa0xKRoLb2fuvq8mzdROiELtQhTzM8WAimekfPkWVdqEHWzPs4c1R6ffC%2BjZDWGwcLK2S301LoPKlfe%2BcZvpaOIMg20viuOeDLpdpPGjDTi%2BKroFXLSxPtudeVzHQAF99%2FsRz4IQ%2FEjZXxeORSU6nJ0KvI7XqT7lpnPyGa4sGaJwHnmCXnph%2FDWcRCzQgRt5DKj1UixeAKJvamjXdJhVE5DqCy8VC6NCidlfGMs%2Beg3any7DhYFwrqaPzr7F5EaMZGlq2Sz%2F%2FHE%2FxMLsE9K6E6akeFAk712JqIm9r7CBObsFkNX0GF0dtUBIuaiRaS1soqLBNLGJAVZAnUs8b1kDWnuvC5yiN06ZvmFHIJTe1aOAaN72MEZTLKLIb5Y8iqkGp0UAcZgsSCq7ulHKYvZVvNQjds7OQqyAQn16%2BzXel58UfNPX2a5FzgMPWUydQGOqUBYOSHI%2FcGYbNVaF7qc9pHafz0pIZXKKA50IxfR2bvIonYIxNencITWJWZpJLqvEiFl8zFgQtTHjiotKMnM%2Fj%2B%2FVyxdDfD3Ug07j1JFNxpZ%2BhgRWP48wRKH1rnHIJkNW1WsFSSMT1i90xDJEHG1sh3o40Ff8p%2BznHtCfBRsLx9pfkpP1erv7%2FMfulkej%2BfknKLV8qelp6Kf%2BSRB8TnnBFArQxRMc%2Bk&X-Amz-Signature=7f651751a19cc6d4bc051efffcf8dcb2482dde5c6e2229fe62556e5ca092ea64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
