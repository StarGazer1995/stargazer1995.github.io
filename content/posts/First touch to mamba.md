---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E6STEFK%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T125628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIBzI4xqokCrgzN5Us7Mbslapjfqqt%2FhVlyhYqTDVMHnWAiEAgEZPM5k2XgNfTQBGbU6n6Gx7m%2Fn9HPiQcwol1LwJygUq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPuitbqPqRehjgROsyrcAwTwDaCTT3CqzjVdiefpWLKg%2FtsKtpGWv0EOVBp12oziyZQS8VCNDHAojoJ3%2FMx0psP%2Bd08tuqjtsfewVQCAuCvxKIYNgfURw%2B3njXO78sBE%2FByBBXvae%2Fs7eNlpc42x%2BiHnKqV5xqihGtmMvj0mOJ1PiR%2FjeqUVFZvOtxOr8f7QeLavO8JSHK3qjry3DUEm7CcgzLJ7AalmebsjpnM%2BwBU61ZymEm%2B5l3SVqp6x8o8E5YQDqeRPaW3P4pJVa0q4UuzR682tqMQJg7GHR9l%2BK3CR%2Fdw8b7V4C7OO1VV50rJ2c2HmrYpIwFmBCjzdQ%2FvsLnuhFx0PwhHSchv%2FJ4XhAdB3dvF%2B3cqK1fQ7Nk8aMzVOHFFDQW6LFkPKucN%2FyPhZj4G6giWqgPGnncbQqts6%2BD7By2taKIazWL8101TRuce6pFfUe0xlPFd56C7xvmUJZPW6AZpgVp%2FIbOt6wmEZuH5ZQWIHcyxAdUXeQ8WooEUp4UFoqEsRpURyqMdaRwN4rYPaYiQipALvYe73QWk%2BhLjeG0Cu52zXs8%2BsNePhLTkJOL4fCkCVGhcrKEVOuC86%2B4OL4cLWKr4ykbui%2FEtMZyiotW%2FvMQ2BsNG3DLQ0YY3eCVUPAMvL5sO0GAQWMImSxtAGOqUBYBTsu0PwwP%2BvkmGxqh8x1DNv360Runo1M5FmkxgT4u7NdT7tg6uwvyMWwVkh5STD28EFKA%2BGv%2F%2FKirB3AsK5X52HSFZh3oCEe5go%2BqrN20tpuInOeSQyyZRQIQYtq1YoqBrO2En8gFWCpm75xku0Em7pKMPt213leCHJs3DI8R4CVNF%2Fa0yx0m%2FMqavKLAnu%2FwhcJrFBhTEOV7vfvtyLCifvSDhM&X-Amz-Signature=85f8fed722dc4b59dcd3672a23debfecc808e4451c15854481828fdb39d93133&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
