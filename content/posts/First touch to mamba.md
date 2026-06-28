---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USGVZMFP%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T020954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHtsgAGu2H%2BvWFCoc6Rmk4BhdIjyttXS1AMXq59py9t7AiEAxC1ifU%2FHrlhL3SJPhhc4AsI7HXLbcJgHCks6JCKSLxoqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFipdmPpuzHWg2ZfMSrcA%2FrXXX5rYLjm1wRhl9w8q3YW1b1tDYNUE8dj5gNTqv%2FATULfTAd0odnxxnLtpJ9RYiWs18HChUnnbHGGYh1HBnsT4airbSt%2Fam0OVClfkqRiPZJk5S2QaPydf8LuwvL0DEGqXddbSbRUoxNuog39v%2BzcVPLfhi%2FFIQGzIZlOiCuZsQULr9uLKgQ2EvZs5Bv68iI%2BlfhFApUbWBe6yonZ99IA6tz6iMTTJ7xEk%2Fiv0xdVPTIG6w6i2%2FevBOG%2BpdhpRmja1hpdfQZGX4WFOZ3ONoAoHQnBZcrjKjDMqMD7eCU25DEJJJMTrsIDOPsnlpSD2JxzAAyuYGCF6efNodZsW%2F0Dvj%2Fm%2BaXmKhgps98DG7V9TQK3FQFVyJfbyofaywOQaWpenyb4zZf8FRBuCTvNr5WZ6YhK2mmZi1fOeibzEB0yqG4vC94UNRpphiA3slFFKwUzYK8rfqo4BO96Y2Dp%2BSDfcHrNqKPI6nWqB5jr3C87q26YoPGmjWZueg%2F76MvfH%2F6Gue5TO8BZ%2Fie7asYt43iU806c2NiCLdogN4UUlFWzQxZ6Vx%2BXcKp7yJ%2F7lyhAXILEruHH0126WsuRqzPVhTvCIgbbh3kHDVGfYhO8bBYDqj64UxAejt%2FPzVjeMMDGgdIGOqUBq9y5v4Eb69Ld%2BrGaPM3QU4Ge53bl4h%2BhObPIMkKR20pGO5x3JYMYGYtt2RGf2E%2ByV%2BXFv2%2FYRcmCRbZXKI7X0zHQvhhtZjBjo0Uijrp9LXn7cdopfjWIyqoCoK66WNqo%2FlYLQxoH1l5id0NqM0Y1FLsnycWg2znEZswWxMEve0ThGVxjUkPvkrI75sdaAHOmjQcvENBjLYE6KJ6jxJEOiml89SFE&X-Amz-Signature=0ede996b92d7f8b90ed27a804cbe48c974e3516694aa97a7ac6c098bee8770ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
