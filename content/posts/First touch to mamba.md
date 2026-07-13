---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC2PKHW4%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T012649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCID0vM1FZ1dpcgevqzjx%2BJ5T4rQYrlEwRoZ7zk%2BbVVykbAiAxO1ocuRe%2B1OHXT%2Fs9xWaAv%2B7PoTukluCtNOGdTi29GCqIBAjw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTGs3s0krgoqsm%2BhNKtwDMxfi%2B2lEuBQlTZQgPZS49gKvYnTRzbTUb%2FInjFGBfCDF%2Fn%2Bx%2FYrWQywarM%2FgxXsoNdtH%2B8Fpzx%2FAfBWBN7iT7GmP4btElu%2FzHcvW0S57mQJ2AaelEbM5xnIP57bIbSUnzQ%2FTn7bKXlROwFWm71tuNfqPHgg6xOivg9hTAqDe3pdrTxCAdUQNWieZlFKIhLnjgmf9Oh57Kt5Df8lMuof1LAORSSj2cknbulS05M0tC%2FWMXVsDjaWfT47Ek1uXt9v3aJ3r1oEuDb8bzU7iV5lvT6XYkqkqaGF5VUSouUHidlSqG9s4faUlCbIKkroSA6klbjpjrjvBb3DTsSfjRYHhubNH%2FMI8Z7M4iBCtIW5XZAnsu%2BHXn5rzDUFGEZ6I0RjmAtou7TaesX7MZNRq%2Fzm1sO5KgAEpO8RYdVfWik8pglrx3i9QBnjdp6nG86FIUJuWCDWLgnM6qRApsqH%2B29PiLvzaM90a3Gop%2BKUT8%2F38Ax5lZRyN0A2HUUzRw6M1po4jTRJ%2FNXxYGOkrKbRdS1dLIecihSK3Brt2aRZRPQs%2BflM4cQvm0HAxSVhVz%2F1QK8I4uasjmwFSHW1h2fgAVxEZJV7bxlkXrGjlzxS6zhjHLOCZasQQIk7I2gysaq8w9LvQ0gY6pgFqpUTi3q91VM7eVgegM%2B1DlPd2gAILwrZleYG8DvLJxVQm5F0FyIq21MR9XXBxG0iZ4XiZfe0Z79MmZ%2FJTVh9NV8fwR8J6KecFg08jee24YU%2FQ3p8eXLKsx4KZBV437S3%2B8NY1cDocFnvw6IlgNnlAiDR%2B962F8%2F6xTGGnwyk678dDlhodo%2BFw8yj9s1asgz7UMRFkt4XLHeuHsKxkRZ5DhHr1Xbis&X-Amz-Signature=4ad4888e319cdfa06982fb314b192b35a33180f04382e3df6eb188ac48110e60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
