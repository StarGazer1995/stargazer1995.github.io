---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOQ4W762%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T122234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFuyZu6JjMKVyt2lu8NKfg9dLBpVcVpoJjaa3y0lKc1pAiAsoG29DTll2P6%2FyjIr9bArK7ydIvCvBYouhOV3khrrqir%2FAwhqEAAaDDYzNzQyMzE4MzgwNSIMJlyBcj709qNpr9QPKtwD2VQcab82dm2%2Bra6JYobG8W7zWQXWLTEbjLnLrbXhxUN72VQwx5RaAKj5QraxB2jHFyYblpXIxDfYOQ2L3AW0%2Fc0ZK%2FneN0sw6euC3Kwj%2FEalQlvWG2xqRWkmTA4sRWktVOajpyQA6Q%2FpqhJw6oTNf9D%2BTiyFIDlNAaVo5ZdlGWfXxZeXvUPYgRSm3wQ4i3TFQ7dTnChzmn1sWs5z%2B9R0xk2PWni5wdsscbQ6UlsZD2%2B0l0o3%2F1EDeX9qf%2FZjPCJq9BcuZVVoMjxzru7HWSmoGj7mp3vSg97T62zKLnYHl%2BTHa%2F5AE9gkDvvnR2cd0BiOpygXQQLZoaQ%2BIVJk1LCc7Gbj2kQaocAHFlgmc2%2BuDoi65llN902Wih07ECZptjNH%2FY%2FzD6jbf946RMH4UqyEswT3%2FRG%2FRNQckFCvxOzn3%2Fhz3zTm9mzqpgHq5Jw0jDpJULJIaqDEagXa7iLzC4EXqaaRfeqAA9joajkbDW73Cyu6T%2FPQWXs%2BoS%2F6rnBspEGCPCn5yRKQfvCzzRLVzbgPGLUcgP4bNNMMJQORjMYjZs1ur3SQvCE5Pd0ffJteTOFdhr44HrsJ%2FQEWV1VP0KoX9mnldIztIzTd%2BNFlzoaHw9ZM4tGLBAMNSjWwxZAw0Nbb0wY6pgF3PSa6gSHHuZTaSzAAGlBIn6qmt3LDd6wtdONLxGVv2o%2Battvgx7kA2TAOVGEFY6ImcYWRVbrnj%2FUuNFl5ifWcanpciEkuWM%2BZ%2BtgBaj8w26Eq3MdRL4IH64JPJOuLNCn%2FfcwS7sHlmssPrh5iivTZdEYUlVx0wcCzZa%2ByY%2BLIkC0FgXeJIWdQPtga0uSZzjIDCy8%2BpedFrxtak6nagxFx8Rx9ZcoI&X-Amz-Signature=59a346d8da3a0dbfdc0855bbccacbe7206d46b0982cf51f5b562cec4228fd0f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
