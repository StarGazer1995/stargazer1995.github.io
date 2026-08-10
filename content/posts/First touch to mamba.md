---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4MKJLL%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T222531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDqD74x0VaPexSJSnCZIZe9XfQ83f67xHd9g9sQQQsm8AiEAo2NN2t40r8PNPgenpX9mrW3%2FgDTYMZLTqguR9J5VT48qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCh1%2FzgExrYYUdEBkSrcAy4qs5uAB8yffLU5SpZQb3ax7%2Fm7VBddXS83HLzaB5oT906zLDLhxv2v9oJc9Mhu4hrxkR00wPWMS%2B8LY%2FrCT63eIF01%2BI4g5UnTzz26u2bYCoqmKDWCCl%2F6GjoQe0a9d4gklct5yMtzpTDaZfAK7Dvf1Hbi48waQJ59kZI7h7F0tkjqERO0cd2BHd%2F58i6SVaIaX5EiEX9rjDuBPR1OCwnknDwcNDTMhgizg%2Fri4YuH023phG0RFmIih2kLr2eoOZ4i7mI8bJj2hNP5Ya13s7mKvH8OQ%2BH6G9K2bQdxThoL%2Bk1QWrT9MnUIBnKPX7OUKjvRAaQo2Y4s3oODsPTNmJQNp835d6FBMoz0XD%2BYvyNzeVolDHSFspQXO01tXhosNq1aWpYGF0OJzpI5aDVVHJUDqaaQN3rJ%2BGJjpyz7S7xTENNyeijwcZj%2BISXFLtzF%2Fzift7Sma5G5VlxbxbGlFrTtW3cL%2BH0%2BwJD5CcJLN9kJ8YVxV8m1WnhO0kNnxDQAjQiweg1QQf0errqvzpU5abs2XKKHE%2B1UFkHGFZwcIYsZUKm3lkFR2Pa%2FFEfKKwEMBoUzAGYsqjNT7YBj85EZcrIXk3Kv1weZYKZbaUfSYuFwm03bPl8pF3ticqKOMLnz6NMGOqUB6XQl7DpyRmdHoDuiHYg7d3fYKUbGoyMI%2B2dX%2BPVN5KamhxpO4BhuKUth0%2F4zgpW8L80RV%2FrL5p%2ByC8IkWiAf776SWQ7y%2F73linxMWvirjRiQ5dJsLpyrYRQIduw1KwpBHpgrKThBzoDRo2Cm8DTdyc0wSiriwCVc8MFR11ffMy8YkTNpoSzsXowuZlkL3fqVjlvfp5QiUOLrddnVUz%2Fuh2WJQ%2B7F&X-Amz-Signature=5ccfef8e2b382a9e435490ef393ce925ca44af139e30798db665d8320e4b33d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
