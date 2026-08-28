---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2DXW2V4%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T132856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcW%2BfM8kNAZlJhB67DQXEaOW3gb8btlW3C4p8ZSUDJjAiBvC6mI0GYsqYpIBszqGQiquYCoEjx83SHtXjCvsIlXgyr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIMUKznvJD%2F9sntaM5VKtwDA5NW7Kc6f7RNWC4Wzc%2BKBQbpgQMn9tagRfYZp%2Fktung173fml8sFlFnFLnNWoFz1fstPQBvh1UauTztsxTNzNYj8cIeXOAp%2FOnPy3K3RaVyUnvDZt6JEhke2BRy6Ug1YWgB9wil%2Fwor8sfeNHCXNOAQxFwvhLIjLRaXpX4HG1xuLfnRbYTPI227hbB67Whgh3%2FqUBWz5OK1C8wMVjDJcbBpGXzp%2F1ga28sw6tbEbvo8iNPKJDSznkjp3UVArsvYE5voefVk24kaW9lIqsjdPEefMDq8EukBrZp7u%2B9cwfcJOTu%2BLdvY4EkesraTcaj4JAxKq0cD0ZbeCGHGClcb6AAddi0gdYOn1iLtUb0Y63gOX%2Bqiil6Nh3BTIoc8FHeyAf3oNP6LGudU%2FmOmyfBcpwxVuUqQgIUVtsNePdM0VUIa%2F3WoyIb2dmx3CzPaaMH1Usl3kYe5tRhTgwKkQTsOKYmfHf%2F5NHxnQOIhtcO0LPcjxViCMi9zLDywo78g8ONJpBDJ0nBT3CaOPBkRr2xu6Vp6OGKIjC%2FHn1LDwKXob6gBhczqekPSxU3S3FBa0RvZZ7aEYgaSkU0zRqcmngwTBdDfoCj8woE69AiCm1dg7DCnbgADpY%2BCZogbGkMswzO3F1AY6pgHNT0h50o33nk8uFG95mCzblcKSH%2BEccU0VF%2FMPQDhEAkiKumke0UytD%2B8XEPjiNIabWChhVokW5bn7pPp6VrnbEaeIlanKIgp7yER20YMPZItphM8K9tUKbFIq8ypXdPbc3vGiVMPzsJNy0mJKnrKKmjZlpdzJnDjSLtzZTCKa9HUo46Ow3k%2FNpZ9oUqydLiaOt%2BozojYnWgae5Te8S8GM3XVEPxWk&X-Amz-Signature=e14c1d6aa806a07e09688f02cdfacdec270f4dc1836a58b7b0ecf02505c5ebee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
