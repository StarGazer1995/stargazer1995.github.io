---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642FLQUAB%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T111109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCCpguscoUpfPvoc28zKHNv%2F3gkIDCQdGkHLUOFezSXXAIgEfhTEvlUGz9Pzii7B1Qy5sdGuZESuaOTQEPmjTSsDB0qiAQI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDODINByHlUA4RE7TnSrcA9b51QiXFVqtSPQn33fTa8dZJJaIpCA3a7Q%2BU2Sp%2FCyiYQVm1MCr2mSorS7ekdKxtg2TAXmUKEW65AYDEKTgTIOEH1GghVE4H4aN%2FKQHQWqouJNhYWZmq9FwaJfthJkjSxEX47NIgcQTsXKewfPtApzejAq6aNuemXViYXc0FsJvuZQkgxnepEtS232suSqda9Vd3NTBC8SZFqPTjtNQ9rBgUw8gZEhCZojWtWvRY1DcwvPFnGfheYCJ5RRGL6scmy560th%2Boqzi6i1HGOCJ%2FXg9gbjoMMuJqWOjSjrgjL5pvRg%2F%2BR3JlzfaHz5EOtok8L2gXI30NtzxOZkW8bbKmhmGMXXhAd30weuXuquaBmZTgYVS0vI1d0acFSRatQF3HGLWjEeuvC0ccE80YfZS6H9O4ydD%2FC%2ByPA8XG9hsitSEcqQVRRXjECfjd64sJkcsx%2BkTwyv58%2B1mjYp097sqIwrUaJXNfUuWXb%2F1zO76RI6W03T7ktPE%2BYq9G1fBxPZXVrmsfIFJzVFM51MOs8XKaqaU3%2FnqAP4x%2Bb6t0PeZ8K%2F6Swh6%2FHedqmiEJTaI9LlrwOKcJkxl5zMuDAFSacQhYFmsAtCsPGpm7ddV0ULL0JzwaIERPCi34SI5SoCmMLGJ69AGOqUBH%2BTEpL9tg8nRiuPrfN0GCYu5DSiYRXSfD1B%2F8TgwBYzyvVaUZlEviuY7ZpYS3KASt2sWsTWnT1hWLK5KQ6Skh4IRVJ4Uc4YQz4EX6j4WgrOWhwYnbr4fctHeRqHy%2FCMIjbV3pcTQ%2FFIUnzQjNEZxHjtVaGEZ6arBTMnN84s76N7EaLa6LR9N5Z87bDEoligQ4RlvCjHl2ZuTINmxvw7nftGhawEn&X-Amz-Signature=cfa00ad5a01f17c77a379381b8a1528ff9895f8a2dbc4d58244d17cc210c88eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
