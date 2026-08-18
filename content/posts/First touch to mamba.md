---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOYPOHOD%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T101654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC73bhsgdAIytCUVf7R5K3fX9WSu%2F0LIbx806PPmA2zEwIhAP%2FTJUkxo7QKC0VvD80F1brsN9%2BIG7fN%2F3UA11T2TscgKv8DCFoQABoMNjM3NDIzMTgzODA1IgxFxdBsfv3dzxdMZGsq3APqVWZxDae0b4ft%2F6904SPCXnqXmOqO1%2FFEc1tsG9Ee676vvqxRar1Y0fo7ujvqJAIhqC1bbDjoV9k3TV8fcK4RFKQvZTb99rmDzT8%2Fjd6ig2Z%2FaD5%2BGu9c6Qf16MU3L5l9c%2FqQow4cog7Y6OjBu0UbE4APPG962hCRte9xKir4xbN%2FHEdoGul%2BkCn3eL%2BXZw2ERkUkKTm4xD6zTDS3uFmYN9q5%2BsarlcMrWtx8IRCy6Hesi9VEma0iYTOlW5CwgFQfUYjMGk5xgHMHruuDEtrYIOBgQyj%2Fi1nzrULyXpQQ88ZQIEcEfk1lAoSPxW7TIQwglDdavM%2FMMPkTIpTzraORS513DVESYEMWCtNTlDhoI6RaoajZn1AF4ueiX8hhJo9udnBTr7zZ8CPCgfSXjblJUBuzrVseAtGHuiJ%2FjGsApUB5ZfA%2Fr2wqZ7ZF9hVtozFGmt5YMVd8%2BwkyabULdaEyYQVFiPd44X8txvCQEUquKKWkZtymdF3%2BMi6oT8Gc6Pap7Rt7RwFO5dqwP7%2BGKcmvY3qtFPvtRKwg7emNbHiu1KSl%2FiHzpPzbVJJQzHPAwAW6WqmWlbsOcIbyIq2soZM9azTqC0RwHnoMQqLmrMPiKUbd9dfZ6dh0N6O05DChuJDUBjqkASHGt%2FZlPy%2Fh7WI3069zaNsv9z03TScYMxFUqkJke1fvdp6sFLxXETEKo295Pnp%2BX3iMtcf5id7ST9t8U45xLVD6FRDUPiOeOE8jjTcb7rJs69LmIunf%2BTgywYKPolfbAVaxtnBZjPgeM00I%2BuGzx6Vyon9FsDat6cWwkLwYhf6B5iA3kBq39vpYr1kS5uOqZAxud%2FuFAP0fHXxenEtnOZsh6WZz&X-Amz-Signature=0f204ba31ff6016cd315cb811a0ca0a765ea7c9ea2773151716b74c4d796a95d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
