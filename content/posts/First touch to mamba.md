---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N2YYXD3%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T012621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAH0PnLx6za3mff0GxGzLEq8t3jLMTh1SstsK5KCalj4AiEAkuHnNDkxB709bC%2B9IuJf2RXdUcTM6mTCTRDZUXMFon0qiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIczl0EwTqkjOZZngircAytRp%2BpnZuakF9eO3gzqHEb7jQjFa58RXjbw%2Fasfwg1WPs5P3DtuKfoMFOd2qJfj2IxYd%2FUVOf6s6jVe6YD%2BQDgJk%2B6RXvC4H%2FjqtnXDd8s%2FLafvkLZG3zTzEvDTB%2FEH10ODDH1hRvqnsvwUzkkBSGZo0nJK9M1k%2BCXslDjtew0kYOb%2Bz%2BKbDOZPKof2%2FMRl055ILH7xRLCkW3izx2w7czgp5qnKwHxPU%2FYy%2BZEi%2B2fK%2FtBAxKyCUtwDdRjINdBH7pyp9rL%2Bz%2FL0XAVf2jqLT9icrSV7vPEoSHP3hFg7QPrOnHrfNwoc2VRfSMEnePhLGt%2BiLfhVHgTa0XGF634ppGBfRe3hz%2Fvg9Qe6qYXYQfm4ZI3wBkTg7mQKdRYtNC24BDmlWB%2BZuk5V6h6wynUtvpDUw0ZV7xsJ%2BvXfQXHmMct8R%2BFsiJ7QtaZml1AHkYjwkyHlUH1m4%2B3f%2BFGtpv9ykMylW9rGsmF2sRXbG8xK%2FzMj8x5viElcuMbVhQB0j%2FiRtRpyJBvBVjCTEvodLBMXPZiI9lK9qNYxAQZ8CxxfNAdSIIZW9ukH7EVUlL6WgalUl8q45435EPoke9z0KEsI2bwb5aPraNErAilGEJOc155%2Bz2HwD%2Fr0Bm%2B9T0KWMMSt9dIGOqUBiDW9murQuTgA24Q0tyDKZ%2BJ5wtIs93Opwnh8%2BQDzswga5uiPqWXpxYIXwBwTNjvnLr3LhoJ7rVsRAhtEDnvIOno%2F6lvkm8lk7vM%2BZ8l7%2FOyOo32eNMZYaBaKZlg3mOsjsvfcvvuX%2Fc6o%2Bxhxwr9w5aolgfs6V6mByAdm1YTPYLKAp7nKZs%2BUBKC%2BD5fou5sL1jP%2F%2BqZX5%2BP3ZB56u%2FnZ6lrBaa8a&X-Amz-Signature=4bd096afbaab1c47054b8f2a5d3b40887cf61408fab96769b0935de574192e40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
