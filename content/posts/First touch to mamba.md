---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYUF5AYP%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T075951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZ%2F5xYNMl9f462yZs1g%2BJuUGY9LkBJcDqgxd7Doa4BxAiEA7jzHKx2jEQ1DOfKOKMYdJKPu40J63rQgaEp9Japzz8oqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPPAuXLjA%2B1YdnD61ircA%2F9p5LKGQSlXDM4yHQZ%2FGhUwEViVgcCyjedPCWoSp2VmPwICRiy4Fcldvrsk91a6%2BfbYnaywX1oKoMKFVLXyH4ROvlpr%2BtnSBoxkfg2hVVy%2BWmQZ9Y51YfGXyaX1c7CBbmySrY0v9otwlmmLx69CNGZsMURRM%2FXtRUZ%2BgkjfUoUo0T8wqiqfeTGEYZsVlSNYuGiwia6dLphaLUgPCyMnJi7h0jye07%2FXiepvSj4krQlu7jzyTH85exLiXOnsBpbj4%2FkqdMLXZ5dt%2B0%2Fpl1T88vVPSZdqUiOuw5H%2FDUXcXzAC4pdzOUyGuKD66gfRnF5FfyzBRK1%2B%2BBFZ%2Ffkx8IRsOxVtW2zv6I%2BwWtS0OKMJ0lakkfTPg05nZbGIK9Rjd5XD9AvvpmElvSZmZuoOVv05eitJsKLceEDaVuL94IoZR0U0i5bu5Sh32W7ehmEjy8yJHGEiWSqJu3oJuIv%2FvcjPl5MCUmvRujJx1hvAQ4aE42EInOAQSiuieNWfESu6a8yocak3B%2Ba7XIUepjXhT37Yv%2FqVN6BKnDFpViE9GbiFDQBR1%2FxHawdqQDXvMxrXx9rrEH0slVWwSDYqFYfa8BsBDE%2F8DO3CZwJq5S99fIvLnZvSu114Mcbqu5QIY4K9MPvO1NQGOqUBtvJVuE%2Bg7OGgCbMkgIl%2FuBY66bMHc%2Bs%2BssNftRKcfbl4T1066HOd3gtNiz1WY6AYlpMeqg1%2Bfy0NLu8rQlCTvwiWp9U0MmfHxCVe175GbCTu0XYcPFrhSUqvXcqyDV9qW3qegVFPmSqbf7tReQG0PR2bSLn6aRWLn5XgwtGbPyT2X9M8FwcMPDfoFuGlED5wTQr8vUwM5vpE7%2Bh0VF2aVWjdq3Zj&X-Amz-Signature=14cb8a68cc958703e0dd61dd9da3bc51bc234d2dc1fbb3b01208b694aa296aee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
