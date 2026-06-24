---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAQMQ6M5%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T211652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCID85QxfvFUpnAFk5Lkd0099L6L5KZDf9LvoQAHREkNI5AiEA6a10unJ6KwN82wg0Vh0gnhvCac6%2FSTr9ZXM%2B7jh8P7cq%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDCHkL7OKNR64tzn93yrcA46e%2FuL%2FSbnAJow%2FERMSXWE4tUSdEiXoIaEMDqTSj3yjeLPjGfK%2Bi%2FydQzdQRpXoaLQbwbQ8pps%2F9Yseyr7%2BwiBDbM%2FbTNOxnsK5Q3aoaY6FYrh%2BYSigoViy38nYSUSHn6oNBBO3nenEWIDD%2F%2Bk62QpdTxaZi8xH%2FON5Ecq6wkZsPmP9fx2ikvvfEVSSYXyPP0Z6ES5n7Sj3Kj7e9OH4ej0VtNxd4Ceb5fsbEVkV4tvpQBPDZfGeXvoVp3J9kh4RU32Vlb8e%2BrnSa7ABSxb24KOQ%2BstW2glwk%2FUSrqe%2BUwrrwMVwVScYlGuSNLMOKaRwrQSpLsAqZVfb%2FsPE3iWTwxzmOYdjMFTatCCzklnBc49qsR45wLjI0kL8ttmPzF1QjA7qQHsRZzGy7Fs%2BV5oU8PKWq92wnm23F1bj%2BHBuGItSd9E%2FERIqM2QBNaWnWEISuyH0BLBWVp3XIRgLpGUxG8nDATPNtd0l0qCXmuUPZnGDksosyavz5kiZVDJNOlXLSAznqSgVKrD4%2BzIau3S4LQg%2BfwHOjz9SFIm4aTSL6Yc6rUloPhe6Qdh0RHy3R5ikjU6yLnZ3kys3rsW0DR8T929bhh9X3fR5w5vEphQyssup9P%2F%2Fp%2BqSWtEpocgLMNmV8NEGOqUBBqFYt8z2t47dfarmIgJx69bmgjhpwXceZDECm0d0VPau%2BP25gsG%2B7J13%2FgF4OzQyt6VFWpHFT73DDrrCQjQNqkZeAjwZTiG8%2FI8ND2RJnpWxWVC9IiqKGG3owSqqt0Yxcdhsk%2BkkoXaWMl2WIIOdgK7nA%2B4zrcBBgyxsOJVIcrCT%2Fm1S6CXM2krl3%2F0nTGCG%2FODxuPmxNCKjMHxwX%2BAf0D9T9aZ9&X-Amz-Signature=2bc7188d0d8e72f5b00e9ca636d96710ab58ac930c9458a263c5a8b9f46be9fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
