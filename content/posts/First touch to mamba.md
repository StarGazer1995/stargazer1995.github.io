---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GOEWDG3%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T102435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhhZJhw6IbblrV1A75SeNBRYEyyiq0nA3m2BKYRxPQkAiEA3aj1g9yxmkTe173OWc1rIGyriGUrkeg3PW%2FjCsfAK8Aq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDOZ2gHUs6KItiWuzKircA%2BeafUZBJA6meM0i4oR%2FuDTNQD9KEuyKFr3xvF1EkxXHEO66nHXpuPTUqTotyGvIfyWuTgD62iRq9%2BKDo3eGwt4EVCwfKUTDvVyZdFmCJjt%2FqoCuKWfykvNiEpDoq472md4wuoaUdD7u8lbj%2F9lFG5ctJIBd0qp5wbCkHNy%2FJ5COXVtVeRQzsk%2BsBnbR6isxsMWAN%2BsKn%2Bv3vAzpmCpMslyXfZIjpwioUNEa1i8qIOeyod%2FFGSHPSHMlTTQ%2F7ld6o6vqnn%2BLVr2GClI%2F4bkb267n4L1jsDY6DhxeFS9TbsK7DwL7zgbbAP2Xnj3QN%2FedeVDJQIvXSAEfqR6TCfv3CKNDWc242tB5KKx97klg7tE9webdezxsfhPEvaBUHBTwDqg4DyCeDHMsJq9HYKLBdo%2BlH0XpSPF6yLd4jA51u7kn3AgmKPyDpnTZ3llMBMYtHnPXVicXxMMdeA6DzUngW39lcS2xNZLggCFQV9MI1iiguFL8Oalp4hkC3zEe%2Bka4dXYhKiv6h5SHR4t1WZmv6N5nrNdossHfAJK6Llcl2kutYZBq9SHnmW%2FFl1ktm4GsgHG%2BR3h9dz%2F3%2FMVlwCZ%2F4DggY5SXmIiUdqBRoIeOn0qhHJP6cN2Qal7TvH5vMOSirdYGOqUBVRufslW6wETJYQ0Jc7HI9E%2BxoA4e1F6R1fiu%2FzhmOaTi7T%2FSjlK9k7igGplPchrNDo5kuDixzMMBk3sDGNevqnFYP4bNH%2BiB%2BM8IZElTMl9cN1uVkJmQYRHJah%2FAhLySZ4KbhH%2FVUBONaKTOQuQs%2B314j%2FPa2vVBhrhr2AS7Bqg01blup%2FmOsgiHd5RBro8P6jdDTBEf13%2FXGLIp9%2F7ZU%2FKRc2%2FT&X-Amz-Signature=021cfbea0c30d56d5d0c91cc96623fcee1d9b31605905aa4844485b0d078da9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
