---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOWHVLWO%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T205925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6JTBYMi4%2Fg0dykHtazok3NgYZF1MPUOuaiFqzEFP3KQIhAM886kSBHawOHAkprnGM01P8N%2BibgwtZk0mYLP4FJrbgKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsnIxuclvNXUoej80q3APao6wXQ5UIMHSM3aq5rX7jQXtPwfVG0HO37%2FE0Kt2U7lCFm3krQVp6ENTcUPBIaXPZCEtxFdJ%2FjGYu93lB7I0QLmokjYnYInT3aL%2BpQ7QciLWrOVycLOw4BZC4NP10ev3we7giQJ9WzYb31L8R7H3Urg7WJYk6j3Ei4eRkJQaozrFIBi5hkvkhgHsZG32cL0A0e1bNJrdB7%2BVw7XTAnhvFG8MpeRRHdlRq8RaXF6qIZI9rrrkCMgpgDrvfnjPM3L1xUCnePCxTW2cGeqH0wFKfYYMUEjg5p8DT5dkMJRuyZ53xXCXg0S1AkYEKmtZoNA2i70k%2FPywm%2BMjxqjkMjiypEbRvmLF4oi7n9oedbWr8M0BLw7kG64EqJn56SQQsX9tfKrrZQp84xFHMMIcRtC77YhJ0t4%2FHFJmJoTcslH72ntOC3tSSarexV%2BMqcZFSj1z6rMDqD3SBQP%2BqL%2BokM6pTBEogNKdCQ99uOvtxqcKhQmNWtMe0uBUPCtodRfmu1kxKZKPL1or6F8uvyYVsyWSwwjvXzC0qL4UHneFvPu5X8TWCLbTzDuTQ%2BAhiB5jGupNQlItpw51%2Fv5PtwzOnj5BZydgMPG2B3kfNHE5Ye%2BKCjlQnz3iW1bV7B1b68jD24pbRBjqkASqBYQBmDCV6yDmNdQ8c2yOuxRRP4RJRsNqlD5wS1DxVzPS3oDbrWcu0xdRHzKTcVz8o8K1uvnwqCSgOHwS0bziwQDyVhMmzXTlnnaDpVXDELmN89%2FGv1ajwlyVgPKjCJWfTEcQicGH509VJbBg%2BO%2BFX8WIyKG3GQJuquhqJIGD6GSsNLkc1mzm%2BsiFVDO80GiXnLDDU9eZjbWnyY8ypqY%2FEV9l1&X-Amz-Signature=142e5b2002adab7917107645074d494c9eab14d103161cbeb1497f76e9595ae9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
