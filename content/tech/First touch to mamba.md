---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3MONEB4%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJHMEUCICqwXqpqDj9uKQC3ftSqqWZ%2Bta3p7cMN1F8CsnK2NFNXAiEAmMCxV2lRzvzA8UBQVzRYBWtz8NAm9eIPiHMFJx5L8YEqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIkw0RgZFHnCJY%2B%2FryrcA4DQZq4u%2Fa2WVpxHAeFiiPRWTjSazBiaZE2XFOU1VynY19o69LkIK5sraFEhGSqnbUAteEhuRnBWAuwcZqQ0ApqwmEGOMGp1K1jgjuV2GsvEnpzeF4FaAaq9VROKRTHsCus2y4UcY3nQI4uGB4pXFucgedlo%2FCGd9WOVtd5zi1IbjE5f03J8EZUKik2aB8QQ9dRsHX%2BlE7BC31H8mDeEQWTRvZUaeSdPhVA7%2BqBEmQVS%2BVp7DQgKnvZeZIvX87qKctYCRIyCUzaGPUOoBkT6uAiSLqtyXk0psr4KMw76ktpIOZ%2BK0FTWvdvkkAHrsnCN8wyI6rg9xoenqGa%2B2gsjkLRauoTrHVO5PqJOgDy29HPahrkfIlZY0PXQASV7U0t%2BZQ8A82rsemmMxP0RP1H3IaF4xSUEVnhwk8M%2Frl3vUmoj%2Bt%2B5WoiuX8iUqPTolwsMvs%2F8it21JxaxpmQKHM6%2BKVia0ucwulDX2b2bQTGDaEzv5jlnz3IMpWKeKkORbv%2B%2BTjc%2BG%2F6bSVMNpZnUerW6OorigP5BKTBokguKjWLLa%2F7xnYgSb6y6MmGf4foQsGEpxZClI19S9R1aqh3NDBkyPy60KqNDNC7qGWfO4tA17nJmO53lKctllilOOYI0MO26zdYGOqUBoNU7NuNbTViIGvL5SRf2GRL2N08dks0A24XeqTwndYGqmAHusmEHnmo1dOgam4dg%2B9wN4o4B7GOHmU44iL%2BY%2BNxgw9viTiHDUc5YoRaNlYjl%2B9lR8X5c5lfe7kKDEHGZJDGFp2C7YOsMKZKu6jH3uQyRau9QqBqHrZyrQkd%2FZ09TBGlOst2ked2E9Ub%2FMB5xr%2FHXBxPfpR3X9pz8EMWH6pk4lCHf&X-Amz-Signature=7ce1bd50e30072aa4b5b90f59d35f94db6755d3c285cb7a26179f849b6b32813&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
