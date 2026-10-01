---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673YZBPDI%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T075609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHZBZt9RcqqDuyMyEIiCPt6G3gBQ1ArgHgs9%2FZ%2FPtFHwAiEApeCvpeIw0hZ4sYfI%2Ben9C1hOx7db1%2Bxn4avFzSltJbAq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDAZHwLslg82kSHdZ5SrcA%2FYunN5WcU0MH8jZiBdMhPXJg0%2B%2BmTL4XJ2y7hmFmbQIGmVA8NnBjilWUVDZdklWp6N1w5luRxnhS8A4Eu%2Fh6fuzafyFcERudm1qsGsXRKuC1KFTcVcQHaOs%2BJeIhH8AQZje5%2FDzU7qV9D7rERVc6Q%2BNe7mUewYwKERcvBUPPFfbhBN7524GROhsy%2BjET7Sm5ZlSf%2BPqNbczNf4Hq1MMrYmyzIjnH%2B2lwPTl5jr4y9zMuWncE1x4xLpj2SnFI2XNJj3I1PFyGzV2KTWiaQXkZecfp%2FxxRY8F432%2BhdQUEH%2Fxdxm%2FgSjWWvkMInkquKu0jh6HEO2VmELSBAV4%2Bv%2FXBfxHvtpzT%2FeFg6Y05A452K4Tb2j1yb9haS%2BzAgnnA9iHrz7Y2p%2FVT8Mu8H8fIaE6th25b1h90S%2BtmgdtUnfrjatP6gyygnyNBBMSgczXQm8inyn9r%2FHwyJzuBUhBTERVcHAZjt7OxryM4wAlP13AYwKVI%2BLrgMtcPashMtVzB0gkbyOQzyH3KUGX3ThIobF6Yz1SphTRnXwSGuzd%2BkW82igWdGU9Dgj4o%2F72kwvkhEEmFH1y%2BMgJ2Zr9WKKkHGkHisNydDSxIrpvgYURF67JavPwtd0vy5hO8PXY6oPZMIuN%2BNUGOqUBRZg%2BybYyYI9l75BDh9Iscuzm8cJda%2BF%2BdA1sloQiYL1GiZ1ixL98JmSbJtlhQHXYc93hsBurnuz7zOYZzhH9CUE9peT0jKnXKi7QcZnyglhkd1U08D3cFOOI%2BLsksqzQOiSUombQsu4ZARU3LOu6hGl%2Fvf4MFFLGjjwS0FOIlQ%2B9hSLr%2FXMPRHTlSvZmDqehYhE6K5DiEAsamFWKZelIypgfAOfk&X-Amz-Signature=e9e5ff560782227b160a07101cace5f3b5dbd5dacb587c400cc7c890bfa4d6f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
