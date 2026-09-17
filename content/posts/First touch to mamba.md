---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S4W43KL%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T143149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDLrodYsoaMR3MYZZAopZYQ1ef8FIcUxCcWqrinoJNESgIgdK80R6wgcmlfOcbB3lKOGFPkyjD1Nmffo7VW3QCsSP4q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDHp%2FWGxuj8WNdq%2FisSrcAx7QLpG2WCdlA2ULLBmZonbNZD84S59B5OkMmw%2BQRQkgs2b%2FrfeYe3IjjOwqYy7X%2F5G2j9wzUv4Bfl%2BTEea%2FQGLB2rj0uvy7kupvkRfbMFqcMNfMC5jgZ5c1vTjCDLnmrrRxSPDyQSe0QZK%2FKKgFLMRafJ047HF4uxhwUtNN8Gktg%2B3e%2FfXyDfzfGAEINVzHCLaaWdNB1BUMrAXdTxhV4Hsr6KVl8STJlHYDgH6Q6hS8T9JNnt0t9ycW9A%2BNayvHwuYdpBqEbyX9KSYlDvXZWMhLMOQ5C%2BNb00jrN96Zl3mVQhjinlDIniDDMuX5tTSP8BUDgijptlKUuOqLAVGmJS1wBO5A7YSA7OyZGdzCOVABL09p9dTFUeictFl%2Fgxb%2BahZAhvlr2smAB%2FZ4tmhfnhneIiohL%2BJXRJ0Gv7EN0e0crO5TJawi%2ByGLrVHZhS6yD%2BC0chJ2bMbyhN4gtbP5%2FRZ43iVobdlVnRmI9JUbpKUz3QcD0qqUiAA%2FH4C7vZxi9RNVY6m16ve4UrPn6AJrocA7MRtjLa%2FY2fpITAxwyief2%2Be8I%2BRFMhPfRyduMZCMV5WuKJhjUU3oi9nQC7p9X5HtYTC2t09%2BEsiACoh6ukypajVFWAAwQQN9LQDbMM6mr9UGOqUBXn9QboZxLQaQYjSd5aXKGf74FUqCrUaXK5L07iIAipgm%2BcugQkEHtNJEjViZ724B6pnmr%2FesLP%2Fr%2F1zjv5fQ94KrxKGoBzu8uA9UPSZjqzcdn%2BSYO7iESK9LtMEoKsfPPEW61jG0GjmMiifqCPq6fR487j4ulQjA7ZPrU5WAE31OgOW0Sf35Jik291nFOAw%2B2ypWyZTv01V5uY3aCm2PGpIP4MZl&X-Amz-Signature=825adec0cba35ef0419c9624edc2f27049d5a1be3ecc724b2140887f2527d9cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
