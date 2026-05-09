---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2UHDZ2D%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T203419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIAqYQEmJ3Vqj7ANkSXB7le7%2B%2BSyIoKr4rGGlZBcadeRmAiAO%2Bfg%2F1YkA4L2aMFMTyggq2PaAoMC3O%2B0ra4xeK%2FLj%2FSqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2sSO7%2B%2F2AI3DIMBKtwDUoR0vxsAu4pd78XJuW8QpXWfEtdYZn6kRdcqWocdiH9AWzxSEUgQy%2FirmA96k7Dp4GuCKNy566MnPOIJJWogBSA%2F7VnMJ2Bn5QEN6bAxa%2BmxnmtuS3z3zUkL0Ic3bWvQdEzsGbwuLotGdTX9ZCWvKeX09%2BQnlrHRPnjM%2FQix7WttVxNSSzIIb5Bp5SPafGYKOYmrvO%2B%2ByNzlndiIs8%2FaKKtWBxVU9lqJ%2ByY5ikuFrJTDg2EkpBJXGADsRaf8q6%2FhVQD5Q8yWcpFVEAV8Reb2f%2FZywmvZmcaX5WkMi1M9%2FNyrMa8NzBCljdS5FETrCUEH%2B26ouWT6vqy5CgPYQQ7XRLD2I2X6d79Hbt%2B4keoTsHZFgrOqyi3rXN7hccETkjxS9ook718F75uQnl7u5wi%2BJ9KeajbAk3%2Fq%2BLDp3dG%2Fc5s%2B2CmBB2FAvUV004mYOpqOcwQo3q0tKtWFnZ1iswSM1o7bAogiMQSDOV%2Fu%2BRKzE02CwCPvnLY6e4DwEvqFjblriStSFpLJa6j2jGgq24FhWAfIxAUlXHMgd2RihrtkGy7raToUi1vgzs%2BpD1xAB4OZ9O4BpWAQoJJY2XkMvp6mxPD8xWmEWp7ZB4haG4Q7jnl18oO5c8fVtrUBiNUwo9v9zwY6pgF5bYXdgCn17eRNBtdxZevKDvZNxWMzOibZ7KFcd9iiynQHTZ9LF59MHU6B9tPAg305d9x6AoA7%2FYClM558wA0ZWRtLe0eGhFAt6OH2vaO2sr%2BMbpTsLytTB5bZvrProTG3MKZ%2FHsjeeZsD3ZDUxVwCzonowDzkyCP%2BUvGA7ck8zTCfXMEu%2BfYSWvxsOtShGKgqFrAUDLTf8795NSeBXQ7BTkTBxpOb&X-Amz-Signature=e1b30aa5d0765b66aeb9cbaa61ba883e77c8ff1ca354f4b45fb9b46cca7d3b8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
