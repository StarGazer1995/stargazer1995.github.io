---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642DIHNCV%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T124314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIExYPApQH88lfY9EZGbkiSk2i8Zx9QB0eie0gbmI1HyhAiEAu07Tqqy%2BhQQFD8dTyFsPC%2FypI34DRILbj7ZyaMeu6ssq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDB%2BnTbKEHi%2FPISM4QSrcA394G3%2FeY9izZVjVHu3H6RvjW%2BlKr%2Brshe6TdYwm0VBw%2FA7x4YClEbGpdCAcL4kSIy33o7vNwZZxiTZ6d%2FWtqXx2BNU4dLyxOmLQwAOhOChGfNlwbCqwN1WodhvvIXdpzUgoOdcxRJ7dMvvn8iE9k1AmD1BDUdqDZw8axeOxekQ65I285PmaFyPWyt0ga0RNMg4vzDl4JayaZM%2By%2Bx0eJAgDzd9L6hAdIJuvuD%2FBj0rZ3e7S1y3Cs298M6kBZ6YriMkTd%2BScBubhUUL2wPzt8L68RaTyyaVEgXkfSasNSBgQUwzpnNPAay%2FazxUulI8ieee%2FtMtgQLzSM1hm1mkPA%2F%2FDauacUU%2F%2BFsvft%2BvHdaoJFqy6cVSaqUrdu38OgAICyDwpLU%2ByjqygQOb8AJ%2B8q43CVqi9gvEuqBB95mgf1wbMWB3FT9L4rXmSb%2FHJj5IxK4L5D0%2Fc8QGlOMr6%2ByFqOvEwhSiGBEwa%2FjpMjh3Gq7iPOzfASch9%2BGnnqJqxoGlMu2n3Yyt%2BfaG9VJFnycSm1W2gfngDlw0iGVYt5ay%2B6OTDuij6hiIIfK3j%2FkW5Pt1CiO9KqZan2BsrQUykWG0o6l9WUmTs8Hz%2FyHSgW2v54xCrEsjmJmRKRMiErxeGMJH7vtUGOqUBSFKnqB%2BGs1YuxTooQhBavzGcmMyXZeAlPYtbRuFB0tPHNAhF1wq8q1x0GKgTuTnJUalD9etzkE5Fmg2rzqdFg7M0nfB054UaoJj%2BVjAOJmhm7R9xa9YHpjeU5PrhPpu0wPJKBhZ2b1225H0XmF8poyLjNgKBJh7A1Gsl5W0dZqjaB%2BFBf6jjnm5AJVDN1hu6l7wXFDB7IQsQ29Qy9bbkAEgeQQh0&X-Amz-Signature=29da67052f1b85e4d1504fc88932c85e09d5a77177a97064f9f6941dd30e27c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
