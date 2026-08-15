---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YV6JHGOP%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T024736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQCeD5oSEacATgB37TXECePQ3gbJtgSJEDkbJyD7%2FK%2BibQIgMj47ca9FRfVEGBz0ZCeA5JsQnU%2FkLBndCqVvB2XIhgcq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDGPLDUmQkQ2Mvi189yrcAyXnJbEIjEtgjGe5VdvE4d8zPUhe0vzAW%2Bkg88UlF5paWr0qoJVpNj0R%2FINCaqNXhBC6%2FTqIU0yN4SFjKuqOZbaK9LNsHT9oDyyvLNfFG2qSl3u6O6P3Wm6RO5sc4RCrcVQuHr%2Ffl%2F3MCdb6XV8W1YcXy7Qlcc8s16eq0KszUcUjhnJnfmVDx%2FH11L%2B00xf0KYuweYs%2BjgYZ1jnM4vBsHRXG7rXtsGwsvi9LiKIX2BAyQkdk8awGEeYX2m9WBjvBxESLmJMYk3T8znkdHEPHMFmnQvPwGxSapW%2FuOyfbw79kJyLj0v1Wq1DpGdMszpYt43i43QXpnHE4anzhD2YxLw531f%2B3pI8ZdW5zIKN959zdQKjigxlOZU%2FWGwjVwERf9DFcfeDMId6jSMk65T0m7UAO4zIGKwvpCIA1xKDseg%2FS0alUUF3pr4kmhtECIt06sfJrQUBmKC9DzneYo7A4MTDHP2xRQ6Xlj4ByevBoT185%2FsIMpc%2B%2F8eJ3BEvYUHFABDFyKFGIckZ8dmsJzErFHlRNnOnnI7SqhKDGuNdOULYzHVHzZLE24nW9q3p6CENwUZYl8qsowSo%2BB1G%2Bp2HkQGyhBt2Zk9AzHO0yWzR1TnjMHB4uqvoznKqwrI4pMMqA%2F9MGOqUBs3ZCwGO7eXtf7f9TaIwsPIPKdx4YuAY5oityW8CixfpvoLCInPvPliVazr1YnCXbNRZz1on3x0WvYygnlYOAOm1IpbH7%2BrKSeTU8r98rnmnUbREm5FFPZOd1cQmu6Kct6Q1LujRohqL%2FvggV0PDnTLDZAvulhtPBPHAmTjjVj9bF2Pre3yivMsqgjHxMmKaf5DdwgNgGCrCr%2BttH9%2Ba7uprFfpgl&X-Amz-Signature=dccc749a6bf6ebb8bc828923d662ca63b9100a9df0fa73b3d7882e925a13394e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
