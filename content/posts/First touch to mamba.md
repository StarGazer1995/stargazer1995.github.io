---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642L7VM2W%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T124859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIFHmKJAj4F0D%2Fa%2B0TrTgTVXYXXohoXg96jburkIxjGVHAiEA0duv%2FEKEEokGi0yB4LDa8so05iQtLyOzfrMU6M4EpmMqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5tA9SIrqiUPLpFZCrcA6oeANUP6Mic1NuXb%2Fa14MoJOV1piVUHupgEXbdMtOkHJ%2FaUfTVYdaAYI7RmycIkAPfpk2imW%2FbkcKHS%2B2dUwH9%2BBn0st6jQu4e9Cv4w6yryFF%2BZNa4iUrgb3%2B8JkLX2sYO%2Fo8UhPFt1FNUNV8UI3%2FDeqtnC1r7C6T4TAAvY4EvgtiYd69eXadmuFd8s4CyaZDYE8m6x75nuzb6ybkdZM3479GoinOBd39TDt3HLMusX%2BFqAh2GxvvkDf1lE7V8zSSXQbs9XwtoadNbUzzaSj3Uj3Q2Xp5tK0CY8HMqUnQBzc%2B5Fjg%2B4rIBr0zDoMGU2ituIvqwl5cfbI7nlnt3rLbcjJX5Y1mTBiKORHGXh3STvyueiDAfcPvqjtz916o0VeKr1ZDqlqRVuv%2BryRty0Gp%2Bmz1oljontk5Le9w4AXCfYH%2FB4tDeQMWAnlbsoTU4fMnMDGkc3zoCWUn0HqDB93SFIjsRPss1zzfFFEj7JamOTrjZame3zkSS%2Bh7PrrSUVUI3bT7BYbJ7MwPGbtTGwmjbtEwPWLnIVkbm8TUFnmKM2z13vcaPiYhmv5iT4RYFcLMAtC3MOQeIjcYP4fZoLwjkqZy8dtxOPQNcueLKWKg2BbH9IpMJJWVmWm80OMJCkyNIGOqUB7saySi5tSRN9VjZ1hj5PK74Peb7yKFn7vPF9NTvbksF%2BhpnHxOd6%2FWwp%2Fm7w67fNrbb1V8aNkQw92mVHgYCAs58HUMMS%2BB6gilNJkl6hJA2FZZjHGBmpu7T74zS9kD08JjaaunfF2UzjO7%2FUoFAFlSXU6yE%2Fa%2BZH%2BM0D126i%2BX483Oa3bxk761bcWzL7lP0rXxBVdO%2B86ajO2ftyaQvzBxOnXEpt&X-Amz-Signature=8ebc467d187caf37ca76f8d9b96a74e21a5a17736b0ef66272f108ffcad2bdb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
