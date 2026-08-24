---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSYRZSM6%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T143128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIC4BhGhMb%2FRO%2F0mhnwFay5Mi9tVRRefsXssUZ89KTySQAiAp40cJUCJgQgFGxcVKsS2hQ1znACZkTim21k%2Bo9fhfrCqIBAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBPfoi817xvMH70qTKtwDqBjIur6rjGuzLk9mBoLFXO6t6tZYn%2BH1Y%2BHU6zv7Vk7Nf4%2BT%2BUuwbPEiptRMH84Bftdn3bsFAh5LDhS3PTs%2BO4K5oMKgqaVtyAT%2B5cKZOPbXcEl4grs9ZQs9S6QFCjXKRWQeiA00mXGRoX5jR1aB8ESD0NGUNFxVQyJqyVjhqPlQiTgmTyegZ0XpRlyBQftb1HqpJG7HHn6KxA3nHz8LkfnlgekCpcPyXRTjvSWo63fUvTuePOlJHFvzSeC%2BC2oCvw%2FQH1kcWU3Xu8w8a%2Bn0IVhRFYHmKmWijDHKndbkP%2BQ4E0a1FZN%2Fq2d%2FvLT8Z5UyMJkrewyp0U%2BlTUtInJ3kmmbjKXDUU85%2FYbDf7YXbkM8zxX5mqRwV3qQoSvwDCLbqUBHBzMGW3MVFxSRtpJMq7Sj7PD%2BiyDOC8k5KVB33T90Gkvw9Athyztxbo6%2BPyIuL7Ya9WydGPgRv%2BugXiE8D7zyIKARFMmdBWBQejxbVUgSOGCKXC68K1AFlycFmM2YCu3AaAJx5L3UXL%2Fk2n9LWZOkJWfWInTG%2FUC7Eu4IZjCCkgpKuYdlIod8fIOILqiCVCu7PGFAJ9%2Fb8jla5mpwFEUooGrjZorz2f8lH1KQi9KDToWhfjM3xGo7izTUwoKax1AY6pgH4NfuxHxXTIn3kHw1cjG3jhsUDhCusCUz7WoxTfsFDCblIeSESZRiFOmwPsn6NEZuNgDmRmw7Zuom%2FPbUpeISprlKCblGOjajFSG7ELPXbr1SouuTnuTJ66r1edPuHc7C9%2BGCqIVEaTS4x0eB0nEd2deBnJg7GPKY6oKmuQ1TEHUmxVBSt1z5lM16KXGhM6WvXX%2FB%2F32R1QaF8e%2FjuoE1JPzeOrA9p&X-Amz-Signature=77e1158ae282e7fe3d94e8abf8e37a1a66b61b8efd1e3efdd441599d4f60ce7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
