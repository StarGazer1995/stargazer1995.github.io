---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC7UJGKZ%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T185903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHLBLnVo%2FiihouspvtCKJDiR8T4Th0Mp5L6%2BI9fb7oDYAiEAwh9ozkcn05fX0kMpEyrycoV%2BMU0xsKTLRDemcrrZK4AqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHB3nJMpoMo7af9sDyrcA4loy4JzL06hAFQIAeXMg%2BAVRQ6aRz5Ydw%2FLWjQCMigZkO%2F2ObJ%2BkXUDH0e3gaRCBRaMWrbSTBV0LZKmQHZFxYOp0I0df%2FZQzUk%2FRAcVFA4gTG1vy%2F93MvjgDBsg%2FEdVmQJjQu5NmMiEr5zXcldVIMQozbCVbAM8mvyVxznulxw%2FDeCmhCCsTqAZMQLV0PtcVbCkdgIiIbAyo2vaVAyFPLZfvg4gstiBrqe%2FmJ%2Fn8J8dBucF5YDohYSOCTQXzjVEHvH4fjoGUYM5%2FA%2BSp%2BODjShrCbK6f8ES%2BZmMOdHqNN4Z74wJDPq4pCtda2HG6e1hXOtutOyNyjahkfIXGLfNL9HYWkGAVTRJrW0ULov%2FI8e79g23VQ1l%2BkQ%2FWvmaShX0%2FwJ3A6bxj%2FsQSEXwq6Me3FL2Wq%2Fp17EM37mYBLANCATWGxS5X15VVSCgHNnvNzAcem9XNJPCf76omHpJCL7dmwwB2m1s1lO0uggc1iqVYLlfWOIJWjjSGRyIsUZGtMXqBnP%2BjSd7rVBTNZjAEivzr8tM1bmYqqKK9jnCx%2FdvWxfE872hsSyCHxN%2FTWxXi1oF%2FjsgTjLOwLdWLoNDokj9BYZobwbMcN4GvBd5w7spM2ctGEMU9LDmmdMyNEXLMK7R7dMGOqUBOhdQ82GwJOwBAuBi73YGxmoPSrSZAA1uusXp9Ed1ITM%2FKeDMtbN9vwaCk1rdTm3OAkQeYhjRvrVTDGSSiiA2pkWHuibqcMXlFcHtVXNUpAd8iL18wjaXay9J9ReMeIBHFjbxJAF0lr3HBEIvzji1Qs2%2Bkits2TQyDqTd7l9U7XXkZ1zU3zMdMasFSEn88hVTn%2Fso7D5kV1FzMhQmQ52WTvQAIh8L&X-Amz-Signature=83ddf61a6bb8d6225a4fc9970655fb6dae49b4ad655daa4686d6ed877ad5688f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
