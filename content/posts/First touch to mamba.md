---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUFVZC2G%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T222234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHW%2FtnlurNE5RN%2Bwl9WH9r2YveZjlK7MNudVgg8aSuKxAiEArHy0Z%2FWF5r0Q35kBVopSnqJe1%2Ba6FwzfqF67TaxKouMq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDDJgj0lPzP2P5araICrcA3mCgPj6n6Cv1XoJ5NFue7IeVENJmPJiOkoi%2FG%2F2Wgg%2BnwUFzrBD%2B%2B5X8wpB9ujUwyZ5rqM5LmsGaZBFHKHCp%2Bcgx%2FgLEfI71V7lxflb32TrB2jsxeNiQb3CHSOzaWyOOBeIC4Xyzo3vS7pOcAedYoUgr0pEsgLMOxFaRsV0RV0Bxvx7ZqRYwmMnJiggefhiYN0PIPy2W%2FFFdRKvTsWTKdYum371jAsnJyzU6kNJm6gGLLFLtVF8crlrPS1zye9VcR3k7jypuoBtU653CyoWGqJRSdimOUjgiRyjLGuo2YmwRbp3S0J3MVWfmNVAEDoKlRqlwlx7tRv9eFm9XXd%2BRgyAi0YY6s1xcSmYE5OjqPnoF5WqHI5XwcXxAjMevMLyEIp0uA%2BooWJXxr68LrEd%2F4CgB6Tn00aVa56Q3l3yhajFO6e2ONUuGwTASf%2FT5cI%2Fz2FlNwUvZV8Zzj%2FC9V%2BO%2B94a5zfiyji0dSTtyiaMM5T2ILsp%2BNtlYupNvH5cS6l2MTWq2fvTeJomqyR%2FUFDCAuLzTDZ7icMLFB9GUSYZcW8HKnbUp0%2BXhR0T%2BEIuFnxm8zLaNMAaGHWMzIVmWJsvaMWb65PgtFbgEk6JzdIdvrk0ZQSeltClZcQgjGYKMIuvmNQGOqUBabhKMMO78WkDSHqD%2F5%2F1UjuVjqg%2Fygm0qjCu1QUaq2bXxh9PNABQO8RJY60b4tTVCghq4f6nBooD3QjrNJP4hGQQ4zWbZ%2BcraFvVFHu%2BMEPg%2FTX8BxOF2Two%2BG%2B5%2B40qOZmx%2Ft9xsVP9Z0RL6GcuRMyy3vH%2FuaJgobhW0pkvFQaj4JIuNg%2B5bzNfwNhJd3vEUYWWFeyfpS%2BAbTHkXY47cTe0qDui&X-Amz-Signature=371aa1dfed0e1e5b4ea1654482216967d84c02018591e1603d096f6468779866&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
