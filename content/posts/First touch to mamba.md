---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653NUS76Y%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T200801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpdGOGVeJeX6wHtjmqIR4tGNHs1D7cxgfSfr%2B41TGNUQIgZAd%2FUq3a89tf2pOz%2FMcyl1UgIa75ufTI0KT8r2a6GsgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEMhYHZoqgsgRXGQAircA7YRWnkTKk2stiRWrZDuSMDE3usFCxPYuhazlLcAGwPrYb6Aafvg0jm9njxJNdRsu7kiCQRmfpfj%2FM9OOTRsgT%2FTdZoy9E9WL3%2B%2FDiF%2BkCMsv7kzakMyUiPyM27qm84rmX2q8ndBv5RUQhcocD0EKhWApgDTmZxeuyxI3%2BPXGXLmxhfNNBjzBkt%2F2V00C005%2BQpyFMIqbZNSmc4uPtgiNbH8HiXShN9myacuIxuMhg2Xz%2FUNlG3ldv%2Fgm8Er4LQazHoX8uStBrsow3tUY7O77r%2FXSK5BxDTb1V7Oqfmu0ht6az0%2Fx%2BQP6qUHfhdDcIoBZVefqt%2FzHUUtYAT3kvSsXL54w8EQS4vYIfPkuuuAiN1RBSJE1fjWbl7enWd0qZlH5%2FbED9%2FkC8K5vZ%2BsSEboKbQvqm%2FDKOfeLQRJmCVGg2wRM5u9T%2FhuVBsk2yItraCNPI43nZAafgqszmjvLiLGteBsdarWRm%2FMUhbKATKQBkswShaDEM%2FNj%2FT0%2Ba4smM1ykfrNDgSbkWNyf1WL2EeBz6iWkyVLup8y8T1804gI5XBsXmzsWTk6B58TAmc6X5pPLYOTuWkjwfnFVo9icXwWabc82clrpyhbQi6YccI5I40yhFviJhwxRN72pzEDMJ%2BC0dEGOqUBnRH%2FGVWH2bbRv0dkIKQHkc1XjpqbmfN7460whhKA0zoPYj0xEwxCGKcAja3R0N0uodS4s6LCb7BO9PaJR%2F99r6ylV%2BGv42qru4vqoEMf%2BY1RZgorA3Ts83946rMcfay%2BaSOaHNdHKL413goiW6HZqDL6mwDibISmUPAZUIPYR0hSK3MUJG4YXMxY7NO45aQ1yE2QozLm3aldUP%2FRY%2BWq6JKgwWDb&X-Amz-Signature=d407c28bb1c0d5e2ba0db0d31c20f74e453f7f91605ef1d4e34fccd90d9c2ba9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
