---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLZ3ZVB%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T023406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvfHT5P8n2dzNvQjoNUpWkrXvXuGopF82zFVHVqKCMUQIgW7rcSFpbOiWi9tcjsihsZGiR0jFSQDa%2FDYb6tFnl97Qq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDPwftaiPbm6PnCD67SrcA5bnCPtdlorjd2lNgnw4O3bX38t5c6VYzbIXjllQ2dDd0XBzx4%2FvkSPh6D3iWY2kwGDbu9m3szVktf1cipOz%2Bd%2BW73hi2uo38vKkGbhyGscM9RqICEeybXFDb8G%2FUbIyUYGGt3kCxMwh9qz8No9iBZRLsVOouinHACGq%2BWAXMcX3WPZs8wRy45jOhAClyQFTYbB5rsu576fp7SacCD9pN2M5pk7kagiULLb%2F%2BEmqoSvYlGfz7qgyeKS82LQAGwEQ2nFUHztCvbN1RS3YI99QXCoxQQS2ShlT9ujUFGJzCoLmcrH9cUWfKbucC5g%2Fbx1YjqHFckuOk%2BK7qUrxBO5iB17oVZ4QThFDv3WxBNi%2FrgjHDLWH2Tu0rV7WfzpB5ALooltYy4bD0a71RwO%2BLXV%2FqIhQUvOVvCWVJarVKoNHy76zxa5sNemXfY%2BZFsKL%2Benn30tiBTK10eFM4SLl0wMFUsWgxVo9irGR5pZ9g%2F0A6PoR5mkhSTfTcZeIq9iarfs1NqsG6imgIBJS6Yg3k5ryOst83jgDAfaASd%2FrMj6MB%2BuH3ZOqAzcGKdIy9nJLvHOZpHWdNG6VrCEj%2FcbjD5nUEG2LAYAMV%2FK3b%2ByOVXp42DxCxJ7UBobcy9%2BjWkJbMPvlqtYGOqUBNe82x0P9%2FK8fVlVAUKWI9iczT0aKoTes366HZuNO%2Fvyo8%2FON6WMziaoF2x9xup5XJpXA0zuLLUj4CCVb%2BgdZI9jZecspWnX2Hcyem7fLZ9g4FnZg25%2BsnyYAtxitpjLjxesZgBhhJgtCq9of2wI7%2BZolmq0iDCdoMrOI2qRgud7%2F4582mRACu69LqApIk%2BeyOqbwz77OGrHscFD6AaMi%2BgS7tgfA&X-Amz-Signature=4bbbd0170c51c0a983978c8d6d367802d99de1288e2c828789ac5f56c252c1ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
