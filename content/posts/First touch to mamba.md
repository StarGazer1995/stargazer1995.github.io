---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REVUFEYS%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T012216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIQCEJbr9H4iHVLsR4wfjeaqEQprmac%2Fh6KaXtLMNy8G3OQIgUCbumvCu12VI1kwO%2FCa9%2FkZ9tRb8cwR3vZSVN3hsO08q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDFKLVY2jNg36WFb8sircA6Z85iiWHHRZ%2Fqdiu6MDU%2FG5SRZrKz0IuN8Aqzpcf7Xo6rl3oojdEVDfsOqIyZrAwk4FZaoHLoYctJ6MkToFehYztMjKYi%2BfbeMy4xpGG4%2BdunJIYdhfbs02Xebk62zoCiCDJkXA8HVayf%2FdXKJWphYpU4iLlsOB8jh17BNoT%2FvWIwE%2FZnbD8ZzuWHdMU9rt7j8Tlny91OFPHhbS0YCIQZ8stydQuDVATTfv%2B8mCSnVLqJ3wJSVQD337G0wY6SNVQokt5WA48W%2F2CQed65NaneHzcRk%2BaGwZyyQawJYYPPi1RIWJ91sTImgXhWNWcMXr5e5dsQWIzHGCm3duVSmqYo82aEQYHWw%2F9eYrs%2FZxH8Ki4QcG7JcnrN%2BM52BKkxLH8%2BFbBkGS2HXKvXjMHp9qzQmRJEQ64TnLatB2RQCFihWFUIn0bAPHP%2BxS7UMZk%2BJiu8mtwZVonPunm5Wa79Dvg8B%2B31aqBXdOtb7fjknqePA48Z7cFFglVxuzp0tNyD5YI%2FbuDfUI%2FDG0b%2BlPucQglMyGGrtebjHjlaPDumCHF4X2sVDQtgKQ32RONcv%2FPEQagCFOW9yNiySo6fN7mld5yenBPpD1yNBKt1tpNb6YcHPrQ17hsyXoOCS%2Fc7Z8MLDG4NIGOqUBltjF5J%2BT9N90zuiDeTTgpIw5k2%2BoHL0wzmcDVF8eAdSxrZ6pOImsui7TgkniKEEObUMnQKoNhv5pLYQ%2FAWPh6GgiKHnwD9O8MJWebQ2EpoayLA5TfaWMjEeor5%2BGC0qnK1CmavxpREwlX1f5oXYOSI7gqoHl1hkgpG%2FDQdAJ7C%2B6VMPvxKr4hlZejiYNNpXj9nq97ma%2F4ehzt9jjONCKuR1TpML9&X-Amz-Signature=ccef9dc4e31cac9eadddcdd29f3df21805b374d625c4d8b2c332804bfaa154d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
