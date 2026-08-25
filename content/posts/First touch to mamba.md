---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665M6MEGN%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T102039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQDO9J1bcncadiqPf2FcYFDcyVGBiM4qdIG48Ho9zfxmJQIgR9TkJSaAc4ALVGRCZ3WYUs0PZtHXzNWnGD6lZiUifpAq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDB9RuSKFaUJWRdvS4CrcA%2BAw9kGlpyZP%2F58zh9iOimjRRoYGZGeVI8B43CUQ9cQJtFXOSPSsh8B1zpI1WF%2FYwFkopr13%2FGg%2FdvWeqBjZeudwZpjRVfs8grO43IDNwvC6yEOK%2FPyQ9HC3nnF3Ln7n0cVYd4RVXZ7m%2FHlq6OqEi3bn5Lul%2Frhyw1WeBXJ69HsjN%2FD5jCjXe6VuK2pBbj%2BJ3vrGK1BrHu6oplWOSY23bEDeF6axBZxSKkMIvSdyEkdGFfWA6GV5G9B6c%2BVmWsOSP5oukp76c4wsZbseqldr54Fs4NBM3ketkjNuHZiay1m5rHMiQpHcPHRxy057e%2BHRwPzcNsdzvuPdrghXdO2jfLi3SzLuI5tV8jeMpa4kNIklsb9Fmc1ODhk%2Bj%2B%2F39tcb4oUC6QzGG6oGCJxOzHis%2BxHitSpFT8EJcRUCvKVfo%2FTC7pTe8OlSIfsPHhJMfw19eFGJa7UEBykCD2ALAdSYQhpHgo4N4pgtz5XFogkN3JXqefDwXy2NArt7MKV2a4Rh4ugcG3rcykH%2BK0Ah2RLODYG07yyID1mx9b1n7PEROPwy0Z2S%2FyOHAw%2FGlK8yErBgVzEWcqPrt2Q2Phj6%2F8%2BhqVdPS51oUdpRlshGdK99JL%2FEZEDQoJrdJac14rt0MMnUtdQGOqUB0mJABwAj5hLrHZA4fKWTIJc40r4bBiTvY5mi95RfWH%2FCMh3zvZK8cg7xs4gr8j%2Fn4Cyau8EjkjPQyoop2bisNA%2F0OWyZU%2B7wUv6zNqArf%2FBz0IS3XXANkLAFVqqv7uM%2BozG3sXw5O4U2hbTJvgeSPIMYOc7TIJ343lqUYaiEYnz6kPbhxdYkVa%2BwmhuBa1tZ5ykUBY8lnwArvMtlXqDrkUr%2FwQTF&X-Amz-Signature=3f54c5773eab9d0fe8065feadd11bbe5cafebf4a8e88a64fe38b35d3d2054b7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
