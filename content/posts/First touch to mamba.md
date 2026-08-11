---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TETM5L7Y%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T084257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCK3D5%2B0LMbA1IqS4QXm9PNZ0gjm6kpAva5mqsSwwqUGQIhALUF9sPHJMds7ntoXU%2BK4YxIFUWHnJxLe86hhVD5aFoZKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTbBFTSxS2x1fVPQsq3ANu1YqXgY6BlRkNRkEI616kV0aQsWaOK8BYPjo8op7iNiCUMQ5s0XIbuauVA8aLBli54EUxBDKzQDmIBdh6KmOYEl%2B7Q2TLBKcaBeq7VRYlGYK1RDkbOCMPHQapbQmxVrun%2FVj99%2FiVkGlF%2FzVXnl%2B94a0YXeEIsdE3ixAyTXWFInJvqTz16njxxeFxEgKNq8P3HvIerhVNQVMXEGP2YzwALupzwyt8VsQA%2FVNkf41kIB7pjjVouPDrwP3KA9pOatqufG5RpcEGeYTEPANKVdv2sB08W43YYR39KC%2FBvqvGnv3RvwyNovwu1UC8aKXQcqINLQftH74VYuqxg5amhDd1%2FainTWrAUq79KFCQB9tf%2FyNHvQlmFWwWR0Pr394v7hzFwnzpvb1A1b06RByJWHqPzBG7igCAG%2FR%2BwtxEgtsRTLFK6%2F%2BPBS2l%2B%2Bsk8Nq%2Fyn1n6KBXWsGi3lv2OjQzuK28l7Ez5EWIpbl82O7dvcOk3vpiB5p7SqTRrTb8%2F9lQL4PNIT6pN449myF78sJxrja0uHh0iK7pG%2BKuZsByxnCoQIkbU3uj2JeFb4n84i%2FApk64DZ%2Fgb5wsXvkhoI6MCd7xGp6rXCR7FZn96ZRbLx5OvLWBA1grWVext3YBhzDgkuvTBjqkAaQJy6feHBdgEePFHm7LBcYpcKxY2C2Tc0PhnxocjMtpIJUu0TSEp3ANgRY49iziVimanWSHiqlcIPA%2BevRebCKQUIX1q%2B5jNr8et7jygshSmsxVjsTJ4%2FOpWuXqAN3Pai6C1GBvLCMt%2FLz9ROOcSJDkwCxiVOYpPrBtYziRr5KLUin6VpF8BEaN3LuRCQJb0eFFpZbJVz6X%2FQJUVMyqDXx8Z2Py&X-Amz-Signature=3ec338f81bf6f6c601489c377e2d56bb3823242d08a9cdabbd7790d308ec7deb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
