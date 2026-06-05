---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625OBTIUP%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T174626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA399NCfOy%2FWncGyRonh0gML9c%2FFmJYLwIzhbQ4X2aAYAiEAvld7Dm0gdda9fdpdUFqTYdn%2BuTWJh0c%2BRUQvEoVeRnUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDIdVy2v6nG9HTrVdtyrcA52X%2FdGBNsgdhJt9ctjQD2LHe2BSHKeKqBbbKXXZ9aYTpRnKtrj1W%2BQQ3W1dHV4fIxt370XdlRc47zD%2BOZN9sBac5q9QbdxDIm3ukqyiSMnJO1iukrYUJgH8DAUsT9kes8gwAwsb72TCJvlXfL6lws6RWN9cJ0ut4eJ4BzpYRj5i5MjvxZodZVXIbPniVax6juqxYxggjsllYJraM2VdM%2Bkzaxso04AF75O4qIZyEg8ZASbb7oVnXsasW%2BPQmjXy4xc8nd0X2%2BhKnZ5p9787C%2FDn%2BVDVBjw2nAQ6FVzQOkfQwAMH8swzBHrF1DdJ9XGbbW6YnVz6jv48UY93L0GgJadqboBUAXjGrewMrBf5TLQv5XTIpjo68Zix2wSVyr6WN0K9lEGPjD689Oakhmn%2Fbw7ShIusSjOVJQ%2BV%2FoCvj5Lyu7xeittj77NHPMI%2FkkYzd0vpAKuuXPzegwBa1Qo9ZvkBEl5TxMaFneRd3yO6R0sHETYMMFo9PXiZOZNnx7lck54rPXTY%2BnZcSN86bb4K0F676lp31Lied4VRFRDux4FxXD8eiBWeoBEezjqeGpaOKC0PqRdsx%2F8GJPEZ5Z60jDRXbqjsQ4o4He9NDKIwWHtRmd5ly2ke%2BdT7qMPVMLbsi9EGOqUBsKItbIUSXptEqWgTWTzkcw8j80ogB1zN0ByjBM6WNBW%2FFtfNr%2BesOpRsr6oZqo3HqOeDZhMh8%2FvftKK0YiLj6JjcwNxYGai2sjknh6%2FajZL9wRJyhU2DA45xtZA1WnPi2%2BGo698o%2Bto6xYZ614zMmcVzVG2kxVnbvWr5BeaPtiTceiUYJGNUIEduMuGKGMuHQ83RGg9V5H%2FMjqoKY0HoZlrY%2B8CA&X-Amz-Signature=dae596a4f578948533d84033504f499a44614b7bddf34d6ea5d81123fadadef2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
