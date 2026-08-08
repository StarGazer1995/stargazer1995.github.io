---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZ5GRJRM%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T004353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8KIPadJo39mVgboH33AmGBvw8RgU3sbnpqgyy0V0HUAiEA%2FyY59qxle%2Bxw7MemOj3Wn9QryxGMwZWXAZOM%2BkhkMmkq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDLMlZLjTmOaAa5E%2F3CrcA7YYg6xrIqQYkKsNswCd3DS59tHbHJvbyODsqjXxvH4zvC3lzWRlry%2F53zrQ0%2FeCG0a0a7Zdw87MMVF9FwG%2BFg41mTrOAokcloONZngEI8gSQBsm2J6A4cY2nZ3uuNqFPFKJbsrWQLf9CcJ%2BgDGoRqcFT1dfVE3%2BIZ45cfT96r9fhE9qJo5Qtr8o7HBPgBCY%2FrJ1b4zd3v7R9CppKNUz5Lo4TwG9vhVBmwRy9EzIRWKdfH2ZUBOsGnl40plc%2FzlNOLYTQS46%2Bd544SQVfyEuPhizpLQU3MJeWHDjyTjmqeKxhkoO4KE3AoRlLZnkkJQdk3aceZkwCKly1L%2FsF4UHqlu3QUZGJuBMxlsWPaL9rRw9MiNLWnFpqx7ihe2LcCrJ0HfvhqvFY22STjfnNMB0a8qmK9TqrNzkL9jEPhgnfJ4kcrJUhze%2FzUQIPHj5oVcBFaTBnJcj2BQ0GdldWxfMBXx%2FhlEp8%2BoInexbUDnv1rne7e3KquN6LRzT0wyXRfQ1k8E5npIZnHIcd2mt7NroIjG30vILbJdSFsoYa5tGoPXIVHWOADFJil4RRznaTRj%2FtB%2FEMCsNVlbObQiFpeRIcSnD0%2FmRs8sN389cWxgEqt%2F0uyzfFM15cas40SD3MLft2dMGOqUB44mSSDrjZjhSyUEJV0v9DzLAbrf4vf0tJ1rANQh2Tw5Lm0H7NwAJo7wN07388KBAJcr0TciOaTFLeV9wMZjCYszM6NfPPEpaMmU2zl1O42viPNEClkbIw5aMzNpvJtj5v0221gB7S1H9rpFW%2BpAF1Eyj8f6gsH6tTQsYd20g2KJ2CAU%2F7y63ua0hiO6yJtKt%2Fhssc1OojCbliK7Hj9dzTO%2FopOR1&X-Amz-Signature=ebc0b3fb515bc7a5cc2e094ab9b8930bcd500f4da8c9f6537435e87b2b9b7879&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
