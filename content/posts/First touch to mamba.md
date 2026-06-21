---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYYBLETH%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T120518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDf7kDEqm1F7E4zMzrznj%2BCyHd2k2Z65GBffOLU62teDwIgc1W47zrNueYvLhYef8yXKaa8qIsbQUad0PKrJ0AdAM4qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDx%2Frxjt9PaUtc8N8yrcA2eRWD5ztjlqQw0wvWMmn9mjfTUAiMIEKylMYVlHx%2Bve0YS0l%2BRhUKUpzR6i1w6WklvXh7FTWndafhyxxq7JuCuf8PzIWVteunK6c9lRXswvBI4g89%2BNZc3Jlrw2JG9Fu8G%2FLG8KLp63PaWPCQnXoUuDR6ddZgFh%2BhpLzMp1bAJR0KxkH942LwFRpPfbKKvKkQA9W77pAhZX3Qavl%2FgLSwU1xpK%2FY8O%2FyUEHXlwvT%2FD8t6h3vR5YLz0XatWX3tUb%2FbeyWj4NXW6g3FIB%2FQSvAX0ZtxFfeAtdqXgQiBo7%2B2nHTfjnz2tBAbsU%2FYiWBVnQvgH9py5IVKiJpRB%2B08PvW1A1Ss%2BIy2T3NK0UlIVI%2FFbKDKte0KzKXHc06WLE3%2BTu58a9fH8rF%2FfKF3Qekd3HTNTBsQCjiNIyC1qZlJOZjPtyZ9QSZauNqT6G0UsFQ6e0oUCox6VivGsm7VB4tZfwAtNe%2F6I61iEgV77DJK1NO0iReRdUspmQP7t68frJMRh9yAjd7Z%2Bb%2BFdanjs0n1GPI9bHFjGqdeocASU5xBkXwN%2BBgtvwlpH%2BW%2FDxPXvsubDEH8VQPCeywD1tVtayGKiHE7QbTR8bC2oAkBrziiFAQJm2cMsOX9AG0gJYztF%2BMOaB3tEGOqUBT2sRvsNaBW4FyX%2B9VIH2hDGVWEZoagwNcZz%2BiYjL%2FbT8nmfXXqEHpC%2FDRO90DrGRt3iN2iZHbh%2BsLBwJ4coDnrWxSLxv0Z%2FIsE88HxnhCv52sW2HOUkkheIaVRWayZZsb2OPrg2deOpWRAEwtv%2FHsEZPi9vLuDv%2FBGpN%2F0rb1Aa4Ez7JG6LK2solCUVett1lbtbSs87%2FniSDbQqXK4YEyzbviwAt&X-Amz-Signature=0a71adf9660741338eb5e1e04c5b309a48287f99a269b781510b64c27bfd4f20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
