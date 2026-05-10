---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QCL27HE%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T184426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCICx67E98ChDTq12tCFfw4jd1rsQSqgUwirXaccPx4dlkAiBUUWxBg6COpRCTSiqyPcKYUH6le99%2BA6E08WobIF4iqyr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIM%2FYVuyCsd1S6ylqhaKtwDbOpUusuW7YL%2FSc5mi5ev96c49dS%2FSwNQo4snc8EBbxFgKCGVPe8GKInl6BbrDmgoaPshlKFPV2uC5GHgzySbB6Hh9%2Bww8MJvzPT7%2FgLGsfN3GtUxbifCLcxE2BOks94Ln3pAYMTY5vY6LhQcldBFD6yPPeT2Y4ikf%2BeLPx2%2BlemnZ96BW6hfiXFnxKJ%2FsUmqOuOs8Chf2JdMwFJXsrFkSxUlFJwgXXrDaEClQjs09z%2FHAzvovyjqK5Lg%2BrDom%2FD%2B4J6%2B6uMf5BepTN8EUf2jD5M6pE9Rm1Ip8ZTXvoE8inEmw1Ppz8WM9sLGKyaj6oSEFTgbByIXA1OzJb0vvtfKai2Q59PjBvSskwh67YttyH2k3EBRtuJx5U9TrzARzxTNQdNw%2BehxMbABvCvDUk8XAhn3%2FiutyAg867nir%2FN2Qa4KbNo0lwqVZvsxjhlXyO26j5gtDNrcHIS5799ZugMRg2XcfIZxERxyP7u28gs0qm9vZ9QAxw2fpsTDJYu6LDPIEzrXa4bCJNrzqLMRTjcBHadSHy41ZskwuYNb4Mj0JDfsi7cScgi6Oq8i9zJXfByMq561Y7DkSTLcRv1bP4nUnQgCvmLODdIuzCFYfgoCUf6hU38f%2BKJ%2FTb5rZCYwo5OD0AY6pgH89Axyo9I2VKkCEpMRX54EAYdDskrJG5Ac4EsrvP0xM68HOxsFMG%2FKs02xlS8E%2BjkRjnvLJZW5Nf3IrbpAY7KiEEp%2FHJjGN2nSAMmbuTQQwpNzs0TJqdOKiv7zyYP%2BTuekn96hxGQQ1ozCy8ORNfvHsPB2h0tJExgy3mQ3bDU7c49OKUW2rpwZsjyHISnzikT6hzHvm6D84a3IvyagOBKclTkUZOYn&X-Amz-Signature=b993e66cc5df7abe82090c3c2741e13534b9cdf86eb5d9446a5eecc66b7785e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
