---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIQZYTNM%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T012140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCnEHxJ2NpMhXDHQjds3vIUOUEIGHPzhwqMpVCwWIzDGQIgad1dAT9OVitDaXpNgnv6KLiz%2FnM7lqmZEXf3B8mCgnEqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOmqVDKkRgDv2u2VgyrcA8MzO%2FsqH905GPwI6Oq95S%2FtNw3b3wU4CEl2Nlj6ZumaenRB0z3f13ZEF2iKNPTVY84pDNRX2Va4quGS0bz1UUziZUmsJRull4lSaarOp7ZVVSGligj8QjXNrUB12K8gV47hYcezdSKRr788fjjThc75m%2FZbt4aWUmg4oerLJldhbvSGzxcjneHIxYoCybrgMWBgLuSh%2B36%2FNJhvgGGGuxcaWmvXXyMxRP7w61iVEyhZIsscqpmy2PyTyvqcty7wqQDAWo0r84VmIbj72ozFZ1LbTWZO9t92OzoHFggJJzc20ek6S2BwtzUa5LCGDo39JncuSyESMTftSrYbYbpVCrgbawsBsek5r%2FZumJ9c4e4BrgPYBbj1Zju09Jw6%2B0okZtQkemhLzb2jZlCLghHt56ic0HMgTbvjpiqGynHPsFDFwgJ54Baziuguslu4GeJ4KS61HhEk%2BaZRD2mQ088UoGBT%2Fx1IRSAQSjrr50pvDJ6sN%2FvhE4s%2For2YolCXenunfAssg2ooRfJMkX%2BObonyg7HBfj65BQTACftqL3w%2FN9mCOoGu6Uu5Sr%2B5WN6XiWZKUDbOX0czk%2BYuPk7787oykdiHaUcQEL%2BaK3%2Fk1MecCdprYP0zemN9WvoH2jJyMIiTgNMGOqUBtcy%2BTgfPOLAiUFIk5FxHQjO%2BFrdvu3EKFTQ8cYe1bN31LbzjHgxT7dh7gm2UFAw4w0cAN5TddtqfAJJEtD9YqXqueXbtWYYdRcGdSJV0ba6Au0YsyXA6VwpswFCy%2Fa%2Fofb%2BUs9cHUA8k6f75bVUkCAT6piuA5APMEP%2FZm5eJZnGuClvpMOtoOFWme9I0dlJRkw0Wzxoc0yxDdh5L9JVleGqAMpsE&X-Amz-Signature=fa449fccbda1bb6076c491661e50b2d8472c55d14498488cb75c208a1b7c972a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
