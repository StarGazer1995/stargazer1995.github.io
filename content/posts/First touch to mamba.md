---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULDXSPW7%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T075444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQC2aPHXS%2BOAZcJHRAmRnbIAKRA1eFochBj5JH%2Fi5dKb%2BgIhAL2NqFCcze9OkulFxZ%2F3KEbD70c0NjCra%2F0ffsipKQmDKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDhyYUhYIFCjZpJmQq3APhHsZW3q52c5YU3dTV7Wq0%2FbOz%2F%2BRhu6ai%2Bn0UwB%2Fq9PKDE9lG4XY%2FfGarMJonT4WMIOHR5aVW0sfMfFse7W1MTJJ%2FW5C5sqfYQr8j2xjMvSB7tffHpbGc3HdFwKf5x4t0Ycuwf02TrNe1LeDBsGXDDDf%2F67W2BeIxHZVSpycpllzo92ounxbK1wp%2FkPDBfKKEJRrifZpMJrC46R%2BYmRapOw24wI1wOVbugt%2BpqMdeM5TNIoLAjD9z4cq6Wcj%2BBy6c%2FQNGWtxvKBpTNp1Y3Yx%2FKmPMWgAy%2BbyY8x33qmdlXkBQzMo0oSSpFujLSSgZIIoQD%2FbmeZ8KW0YdQGLVW7B3wAyAjHDn4IVkH4fCKI%2F5VSfy75KKnmjStCQ2AVTdmbKxkrl%2FZn%2FXVPTuHBLvYDxfPqPnK%2FUS3PXOnbGHvFfzROdrJVJejAS3zF%2F29U3sgJ3rRnErvFoRI34o%2BwU2G5CEACmPnNlqODmLY2dnbcGtqBrjjbJGzPHKAxoMntzNSCF5G9bG8M%2BrlgnIlHGkRF0Y86HEnQKmuRd3w7DSVJIt9ZnWZB1IZvUNpXqSpgVh4dFqDy7Igw02%2FjuZ9wFIfZiOIpweVU8YkaQtjk3WxU4tdCcrp8PGn%2FvZt4DfyTCl24DQBjqkASMhWaXDM0HV5mnQF15%2BT8CaS%2BP9yRTy%2BHBQNGZXbREgkdAyhLBB5S586FLm4gqUjmYArfHyNPchD8QsWsYCWf2Glzo4jH4MgR2L85tL%2BVeWMLoz%2BGo1GxNcqFNocWkyAptClQUDbR2JwRGBeMSDylq4RPitKcvc4FoZOFshqVJcaK41UfcDXq49XuM%2BoA2Iq%2FD2EG0G62vB5Sx9%2BGEU3eQF6CQl&X-Amz-Signature=8ef058c637aa3b1523a6f83103871fe145792b6bd59fb8ad2fa18fe55646d55d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
