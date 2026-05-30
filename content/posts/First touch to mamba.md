---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQA3GJO%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T224621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCbKgiPFe6ujamVT1XBlctLItIRsyUwXO5BtkJ2hgpgcgIgeW6PE1fcMhe3ej9IAvaCdLUSovfJnpJzYhOlvkCANMwqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLiWQII6TYfZdtEPuyrcA17iKbnl%2FjUsyp%2FBDCQIpkrjZhGnBuE0Ocszqh3rpiZz9HtUeazkMsxT0hrdxp2QPcMxXKGaqsSQPzKAwkSEWFFsoR4nGU2IoNIRNLuhVUVvwBpAHXN4IQAnnErIsdY1fVVeQm%2Fipddj1TFv8yqoIJ5HqM8n3RbXC%2B%2FYJTJohV6NzRp9FVXDWHXYNgpsC4J5ZH1m1CnPo%2FgHbYWZiMJ96NNL3EH2ROnXKiqE5161nX0aFjFxTnYKfCqgVdR8B7Cz2v68dM%2F4bKLg7QkWiQ%2F9nuhaWGaKsea7a45qUDv0gqnXApwdBgIzxV5iULR0xA1zg5Ziu84fAAR8P%2FaKqCQFgAVGe%2FSovN0%2FqhE%2BBECnBhFUXBjyT2VgtdorNImdhlswxQ%2F7V0T%2BPYV18kLO2JauaLuWlck5xzeR5IfIxy0OlteAqqnQ%2B2ED7LwUgPkkN8iSJXRloYh%2BkNmHM03U2VHhpkiyb90J6fgbLGvDSXkhR%2F2RDLTtWrNaJJc2ngNRH4LEcKi6OYopam1V9KVpza5DjFSthCk9zeLmJjvDyTLK6xKh1wuJ%2BuK9%2BmUJhKkpHeMrWQGLB7%2Byxis2i5MIajhzjm9rs9noQwswJMvHhITNfcrqtCIv7QpaiYFsWrxuMM7f7NAGOqUBFu7qFhEyIvk12Fgb%2FF9Vg3Z909wlG6MKb7vcyNFlzi2VoxCj%2FjKs4Z2kWW0nwFYMt77xDzipoF14iK%2FdGbcVbTlE4BS2nGD6iQq8%2BomaiCyN8K9%2F0yLPH1u56%2FrdCSs9HmMGx7XZVDzST1e6p2JLQGnw6R74gWgL%2Fj%2B30n96tJp0MfJyZ8gBCDBinJGQUuHS8JH9xsKnDI6seJxAwx3ihjrQ726S&X-Amz-Signature=f09abe7bf2ce7b99037731d36363ee056aedf16ea56b36d44fa935e5000b6bd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
