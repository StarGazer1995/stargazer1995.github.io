---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZIXWOIK%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T074700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBx7mBWRykd6CBtAYYOclD%2FGDF3LtjB8dRTiQvYg0B%2FwIgbuPN5esJ1ERZWiC%2FDR8fhNGbdIRLifVj4%2BjSark3kucqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFG04kL%2B4%2FMZ4Qh%2BSyrcA%2Be7q%2FBe1EK71JycJkvhclpCYH12mG3Tupn69dKj%2BaoeFrWGovWTr%2FYF%2BAjw38dg21LKyF2GjuErg%2BKevdRmf7SX5xdH8vx1tmUxLqeXps9CWF8dTgfZ7FMCsG%2BRQq3GBSQcL7ErSS31JQXrTWlKue4lbE6oFHSlPxcxeb44ZD9f9d%2Fp9BWMrzDwGDaoUD9YDK1%2FSojqk%2FA7vE7VkDEUvKbn4M3BjqL5Zu%2BCka%2BmEysshXyWwLnJjUv7rYk%2BfyH9uam49X5kHmz0IQ1MM0iCnKJZQ0bkUSfLZJnUFoQGAAWNLxKJyms3qKwHtf%2FWe6soGWRmsgduMi1Hwwtlfs2NZqsglLXXaHhVTqZxO%2BnNiqIQUKE8wbxY6PymL1S0ORO4Q1m5EvE0PAorVAXeM2Kdzg%2BHQFdSmXhrdpXihCsolSOk0GXwWwqhx85NYA8%2Fgr15gieAKcRMrCWDZGW1mBUFwALVGwTHJUtMZg1UvWQJ9dCaYUAg0EBwCslCA54tZOlZ3X%2B%2FtoziqBL4QovDGw5cyX%2BIBpBvPzu4o8rC%2F2Kcp98UIK1WNamP44MCwSEYcSlm3FtUryAlZqwQffR2hr5Oj0T4EceO0d%2FmTX8g3olauT0%2F3lb3Z0oJ19Ln6FofML6wlNEGOqUB6fTPiz%2BFReShKKeyJyG1x31dfx6yxsoa0L2%2BRftnyit8t9kpo%2FrENzBkiZ%2FuMHqx0ToZvvMxYANSrNXKfSpuiv2McNojFG5%2FSc2wmbm9zyGeVYkSUt1NoIJwKsvlHwji2TVxp7JuVyRLjTfset96ySUcUcDwNPgxDmULH3dEX9%2ByNglGFufwuoUiGA3syDiUMXtBxBV94h25KWOPo0eK9PBtPWtt&X-Amz-Signature=44c5da5ee59d9a368a18ac67798fa4f631f509e6a679a8d76acc637431ee31ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
