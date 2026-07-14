---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSX63O72%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T074439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQCUsMVcFmTx3JvkS9BTHN9g0llY9MqFkQWZ1SzjAXBEqgIhAK3r%2BXAisDOfP5obyY0veyCC7LYeZDQ%2BGZMVbsn%2BNwP3Kv8DCBEQABoMNjM3NDIzMTgzODA1Igxt%2FjpHFYn9TENTYY0q3APdVa6xXOFTd2P6FuSzSNHnIlBI8aGaaidMr6BswGDkMYHEifZFqDvu4wBt8dzZQRgAGZolycpzLs3avJRZ%2BBlA6dWS696%2F6wmndAiM1p%2BI6yvQACnZTfy7dMoE%2FHZKI5Smspcj6aOMlQ9NemrRWxav2qMP4lwAiqoGjMFKhD5QEkvLXwJbiYDmTiDSoMp%2BbTnIVweZPP38cep08RFMW%2F%2FCKr4YYhKWMUdOc951%2BxC3ZtiHSGQJWESylhn5%2BgdwfRbIm0y8FAMiqnWX8B5jR5vAa2g%2F405HFDILkbXMbCwr0tAWK9DqwlqQlthq9zxfQEYu6sxWKcobLqznrFMa0G0BXYbWOUWj7bq483KS24uknyeUtV8yV784VvtXltSi2qBlKu%2BhyVrskVCRI3XsPVqWNaEMvyH9KaFD6FTxxPiW48XfvjGvdTCQhTsuS8i44ILy381Ad5uaD57wBdTt3FGjPOAJNesmV1aTSxnIOnPhUnMKkUmuQcfxKXAIhmXOphqLc7IRq%2BgJHlmXyW2GD9TI2Ypwx%2FyHVIZwQ7Ajbh9ax%2B1Wb0RWPtRb8yS16Q%2BDTNZcYseCc9BYCZZLy4BaAvH6Qq2iSHIW3uyOcOEVOI2lQmplR8NQg6Y9sADw4zC4ydfSBjqkAfBotdBYJ%2B%2BbQIB2skIbvC5RV6gRycH0zFKvbKM%2FikjIaM%2BOtWPljBkPlkTeIPv3CYv5XqAXhk2oZZ4FqiWspcfZMGWXdhk%2BQhtKuzFCsF5%2FgYTTryze75xuLe3VGjLnO5kInwq7RxsYMzz7WeUnqT70%2BZ7PyRZcQrXJHqvsb0EcwtDvw6cALEclL196nRdQhCUSZM1BKodCPll2yI2jpOLMxU%2Ba&X-Amz-Signature=a617de7129e8b3f542ddbab55d8c6a35633c7ebdb36f0bb803b3adf065c0f676&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
