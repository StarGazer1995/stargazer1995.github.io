---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXGA74PG%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T070543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC9FFlKW7fxlmkS8Qqz8rg2TK6UpWxWsl3xGvL1IQlOMAiEAyKXOo3uiZfL%2F34OIBVICG%2F%2FhjdMw6VwgpWK8WoGhJ7YqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKKOW3MRMO94oJvxOSrcA%2B8%2BikwdPcGEZvrbIoHuf1AOwqPBtipIH73Fb0tGKNX2dNRSGLu3N5rE0D0UH%2BMQE%2BFL9lssXC71Cf70s%2FakFqIIvuxo%2BFVjDf1RqE0bFVRGjVPZZUhhP%2F9qCJWNoK3c7zz7Zj5tGRbai7R0kTKUXNq90jpIDQoWCUTGfzg8I6hru%2FDRqFmccvETaSlawhkxvjSEXQdJhbtt%2B%2FtUZyUyFggmCdSP4DeNlGPJMLOh6RjcYsBESGBhck0uVyJMfolmWERO9E%2FWf1S4RQInGFRYHairwJo8tNhXaXISFY0y3rrm%2BrVz3pyEpxj3nmjX%2FrsQ%2BpBF0sDusc2ZxZnP1J5VKpi4Q11b695v0SYN1eynSf2mWWjBt9rPax4dFHJ4L1HmZIjWnDOmISP7IS7hGqIKr%2BhqXqMg4g1zZgwdQcFygj3WJSfmQYM41PluTrInlko2RLJZzNq9PMIRHQFn1htfsp85OieGug4G5xbptRAoqZmuglWcLjceGBXIZeW9bqJthnQMB1Y%2BzWdP4feagGLcUcZrWaH422D7Fue8KcOVo45l%2FCSHYdAmn%2F8kXtHyWmJYko9up%2F6O%2FZuEy74NIn58hxqntxjrlC76Fjc%2Bme2UvrnF%2FIrfbgij8FyjHd1KMJLN5dMGOqUBQOv%2FuHMKvJtONOvm0J9IMFuFju5yKWzlqAEeADXZyL2QAMkoAnQosSD0SmsR0kTM35wdlQitriQaKj%2F7xt7zWuNBOrcg284WruSevhPZSaFHH7p07bmCTAT65m85sUHLo1NB%2FYJNxLV%2Bzqp0YOAxJciyiX6NMoJkawEEP2wXAbdNTrYOvZLhliu4dx9pob2xEy9P40HsIGihdBUCtNSD11kIFm2m&X-Amz-Signature=41846f4f1f97d4ddb6f076c58396e0ef10ef714482702c37acc9ea62fe60dad5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
