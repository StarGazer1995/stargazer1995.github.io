---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BXIMXW%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T011846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQCCpdw2pM9UUN%2F32YD%2FyCjDUsvEfBNz3NO2vxdcRcCIpQIhAMJm4pZED9i1ffjoRCdQiLGBm9vO6LZNDxAfCNi83dm%2BKv8DCAIQABoMNjM3NDIzMTgzODA1Igzjyy6qVS2VEvkfOc0q3AOx6zweq4xAyEz9Mq8ltKFZfFqX2dxTofX2M1OpQvMYaa%2F5u6tjuMd%2BGZfldAMHMkcxEojzuZ1Hn%2FV6KrJaqPS3f0vI6oL%2BihBYJvrW5bYcKjlBmdb7eS8J6%2F7iOE79YIs%2FHzKGqMHcV%2Bl9wlES4r0jXYtsWa8ArejfBig9BPM2cXrdB5%2Fd0ieDb3lgRM9mVilL85suapDsfboJJr5jUnLf1Zc8U2XnknYzLa%2B93NboGRH9y%2BLKwefLi6ksjOX6k9iN2FESApaAZ8NHXOSpUAI6zZHRHHKe0RtAWQo4%2B0L%2F02Zj%2Fyww9Zy8CAl93DC7oUtNhlNDpIVlfSsc3ykRkpPBCIsLpVeIAh%2BDqzcjFLQnkinLYWmp6kDpzKxLh%2FrR3XJGPenwZAjaFxasTfY2xtMnbQNS75VvGZUa4mmhu1ysT1uwIb6xinJ3uHkSqdcs8Vr4L4IE01eSTU1aibF70D2MZpLe5Q89f1jXE3DRQnAj9wHYYWQ8pRitHUOPcbxY0a4HKIuC5b6O5bLXNfTqIvitLr3FqERVHJgwzt9ULIhaLZ5zktn%2FfbwgSIm4B9mXJIwTfNNjnyDNLLcGn2m3G2yir7WUAxHbxzHL%2Fm2kTPkp8lbQBk85sKxml%2BSOXzDD4sTTBjqkAZ9HMPnJwhrbrXp%2Bkx%2FxIS70wfjfwp9lNiqTh1y4kWJl%2FuYdDkC%2FJJ%2FqG6OFFuZGq5WTEoe5CqNMBdh6hbnI1ZovRpoXrNJsdJeliSruM58uZ9Xx6%2BjjigdJhntwN7J%2F7V5CyoARnWc2FhXtDU4InonI5vE4X%2FAE%2F4nBwKpcyD3ZcqJZVY981jX5n8ZRCiR8LeRK0uR%2FzFNw0PsunkgEg05TeD0B&X-Amz-Signature=2d5200d59bd1d4c3101d55d78f7bb2feedff24d1608c7f947029b83ad0134034&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
