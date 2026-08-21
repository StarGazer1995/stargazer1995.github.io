---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU6CW26R%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T003517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNIYcT1ApVQnCevYejin58zwgbu8iKS%2FKu11qw6Y0vOwIhAOyVM75uADb8n0l3jTW0R9rNVEY7nOsJOEEyihYLtHsRKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzI2Pb7gAPU5ChKAKkq3AMKkGQHyVKfLUf2tuHLy193QVr2iZecnfsrAGfar0GkIZj34zzT9ckQmiSjaChaXbAZEw%2BUsEFzlwUuH9pAZRu5oQZlDyWY7db8j2eWLY4LZqSZqhrXnA9wT7eLqKvs0T5W%2FeMOKM%2BV1J1rjItP96rFSV3qa6UFrabFrI9qiBJKMtSIrMmMo7WhgnwSag%2BLX1lWYLXCO4cbebRZNP3gjsfAdnjmWpk4JbduzxMYozA2ilSqOcfhHuS0hwIp8tMLqBgt3Y902KryIhIdDSAQd4yggrxs%2BRxjVlodVbvaEfsZS3FvbZ5uKvObxizf6hh5S4Zp%2BgKtTvDIfHJj7JBJs1yQPOsa5TETaJSCzRH9ESCTIE4ai2oYbsHCGGic%2B0NrRB6teKrDtyIKLjZOrypBGPjTXI5VdUmQfxubAp5CupWiKdcTw91Dq3mZOFAIk%2B5dE4FIMGTCWo7EvwgT4Wel0QNR7B%2FOXLd%2BJx81AttuJbZb7pcYtVt%2FI2yDi1k48S%2FiKw5E%2BryaBt%2BvPONY3zWozT5yQ0UX3EHu1YqUyhvQDKPD1jIsDlgmoex8ictStOHWvv5Dhrs1R%2FjPSoX1JThpff%2ByZ3TEbCBGgDH%2B%2FLHYlOZ5G1Ts1AEJf233ymYybDDTrJ7UBjqkAVbFAOen2Ga5NmIvG3RWzndXl%2Bz9jpaMjzJcs%2FCq%2FvmAZQ1NFGrU7ERUm6IqaL5ElIhktq9s79svJBfLB%2F0hp6qoCtg7MImyM0YGrq6HdAIs7JrmlSHVXj5pvLRSK6205qlPHSrJRIEOyA3AkG7mmyrZsdcjvXF8TLTvIf%2B5TJJ6KI23oAxjMZYt4Us7zoNXW7x9vQk6l8c8jdAFcnLERq0ROg6f&X-Amz-Signature=09b64be7fd6bc0814a2fdb366ca7317d58b4a9411db5b3c9ab1bff0663b502c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
