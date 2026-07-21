---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNPDM235%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKOWZBdFcWJxPfnTx7nQ85NPc8tVy2%2FHI5nRQTDc2QjAIhAJMEGk9hyEv3FKzatYF2zt14buvR%2BjvzUr5%2F%2Bh6pFuUFKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxADkLf8R0ygJzWm9Iq3ANUZlWGMRN%2FrOpZdZq85nKAyJdBYGgar%2BgHDp4Wj0my274UDS1FJAcw7y53V1NZHMKh03U9aBDarFNFJ6sI92VCajUpBWpahmTtHVsxnvtUm9MVmthRVXV28%2F2VVWegBB4Hx6wuCisjl91NhPyyGbHtRYPjbCitOY57qx41mZJOBox%2FtJXv2zbBmv7%2BUFx%2FeD%2F1KhfKcCszfb9kxTHkymhMmLA%2BWRKn3ivX%2FuLQyUyvbUei9bHTEVczY%2BuwMoWCd%2BWP1PZlhCMW3mFoEaWrfGFW54R3l7QHEZN%2BE8IpbESL9Sdp5PTKU9Jr8nJXKUSEhk7kGlT8Lv6to1PGc68J3Q8MpqxT2p2x8HvU50VxY8YF%2FPqMYIMvJ8ZLZ9UtBSqZcSLtl47%2BXz%2FTfkqZuY76p%2BEeyNye%2FTMiqtChpnRlahj5h65TewuvcLPucOmepIG1iwH4PwA0rc81LWmiLr%2F0vSJg7R5TtLih4IO6RpZHMvDHaAThuix%2FIffZzokg0SW30dMFOfQx%2BeRkTc0TGehh49rIEkqveNipFRwDTzkZbqeQ39rO5aO5TcoZWcu7biNBe8M0XAMOuB8X4aidfzs4DUUE9dUxQ58miWYU4X3nzwHgZy3ag6g14m1ths%2FkPTD%2F%2BP3SBjqkAY8qzvTiknQmrt7OutTAeIqErZja9Q%2Fpjrvq5B186KLveQXR9kVajhvnWmW3y3ng5km5ds5KUY1IKD1fZ03GaT6dB7r3xwL5Dv9rbD%2Fh5W4Klu4X2f4k8kmdnccT5d%2Bkey6pBVRwxLiiL3Gepy3LoNk%2BjODc9IB9h%2Bbgl6q4Zr1GJaARDtQCTxyLGMYcpmlcmvCuQ4xzu5hZE0AuG2iUqt5oDLlq&X-Amz-Signature=c4479bc4d13f0c8951b61fe3924ab55f49614c2a6cc58504b1984496361d6ad6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
