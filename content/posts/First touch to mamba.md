---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QU4FYTRZ%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T102206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGkKt7%2B6u7a1pvOhzTrdtc%2FmhDIVpyrzBgS4%2FWQ%2FRm2AiEAuoPTmOsO3zTlQ8OCTDOLR%2B8ESy6U1tK%2B0ABPg%2B9l4lcqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKq2S1JsJS9Y2HFbbircA0q0e067D20SCsK125Jb20bzyAEHcofpE%2FH244gQPqf0fpA9ZiWcF41Xxn8CoF3xqxmsSTROKzYTaQVI4UAw8e12L6mTLgzsL1sjIrWBBIPHTsJDf2B4opCmFguVrzbZwDm25upGIsbRvDMP59SExMsh4b7eSHuTxOZfvmOoyWlE9A20MSkqBM8ickE%2FygTZsHaLPj1sMYioH5IKvE1sqpViPncW3ZGCogsS154g8k2yk1qo12NeRXm7KM6W3UeO7kU0uqQ2W48yJG2Zl4kBP16edG7abIpiahLTrcvAwqEclwQ3LzFGDtKOAo54TDipJHH9mtAPK5MA%2F7z%2B47ro%2F5eYxnNqtTXO9Cy18mr8wlfWj6HkvRV2irATJi0CB87CYGfsZZudwY6%2Bmp0sGFeCUU%2B%2BYDc7BdLXqSfB%2Br2NEMVw5Sfl%2FLW8f%2BtzKEJk7209MeUifFjg7qUOHnsZFIx6vtTeSkSug2eMkmBauV8u87%2BZ4b%2FPTNXdxhyWxakoPJmdiD055K04dogO8XLrApY6%2F7cZJPsOXSeXbwK7P8x%2FneN8SVGIUNOQUUgC2Br96Hk1%2BkUNfJCdGX7%2Bw%2FcYJrbOg7Dj6eyDmLQ4z%2FkpXIL5knpSy8FOdTy3MOZUV6seMOuk4dMGOqUBeYKXrI1uwhunhP8bDNVxgEGhFrSDVb2Jsy%2FaiK22EH4fMPmSr39N4cGKQU4pv%2BUQL9lPj0JQQxRY2jK6V4B47MY7m%2B8O6R6sjqI2IDx1%2FbQr2fsIKdUfqWgMta5Q%2B8gAavR0oAy%2F%2F0zm8hBZIr43lBgCdOemWWkExiu8dv8SrlihKF0qUTtzyfshB%2B8tgltM%2FxL72UnmiNkvLPqSNbd7CE%2FY0%2Fx%2B&X-Amz-Signature=d980e347a2b725ad10e4ff88c4ca9fbb000d7f817a6d496c85ea6b3422087be2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
