---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STJZ4264%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T204250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD7Mpdjtle00xLyi2WI2VTU9ya9B9Ucy9cW8O0GxRTqggIhAMruRKtfFik8pDKluDxM4rAJOK3dqNw3tSdhoi1BWY0sKv8DCCwQABoMNjM3NDIzMTgzODA1Igx1eKZDitbu2SawdgIq3ANmFx8AOctJm602wCkzl6q9Ch2Hv5pqZV1M2xpfsNEbZmB8FGm6KimIZN5WFUn6UBV5aL25mOy6fO3kkkvI3ClC6IOIgc9epQGWt5X757qbm0SLVarw%2BqWEi0aaCkhWguE1KkueooXn%2BsrAOwz4I4zG8V0rVYJg0uGH5Xr%2FvS9x%2BQYYbE0Ps8Gy7KuVQ7ZMomm9OvOCStX0M53iwkPb3A2YUp9RrZrvNKFCNuxvsOUrCL5HW%2F9KwSBG4SENrtxPqyiLMFtm3h7OFHT8pzMUhg0b%2FZnqlsjQRzoFPTIFpz7asprTq4t1QBirtWQmUqyZ9g68LPluEpjTYcBApHxtrCeAKmgACbciykaZzIKgFT7uwRwJahJuoQ%2BctnE%2FEiIAfHobLkpqyXfC1mmG08O7zv%2BmwA3J2%2B433FsSiDc5k%2Fw%2BA7OATmliKJW6rDWFEmBXlPu0CqOgdBX8HWV9W000AUtF9ouGAZv6Ycfl90%2Fcfn7ZOJFrZz0%2BVJQ3IYKfOehF%2F8gupKYN0BcpEBDx%2FVnIgjOIWVQHdVWSVgpAvySORpCHH%2F5uUnp5vbD9KYfrzdVULycK8nqlOYNo%2Bf02gAgZz24sp5x8QBj4QghPdg0JWilY79R4O6%2FUrFdNDsk58DDesaXSBjqkAU%2B3Q3MvQvIEbaS8ijP1gyTkHOe%2FzT6Ako9SmkVxafDRMcp0M%2Bd81Kx6Gf%2FlcVwlrdbgoagNDutb7uq0M%2BwcE7VDg%2BcTN98V0Mo%2BGq%2FA5OQlj%2BH9FP7RHo3BVFDRJGo7S8kS5MNs77WfCrWHmKLx%2FhCUbagAqLdAPFUxEOcsTJawSu1F1R%2BQlLX2b8F0uLK%2F6DsNOcyyhjkTnYi9y9PmF%2F4EgIuf&X-Amz-Signature=dd5e2265dcd4ea7a79d61a4ac728e77b1922c143daaad28823cf5e2ac3f6d9cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
