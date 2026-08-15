---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3C52JDM%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T003322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIDspqfTVfv9dsbkzO%2BgZjdj0QMhtPMq4lswKUwBu%2FeJGAiALQEyCWL1Iuc8bVJ9RJ6nVRX5xXnMEAue2XrXQ%2BEodQSr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMfC6ZJ07ENlJ6tGVqKtwDF8gzKDNI8kaa1TjAJSG%2FLdjy1%2FpykRp5xxeZKxRQSdcssM%2BmArSSa5t1M%2FRdpS3w1V1193HgxINFUrYeqPGXAXyQsgLzrFDlq60perDe6BlVedYJ45ZYhv9gfKQjwwMTOCGm670%2BY%2BzbPj0owCIIjmipB96QstLbJ4ojehAFwQzI6Y0ojnYTLPa%2FG9u6OfrjGG679e6Yxb4YxF7Eu0ki7QpArNBA7cG%2BXSA6h0xvPG5jc%2FaVMebM0CYrdyQGaq1lWZV7HMFaKWXWTXO5RZJjCCzxk0TweZYZSwAUSlbIOuXwrvfRsfgpL2LTIH%2F2%2FcB0fixVu1Lu1wGo3JR1ctIziwBV%2Bqx5x6v9sueHifwbIIZ0YmYTp4J7bJLqpklHfeE77jvMNlaZqa8DuMYZw5zKwwePwcB6CagQE7%2BecLc99tL67E6Nf3TlSFwP8sb6KSzpO7eiFiT%2BQkN8g7S9d0CguCbYak8e6LCRthRCFywS%2BOXQo9kqb%2BH5c2fsgfs66y7QnE3Ho%2BGt56M4z2Thy1%2BakdIeNH6%2BTvX8n9plgcChVOqXYHyw3F6uHyrua%2FrWRBDIGE3MYDxHniyHlVFKOSgwv0g7oKkD9v9chUZ%2Fihc8t%2BCrXDudZKGPErKsEt0wo8f%2B0wY6pgGUF2wzV6k5P7njde6x3OAS1HNaC1SAkIi5UHK3NEvrhTYK%2FkH7MEAU1LgdKWbKJKQnRc27u4O197oLp%2FJEQtkfGB9nKUd4UJnJWpFNU6v4vMe%2F6V1ni9weKH%2BfyeZfaJIlKEk42OsWRNsLu%2Fj2BAmCdKZmHltjxHhkOFa%2BQWRLQDO8eA3XEgNG1PcrdbnmSjk5dGHSySJcGUgtARDSmzws29lEWCZB&X-Amz-Signature=4ef1b7fefa0eb81caf281bcd5b3c7c1c435660d6b0c15ab27fbb58c7a3ae733e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
