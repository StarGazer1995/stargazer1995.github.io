---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RSALHRE%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T062215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCc5GwAfmW%2FqdwXXa9iU3a9KHTPHp5iy8u0HxvwLF6%2FrAIgETkob%2FW6b8oW3LAZlaWRjTHdnBrPvTQh9V2rViyVbAwq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDAR8Q%2FwWHWkKlbb2ZircA0KtYKecPDn%2F%2Ft5z13s%2FIwVnZVjUWZf1zYH%2FWSevNqYnHxEYH9bYOYel%2F4vCkxHITgX1N57OU6Mf7WIy8SPAR%2FviRxWTNGUGuYBwUxmDFdBdw2iwOR%2FL97zA3WA1ERE3FpUjj9nVV2UvTn9DTgkNO7NfnLHh8v2C%2BHKi5LBcdHweWNNPmulPtMPclO%2FHT5xZYi5KXmoYuI8TEyZOS6BwmW2bkl5BxxOqA48yK1%2BxQ1xd3kUpwXUKu8dRLR5L6BTN6p6HpS2qQW3t7p4FmcSMQPoWWk3LpQzH%2BxObJoUf4MC1333S%2FQKuqDyuCZi%2F5JjWltu4a%2B8O7eZ%2FNAVy6cbXlv0ns%2BlBnLlsohgtgUtskcEV205rTgP0HSzzw8hXG7B6%2BUxADwY9rv1NIw4AVV8h0UNb6Skda6VWxPRQ%2FW4bRoduWEbF6pWEQ9Hx323wcrBUbtfIN0D50urpMOTk7B5igoiT3LZIZWV8CZI%2BRJWCBd%2FNa%2B9VxImvkrLzOYymSgKDir8sKQhGnnqPuXis1lqmFLkIpomBRJNu14LGsPa0lNZRD8owMrqahHpRzMC3nzvQ0ARTGVPFpZXEwArpaAcfy6ejHMtjkZk37571X5KtKKDi91HIkZMpUldUMINjMMuyj9QGOqUBjm9QZI0g7iHTNhoKD5bdYoBpLsLjuEjpUyBU38EOeB2SGIF045r8NfiAc%2BPqNoyYiMZAPkOZ5xx6ndgPafTi2q7iVGb%2B1tnRV68GBvkJzJSBP8brI%2BuHXCFUwBVGfrc%2BGvbZNSf%2FlCUz8GdwFQ6oCDFxZQGgxc1Gh9meaZq%2F%2B%2BR1qkTaO2haAVGHz%2F%2FfLxwVbKOUkmAyewOGOY%2BHHv3odGCtv45V&X-Amz-Signature=cd8f98ce5868b202d0f8c8574660d771ac358114ba81d6f89d270728e37fc8b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
