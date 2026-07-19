---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RDXU5AR%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T164304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0UDddzunuW4RL2QCwwua%2BZG7wuYAnlvtZm78oFvxvMwIhAJF1iV%2F18g0JVJh2IpGOf1p%2BRDBv5hUprnbY2H3EGKAlKogECI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzzzXrhyfOnl5d8urQq3AOXNPq%2BcRyiCLUNN5udId%2FWiZ2K%2F5UIJ6r0mvJ7q2mQfMiY6Ge8%2BQZnGnw0xGVfOdFuiWXBW85uUbA33l14RKLsoUFdpd19Dw7%2BCgzDB3aNHqERsBSDdp9xX%2BMx5DFuPPsQVh7Vwmvt2LJIFUKZKZCHR6ZXjlGqYckTSZkwA2ru5q8DoYnNQlNkZSmq3EYylWvIEUR%2B0fsTeFdkXU8fKmq2sZe7PThdtYgrlLQ1V7Q0uPneu9DyZcl0re2VGBdvV003ujT%2Bcaqr3ePD%2BRMeBw%2BWvaRmOdSoVJfTAdiM9I34NdLj3VF9u%2B54hpKkP%2BZocBH1z9n3HyyyUitR%2BQH20Mm9YvWcY99sJoUnzJ1oL%2B4cjlNwwZz56jITSeTx1JuYujdinZ8JagDbauQZGyCarib0PtM3BxAW3wumflr4zauKaz1OiuUDPR0H1i8ycf8l3g7E%2FVGmMsiwf3lyeEzjT66uOVoqZUniCLmywezuLYx9JYSbonhGyN3ri3WeqwKJtD71SOTGCDv9jrx9swllqBA6fTTEm44j1Nxy1ahJLrOTWrmmMFVM3wt1xrtCKqyDKJCDHnBmtBnnUxr%2Bbbt1LZSuaoHTTyGLRIFJvEWuc7Py1kg4UWjtar6mLP2eyjDuofPSBjqkARPNAYN%2FyDzPtyMBJLT3u%2FDvddmjPAHKKhBTyOMteKq1smu2AjNYX5%2B6PMn79yezoT59iuBW9CTM57Z9jDsMUxN93dDY8cs6cD2JkayBxwdnky8yBy0R2Lr88DZ7R6owWLvunK26qaZbG0ccQmC5%2Feha5LU3qu0w1NxmF3cWHZIT7n4IJbb6PG%2BbZT9CUq1J0NdY%2FHCsUWlyXj%2FJflWz42MxI2ZH&X-Amz-Signature=5232753487226244428a5acb206b6d05d1fc34f6064b5e62ca5d75092cfd8fd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
