---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466667VSG6R%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T012430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuR7SlnA3Yf5Uq4cW1SNBZTqiHqjiHnOdLrVSUkvVe1AiEA4ssktjdOJxcB0IhO4PtzbB0ULjAnMLhbxajXe0q3VJcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLiIduGk%2Bn5CN%2Fxb8SrcA0Ui%2BpJqou%2Bluuqss0dhu2ThM1Xw5QNuxT3Y7eGdr%2FYbhZmjGsMHhprTdz1N5X%2BLyD629D20l2GFpqpfs9MHpzEjnlEq%2BicYWrtVm7UGTOvjMIBZSozWytsHgm6DwD29sOTuY1lXUyggmtLak5vl4TXY7kx0xPa%2FpymZf3WCJLUZn3%2BDNonnIKF89JGBSwErjuv%2BXp%2Bu%2FKmthzQBOKBRY8VAhy1s9Nv0d4I2pG7ap%2BYhfFiAIilu8XciMfbT0Al%2F4wmSuEGVnypPPHFq%2F5AUjfIlpCx6baol4ffAvlMk4zGwvcRZ%2BCzbULxWk%2B4J378s6Kr0bFCdXUiq1q9rE6DMaoYRyHuwUcYAM04oaQT3RQi%2BsWl2LKHAC9GUMldjeD5ufEj7ywr81QwLqcBU0ozwIfleM7cTstE%2BV1qLenJqZN67%2FoUddvLlJwiWXmM2d4Wh5ysxikFnphNxeh9V76Oqpi%2FMX0gFr8wo9g53o4tL2xxPwdPCe%2BC3tPxq9ltFdCkFReBuRuiPa2FdIXMJhcZdDdeW%2BUYea31jLH3HoxtcuqpIFJubj5f1VefFqLSXJ7VIlZfWDwTPwcI9wynGsz6ZvSLlxYixxc0pcdhbKxlDpKmj8GxphEh4VJrrta7AMP7LtdIGOqUBlhYqvrJwJIkQHQM4dMH%2Bo%2FWm82Xquht1Xv2RLg%2BHJ%2FUTQr7LQaw7R9TSzkN6krZoLO2nCo7wQmnWX4nuBO7nhjVkZqX%2Brd9JlsHmPk9Hbum635Mlz%2F4jMlhsQz9ozzXN9DbXo2Y1esxGLmMw3tcfc5kjR6H%2B10JoCDmqFLZrU6tHDoxxOzBnOhmKDE4x1eNztxjGU5eTdO%2FesA0w0HoT%2BLo%2BW9wN&X-Amz-Signature=48be0f6706a5a183283606189f82ae67419a78274d9e2487d2db5a509e4e9ec5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
