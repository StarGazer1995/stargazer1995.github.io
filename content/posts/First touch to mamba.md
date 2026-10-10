---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY4TD77W%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T012544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDwuLFmbbzSaXVWFq7qzosZtAhlMjZGyVbmbY9b4ZoyMAiA22A8S74WUCyO4ciyt3Lbxps8knGRATLR0%2F4Otyb%2BHYCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM%2FOU%2FlHEWFncKYqgpKtwD5UCXeZ1NNVV89ORRqLFQzwbmoULBcJvxUUfDB4XW%2F295ikvxpHsQHbm48FdOqzSuCDlYHEFFGTsCgfU6byziTAN8WKKWYiFgV%2FTfS0xkGQCv1SpZdJxhvVkzS5p3rT4iYT%2FYTWA3IbtnYzTBdNBukTXEwxLxnPIwUJtwIz4LX%2FhQ3GKk7KkovtkDQGibxWjM3mJqDAPTyXN2HcRw%2By4q3YzhVtGhWgEwwtXhAk1REsQVDpySbvtpfUfuOvOXWmdGhaaLD8Xv7N43sQooWN%2FJxg%2FrK0v9%2FB1%2BeN%2FCkZG7%2F7mRZhyrkMDEPIYpXr8OGBXTHra2KiepamNwdIrt4tS4OQElM2kUHCy6bCknxM69FvU7H8Kx0bYeKsFcmr043Iwzorqe58sGIUSAc%2BrUqsB6vbWRKidDsdenabo4S8%2FREL1XzuaaXLSwV91JxQALm%2BY0BmIsF11vCMqFl4fdu1cBna0URLnStVEQ0GYfMZ%2BBVKa%2Fcl4osILMA6j%2FYkZVvYDiYdWR%2BQOnGqqJyJj76s1AW%2B8s5fqHgedb0UZrCUXsvVNTPryAxvV6ysHnDBmTqaAm2u4BR%2BLsoIt9pyGaT4Z5%2FCzxPTUK1Tdj7MBI4LPr6gNA%2FflHA0%2Fv5fxnpxcw%2F6am1gY6pgGkxIJgyCl%2FuoA8ysj5mW0%2BGsvBVC8fZpFAMWYWKDlO8jFMVyc4pAkyFCxvkgw0ek4Uh4oJUYKlId9sUCJo0n7Ddmef2h2D1CzHB31qGWjMaUvbGE%2BglR7by1wav5jjDPmxtH1HW6dM%2FHki7Zs%2BpF%2FPof2E4N4CnGJfpgaOrSwA4I%2BhPqp5gT2z1Hjnlk3%2FJPtKaqBe6T7cEsYSoLWEPYZtfLW2fIOr&X-Amz-Signature=bb678be887fa227b5a90462c1b7a6f52a7fcc746376cf24bede07f8faee5dad3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
