---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLLD62IQ%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T161634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFh9UAWQFZBR7TAczYkVI98rnDLUS5Y%2B3WtdchswhRrDAiB1bKST60H0J8F4LT4Uvl7KRZCdtU72Ji6HRjTmquhjkSr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIM00fIQtGFN5tyLv0rKtwD1r8QhUvfMCLOX8MaceZWdvCO4cRH%2BoIaF9%2B3pYuba8AF6u0U%2BMkBDexCbVQbucjBM7QkAKLDzGXSu2XYbPoI%2FXlNiwD8FNO1UKAmuLFD7u8W1Mcq6T1g%2BTe16CgPWUdTqQizYYu%2Fr2XMJOcnwCNncRq%2F%2Ba2zW45q6yoaQjpeKgisrb5iv%2BUqZanUm7qoWS4SYdVbJ9C1r8WVMG1waEf5k9D0Hv7LKn0pL1o%2FKKubA6oVgqrTxg%2FH2bk9%2BmuUQ8%2B2rqHLzwRkoUeA61nIY%2FB0aHLikgVssYJItZ50VYeuy2IDPoTSJ8MrsA5HdWQYrUhP3rr7udwSxYqEkIqjDtugxjIBcbEkbPB5gMpi1YIgWU6uplA%2BaOZRs4v%2BvdoVuJ5Kusifuerv0Dw1dzFG07cMPCWyFR76uJ2zCVyKEsRfYU%2FWsrYJeAXbVU%2FDDbfp3xogYVSzVV0zVMHAKSebHYgRIxom8B%2FyrNi2NJgzbZ%2FmkS%2FQy2ys7LfXfVqOo8iQjd8Gx9cJm8aqbugaxn9xzZ3JH0EyJuRBh0G1Pt3nGRvRbcsDewfBvJRv59d9o4EcCK%2FLrQ4QM%2FSTNSJxjZPVZ5%2BXmjin9nclb7OrVw0oPwCxLCt1nftIdqiPPW6ZzjEwk7S00gY6pgHnDMVxFiymZ5YF4Fq1Ic5D%2Bq9q3ENwpzMDsbpOScAQKYmAD3iM0ABV1ted6hRBWpmtqCtncrqbd3z6lMJVmgw7GK3RZ29oXtGNoboGHT73%2BWoLeQ5s8WP0NhmZ%2BvJ1TtV5tl23eHi07GMxgVaaLdu%2BNPG5T6Htz0MoVcIqx8CqCzku3xwd%2Fc0i6p2Ob%2BUzW3Ykk84z%2BpE59uRW63%2FJHONnMTggCYsq&X-Amz-Signature=d1a662b8c40591e093a0cf10e57e7e1d43e373418edae4a693bdefc738137422&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
