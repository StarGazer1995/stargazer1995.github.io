---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662PW7WLU%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T205737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDW2YTZNoagN1W%2BdnZdWqRpNmO4oYIscUEs9DSnnmm2BwIhANZUYTqTfEh5pA1hz5rj49m5OBRmFBnkZsu6aLEV%2B4YgKv8DCG0QABoMNjM3NDIzMTgzODA1IgxPQL5ecdMrS4XLTfkq3AOw6uZOLaBwivR%2BAXM%2FLzQ85XmyT0njBcwSV2pPSNOOqBxSUElPkC9LIOw2RQrvRV1qfjGww%2BuxK5%2B83Jh%2B2YAwJWtLdfkxdX48fIKy6YiBGBckKzh6HpQSqc29pTB1U1hVpedE0bYjwT95vOyqwwSIfUPGRh00gNsQTC0%2BpS%2BdTs5MgNu7hfgIYYGJGFnJO0IvWE8ZkG1bHAUbZ9aMlIJQRgVdo4tdQgM9CTiR7DBL87CsLy4vtMUOFmjmdCmylG%2FB8m73gcSWYCxBi%2BrqwNa7OO824%2BVczPut4uBsHdizF1Xz%2Fr1xW43olC1NAoGoy3K2clx0kDKoKnt1RUdXL77XZfHWyJ3XSfqyZD%2BaLMWOj%2FIHsLpB4X%2B%2FCJPLfBE84NippUsZsMhU708toQNX9S7P7hTS8w3T%2FWf4ub%2F8CqWk1qLzqNTV5iyfK2zcbQr1qiSLlvJojAX3evqRAoTDWM2oOHOLbwJZIQCOfjQeDxUtPafGsnzcEM2kb1zynsfMpL0YpmwMkkVFRuEf95uCE6pSoiZ%2FHbJl0wcPbAB7MM6yX0%2FeEgDqntBPqjtOIXT9LAldcmAbdXY1nN3o8TSYW6LTYnnVRkZeR%2B%2FWQWRiX4HqXXMzco6VFEypTlRVfjCOm6TTBjqkAZxZL63gMuN0YkxOP%2BdeEt%2BoS02TstKYkff6ehFlAfgQ5S5FbpritqWYNxNTLBBVzqug17qUgXfe8CYCKBCfgUsnzFoSdJS%2B6nII%2FWQSB5AYuDLfMRMxeXPmsti0Scs%2F1A40Hh4JLvHhUhZO98Cvphl4SCMpeDXvNJC5WZuanTq1X04AxvOYLazTFPVdlPJ6RHyf9XiDchxL3rrncQcgcynyN%2FHb&X-Amz-Signature=99126f5f45c83c7eddd319c0895707cd8af05488f4100e5bb13ac0f26df9bc94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
