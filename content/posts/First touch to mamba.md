---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HPDOSBX%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T060016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDidA5xZGsFWOTWyt4jLD%2FdBKqiKIx3fcLno%2BUrPhLlmwIhAPjQWZD0D4woMzJIDZGJfEagBMstz1guymzkCKKKtmhcKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6OzXoDeHjepSg5VYq3AO279hjLJSWkL5QYEanKrG9R17g3VV9KExaEQ4%2F4mUoaFvGytskf7vZfMfc7Bp3BlmrvqrBIyOc4wcxlBcSGwPHjdxUKP7GHWFQ4s98%2BQCfrEWJdqbo8bMWqrFJ1Yt1OURErkySqHQ5bOpahsdv5FyO8%2BgKdZ%2BY23TQJ29qHbg6J72Fpn%2Bz2IpEh9WuU1BSjUiqIuM2B3%2B3fiD6rlVKNRuaiMS2FimUYZiFHfu01MutOB%2FkEX20mAwFrkCrN%2Bd9D5aDJ7zPXyX1MZGXfpPDk%2Bse9o1fLrDO68fLCQNuLCn5FsMDMOzgJD4zTef33i1QvKJn7zbin5DAjJTnSY3c7pAxt%2Bm9omR4tFANBcOxuvE%2F%2BJlm6XisSlgBgCasogxC%2B%2Fv8buX3Ry39qgceUJVQro00WTmVJbliQFLjNcmOzid93b2hSpFxY%2FP4zmK%2FrlVmNSRUlLAIIpG9g%2FIgppRsjc5NvE77I9WVvs%2FLkmojbR1JNTMnyJvuRYohDbzXZNXSW5%2FRhSuk%2Bfd%2B%2Ff1oe1yQy6JyYP5Ky%2BsW5gEJ3EtzsW54bRZB4HkLkH7kU7a3iAAx6m0e94Jo8heLzl3Z%2BEX8jy092Tto86%2FblfBxsMPKsGDWpZpsKMM%2FW3hrdqo8FTC4t57RBjqkAWe1gT3V58uLjynAykU1R87nNy1aCDz8TGeluhPeYcLFRtwgE4zZDNsz9a2RPz5O23iOBD65E5XgjdmANGnPBj4zVxs%2BMSw6BQ57%2BWrYB%2FPtU2eyD0OCLsPRhM08jN%2BrKSbZVhCSO4mKsC6OAeqlfuAfZaE6L4lqR0f8h7JSmCE1ayYhrCdjhIRLsgMRwmKCRdnRS6j%2FrZuZQUaB%2FoSzZJTk72xp&X-Amz-Signature=cf7dcbda91d8b8582ad9f5df84523e4cba5173426bcf68a43da004109ecd4c5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
