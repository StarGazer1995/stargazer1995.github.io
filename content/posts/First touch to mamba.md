---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSVOTAT%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T020210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICqc3rUB1sxksDuo%2BfDySfrQWTWPBZszUvUZGgvwO%2B8FAiAFNkcvBMWGnDEyfGNcxYNWIPX%2FvdFlSiKpYmtW7ScPEyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMD2SX9TcBIH4nL3DSKtwDQ8q2QjzcS0hoL7hZoCT2o1UbIfwsoMbRbLSh%2FvCQxoB15VgckcfoquH74BvebelHjYKlp%2BQ8GgFxvLM9JIk%2B59VKMm0oOu9pqTF3ykyT2jv%2BRKMcLAvkSW0fCf96FB0zRunrvNiYLtIo5AkVMWka5HiEy09W0XRP%2Ft4gUpy21yAT8gpRZVd3jucFs6ltxxPb8rZGbK4GdhCMgAkz%2FcDJ5ghpObnmrPOW6IHb06kPvhYZinaPh%2BNdwPd6AsT5z1zCfWcEYOOeas5cQUYLdw5PpX%2Fu2kPNSgeUEebk7rVB5p6TvSZmBIxjZdVyilbRaaibMcv36ILytEOMj7vbSXQhQaJCea7B%2FXOs1KfjGSwmuRgn%2FXbRUpIJwZQiB5fXDV9E06pM2ZcXrHZQezYj5RCeyVZB%2BrbMdgKlPUWF8oBwLmE%2BcUL02G0T0A1AA02TdMUYibaFj9Z8EvXCuO2o4bKdyHgfTPGVJ%2BCTMVq3wjMGNesEusCK6yEdRZFIMWwB5udId0fquWC8gYSXpU2bXrv3U%2FKnvLA770gUjLy%2FpfiQ6yfBNiumpXVn7xi81Nf%2Fhw%2BpFfHqjrg%2F%2FXBus8jfyGgAp2YNTNfW1zf%2Bh826ZuUG8ppWxPeS4KLSH8bJPnAw66nB1QY6pgFAkVxoRPCx4JxrL9dGmfkcm8TwbAGQaK7E0eCxO2Kb8Ck%2BN8VEt9e3NLUhIsI%2FMx3PPaL7qwFjYgAyRmx%2BsvNimRWphuVVYUNIvyAynO1ca5Vb0Nekv%2BF%2Fk49QZpOuowu9LDB5JL7d75BJDulLE8aYsOdXpYiHY567UWHrY8d2%2BhIAGt1f5uIAGe1NLcQj4ZEmeHGMBYSn7TQMExtXty5HOT2BcGCi&X-Amz-Signature=b7ac6ecaec9e5f9ef7fc4cc7e0bad8ae719a290dba19955905b27d7fab1cc155&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
