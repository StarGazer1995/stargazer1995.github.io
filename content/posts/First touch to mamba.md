---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAC4EDWV%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T063304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICf%2BOFeTAgTLJbTvhmeuoOBxpjapDVqAByrTHt1waO5NAiEAsAW07660WATB0nYwiQZKsrSsDanvwqUrscOvdjNvusQqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWTEw%2FbLd2laApnFSrcA0vTSbrvIpnfclSd92VvZ9xPrWTtTbCg%2BscG75Uhld5zfo2KABQIavkW5NfnNaoUcGuvCHuCg6Scnibpqlzq%2Fr6HT6Msl0Jc5zgDfb5AMH5GkB0n%2FOK9LNHJrVl704pgi%2FIAnPpVkCh8CBKaTTTUg2mGCTlj1cGd4Ut%2ByJsVUxwnmpq8dtKi3%2Fq2vw4ys3Q4gMYVOwJ1BeiZJr5G59wTgkO4eMJe%2BNeSnM0JzlqPqVKr9ZKM9GS9h6qVkKC8%2FxW5dnLFcT5Q8qDB2vfvnJEhcJeh%2BWy1BAdgvbf9B7PX%2B0gHZMrjGy0sR7VUIuHu53Z%2Bjh7sqMBb4l0qtWUN247%2BTCVSt4tDN3fp%2BtQ4EGJCWNnXCnvJZeKnLkmQ1EFU5pDxxZMTGSTNHEvUKG2Nx8Yw8Pis%2FLf6AQA3419WlgZ8LHtqVhy%2BvEZZK84%2BC0woQPrC8SxtDjyaWVVrultXtazsWNU%2F%2FQouQxNyrKiWjIrK4TFTYNKZ5B%2FA9ZrRnjFoVek5FcnZEC7QVmNIVuQHWk3A7D6bgfo%2BtNhaSjr4suXYxytuu9s4khTUZhbugvaOF%2FfhIJ0DG6s2trCmhiHS1pq6PXa6ygZcOHf60%2Byv%2BQ36yriRTUtcj4ocW7DjrLNyMM3t3tQGOqUBjiNZEpLbH4vb4bWnaltCUrTBRemrBhz5CZuGcf1U5hJfxvt3QxaBIZizDkW%2BiY4hulGMKOHFkuIKU0w1JKrJ69CQEFyKAJ2yCXgWzTvUkEUxEarMLnIQoT9881cI9SldEOyaWHvFeDUnnXOatUnd%2FrZgoJN%2BOJqpCSZMUj5AHhxyR9LrR%2BY%2BVUt0P3CQoMHliLGh7TJunMiSlqh7%2BCcs6VvaFCDa&X-Amz-Signature=7386d3d1b75768de7532b51dbb32a9ac3f1b393ae5207792f81914b9744ba87b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
