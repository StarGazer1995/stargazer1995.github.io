---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EMJLHFU%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T221311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIFttbIuZ5RRDjJRFGrAe2UwfSIGuZ2zaeJ9ic07HcwK3AiBYOAit%2B1S1Rg2diBH1iu%2Bl%2B6RNPZBpZYzJ4S94PIrRmSr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMg%2F%2FEf67q6bGxJjsLKtwDm8skcdFHhBYY3cHIgGoKikaM9HqVoCFKrlHppAskcI9Tru9Z0YmnrJ61mt1S0LRHexpB5LxyYxwDl0bYK0iJc9eaeb%2BZ%2BmdfBVoDrAydBcVDNKO9GKV%2F4Ls1L%2B9IQKVq4Iqch3VgJIu%2F%2FGQJJVO%2F9InIjGJZAMItsoTyg9WIabKakiObnj927rJRzC%2FD6tx3%2FRcwGPogUDvVZ%2BuUHX0PPjH9ZXMZjDD2EjXLw8VmJ7cIZm4nvYLA%2FlasBBMaNmbETj5K2GCkr8winL3UZcYGtWqjACKR3NWKOfWORTwazjiE3urTsLKHSdYNGrbn%2F%2F%2F%2BaIFt%2BOEKMeQoMTbo0iXj4SD2y3ttN42k%2BI7tLDHUDMrCGb7VgW63UjuILLzOaQT3ULyfHeWXVVTSLCOuMSFwmEMjD%2BfqGIMV6cXRfPv9yBYuGwrGeqP4q7lYrRsi6js1k3j7vQxEMGwU5hIaMV1R%2FA99gkFkU0u364ECY8jwMRIeSXEWVTKNDSmcwOKzGF7WqseLdvdIlag89eysxgINNegCkLYsU%2F7l4EzAucQDj7Fio0%2FIC4Ub0zXkoLtrP0CSH4vXD%2BMdHnVy1%2B%2FlttByHUyQgYhbwCakkv1Xvn3tJonmYY3RDm3DUSXIEOAw7e790wY6pgHCb7zM1K9EV5DUJt8tcldpN0XI%2FHVBb8TXndRK4xtjghM0V9l1hqjO36k5dCn0HMvRnbhLvPByOnRMVOp8cp5hbDZt91Rcdrj1zACW5rCzqaTiI43T2BFCqHekxghhHgY3QGsiAfeC%2FmQpuIykbxDIB%2FZO%2FVEM%2FYP0Af3MTC8JMJZmVgwh6dJRYrHFcpNYzw%2BVf0ZxB7c%2FnKDLtNmMsUn1ljMZVwZR&X-Amz-Signature=e3ffaf0b93cc6ce6e006df602c85242a65132d69ba17f270ab3249cbea5f697a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
