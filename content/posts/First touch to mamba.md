---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBC4WGT4%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T081051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICdJZJNm1ArwSpy52a7tda0%2BWx%2BZEipOHw8ewpRwbsIcAiAU3Ws0FoH%2F7aOiGpOVnWqeFqB7KZRzt1DfYhPNLdz4JSr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMZL3X7KLfllBPaWmBKtwD3VMlBAJd8UVCdfPSfRZhGUwAlkQq8D9%2BLhdaRKh5muqeB3l5p51D0phwWxD7rH%2FYKo2%2FYERGuxZP9sFY907fBR4yhW5GbuUf2VO3FNocQpw7UJKfrApGE1ECkxmYMvvrhMNY%2FNz%2FLWvnbdIuN6emWdxPEWT4ZnUDm7yTkAV2L5Ch43%2FpFKFlSolwl98ov6nU8xRyBpsTjP9mqa972RAcY74HtpzcGxZtcuvLsuhLH4qGloDTHzcl24Y%2FDHyNMnsA0nl8QLsjRwpFPidLEp0RA7MH%2Bgs1JShC3azFoJEe9DApFUhAKpIg5iRx0HXWk4Oi7MtQJTCIOzYJ5hSEbPMWKb6sXrGTfegBJf9wabeZeCGe11zK6L8TBgLz69UhnFpxTlXjNFAgeXkuKu3VsmoBEKZgCrFeN2oFkGtM0ms%2FzA9%2FQDH6BiuYrHFjcj4CsOuVdegTUzflXC7zFrmsde5Busxbs1SctAy8Z8OHjI%2B4bcjM6SqrcS%2BSQ6V3kwVVHadHwYIcWR0HLutvo3uWFtTdpU5zMoFRiaLc0sGeMffgezgzm5g62HApm9SYCJbm9GmDbSmR3i%2FOduhmUM2q0lcLe2u0yzTYFFrMCSTViY7zJQz0K8gNlX66Y4mN1Mkw6u3P0AY6pgFarA%2FNN5aSq28aUmeQEernvUOsgAN2CW6SPLwLYjXnPMin0tBjmySPOw%2FGYKDzxH9F9sbB2iT%2FWXdJO%2FoZnKE6rkeSHkshPhcXpHwm5CCZcFRfehPE3urGDsuR5HOJZf94hMpj0%2FYm7garUZbOA1TtUC%2Fz1PGPINV65%2F4wF%2FoAFGeRGnPWFDRzEOITdOgFaQzW1gjmukH%2FbGXDjKrcsU9uqDcZgfRL&X-Amz-Signature=fc65954544ca5d8859cbb3fefaeaf33a3458d6176aec5be4cf8ff7ad08bfda9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
