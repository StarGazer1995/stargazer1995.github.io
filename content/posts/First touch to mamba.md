---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N3HXIXA%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T021743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQCnjpjl2%2BHt7Vi58I8XyxYslJUlFUv%2FBtjc5cT%2BiqjJcgIgGZ3uk6QbXHpfLZ9fVO%2BCRUKiWYK25%2F1uDylrxwGfz%2FsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXAvMXkJTY2o7w3NircAwDwovFbP6Q104BSPv9P4CcOqLo9F8ypSMkVfCPDXzcC7sT82XUrTWgXbhgo7%2BNawgBgi%2F%2Fykeqa0ZhIAwxoDaisIbzaJpBB3zLNu5XAOYpBZYpH4F03qTL4dHu6M%2F2Mt68VA2ZZ%2Bgyc5qYqsS%2B%2Bs11owJENr%2BIiHj0LXz6v8AvGxGS%2F5lkXnTme%2FdLceNkul%2FK0oh3O6ciXhTTn5VHoVjqzjpeXldPPeO2nzyeuCo88UOjQucGm5mWOLY8XPNSrtv349S3Zy0xkKYUV9LMjj2qnt0gXoNp%2BQYTlRVxs7uuh8KfBQZnkb2KOfl4bJ69yTwVp737TwjFH8sW2nbdJubk1p3QEjDuMnHUqWztN%2FWps403twuAc5OM%2FL9ieD4SB%2BER%2Fnm8LolRyOCYaqVYMlI%2FpEqKCBFFo%2BgAyYOEMWS1VzLXlaALDIqsqrMgtT%2B1NhokFB%2Fpf4CoeWiBH75a93T2VvMMX20vPMP664ZuGL1CHWK968I6709SoLvBp9nEyqodfdSdYJfizQD5ZK30wiuznpkMFlGwlKfegF5TbHKNsNPVRsm2s6X3NNie2g1IAOAMU3ct%2FASxHPLuBQNnu2Xf58fxLuZXa5tNUXSnXY1d0zLz85OLzHXPq160QMKuoqNEGOqUBDu9Ke%2FUoKgvYmSO46rK8HwdQZXvAF3Y2ICzzTqKx%2BDqhvmL4BqnExJBL8Pr23VAiXeI3lDy3R76fa6EqNXjfVg7Fj9d3luqQ6%2BZHQV4Zm1BjZTYpTy5RFGRqppilEHuKaqtupbpskGLm%2Fd9i5cuvOcG8J67ZiSC4q1siG6r1KV5s9Ak7fRfy7PBP2n%2B6%2FfymbbmGkHIlvtm9Z3Y8OrVA7rIWIPcA&X-Amz-Signature=e2ca58101343324c9197316f83cfd046f7f5b529b840112d124eec0d5d5fb500&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
