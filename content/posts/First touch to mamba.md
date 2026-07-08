---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPY2HYSO%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T045718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAzcCj5aHnF%2BTGfli40WvVLnHV7V0cvXQwfuDqEKXthLAiAaQjQP7uqBp8Y%2FL1cuRoxSaf6erUNJx8FzEIcgPuQw3yr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMAL33OtyCusOkP0pYKtwDL5yeiaB%2B2riABbsr8AnjD4JTu%2FLG%2BXPJSz0Wpf6s9Jy5qHGwuXzl%2Bw%2BXZvFVPeQtc7%2FIs7qzsIPlJUixtb%2FyKUhw%2B0hDdijbO%2FTW9NU7suHfNNbqweMqvc%2BAYJjkRELJj9uzClYUUFFnNDJs1QLBi0IaeWp65kM%2B9TBonIdcm3v%2FAVRxzilmfUKUWToqOtISmovZxJW9VDPTTeAIpy3vEfIYmUMrJaC5FFMEvIziJZMp%2BxDJwEUzHM%2F5YRpNexyqFOScQIMVzlYUwWKZsu7aQfQqSMxpiUzyE%2FdVEX2yYgVXk75lxFUsFLRgMmVbwIs5EvBBUvLW90IymzgjBg3Iet6D0uzVQw5uBY7sxcniWUqYtSPvbkVzdTEsb%2Fmw33Hs0Kdxhlh%2F86ItRPHCUXEUjhPuim8WCvQvB9k4SfoV5jG2X9PGbWPzI4hLPNvemh%2BvstbzdcVYSgUeI9G9uzKOgtqECr0Cb4iMXPQXEBMKBib2jymQydv%2B1nV9i0Yp%2FFqFxzfGQwIP%2BBRPEoo3s9VB9PHt4d0Btlukr9viteYvCW4I0RD8UM%2FBschHRzGHQmNR9GHOM4kv1FaQfCigdaGaLnwQ5ULeZGVusr4iFeVcLOaUM6hMJT6GYkL4EgswsZ%2B30gY6pgG4IX9t4Hz3C86fySRn%2BTDEqyQlMyri9Cs7Do7eb1ayZpjuSRxCWb6ZM5jAhdkjdYAH6FA8aSOQqLJb%2FvhRRt4qKaOT%2FKuH7BCenUD%2Fd3tpe%2FN652hQp1gStsou%2FYYh7I%2FhpL2BZaSrhqzxTCvkmcM8olALTyXR5uVsq0Zq0pTh249accvMNnNiT75bosO5BgI2RTfVXabpsiN154rhLiWXB81cuSqj&X-Amz-Signature=3736c0997ef8b1eac13053edf5322969bfb55647a5467d20c2a5bcbad26daa97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
