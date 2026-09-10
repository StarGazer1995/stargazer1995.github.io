---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623NJSJ35%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T014823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzoHEZSeOjxc9A%2BjlGPVqQRbSXAkt6wRpHkf2c422cmgIhAPPqbjBJljNoAD52iCoZoDO4SpZ5FHMPHC6oyMhZGmcKKv8DCHkQABoMNjM3NDIzMTgzODA1Igydm4CAaUxayMggxUYq3AOfNCeyUc2ulJXo5SCaxK6tQ2h%2FB%2F6pdX%2Bvkovg%2Fi9QvcZTiLQwudgnkL09hUscKvSthRz6J8tqbBIOl7sz89n%2FNnrXnNy4s2NGjyUfyGcq4cqx0ImOtPldI9D11xRipelj1a9EkJLSjXNOUVoZvZSj3vXk270wNJo4E3fwPO5qy8H8cM2Q2cX3mc64FHS6eYI7ycUMaeW5qjuqyHHGeO4WaILIO68M2yjUEy0bnjdN7CPQB2EZbf3O%2BTgX5QK4l9ziyo4JiWwMmVkqB8ZyTLP%2B3YdBlomVxrZeSg%2F9vd5RMdS1df%2FRN9FWe%2F0pX5TgRRqkfs6bcRSf%2FG%2Fmm%2Bopyau45WvjEUZHy0wsA6ry93SW8Sc2Mzn64T8PaMRrIAlKjx4h5k3qFdSs0aDbku3SVKBEDhJu1q7ywnVYaP0TIbtFonCzpyl4BhWKTujJaDyTge4O1wpBUHgSjmmoqSZc4Tk4mTf1wSPmqXWJJ%2BxSP7mCwo8rh4TFgdmxMe9G%2Bu4dSg85HCUOSLjHrAtXC6KMo4%2BxgxBqvI9jo8zfyuvMzBom58mIlUpib18Ws23%2FSOojTle1ucYJH3NluvdQ1gP2FxDSKDuILYmm1iwT7KqyxUVXTn96dsMBDpWm%2FAMjHTD%2B7ofVBjqkARZd6WoNdUEbJZMMtzrOVZ69MnO5Xa%2B30gi4ZmXW4%2BtH91Jf%2BwZ%2B0jC%2B3JMX%2BxegSGce3%2Fu%2FARLFyoj6OfTuB0SfsYtH1i0IttYnpYwy%2BKZghUft2qiHBkX%2FqAGLIIeKdcid4jJY3nayzlShrIfnmHkqykm3dN1vmTQWdLvVm1fX7sSnZmL4IlCmM1IBI%2F7ebuS9KR2uvNWYb0tWFQ86SanpuRBT&X-Amz-Signature=f1faf1ce64014c537b75da5b7bd588835ff6f435a48fe2f6ef8d46eda40f7499&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
