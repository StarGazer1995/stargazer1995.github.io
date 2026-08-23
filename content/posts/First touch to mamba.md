---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z72YO72H%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T200957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJFMEMCIAXhP0dzBgizDXCGaY9m9mcvpS%2B05ddFTjNgHRS%2Fq7EFAh9Gh7o9UJ38UxIi1az5D5qqRqYR3kkxLb%2FY6aFLtrKkKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhKnQd%2BalW4GkFmZgq3AOpG97QT6hzsDShUM%2FxgGhi%2Fq1Ma9ijwBL47kr1V1PM0NQIwVlx6fy65dJ4dhEd7%2Bm5o9QbLy%2FKhYs29pEryXgyX2EZlRO10CUn%2FXdJvkXinWnYWobBGJr6Jg77CeqTxgXWeVKX5EYPVwdw%2B8jt4DBrYYNgl0SccjGU6iB%2FF68LN%2Btl3m7zISihqe9xHL63QKSL5etwYbWIeg2LErgxQDllqTX6TegmjTy5g1cmdab194znk2m%2FHVHN48Ms1kvhdN8aX8fwdD1DtptXUoPo6BLYbjSrLxaacNYO%2BRFVCffoSjj4GNW4U%2BKMM03YwPNHILLhnrcIjxA6EyqZOrDnb1ls7gb6RYnDehlt9TA1JZj2j2bBWjC2SQrgFsjTsM%2BKebU%2FWz17rraRECLLukRcjxKOEx0Mf6Gs2AgZAR5F410MtbOEt%2FCgD%2BS6to%2Bsr8efzWQMzc4wngdoqEW64EYnnWXCpbsvpE52u18mclhooKxW7rLHNd1R8N4FTzZnEkxk7Z7rJiXqdZo9EgyFRwETmSDqw%2F0pG3XVXpXvCeS4FGrYBsblB7mIVOO1rv0aj46hO7pJ1tZuRLs3JjyRz%2Be11P1V1dZYB%2FgmGKTWXzk3gIufS%2BqdKosA80gHjAXuwTCnnK3UBjqnAQlruicUtTlcg3umzDTxc0Apt3ikTB5DrvAAUzV3dZ2EWmnYBmiSLR4cLoHlu6aJMg7ZZ76kGmwPkY%2Fqub4XjM%2F0BizwxbTsWjO%2BdT4tVO6XMVHJth3mCtti0lSzn7cjze9s%2B%2FTZbQvW1xGofjr9kEzd5e6VXVyfMWUbrtpQ6HQBqXn11FUDkrjHpEtMdQNklUxO9jXOO%2BE3vsgT6v6PteNkVhvzo3vo&X-Amz-Signature=e6327c4a1a33187d4ef0674b37866fca0019d8abd445eabf0a02bac6711cd5c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
