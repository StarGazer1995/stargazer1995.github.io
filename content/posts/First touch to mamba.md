---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GAQRCNY%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T053751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJGMEQCIGzsEZfKx2x4K7Ij6c1t6rFLhnYZILlWPvM3fffhwK4JAiBRCIr1%2BaKzY8vLeZ3cxga73m4RXc%2FRu%2BbYi4O39C2gRyr%2FAwhGEAAaDDYzNzQyMzE4MzgwNSIMF3AsP4%2FvelLtqjFKKtwD4%2FgVoJS2fR%2BYa%2BWb63HVV6BZkAYb9Az0t0%2FDg8nZRpI3WVNfcAmZWf7%2BDg1rwc0pARySU68trMz8wT9f9oN7Apc3QXefxtNNvNT%2BvPrMb4i56ylQephW%2FBMmHmrIgqmUaNcHJwNoDBctAG%2F%2FdIjS9LW50kzftiNxR2NR7efvrYeaAKZyn8eOprcjiZyxT%2BTXgjJ5Cs44tqEeWaespoMtvBhDyId6%2BA%2BYgUAX9%2FdOz0%2FtxnvEbghA0Yw%2B1w1CWRum%2FHY2dmng6jwgNkDQ8qog%2F0ENs5jwRJ%2FdQqudxiZA9nC3SBH9O1tQ0k0ykj4kR4T43ejc%2BVTGr5%2B6zBTD93UNjONPKlCjvSwTmKO8Dlp%2FRt6tBEWuP1db%2FhK3oqsgYutVg7Eg%2FVP3zU0nhn%2FYtow55H5AJZiMCD7xS9Qh0HmHLgL6zH%2FtWUU0iEFs%2Fe9hgSCN3tCJ%2BVwWo39do5Oz5hZ9srHW8sUXKd7a1b4A6%2FxgoS7iRpF0SDiTNiVry05oECTLtU5n11hVRO4%2FZF%2BJ9jdAMghuzk1YOrioMSvcHzI40bMsDrvMe63EDeQPQbg1dSD5Su3J%2FzF91Ao0iD4C7CwDRppqnLSFijbsPWSLdEiDF0iSn7dDZH4xwobYbqkw%2Bc6b0wY6pgHlo%2FE0SIJPjo7LHVlkzwI6jo3O%2B35DLzvuak2UOyzRDSsElQfHgZWadxs1s%2BIdxjyMwFWecv6IZkDYHc4PC6cTQ5q2UBeIazYLIuRyrZt6iqKeYMKYocGIyWKApnFTKQjqcG6icd9Iv9Rl4iql%2FDY87ZBWrzZ4AzGHakdHk4MhlruRzZ7kTbDapNVnwCCiTj4pL39UoCGFdjxL8%2FZpuAGB3qC9iOmn&X-Amz-Signature=99e26c06de79bb8a48597d8109e628b16dd8a045159a89e9c33a60af61b9a5c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
