---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBKBNMIF%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T023000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGN63POpHG6SB7spm7yKfkWX4f5laTn4bFPvXsWHSxxgAiEAqrq%2FKpfFlhvfHikObhRWsYk9SErWpG4OPZCs5wBi%2FP0qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2B8jksqXjYA4Of1YircA4RleMJ6Qu2b5I6l0DaAloxmVjtxnRWdDYRl6ZkQPbK2t5DHu5aKM512qz4TwHMvsL3jd6BL%2FIF0uB0jYfUEKyXYJ317F9MRHk6DEMv%2F5BqTKWWAz1u2%2B39W7%2FZrcf4kiORlIgrXW7ETa8gfb9RCJPXQcHVag%2BMn9lUZdnYVAm2uvvOgZ%2F3AD4mt65c%2BgJDcK2WPGOn9Zqy%2FsOfQAxbat0gYDd3%2BnH1u0e44DXPhxt00QN3RMmeUOYxRJBwpmbGMZTDO1MTIx0lqAgscQUl68sgzuHwmVBHVIm%2Bd5wcHevMaayAdZN08ZjFwT255iS2ADD6BO6QiH5CRMKfXhXtQRjREE0uJdQWMOP069GRuWelPs5aoXM5tcCX3ZVTa0gRQWZ8AGo4rKPn%2BxsduFuh194BXHkw3SN7A3hoNMplc3P3lJ1Dh%2BZXSFREjkd3QRMI%2B1187dFa68Xb4HhV96oC7oEPXE8KWMXzJqoA8ugin9k%2BArhSQImieOnNE89Zt2X6nePnLfETk6zoJNBOIJe4YErzXzuUSTPnIUM6nmhpAfdzfIc66REJ%2B6%2FRqA18SHPXCMG3jxc5JoDQ5gr0OKZtmMoqxuGbwL4XhUlzGOkGO8%2FDJ93yX1JpjmEecUmEoMOCGzdEGOqUBF%2FRS1yeOrcxR7rNALa8AgAdjZFImwKfGEG5ZEbIjM%2BpMSvHkbBPMLd%2B54ysTGjLeYaFJfzHETwuBpVr9AGInXw%2B%2BQSPNFJ69AkAY1BWgljRTLcVRHZVpC%2FAsGHUiw4bzWZvhCa3YUWLrYUbQy2K1RVULVuAFiMPIvhFLjy8Xy0bG7WCeV3TBYU%2B1Wpt9Fhiu7gIbdTVbHcfk01Ofn7E%2F8HKXWJ1%2B&X-Amz-Signature=cb196d8e38eab4fcadc7c74cb7d1b80308a361d353bc0b949babc58256954d8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
