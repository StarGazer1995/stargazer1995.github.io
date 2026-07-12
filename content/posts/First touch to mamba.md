---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQXXXEDG%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T184626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJIMEYCIQCb%2BtgqiQ4C7X0RMVFR6ukcf58TlB%2B71G35a8X6jpe8ewIhAO4IDd%2BGDB1s2TD4aMirD7Gz4VO%2FItSMeFaLy2ZkRlpvKogECOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzukFtp6isB5W4IYGIq3AOO8WeVLigXnjPvN7g6RLkceAZ8WrLmAHtkwtVwy5bNauLJUcT4McsffHCZ7DbBo3o%2Bb%2B7sHtlYWuEuZK%2BxyomQaQCJuhufVQ8lWIyPajEcA297F28qoTfv2OOz%2BmGX3ofup6eviLoPx7HbaoG8TsFKt9rGc%2BaNWE4go6D68W2SBUMp%2B6V%2BNL9enFvsT9z9YlDl6QtmyRmCjPteB1NiQAzxa3YsGeHmzrS2EjKX18NAyuhxKTKOEL1lrUiQySOw393aXLuvxtOIJuVzVCrSr6Qmv3N89vlIYWdOmPBwnjxP4ZFzvh8gacJEQC1bTD9kAaU840IIcdEndJX9Nj4%2Ffe8pr%2Fdku815qAARcgH3LylLb9crh9BP45vyk%2Bj5IE4oUGYjsAcUmsVyK%2BgatFZ9ZmiwbOXyTov3w5As2iMSpQM71GPL4oR%2F8siHyyxubuuD7LP6mVbmWy29DZCE6hFlzWKGu98cfg8RyaPofTYczbi8oBhz4seH1zDZW%2FA8AUINNufQ0%2BmZWHgvIjz60SXeAtJt9vnkMdx7%2FTP5H%2BH8SeQMMwn5Li%2BXDgnZs5g%2B0hekKdvGYG6GHz6wnHQCcAMcABZGVR5iDFKP1vTbbd%2FTw4B6K0j2zCJepi%2BMk5X7ZjDSjM%2FSBjqkAShj5sodDavq5FrSzMMmRKYjycoDHYwohPC0PLIPgoA8Y2D8zcpuwLPDv6deJVvR5bdORuhzh2EdmYr4IDBPhrss0nH00ukGkxkUbazaqPjLVZIFVoUu1iU7D1E1Ec6GjDDECEc%2FK7UO%2BnUbOkj61jia92HgogQnmjhLQIYmXpJyw9wGFLKRq3vnALYS9qJBLuNZ3n8c3GbDdIH4YQwZqDM2c5pf&X-Amz-Signature=48a5df77c9cf8fae9338bc7dd649957ea8646ff647e36262276c24edc593cf79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
