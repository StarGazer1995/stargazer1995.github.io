---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646YVBRO5%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T075448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF96a6i6UUstwnAppAJGjHBau17XANCRHh31ye7gudPHAiB2OkIvMhOWiCqLykgtAVgoJXUsunbO4S67ThAQnbXZXiqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMhE1pumlgWJ%2BYp1qKtwDLJ5bxsc69R2gyToTNwv74Xe93V5rko8upjpe4Vy%2BnYa6CkU6Zs7jOQhjtKwZmCS2Ez%2BFpUk%2BabogSr9enR9jPAszCpXPuT4kwXGnzGDBH6%2B3SOskPW6A7g44X%2BCTvjfmI3M5uljTTOfJ6WXWUs61XxK0ZFuZkckqPGfDZW0D6Fopw23CUwjxDuKLSHPRocRQ3bUu5STcjWvPDSLCpXGJDJzaBP%2BdavVVse84ZH%2Bz26gjbaxcVv1FOau6vOh5dRMoAvKhJpo2jr5McZ8oHiDMq7jL4wsbH9mRxbi9eVf0K1Mmr1dagaXoXCAnkR5G9IoDNK3UYXxfd97csNLmC4Rpm9hJ3%2B8dKnq0tfYymz1v0V%2B4TJsXWQb%2Ftz9iJJg1DxEyYNyxUcUCsGfItxPVnj9jgPy0f7yPdmobVtTpFg0qkCLHvJ7qWEnAH4lAs5j72%2F2dAOmuEqgdUfZAqp5DFerawkq7aARFgw0Nzvty8Kd2XhdeYu6uk8ZPvZgntKEWbSxgS6q0h3RN7ifTypU2bjvBml%2BZIiowm8a0MyNqytUJAhRhRAWYrPssHv7lBzxPydQxsv%2FFGWbTmDZ9c6ysP1RgLhJIXhH3bq1DkY%2BOPaN9Ah%2BQgETTqlJx%2FYmaiKcwxfqq0AY6pgGYC%2BeiyRhvYU%2FErUwKtQZvbfxT8haTTwPlQhDye9zVQTuJWO79F0pK1KxOsExEoSRzOiXO0NvXuPtfkY47w8hAW1VqjZ6h89rgTCEaDxyV2Tgq7b7D4NtxsXI5PB8rXxAYXNxYl6eejgUiHCEu7LHgNBoHY8v64wBfYwCxPaTynXqSD29dc2Jc1aJCqrn5QxGIYaEtAiN64rceMZmNUchi5lmYD0d9&X-Amz-Signature=13b7ed7b7d884cfdfa607ead27269e4d7666a8127d9bd37daae8bceed6ee745b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
