---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627YTWYDX%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T223523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQDR4vQ0vHVE5x7yqpnIzGafQO5KQMOgthiDETehsCaGvQIgZMMvAkmIe7aKBuRiVy4M6vwStGCoXT%2B%2Bm9%2F4lWuKT6EqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLpd4auTb8wBvD5FgSrcA3Zc8R64DnInO%2Fe46v9s2L0O%2BGvGFQnSVOQNSZqgacREsCzBd0nDsYHct6OUGjimmWQHhnJasiFq81KbkPUmfoNeiA6Oa4GhBrC0avHl1COYtH%2Fw3CSpGYZFW7TfWgMgacElcJvb4N3Z8XKWHcm21CyAfN%2BzjIGAyaVRgo%2BoPopcPrdtMldI15icgKVhZqUU7JCUNgc8%2FkffO3TgDdyKlimF%2BqpwH1rcUEgZ0tmq3veNmFOKxJjA0AM2Mz1mycu6VbuMXtig8JfgYrfU45K9zhs%2B96SVcwHHf5UtwOi5mAIoSbpyi97UqVifv5f4uTtYrPPLoz1NjMY83ZNWaNLKuBb03qxgd7h2gM3oc4ByOHoU0oVi6fJ89eQ6VZRgLdALpHgRIqEhMnCCti3TCI%2Blq0i1c5I1I9ehb7VKmJwMrBLSns0dOePzWv4c1vau3QwPKiHANHluJhikDO0iLvYqmezxj9LnlP1ErjPDUVfVHQSAhiYpvZarkdgU2oN8nxPfwyeg4Gi3n0BH%2F2QmSTsZyxHUZ6KiZsIGp0rlcUyM23AoCVnq2H2ZPC3BBcb06Etn1sGTEfXgiAZZMuXXe5m6nA%2FklCd5WBOirqiZA58%2BggCs3S29q9AGjTy%2FESQvMMzHstQGOqUBHbaw%2BNq0Ba5s1Pbl2DIsfWHBNylZ6TVO2svx3QkZBD0JaZMxNcUDIp7wQsGWOuQMj7OYT9%2Fox4rbokb1SjzWhfvbHjE7ZAKk7R6e5Nlmb9TajRRyTQYrF8%2BwsHfo8RSz%2FtUeFJSMaMiz7aPKrSAu7sXVENjRbXIs%2FfSClANl4D6WuM2Z5vAaEoVSzfeeqHET6zxGLf4GmRifVTC62lRj%2FAV1dnWl&X-Amz-Signature=7ab91c666cb07cab9d21b43dbcec408917495512103eab75679a532b9baad5d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
