---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKPKZC2B%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T134931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIQDAWzPUPERlu2eha8yB8MA%2FGNhJ%2FjyvsANsPmLQZK%2FuSwIgRwtX%2BWKzbqKNkJ3PRMleVBcmNLKRNtZbWGNwtXzNLTcq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNeM6mVnUJssKIwZRyrcA0BAK7ixIQuhw77ktJKS1H%2FoiNqRpLQEIGqTbXHJoVO2vpj1e3vfgOOoidT1Y4FEiW1Lzedzw9%2Ba6xRVpCsEZVm4G7id2JLyRGiw91XhMCIyrFsv5f8LOidcsgvqCPjj9FVxdiJSQaWhZZpRIf7m0%2FFZRnnyBpiQ3ENtK7%2BPtgydGkJgFgh151thWN4cxkTJRc%2FAN8T80BP6ET1e%2FuqF8891rCutvHpd6JJu1dWPUGdNnS1Yu39h0UYIUst2Mf2ogdlFqlRuf5lU1ePGwuxE1nhYuLTukYD%2B%2F7T3qpkYXHMVl55rThqDydRq4QQzh81H0L7M5yP9%2BAb5vy4zgFcwgr7YIzqT37adtgP8s0CqltCjqlnzjW0VqJ573fBf98%2BwqO7RgTVurczXoUfPz7imC6J78tWL4MFWMBLo0HTsHtuaDyQkn4NnLQHX79D0auhbxC4RZ%2FtHpJzBbO0leryEDyX8BnMG4MkTRfqE2nGv8geckRTYNSAfpbRexkXLrRGekskLfn%2BH7kRtRM2M3%2FQGUmlMBJJG4kS8zWJK2%2FwhQBiTq5pWuDrEEwFi5IvK2yTAs0La1PWvR47Kr6zAaiArgR8kEICIJHjPU7XKAaBtKNqZAqnhbzz7WTXeGkLpMNHHjNAGOqUBK70OdtCPX4IH1BxnA2tyvFCfHdSFqu%2F5OHmPSIhllcHpwn2yhcbHAkTpLR%2BDdrn5ll1IQqSacByeuiZfwMhQMGw9J71XTcyXyy1c7aMA3tALIgVk7AWs5MbKt0ijItaXQlTBRWUH%2Bip5%2F91RaJhPxKwuWkCn8JnB%2Bh2wSDQgtZoxyoyv2x32%2F33BFfrXPK4ivjs8Ot4OucC1EIXw%2F23TSkme1VwB&X-Amz-Signature=d7ef201d15296279498eeb9845b58e339effd9de58b886be697b1be6324a3ae4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
