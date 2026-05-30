---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M2733XN%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T204401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCTj4Y%2FoSQskVB5jjZwyou1156q1eeWysB7c29mu4hzxQIgSpYaHsR75TxF8FmBT6MyeQJBBwGSKZpNP%2FK%2FLkACOmwqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBi%2F3Be%2BEBsEPw%2BYYSrcAwWcDkzl%2ForHDetFpQU8DdzuivVJAN5RxLrvX4bNgzbAUK%2FgnZd6OE3JCGAfKHK4znpmZildPz2s8wg0%2BePagZdmSubmqSZ8zQ07VaWfHa%2FtMgET%2FVvRaXhYJKC1J46IRo5nYp%2BW7l5WiGpCa9RlQQ9df8bAVW20UEjW1TzfemWX4falfsSZlbJPxLozSqPV9155Wq9J2lMRrPHMbIEP%2FkpWTWFhjLP2w1%2FE1ZxT0SceoyAEpny2asVOXBt9l%2FdcK8%2FoJihWKsFZ1NqBczSz2yjy18Fb7YDH7QkuepK09VLkHYDyMu5RR%2Btra3zRf5DZc3tf5C28EASS3jMQuQdxLykyyjXYLjEmLjM9%2BGXURAvgStW5LjECBhC45mvqbGCwWKRCgXoFB38S6sBN9aYrVoQJHwPRv%2BvMnrhacZttIVk1T%2FeqgthoclJu2pXhHIX067flGPmooQCUU5KTljLfz03aoapz4iaRiV8AZqF5yX6QuxUsljEcfSCt1UbsBVUVce43JwkUN9VAwgCa8dWgJFbGMkWWjpxMECIckS1kqS4qkGcLyYXKQZqQrGC6mDW7NsdVJkk1kpJX12vioWpST60lejgADS1hvQ5qs6nNUWRKxl87TWQeVtCbG6vHMKrg7NAGOqUB701jO%2B6orXUQutkAuNL4Q67PM4ssKpo0jzRVTPr%2FAzJXxbiF%2F6AcIo4KDuASgXjLQt4SGFHQtxDXz7wKrqNE9pEL7z56hrNwrTVv30kFjYKDA8lH6L1oXw7IJQEM0NNhQ1vzeaIoAd4iV048yl2qPuXuOKfhy7jSIzu6dQJuXe91IZaqpU2x0SJSd%2F5le8JOM4Mw4DJfRVLKKL0IPUhdxd9sV3he&X-Amz-Signature=412307d2982917d0e71a3c6987e59ad7338c16d187358fab3c87232886025f2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
