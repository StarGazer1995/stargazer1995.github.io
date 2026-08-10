---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJPOTTB4%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T051542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIVldc1sDsyq4SEoQizqMS45xZLo8xqWmJlAli0YNsKAiEA%2B7Zu%2BDbrO46c1nx1CHLhhTeohHho6qfehZ5dNhcNk%2BQqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpqCjCQsZ3bznAqeyrcA0DPcEhgOw%2Bt7iZ4ZuQiN%2BIyrbvCLvHwPwYfmONj6Uw9bp7bOuIxirvbVeW8OjY89Pacz%2BeIvpRhcvCcOcAArjmX4a5OHV%2FrKrnXz80MWMvBsxddlad1wF4IJ%2Bw0vOJMAn77AhpKg2AqK6yZKgjE0oq%2BOX7yXrroBwvRXDk%2BGFyCvZl9MxM6JWs0CXEfvuyjJeVF25t54JtiUDx4WykbN0sFbojeX1684cBsjP7ARAqxDkDfCTQJ9iRPuGZ0H33ZUT3lo8F5zgjx2GY3WjGA9gdsY04qcPlmmLv4jjhE%2FXDLQwEaRdaF6yrg8tj7fYZx9qRrwdKvfyF2I1uai%2BWMitO5MWBCH%2Batb07YAIqX%2FvQU1FuJn6rXj4327U2s%2FT%2FKuKve%2FZ5uJ1Hwhwo3OqAs3lnj5qNqZ%2FqBXmqHR9uwupGJ0SnhuQ26Sob8bWyonexRWXWE5ZjF%2FZt%2BbWefF14Ao%2BsdqYIvkdaiF0de2CF9TFxmJeFIljh2JzY73h%2BhSrpBeXE8YIHFnUWvEWIQKjJJlnW8ooRH%2BaskiJO7SS0UWT9jN%2BZWYYtrYmxvRNxdxiOze3F0WeAh3zE2k5cqJ%2FJO66SSQ1yoiFbuPx0quIpvXoQGiG7%2BjXf%2B2mom%2Bom9MKmZ5dMGOqUBPOBRHRbw8JqyCJXHbCDTIr4ZX91GjZTEy4zZB8NOJ6TwyiFQJLK9JQptvzKU4%2F6m097kcjQ%2FFJNQHgN4gPMvS%2FXZyODnt3Y%2BQtMhWq3NpoNHhgmPy5tDC0fjBBad%2Fr82QjW0AMxOstfZIUOr6Niainvx5MzTTdlpYtl8eeuPKMtbG701c7TNy2m5Dwrcxs3oYzFo%2FXHa0Q3mfXOC4HoDvtJi4pdI&X-Amz-Signature=893ff3ace784d1ed3d2fe290da4491a686242104d6aca72864bacae9cc8693fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
