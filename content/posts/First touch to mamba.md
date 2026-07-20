---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y22B47VZ%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICFm%2FuW0lngmaxOJ6zYFFFJPVrodM6ddik%2F%2BR0R%2Bx4piAiAY%2BgXIy07n4uQDoVfi0fiwB1apMIIMvtaJBTZ2aIrOWiqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOm60IQanzqGu7A%2BAKtwDWXoqWx6IPxUo8lmYdSYsnN15C94SsRHesfdvaTEG9u1M60ihl8zZDLlY2yD9w5deXRG4pP4E7XZW8gkW8SOEb5lsZRQYOl94ZxajJlg5wmYOwDr1XPOeURn5ypNXnxOjcYU0AwABxw%2F7kZgNyF0sHa3sVLfyQhE5F5%2Bn8GAPWE8vlFw2phX0EyMsdQqWjlcgY5BQnFdqmvgPU35ufNwxCy3lqw0U7Q0WEFeSn0DfnFIYGpY2nSoqdUg%2FF26R24VnE0t3PqoYH9CnW2csluqRxScO1tDeTPm2NXV7SZF3scM5WjET9ioglfG16Q498gZ79MlfV5wPy%2BlAfhpm00Cg3w8O5A6nOukGzqHLf6sB3lpWAjYBOC8tV4s%2BlHEvfGiKK%2Foiy6S%2Fnnf5AsLVxdTwnRnkrhU%2FlO%2B93X0AbFS4dIMrlGRd6QPALGG3FmmAAv55Ax8xWmJohvpgnjvXX%2BKzIoIdYLJZc8Jf0yHcnWpC3PCLmZ1%2FAOlOuak6io6IYe9G%2BbmojbElfic36pogfd5mms6B%2FO1rKObiWhN1Ptt33aDQndTd92EOwBVag%2Fq1zna8WTvRf3c1u3c7TQ9SJZ5G4kj%2F52AadzgKjJG7LY8jB3v9YHBrP1sLQiYQIyAwxuL40gY6pgHYjKSDhotgnUJ5%2BmczlzR4X%2FwcHjtQ3EHZmWnzeoPdgfKmbztQRyOBAmmBVmyfHxOL4LU%2BpW3BRX%2Fv03dAD95WQ5Y5vs3M1bFArMbn6%2B3Dv2OOpsAx7xvxC1rsG5O8Ju8O%2BKxvGXUOHU3%2FAZ%2BZH%2B94LEoInTYqw1FlUkI1oZBMJWRZXqGIqBe%2BqkIWUKMQH73vhKRT1HzwkdOaMtu%2FB3xp2jD%2BV7CG&X-Amz-Signature=ff9280bed35237d29a4b25eb5f789bae5e8725076376e1e32f046223d197a9a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
