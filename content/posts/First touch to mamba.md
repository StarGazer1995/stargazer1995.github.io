---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM45VGFI%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T195119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCUNqIWlSW0bmWhsQ25uXBBHtsaeFw7s39T7T%2BF5b1oRgIhAPfyQiA%2B71%2BMl2NsEZzMRxjaW3%2Fws90j4us3BjjSaqodKv8DCCIQABoMNjM3NDIzMTgzODA1Igw%2FpHEvbFCZvsTwM5wq3AMJbDLx98FZsfUWXnx3sJWmkT%2FJ%2FrEFCZ1sLKq5uBB8J5GvDQ5t%2Fz5RxBKLjTV6QPdpw6fVCoq%2FkOcyJCvToftU1dmnIFlPXS1SViN1fDEMUk7YsRZTnuv8sW2GgsO6bKH0%2BLMJeSDiNgwmQODnhcYMe8pNl0Oul3p5w%2BNzpzWrGdA2uOjxG%2B1sM7A3ynqRrZu%2BQ04AXhdvaVyJYz6OVkYZESKxiabUo5wNi4VS7lmrtK%2FuL2bX6SAUMtcuEWkmjlIYokkGQ%2Fmm9DOC%2BO3OoTv0zBc8anqA3Lka8FDnLZ6jU6zhBCcrVN%2B4p62dkXIsTnE6OZMzajMRAerz0ZvNM5Gvh8m4LjRGyVNBkPHJkHivEtSHqT1lASjRAj6h8w9Zxe0Jguybw1JqN29fmCh5kHCHsm9HKikGPZEzBpEVMF%2BWOHyXG1J8Se3Um%2BQlu%2FY0U1tuiWFBpj%2B37qlzfVisxmIlIIHbSiamjBdEQKe7hrnshDZJN4grtyeGOsTGq53GQjYfEzieGw5WmF1%2FBHuvn9K4Pthz%2FkZ2JEDafaRiSCGWngzf5z1TwJ04U9zcU4XLhriRZkNfQUeDMjR2pT%2F%2Ffj2VZQlL8NcQY%2BCcaLPetmZhR8Gj24SepY3MxwjRqjC%2Fs7zUBjqkAQ26FZPP5Qet0b60XGOe9MEdJwo800448Io7DKwQE0WMXf6eXCNC9%2BwP8AUNlwYDgp0nJjI9tloI9QWwwUD0rnmXBe9nD0xqGO5%2BMwCV87E2v%2Fcqgx6NKypbLIqSFRhUHkAh5dLmNjKaPAUQch8Zy%2FT%2BmPPHBeYZgsO5kdIwP0mcxgX6vrMW0pKZy18FzY8%2FLtAxyyv18w3RQNUblpglEYe0Iglg&X-Amz-Signature=a74a8286cc0214748014e27ab3d238c923da837eedd6a41c1e13f0a040f85be4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
