---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOGMHXHV%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T225725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDyjt%2FVZVTgK227IeSqu2kCWahKwD1eohXA3ZKaww7GFAIgcn1lxgfJSEh0OUe6rP4gPw4jyBr475sJpWZ1cGdneYQqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJDO9MJERB76S4zMHCrcA%2F4eJ9DaR5Vs6zBvR2MHgV%2BKTdZvsOPuhPWeG9VTFKf4Q5mzE%2BI2OTvkDw4JGiIMl7Od4vGLwDMyl13tZgMFqGsP2d2uCNsGOlqbfieOMx7izQVS0cS4XP7JHw%2BekjK1RiWx8Rarq41%2FZwTVyvZeILGFq6qELIBtldiFWwGaGBcno6OfEHoQWdKOyLANTEfs%2FcoGD7GEM2cRPskAxJ8HbMzTcaAR0%2B3F3kRtUOr0sOcsnEH3wAaeAUSmZFCW0WRjg5yd4uvrI%2BIq9IzblekljCKIBflJSYUzpA%2BcULgPk4HEFL0QO9E5lstTgn1xsy7QKLb8aZaIEFmMWDTcwV29xTlSnr3COUyBZN1aKAzWFO1YALeJzHUJNqNa6mb%2Btnm3P7%2B6G8NfOpIYT9YD6rp2x%2BGpZdRCZUeRlksx160eYWRUluW41rElJFSRyUNt1mrXIbq%2BcemGlNjLiKVibAgfb2uCrLTqhIhlKBl%2FkCjJ9OQYkf9xdc%2BZ6GtDegb%2Frxu7RdAaTIhuxczn8zZgh26zaujEuvFXHvHmHSy8umObVYSkdTafO7jgdlUZqbFeldk%2FtRzI7zb0EK8G816FGg12VvS07uu6xkxXViccZlxbyXwn9mCiicdy%2BjUC9xYGMIals9AGOqUBGLCo0Ai7HfnZCUZtNYwe9NkjEqs37T5IxvRJjImA1axM6F7UZhPnuFwHQ9SxoDz4OJc97FBJCFztR5aoynv9TKswfcPjnjbpAJ5dyCSCjcsjrbsmvpuht4sLkfI%2B%2B3%2BQgbD6APNUP%2BPtcNYpNWMPqEjth1TOXAcPlO6Rh00uxKm2UwwnPAq4cVwTrVVJBU0XM3wo4BAIdc6Nk6NIndhmLMcE1gPk&X-Amz-Signature=df8e84cf7bd6c5e1c19a1fa13f7f5b943e27890a413161f961a7b840700a3bbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
