---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCTAE4XD%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T055833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRn2x%2FI%2BRiNtVHD%2BUsWGL9dlS6gHGxKUEHH5A3hlBf2AIgQRrq8qKI9vWOgpkdi%2FYxRzGn4H%2B9G%2FfP7CmieFh4TEoq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDH4sE835yb%2Bt5ekSNyrcA995y2Z07gYSD40CuHX%2Fbdk%2FxcnXyTvmoKxJqyAV7FeV6Dl%2Fz44EkwmWILSrlmYzOkOYDG7teHAMf9wZQX7d8XMKFaXvsTp4UJfQTcCC0pRgn0ujm0gCfo6Zp7CYDs8ho%2BQvc%2BFA5XJcGLsC2XWNIh0TLJZ0hGEW7GdNTDmOJVeO4OtRZlh7pgZSu7ErrAm8bDTyY1%2FNYrVgshwb2fP%2FtDMSHgwbd7cQQTVS6NSkroqhUHRc1VgHP1DqzU%2B%2F5L7voSdSf2ZefJ6eCEM58j21i1DGYsVvGQ%2FuaWYLlzBsq7OaOmJVX6aTycYTJ4d3ZlAdk5WuKioK34Urz83qeqdaT%2BFJW9xofDC2IOzS2PhUfHYk%2BbqWm1syYJ0rxOynYnQaxLoXtor5scoACg0XzAVQJuwuvmsG36DrZdCAmCi%2FU9Gw2b94hR2%2By3V2qkET8rMEHZiJFOaF3FYastsAE730UQihVDBt7T9nj74jHcvoYGsqvOQpppxZvOLHxYA6%2BpIBXVOP8WlgkVQDzfj0vLblD52PjZQ%2FvzaCwArbg5lqRULOaKdJb%2BlZVX1tYwh3HqLMramawhORv%2BNANO%2BKFJKPqDXje2Y2gUjU1Oud8l01OFqipxaGFtg%2BaUVlrmcVMOOYstIGOqUB8PTMRvQTA75jM0ctPXoEZAhzZuyN4XZlmnfk1couXNYYR3d7mL0O64CFpRsYFuSYdRnd7FVJVbdKdHVIa%2BNQ0SM5N1Mkbw%2F4JwgL9Kkqv%2FLl6Ln4iA5aWEcQz2YPH6hWzY%2BPMyUrIvy%2FdaFlUC1eR6KeNpO2AWhnZKWAJdjznGy5irZfR6KGIJBGmQc1lXf2dUCNuXDKkj%2BIjFMzXFk9TnSXFZW0&X-Amz-Signature=82b2db74d84f659144bdb7632ef5d87c8e68140a4ba52bfecd51cf8c7dc8e839&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
