---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665V275JYN%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T015811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGa4AjUwFeR002uE2y6l10w6SRUWOO8C%2F%2BdEp2gOFFvXAiEAow3fxf6mZqxs8%2FxwCX%2BQDdAXbuiDwo443VkMPOajIEAq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDIuaRn6A5GXwYEdKSircAz%2FVqDmAS7UVXZnTGx8CQk2TIYy6fdoxofWLO5xgwASl5%2Bj5JA9shMylKZfGsTILzcdqMgViVqkoew5op5gYfVtp1gBktwXXesjGRQxPYFWEKJ9t4N8Hju1KFzs3r5j98dDu48zCqVtBpnbL7l1kgbBSkH0WYdupVC%2BatvLJlq5UktCbF0YcPBjxNRvxOnx6TGcs61T0kTG5XbZImi6yxBP5pjA6AP2OBAuwFf1fUAMjG%2B67TGGmZOW12Qgq3Dg%2FHGjSBzbS9sRC2RSKXmJazWuPpfv23rjiTDv5E1viOqnwn%2BFCKblHKJBjZdFwyI%2BrmG8Yr%2BHd7XqBooE9Ww3Pyx6SbuCPv7tmp742tqVk3FlpSY0kqxXKcumfq0ypwFt6zJ9z%2ByxfJPzShw%2Fq5fDp4DxMvWbnuXeYwHW%2B8rXgTnLffnNmj7PU5tpr7yQZixaR%2BdVUPrBKomOvM7UL2jXnPRcRJy6OihxOTkLny9Jfzwp3H1YE72pkWBGWflXrttSdqT9HOWS2qT0OWDaQ6YTumt5BH%2BLMIn4Bak2AX0Y4o%2BFNas5LhGx4kSdwjzPrMb%2B8Bay4HpdwGIiJWn%2BaeywBP7zFNnHeYRBgtRtfousy4MUKmqD8NK%2BpUlB9melsMLrdk9AGOqUBnKWlsPlMmIO9Q5UvDVAei796LeLcpTEwqyOzzg0MTeWNumPOX5gXotfeUznGrM9%2FDDsxSZkfnL9uEsqEAEEELqfRpz42Agfbn7UwjozjsjDxQ0i4LpcF0pM5I1cjVPSjgWRO%2Bs8lXlJ62bIoSrh7hTdYzAjF49xq%2B%2BLRJIPUvyR2Z%2BAoS7zd9Lz3qpnC89sRH9BOVO%2BGnpV%2FyO1XVwvMFjfKDoDc&X-Amz-Signature=c416e32acaea8ceffaa4bbb86f9d92d7f5b60d58c7dea11f203215da8a89c19e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
