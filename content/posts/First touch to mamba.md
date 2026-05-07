---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLFM6BEI%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T174605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFbYbB7vkCmZxVmLd%2F0yohwKsA2mzRFdL9Lyzwwyj3oAIhAKzkUp1QEGFA2T3ZmWxHBWMv1Ty4Zj1OokMS1bwYoMqhKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuiHMHtZ0KpLbzLtEq3AOjsEXEjpXTtLwF4N46n8RDAnpD%2BEvLCYHt1T4MsPIlCzk9GoMl56j2fhAohYb7zAyWOrksuqzqBkSMb3mB7ccE3%2FEeFCR4Pk5rS56JCTmyqneo6z6OxaFw%2FpoCBo3eGO25FJLXCTq8Fiq9SDUk69SB1ORqd3d3RmaoI2HW7j1kv%2Fxf%2FvZ1EZamSz%2FqTiof2ADVbDo1Mj5%2FwjPO9F9YrNXStH%2BkcSU1C3uLsW4zi9DfJhzauxZrpK8Kiob3Wia%2FVYqib5Stl1FxEpiclcCcFL5SUBlftNVFdBIdi7DVPkhmxBC3lYmCNtd476s5pAHyLjzU6GzRrOmUXdqKEdPB0dW%2BD3EfhvikaexIWL0szstqOPssbOwSDgoZJAikuddmLJbfoXCpBIrJiVKVeAQ4Hw0s4BeF4QDZ0BNkgyNMlziI1SqaJztn5TyDoUnxjz2%2BlvnI%2FljjGwwRPKOYMz9kOMgS0kQLvc2Tvhx4AhGqM3cepCintLcnTByHmU6m8VJKeNFYuu12pjMf%2Fuw7R6OBZfIFARMBdw2UdqKPx%2BOVu2gvXThQQwfAsjuKdLtXEBeU0PGFFPETAzkikJc%2BSz%2BIBqapW0Ou2K7wWNYzkT1SwYnXtuPhjZKxB0AmdsbvbTDWhfPPBjqkAcjKwlcoNhg5Im5RiOLrw15OKbX18f%2F5JdAniX5jPHWlmXEwWcjnphThaOqjDxwyVOzMtMxiTEBJ4bwbc0T%2BC7d0j9Jy8WaLVTacRkuzA7%2Fm1bfjkSUDzSX3e96XB2AmMXFVI7rvROz3gU8m6%2FWaZ3RHzcx9HMgI3ogo8LdkFy57d%2FMj2qaV%2FhBlRWBaJdJj8y85l5CNI0DD8mymCnml8%2FhWD9PG&X-Amz-Signature=e9760a61f86c306cf51313d38fa4e96e0dce7d326b82bd316754eda8e8334ef0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
