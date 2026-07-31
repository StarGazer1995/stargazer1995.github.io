---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DYRQHJI%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T012929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB9COLbueAC8OOFmbF2NkmoNcAnihXs4P6cjxhgA7BNJAiB2haCwt%2FY2eiWmpVcZWoxVTE%2BxHo7ESJywYNnihS4cfiqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYpcTQlwV69DDF0IZKtwDapZkZQGdEaPv5wJqvV6r0akzEcY4bABbYc4zxBz9UyrtD4D4qhFrOM7JGnp4jM5vAHSOZBaXU%2B0H8d46Q1%2BA6duE0ijb9LkaHvy8lU51Ww32brdxp9arUucgaZkRhrubRYRyM6ebLYREWj6j7BWTIyNkGtxMhajqIlL05U8qSyHqlbBOpFXamqZJubwkTbdmiYUkC2pyoWhjiOE2NVY3QS%2BD8uhs8G2r8dZndz1GPYTvFLBbGrpUSiCuwOSo6b7%2FjU%2BCR%2BHmOzhTRPzuncgake62wF%2BLsTj556VAj4G1g5y0z9nzBTZthOEfcVfxCHMMcqxOUQQi2g0Y4WPRSwRfksLeJRKdZAeuFUex7qrFejuxeGMZFt6%2BKUJjXMwfshAj%2Bjybo3fil%2BP%2BCvwrCBrd72YnZGuJN12vvESB3YbkKbi3ezF703Y82VXODjWHr2kIfCgud92CR97RlDoMjFA8%2Bo2kBi2eEK%2BrrO4W%2B7MVSnweUQZNOwL9bkHxjMmM9fNeSebYoK5M3gWVk%2B7%2BOnqqpH64XxCpkrEApGVD2lXvRH7kt5%2BDW7ZwEz9x1rAQwVlXScwyJF%2Bm65d9G8%2BEyDSJrRh%2BwacZlXhnrofn1%2BilkBAtmXu0dWguwmzWBzow4PGv0wY6pgFcAGAw10pRlytLDnVItJEJ82Qf1m%2BLv3MdMMabNb%2BAh8NSjB%2FAsKSlUPpwkxLLa726H1jehMmZ8m5GOOSqHzxoVav7%2F93coc7B85935BtWBJ4NKx%2B0Y%2BeE2tAOGTLIxdCMKeTCM%2FWl5Hd3fALZNskRWMrnGGOgOinv7hCfWzA8P8TLcSJMEtq5BLiuOsdTO%2BgC44y7OYCguSiqqEcEfBhyMiY0gOEt&X-Amz-Signature=8d7f5c81713294d4b2527e667e79a56481b32f7e24034f997c593c8972f853c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
