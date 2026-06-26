---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHU5MSAZ%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T020505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvCm%2BBpvlglv1oqSImKSSOBSp3pH3t%2FidEcsGbHRq6IAIhAMEaWmMP%2BfMIrydNNgXVIYS2IhewxGQ1vrF9%2FiejmRuqKv8DCFkQABoMNjM3NDIzMTgzODA1IgyLJOOOjWbm%2Fg0Myd8q3ANqaaRG0F9NPukek%2FBPx%2F3ELbiMkC3eDnlDkLmY35mrbWLvtTeibkdMA13%2BiX6QLiMidgmT8hPYOQmTMp9NKzLv6Qyx3vhAXsSnyZr0zAOR7aA%2B%2F%2FVDKb7LR3eLmhm4CvkPtDshE9ITlWn4fqFtYDMO7dhbkDT%2BU5FDFW9Wj6ojtbfbbjoEMDXYXP7X44ZvGMFkRPqMGdyCkMRpUXOExaWGQcGdaRXKCrgIC5inxwsuVEHYRK5Ky0ZRbQLvl5Zptd9FmqKUouBzC%2FJTggjHKo%2FkfB1uZ1TGgRRyXPHklS6YWDWbLugrzWfO4KVvWUhu4bWVXeUO8C77B75AgMT93Gl1rlSZPSvRdzYhrdEVEzkfOq74KfTJ1aRCNyT%2FaEC%2FVJIGI1LahX2bTqEiCk2DcHoBvoJ6Bvysmc3EFeYcK07%2BvguGHubtTh64PrtE6hra%2F6SEa3thG94gr2KGiNf8JNq1itzLVhwh4L5nwJDn84%2Bg0iUypGFT2fPOjpFAzQgcHAUUZrrpF94AcKWcriyk%2BH0yxv3JPW35Zo9Hr%2FTnkpIo0SQevRcSx41I7OpxBDdJg4zp3HBNcvCvJzWynWKAAK0PUThfofgccbzPgAtMADogiBI8iOvawFfGzYvhvTCXg%2FfRBjqkAXmib1witeHMisjXxceZOOsfqEiNi2kwaumZq2gaghEiatPnwKj4YyDMO23%2FxjIgM37jl4eY%2BEl%2F8zSfFfjGbfO6%2Bn7%2FXXoB9T%2Fas8JUBw2riEGVvdSCiPTBB%2BJTa%2FKcMNLbX%2BtsNV90APhBar5P%2BlMPXE7BOZQFzBg2IHbX3JWOnyC7i3k5f8Ko0dfXc%2FA3sTPSkW3CJSNZpf5mnNJWodSVPwjq&X-Amz-Signature=e0979bd47c30a3c353fc0ca8b8c4b9493c25369ee09efe5392e4026e70427bfe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
