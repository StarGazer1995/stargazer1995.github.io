---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM6LIO5W%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T195802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIEP3asmLB1wU6ITUwya7LI4VPTT41ZKE20RSR%2BybDVhrAiB%2F5C6O0e5hSak5anDJM6%2FizMtBuR7vDE1rYK4fiPaGpSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMO6M%2BHsNFnCYAI46FKtwDuVYMPcr0iCIQ%2Fc1G2vE%2FCrIxBcYyVvz4cRlLT%2F3a2M6xQ%2FP81U%2BURuve%2FFCGDxCPfTJ8OYi1KLidqv2LC%2BjDmD8EvjKXIkiPz%2FSmbtFFXw3q3Qn2OEslghY4StY5ew%2BgMlmOOEioedDORe%2FLCb8c6MytsH83TX0YIRCGr0xU4v%2B0%2BZNdCjTwucVK0eAo5A8vFLbIXnDU9%2FyvrIadd2pJ1vB%2BEXm0FN5qW53nPV0WeXGtva38SifcF%2BcMBiNgyVLrmnGlW4veaAU9qhwXYuY1zR3yWNn3exBfOZfl4GObs8uixrBAtCQq8HF1h%2FRpN8znkjLxidI77ZB81ifOgQPCSSPBmRwgvARefkgmpsWM97n6uL0ofL3x%2Flff49uSJQbus2RIY0k6xzqD3EsfH7EVWcHgSbuYTNw5OP0PBuNGRMVDEWHkBT55%2BruYIuAM40Lx5wPj%2FO7fm8NI%2BdyLszTwEhnmk1557ummondLzlQXLn60pMdoQ41eTCUabbB96y10KqBm2xii5eshYeDLb5QSMFTXN3AGm7mgnWup9B%2B2Njqne13GGAIuDGifP9%2Fo8PHKsOMVC8UN6GIFx%2BU3Lzl6%2BFxSy8SSuMPlG62pxoZTxIqojnA%2FsgwBX3mnM6Yw%2BMyb1QY6pgGI9GcCR7nWNcFO1Efk8T0J3s7z9mVtqjJoi8njDfVjEfP4rxrAF52C1UdgjV1mUoXygvVgcOPJ%2B1bXguQCZXt60JZ%2Bk79si93lOLDe3Bxc%2BfFu%2Fq5qyfrAa5w23fmyFkFvbID%2F9ZPtB00mDB1BP7w65c0hTfXx7qschfdfVdMD5pG4lPQd1z5jGBqW9xvYDCqKcwtkeIRdKtkwVh92kLxlM7yYl2EX&X-Amz-Signature=8f30965cb558492ea92fce14035a5c6409059771d1f7e75e038557af08ff1645&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
