---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWUXCPH3%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T092940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC74U9JuxdmcGSN0zXsWblQRTEbWbWh17CFfQZ%2BR7WmuwIhAMGyVAaW2LED%2FFv5eVQIvBLSDBpz17Y8zntaymQoj0WCKv8DCGoQABoMNjM3NDIzMTgzODA1Igzt9fA6sJdUAMd%2BjiAq3ANv%2F1ko5nKvyUW0Rr5K7v4tdcbO%2BM%2BnBduWruEEhQPQXOpstsahOiAq3orGebx1%2BRfk2XwQ1Hp8p4ObOP2tuw3gXNh3mVYNyVMkxorV7p%2FoZpo7eLWz7jf03y6b7X6mlF1JoKj3wOv1lvZzPC%2F%2F7jg0hQf3veg4eqtTcO07NdqEEOMJG6KejdjRLyMsDCJn3oWwuuEIl%2FXVRz5tzlYtxfZWQQ4p9ioawGP%2FPTaPJKFCrgfcw8jTdiNsB3mG9%2B0t1uFBRH%2FmpaZJ5Qsl5oOO%2BcQbQnCFZlwrmFl1wjkJbKeyktyS405DxgykTELQvsanKhsjw4lk6ODA0oHP%2BSfnWbrtiUZc1sqP%2FFvkAaSAv9jiM6JplzzsstB2hzf8DJ8M4p%2BprITvrFBF5aUwVq8BLSDRk7Ho9CQNZDdXE9%2F0BTp%2FH9uck8N8omVIBtRCJNvMnLfAftMWCJGQmK%2B%2Flk4%2FfihW%2BH7j5gaCHHq0KkOiQsCjQYEQxHa78kL7HMv5Uea%2FPg4znlzSYfw0zm5JA1QRdqQo1R5m4kRryA%2FiEDUmpuVl%2BLybzQnKfgj73jDVVngkr4bqgGpzfAmbdNjLlaBUZjwkcCKlC7TE23xYPheWPB3irVgVI5JAeCWwdTmBKTCJibPSBjqkASZQhCAwQDsBIzyavf6akBC5RS47xkLsTYhh5pCxsxU0aiai04qj1b6gHWmIdU3Esdcohfx6zZKVgvLsH3IREF6oMY0YTz8RVYmTnG8HALLhHgD82dir3W5gQh%2BkLnLI6HU3X6It9MRPGPKZMi5E%2F%2BkM6uju7h4Sk0mIyhdQV8SBwoRHmSgPUM6Y9z%2FZWoKBR7xQpDCMqdZO%2FlEa5y5j1swdcjzh&X-Amz-Signature=0ea3ada363fd812055b3371cd3c3c185a43cc85d853d3edfa6b1d9827ff171ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
