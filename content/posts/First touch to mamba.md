---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UVNXE4Z%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T023356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDJsyDxUuKbUGbyDImoKjrtSAKGSXrpmpVLrlvXp0rSuQIhAKa0ymlys8YD%2FM25Lx7JjMpyo89oFLOEA4aczvimniAVKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw3JRVOAJccMXrxhsUq3ANo1KMv99%2FYUu1CobMEaIRyOSrBquuJEHW15Soood1abdXYiB7tdP1ttNk6NBmjYtFTzkPnzEy%2BsEYiCQC70JOxCy4%2BsvNHsTbOGP8DNFGFoUVYKzLJ0ISARbiW77jho3lhlymPYYUy%2Bz41%2BzSMqqBfKXmOUdTY5erZI90WhmhnEBD%2FvdKsPGA6jO5TvKbCFFbjmIX0%2Fn29%2FKQEX6VGUaDV2OESbuvQFKkjyaqFc3I68SMx5y2ryMQ6EhbUPC229fWTYyYYqivTkjDZpKf1qVRhVumLqJAFYkeEd6ujbBB9kPgzc7zfFsCJFuq8UfCjCPcl7HbK6NexwcG789nY7QaO9BP7aLiQeT9hdEFvY8P8x7y7ewk8V2hjcOo1FUKor9Q423zl8jqXr6aX%2BpMucMpQy8T6pk1VHFGZGakL3nr2s8OjOPy%2B4zedNf4w617dbSscqkRk3rF7TMNS4UjAsnqyofRM7%2FceLKwrZmxC3%2BwJvpWtWslGlrXCfzAvi8OR0FV1W8pNkq%2Bnydp0so7KSuJBlxKkCj5rU%2BjD3K9q49MAb5IAKeyfzPbIYTIPePgnw5lJYaDz8IkOd%2F8eBmj8eS3YFu369XUAwjDJ17gC2HQE7KW8dg2S1al%2BithF3jD9t%2BLRBjqkAeyv4IPOqbbr8KLGVs59ab%2FUvdlkneTJJA2OHXbexJNNeAhAqlJ9wtwedRfO6SY%2FQMou%2BOkZ5C3%2F%2FYiSuC1E0YA7Bc%2Fef2ZKrbCmJStTHyyKSO9JjoGsLHJdPuoEAoHoIRRnXOmad507T31I%2BcdN8BGjAFSmvkpwrrPPVZUlY4hJ0ke2XW2HzFtOGaVg1pr%2FSDvRiSA30yKgD%2F11EOTGtw4Zj2JE&X-Amz-Signature=f0b0e8fdf11df9096060dbd750815a665095e9dc1d4c92f05e61dc82f42590d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
