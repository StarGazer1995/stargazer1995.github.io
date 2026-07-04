---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UABAPUWJ%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T125638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJGMEQCIBMvjdZe8GKvKpRq53ij2EsDvI0JOaxY%2FfKiqGAB4xT2AiA4lViVnWZJztRHy5HbJTcXo3xzuH0ifndG3BpCO3kLVyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMTIxezgP%2FxMvE1nq8KtwDLQr9p0JjPNcoj6JUXcUF5wNw2FZ6vL5zur32oieYKVcPl0U%2FHUPxjftUeqroqfG3esz0b1DCUfRJ51cmjGuwtzWVxEUYLNtKi8zR6p5%2FVY6sXxcjkBpA6JX8KyBrAJ8Ym7qKMl6FZehOI0UZvYsvrREgQL8OPBBrZwrLRuGKurgEDSm96xJsut8GBb5mMszEmonJH299zXkN6OccIF2ey60BsRdArYpZ9CmtdVJ5TxB%2BOIaKZy5tR25hLMZbqckPd51zI0gg9%2BOP39FfIajv60pyBXfDZMp7uf%2FKbSkAxlYhRum%2Ftx4l8OSCc1azDvCRn0gHaatKcJPgDMAd7Imp6SOL%2FGxZlOKXxSLiYtX17Cxc6d3nF8ZvEIdnGfaPoC0KcstU4zJp1Em2oh%2BHFvwo1jPCKYdUSXd9qeqTNIqtcbWd%2BPU9avM1RnWnp5OHrul0bE5D2Jh2%2BzdxPFRSFvUPhWf8YFyC%2FHliq7B20DipvlmRIA%2FmlI%2BvLFM%2FilaYwYn8Q7K5ctkcJRxKLBfwU7qQoX%2BJ5DJOcgPjlnSblB3Fpb7cqzWQ1jWeVhMEBdLoWLzUSRLn5v16faEvwyvQTg5%2By7dRr6s7skVIrRQNNnxk1czS3rrOmM0WA3i5h8kwtqCj0gY6pgE%2Bf%2F%2Ff3SadfgPKG1j3ibY%2BguMOE6XmCiXIDgiJXzu3%2Fi2ytZv9j8HcgwwGDtiSJQwghvDO20ajaT6GvevIvitYCfI6OrRhaKY9aAstylD2eNJ161fkHUnWlu16RWLBcvCDnktIbAcbADtWGbE3OFZ%2BjkkNo0F0cuYJ7xTjwiL7kd%2Fvz%2BCxFr2zNOoPm4FgXBhBNbb7h%2B%2BCAGfKXzbtIL4o3g%2BoQheD&X-Amz-Signature=9f475097854b5ddf38e1bc37ba125a440d53da81eb50aa775da15796728d3a31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
