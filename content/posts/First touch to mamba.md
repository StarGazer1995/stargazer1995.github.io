---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZ3H27L2%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T083458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDKDEEL3JL0hJ3%2BX%2F7JYfIFyEpMY6EZu40mS4Z2Hp8v8gIhAKKRo4ed48Q3IUP%2FfsHFEllNB3J5e%2BUZhmwkAmtEH659KogECOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyD0%2FnlhwIDWiVSR0Uq3AN%2FV%2F68schxn%2BfbJgAz%2FkgoY4tQbEdc65Z%2Bxx3QB34hx2C1ElqO5ce%2BN2hK9BWF%2BbdcDwv00mGbIHRV832n8VbaKTJi5ox1%2BVgyO1LF1zq3lhKBAUbPQ%2B2OSAnE4jCCzhYInUJK5EkD2PBTm5n8EEhGfFcKPm32RKeqNnglhayX7wIMNkzsqXUrXQBRYeMP3U%2F%2F4sJFj1YY%2Bl9Yak97zU0uZOoqj6rXWGoY7yfXMHv1QzGGP2T%2B91gXOzUssP%2FD3aahbT%2Fia3VEC89Y8qj1xXk7bi2sony3138nZyugxdP2MAdSBz1WXvj1eggV9AwU%2BzzH7IT6O1n%2FhPUWRhBMkfYxKksZZOeV0k0sQsKKXcwJPfW0pByeA1KO3JPWU9J82XKNrYdXi1SXb%2FEszvBMy0u68%2FbyE%2F8ZYKrhejRvIe6Q0v1kAWbHo9iT5vY2qsfEOhTavRfblG1EM4%2FUwAJIuIEV%2F8jDgj%2FtqT0DzivRVl6T0lHmrokUSb3qGreFYZzFMTnX%2B1Rq1jc1f2XRdKSfXbV0yD4kbMqgXRWRv%2FwGmRn%2B%2BEmgp1lMVkHWY0Jf2Ubp4AhNqTtbMj6RDw2x6X3Izni1bvjEjwG8amdgdNJAtWDO%2Ftbpa1uKTVro1jr8EzDC5K%2FUBjqkAemor6P7HSsBe%2FxSaSPVARP3Xv1tG3ZT9HBOP5%2FGAuwv%2BtiV9RLuNIcbfVRQKJqc3n7xawnp8i0Sq3Bvyz5PxYb0pUS7rqw1yX%2BWcDHp0v09ioay3176FvE%2B8f%2F6Wu07FiLcSnIL53ARbFqzh40iy5O4NvrICz3e%2BlFabv%2FPBdEe6SWuN%2Fn7aixtyDFCeJyRjOYctLnnn7MieDoy%2BFBb9AeK%2B%2BrE&X-Amz-Signature=444db1da44d41c59126530bbd403cc07c7ff57ad7e7dd7837cf217c1096508bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
