---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CDDKPHG%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T204103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQCb8o2YuRZVsMqMzLnBWD1LGBTTLNfZcBjniA8eh799QQIhAINXNTA6R1H8pfOTyhK4ZD5kwaVk6ysX7TbrmLelck8lKv8DCAUQABoMNjM3NDIzMTgzODA1IgxZ4p7nxPhkaY3H%2FXgq3ANCjviDEKBqk7%2BOSMJfbSWhKtLAUnIrlzVU%2BDfc7P%2BA5eDGUTIJyiPzioxU7IL9rMjdMRVRNCyOnxeusqBtTVilb3n1ucvKux8QQEx9YBKmRZdLZLE%2FNeArAHc%2BBJSLiSFnxR0j4sy%2BHJeteUbbGye19uuaSGt4s9oenjkyjd4iqO4w3QNjGdZYxTtBPI1aaTRbltQRwcW1rOxhEkcxSCfjHl5%2B9E2zsZ4beoTWJecgVLHZo1nwXgTWexA1MzEfCKcK2fdzvHBUVF70estZzqPvuZQJFNsmpWhoODDi8c0LsYOXBACzYOZ6mwVUrVn7AWGwBzpexTvEaCb%2B3xMj156ueHcugp%2FZFQxXGFPoGooblz2BgL%2FB%2Fi2KPIS%2BVHybBPNdBDb%2FzW%2BgD8Uf8eFCE5O3C56Cjx%2Bsssp8fkLP8uXusEDVM6D8qRF%2BKDAcsntg4WAF2DbHbBpMcVx%2FcfqS8zFSDVzFDahB1%2FqhLKoxN%2FJOqEP6tfFYnd%2B98PZHPKvrJijQi3eUWabCJvcx6p8feG8unIOFyaUsLqA26S8T4OTLiGkYFjTuec847EaX4l84slr4MMSYyky4gVMrlaNqG%2FF6gjCQiPLmn4ExBkrCI%2BmlYa1SZfaRg%2BCtR%2FSBXzC%2BzKbVBjqkAXVV9syuU7BUywbNoVEQ0d8j8mLJRcAdtzOLSajUxa8TwT7wjanlNLDVH9i5El%2Bmqpl%2F2fTFA2pSsvedyQXEa61BhjEd7UcVOP7U1zSSxO2KkRF92TpZYxVXAHIr3uBjXsL%2F1vvwFkYS5s6jYFufLgLEUFRI8n63Av4GDsN%2F9fP9hIjzJMQJF3SMULcWBKtEr4gnhPzLjO36QmmssH%2FwuFt6fxQp&X-Amz-Signature=78933b59077a53b7dc5f77303d1d95a755088d0b11439ab1245ccb1389a13d80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
