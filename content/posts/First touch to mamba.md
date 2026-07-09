---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPXA2WZN%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T013218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMlK9e3AQm8WY2JXkxbkfVRU7Rxu37ZBuu6bE9kR9bvgIhAN3bepfQkDTb%2FYEwA8xZ84bZRU6sqsX2AW5wbkaxoifgKogECJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVVhH4PjRuBozaMgEq3ANlm8Jtiaq%2BCcUazfPAh8%2FfTFgcpDD3Vd9lX7%2ButPgwG7gCc0haCwKgb6xTb9vVygS4jvuofFruK9F%2F0G%2FDJUlRELx6MNkUHnnV9lzM2IBlNItMQuDDov67L6JUZCf35QHAg3HPCtRrsVT3%2FKXjdcPTWDumPkRtCQS8TrzFI3Kd1mNoyrDfzyvuckBgrNHBqSVETujQYs4M%2FttH0aIO9ZMEpZf8Q66xpqDi6zogRPw9aDzKKDmNdbRWCaqQP6jotUEDdr7TD9BbHowQL6TCyLFI%2FKkVyu%2BAzKDNNy1gXA%2F1k99eo8630fKStJFcP2j6RTapjrdH4kJFSLTgYwyWIgBeb4JHpsVc%2BE%2FIWixIjYPpCQqIt0lduHF93sapPtr6XIohJkwSSUivU9mBm4i223HvcxX3xZOPDMAdg6CVmMzdJgB6KY%2Bp2js6vDZ4lpH%2BfU2POnlOANKseWXfb%2Boduc7y2qvh%2BH9ysOS9fvIvwRiadz%2Bmd9JyhAnDrP67nnMoQj7cgI86UbVJdz%2BcySHZIMelxFz2egkga5CtN58lEWz%2F0HXePeb6uF81Ip2i1XL026TyqhYYN%2Btagfvyx9cMDAvU3noum4YtF9lUrSCLkbgwEOULPegU95CDED29QTDIxLvSBjqkAVukLK9Eqn47MDqD0VbUAP0p8tnHimwGv7sX6%2Bzg6hrPI5%2BVCDZgJ9MuzD2r6%2Bm%2BB%2FA6W6ShOSF4loPUfKArIvNpVVvlMoDtSzpyICVOCXJdVTyW9gc96BcL1cCfjJL5N478xUA3%2BbPy%2F87e29LWr6nykl7DTrCvGD0PPMlDliGokhKmC4o%2FgXd0jnNKRCde%2BNIhR4MgCeltLjyg0KtfSAuaCW5U&X-Amz-Signature=3d0389a7e5885aecca3197ad6185e141e121de01aeaa382ec4ba36ffb45c91bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
