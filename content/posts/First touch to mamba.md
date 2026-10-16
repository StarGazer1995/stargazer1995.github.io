---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665B2VMSJF%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T174502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIQDQOn%2FUbgeJXvd05gFknp6FMaT7E6HyuJKwAUasd6hLzAIgPRWe6Nj9TxbERQA1uKAARui8VwatCQxPfEqWcGxH40QqiAQI6f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPaL7%2BBjung6o5n6vCrcA9oBezyy%2FSQpTW8yqIsisDTehhp1DLBTsdTgi%2Bo9WDlz7SBteiBh%2F%2FbdgpgPO70JUO4E%2FYOVrX39XWpSsnWO%2FS4ogZ0xykbi77c%2B8AfpNSAR7txZc6Q5zt9A1ZdzVL%2FgdU9un1eC6I8JyGikgqgjsJGdyjPHkUSxfMUnoSq%2FWjTWHqPV%2BewB61TYo8pJhGJK0ZA%2BHifiz7OXrZxeP6jBXhKTrwoe03NY6K%2BEK6LJYnnZTMnfF2%2BHOkfN9pgf9F8Bm19XgHYySY9nNo7Z9yAQHEV13UlruWwN8fZGqH86Z3%2BCLACT%2FHI59NKpRuO4oxuAslKpwPRRDmRSKrN7wWnkY26OXFml32Qb682uYhXuqTyWiNayE%2FHBr6N%2Bm0umO28XWw%2FjYHih7kKnHTwDEhjz0TzmasIzsTjLavNc%2FMvwlC5YsWkKsBGpWYjWOPvbQ8yCYAIgTvY4%2ByK9%2FMbyhLbQSLbWSLFsvrK98KO%2FE%2FFF0NIH%2FJ0NtXFIbY3YRZXqodVHrp3%2F2840mO0ebhCTuVxv%2FFgBqRl%2FkngjZ1HACR5qdULQO3lOyZPY20U2anS9FU1Usz8OLnRdAgU3WJtn0mAsCSVC6rnisI5FAKH%2FflivDgOnnYk4sFUQIMEMTglfMPSuydYGOqUBTVKyMMOXpQ0ba%2FguckvkjDBpz2FAV4bamnF0Why89%2F4Yjn3o34LZP5FKV6363f0VHRqukB5V7OagBlt%2BKwZAubkqxmJmdoW%2BrsQhd4D%2BpfldKAwLBmqY0jaLHRys37VZCaaCflahBSUKMDCQ72BFCpSqFtwo2kCQNgeMXo63l2pLTeExBHkJwxVlQ%2FR%2B7Wj355e%2BbfN4T1FH3fQBvIL%2Brz7CuKAr&X-Amz-Signature=8442ad4d6b40c801a656128e7854a7d97b93bfcc2c7af9089559b12dacc21810&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
