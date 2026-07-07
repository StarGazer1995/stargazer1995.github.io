---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U4QII22%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T015316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3mxXgDTKV45%2FYk5YOyWL4rpUkem9VsbBk2zeKmRf7WAiEAxaJ0Pdi34KzasVxn8ARJa%2FYVtnqKiYutoRR0%2BPTTxCAq%2FwMIXhAAGgw2Mzc0MjMxODM4MDUiDEOjjU57w7ZK3J8lIircAznK%2FLz82PAUjeIjfeYJlTElC2S29%2Fq94ZgW%2Fyqeb21HpnZ%2BnFRqEQmzQxkb7shW%2FqM2yxf2hKZYRdaXpLyylKkMXDUkmKPTWmEUYdbEjNAcOKPwaWbv%2FQjoAoAEFxHt0%2FC%2B7DMmrnALYQ4X2pxTrOz3vlaks1JPTlXmYvxJgXsk7z8%2FiGJHeiM6uf2QsWfi4vjPlKRrpxY39rB5fnvnzDjdMylpd7VfCSVwbrs83QRl1iHFtDEBB2zK%2B7CD5zkE6JuK96Yf1FGf2ukfi6QoXUqd9D%2BRdDM3DtqXLJs1IQClPa68wtBcK3V6AGNHH8UOece%2Bowr5cqQl%2F%2FJtOtZm2jrkGQRIBGVNNx3gJBUDGSrbltu3YMtUYwkDFAnIQ2k0gPuNiiRExbkSZinP94QvyKL5OYZa%2F713Iref3oH8uBr%2FY6Z6DnV5CX9Lj9KZDxbIXP8ceLLZ9lUyo8pLBcCPNtkdS74UJ%2FJ4sEAxUqf5pzxcPSzehavMM%2FoD4%2BVVgKt6wCGD5TGCuxwywDS14MEaLvI7U7YRkk3%2F8kSPkhZkvF9LRmBi9jhVTv6s9noJ8CB9wbXmCEyW%2FMsifcUaO%2BNHhvWoKVmXJF098qkEstRRB56vIop5du0N%2B8UNk3GRMJqzsNIGOqUBWtm83aMYILcMyJ0KjrDkOzan6cveo0ZAsNu7vnOYK1wgOZABLaDdg4jlHXaoXEw7cSC5tK82U3QAzrFelOrWtbCFZIfIcTzF32u6Bm1uazc6R6muRWqiRoRiisNwZ8XlqMfPXDb6I0vgl0Hd9Jh0fNpu4L3BTrc3%2BdN%2BimLP2IK91iPkMFFiJslNEgOdz8socuM983CJQ6zQtTnzSFQ6vrHo9gLn&X-Amz-Signature=ff7b3f5228f620b610fa9a685a7606f19d6ef2c3466495e2a07bfabb3d0b55cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
