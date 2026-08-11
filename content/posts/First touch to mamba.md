---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNXNFX4O%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T144925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9ItWIzNGj2eTCyGb1RuMqitnBtvGyxCuC7GG6X3XBPwIhAM8%2BHEQgwnzoVryEoHy3zCO7bE4vXIRg4G1kQsJsGzRxKogECLf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRvspEBXXJ50P%2B93oq3ANVV0CMe1awY408gdg1g5Hsoy%2BzLfVJu15fcS%2Fo%2Bhzlj2Qw%2BknaMKIffVMw%2F3zPdmh3L01fm5XsAy2e87mmHXQI3CFsbN38WBc8qeiMFvnUgHHu1P%2B4wcBBzdB%2BMr8BYKFzRG7TstTjPTF%2BtgtyyTQYHEBEgNdTmgjDCLyDbJz0TOihCuh21Kk15xp09h06ahIwolkeRyPf4B7nV29ZVMZQZHwBBxFJ2Ham3%2FLmeGoyqf0U56ZxR3AYtKn%2FBWkNclQIuXAattX1vt0XYVG%2Fw5OOaLMDKR1vbqRbaleMbia0YkN4f8s3AKYaRgG41iGgR7e6ZU02t8C%2FLFNeiUFpCRp46RcKIh5THsoP8SzMQP6m%2FJeyGJtc5q41R72zWQo2gwkNfchtyuzX%2FtCZ0YPh4W%2B%2BJ0STyAW19rzyy7sQbll7976D0xjdHdFzhe0%2BC7bIo%2BilSblhVj4LSIs%2Fj63DtE73Ox9cCR7IsBgU3kJS5%2F8QHvASEcChE7CHSezAHguTiWRZORMxNJujXvLIsRQQ3SqkM8xnqcUbhgOV7cdadQ8YgeCCr55vBNBKvEns%2FYEHtEP2aXfU47t5zuoGKRD7xag%2FBeJJynXKAMc%2Bh%2FE07fEbQq98S%2BxmyRg0cgGXWjDpzuzTBjqkAdpnMMcOb8xrdpJRhjIWd0UhIiDTUfe5l6bPuhtRUGToEOEl%2BsynVZiQBmBPDbSLbsPmWDnDmoW6lw7egLFKas1VceJHfAIzfZVDhaBRo7KODmYCD1XdvbxQ%2BQn98UlrHHNED7f11EbkAqBTxQDJr6ZPhgdK9yAjgY3vngXw%2By4j%2FxkwbJ8ujW6FS3i%2F6TLFYetbiKrLD8irdXgdhT677Jp%2FwHZS&X-Amz-Signature=5c6fbaeaa278da86c6491278870b6e6703152e3acc5cba82d5c9d6e8e9bfc718&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
