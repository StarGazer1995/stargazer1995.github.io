---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDAXJOYL%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T171735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIGNSqiVZjMdRhxSZXEkMDKqNYjhmGTMEXr%2BuSgt3U0MIAiAST2%2BFUP5y7GsDgWvvho1KSfi4omoF7bAJI4i1faFX4ir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMz4i%2Bda1v3gk04x65KtwD1%2BPxToIrusnvvlfXn3qffrIl9cKMfGH2DQAeOFZIjg2j2eldCexcOQ%2BwzZwDejY2wW5u8Pc%2FY8P%2B3dnad%2Fnd2mpET7%2Fpg1qYrj%2BAckAlSYgNx%2FIe0PE6s8sLLL5b704HxN86dH7CsrEu3MIyIQOlvTiy82Sx3gZEBK3n3tQJgWjyRocjR%2F1lOyLwLRtE5obuP5FsFl0OdZ67%2FWosqvQW8VrMG1tngzs4d%2B492NO7mfGvyisTQ3KOVuop3P9K8uxOmoGiurR5Cz4ued80VlU6l2YH9LqBjC3j8tBquETVrYu5SuVlcKz3x9kb8cYFCb5URQoFwZDEpj5FipunrpLUQPOddFhhUXKq0GssD%2B5%2BhO6%2BGtJ3rHbynAkkd%2B1cdbcvBM%2BFhU0JDUCxCueQ4P5tnQBz%2Fp5A5fk0LvKQa%2FSU%2Fx3%2BrtY%2Fs1X%2BRj4igC912uHCns9kDUanagwvkZynx4LC7S8KASrsE2yBJ7qGcAWMDWkIj9SmJlE70ag3LZA4u26RB5yzIVzysinGWJCezyW%2FANQFf5ifnBcd4vkZpvZcpA6iNckdrCpr7BLGGdEXrqlA4iQGhIWO%2BBBYUtVesbyZUkDKwZTOLZxahhSx2nKtTOHih23QssOgES%2B7jf0w7tnN0wY6pgEYcMaroevSuYp7KNQ87baF%2FuD2kzp14gR5ln8Mwcygpb13hy%2FilD9x1Bx%2FAzXzxoZ%2Fs0g6Rn2OsjZVLr5GlZdCJLkeA%2FG7v1dHvmxHUSAZeVkATJ7tZotGBttlyZbVTSMhqCm%2B1XuXu10MvFGjafbEdAi8iimi%2FEE2z616d1wFRw0KGMaVryygAScWUIKayNR%2FrtMdn5doEN5aJFFCuVcSf6%2B%2B60Yh&X-Amz-Signature=651beb64b154c20c683f6e350db16af6a272464174920386f99ad42bca2c830a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
