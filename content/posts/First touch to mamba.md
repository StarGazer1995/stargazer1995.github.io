---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5V4KJ7O%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T230305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQC6gxocIRdXYzydWVWjZwZF22OIXpzTApbOHCmLo5UqYwIgDjzMtEfn1mejb2YhGMY1jXgggzWBnpBwLtuyD85598EqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH63uEAgphxt8EeC3yrcA3KAWnwakOtXru4NNbI%2BO7bunT%2BzgUcSvWK%2FzsyPm7WJuJ0G0Hq7tL6GM9R2jSxHSP%2FaB1sMBEbghh2mVyeX6ykMe5jibJTAmFmV45uwjqxvDhrD60HnNweUA52FBiGsOUq43OEXO%2B1OFKu8Ypj%2BkdM39qTPnL9wGxVukFUHYAlJNtqYtnIWlQJER23YIt82M0gmsCflm5voqF%2FDMGfKY07e9uEqr8zIkPwEHgK6%2FrW5S7N9C%2FgCkJ%2FU%2B8e4XXpYCL0f5wLEAZtJZhJvDPFxjdVK%2FLDIcNJpl7vYu536f8gW1u%2BCcwvf5C5NoD%2Fj37CM44NojmDJ3ZQM0ZSTxMVvgvVj14nS5ZrCiGKomv2HY%2BkSwOrhpI83Pw9i3YKCznKQR2KbjBwntOJxD2iIxHaCRmVI7l7Y0IZs7%2FRSr8T8iaQJ6Q2QbPcCgJMmUOejRZUyOlHoDHkaM4LJzqtYVRxIW7VbkHyax5DJrJQRffOV%2Bggg7ytuPhvT%2FRSZk%2FHHpZYq8eex075DnAuAV%2F29QRt4WSWbs1fUEE31gOjKqyfQxJgKJ9lV48ryrjcZ9ygaz2uz9k1pqrbjpYsc1jLyWc9S9G4T1ytbrQMdgBDNetl1pmBkHa3OtXRBU7Ay2OYdMMHmkNIGOqUBlYanWGsZ%2BiSNQfmcR2eVtpysi1jrfKI3%2BE19leGX85uAf1O5wJAVGaqVjbHo8gvKIKKlXkj%2F%2FE9a78RRW3l4ZaAl%2BSdvu6O9gs9I%2F2pLDNSD%2Fkpl%2BqqvcVIwp4NeXaypCTuo08c3rFboXNomdeSUTPz3NUaldZLcwqTeDK00pjbgiqFFZ7rtltqOpuiI978ZIC1S6zRBH89VXanrIQCE9brUExX4&X-Amz-Signature=6c6fd6548108ddff2021ab929c7d4522a07c13f6f6d32b20434dfaecf2572dcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
