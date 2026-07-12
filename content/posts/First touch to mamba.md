---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKA63PWF%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T012519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIAgR%2FMJPxLAgQSRjzVg2NlWDvsRngQDY%2Fl55wUwFSWApAiEA2zqzy0C1KcqvNrrnlwhwjTJQHqT2BJ%2FM%2Br4gKn3D9j8qiAQI2f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2GKq%2FlJWxOL0tSjircA%2BHd%2FPUsk%2FWZYgRLHvPwPAcnC5enB9WVDu226MY1pG4hXHBNSjfsHqfI%2BKHZ848LTZrvfwVgvMv4gfb7fzIVeSh5K0jtG6VV2w%2F7Fxt6S4Uk2VQ0N8dSd4qd7BqIX%2FMG1hZr0onYaehxOf36isL6hmi%2BOKsAUMtt0LJQSVZvyIh9LRTNkTxGbEGiEf8pv8qMVTT8zF2ckJVq7FeRkA%2FoJyN%2FL5B1Us2PErGMvloj%2F2uCYz18lIC6PIt6Eihu97R3xD9lhakUhZnmZM3PjLDklwMU5pxfY0diwIBhn423%2FKXPyaccs%2BmBVnwA1AJHKby5CE6WAx5Ge1rFc4bVSapBQnNyZdAgk1FlOz1Isb%2BMBx0NJITHDmOLPfVk%2F8HUyU0FYHFXd02fsRhhOBCtJ%2B3bJdA0ak3ARP974SApFiMty66jsdvK9WEcRCp957G0wIVut5ic0mYR5H5dZCVub53crfQpDITcbjm7a2dWIPrEnsgWZFegNtbX2iFvPEhsYhdOLG4h0owhcdoNB9gtiNaac2IK%2FYO0KZ1CLdL4S92galyPdEoprMciY5XdH8j7uEYtnP2FTWc8rdDxd%2FCaWRxB%2FMwW9qVkd0oVbZbnmntj3zQigxxJyo9zc2JLqWkVMPO0y9IGOqUBzJHlQAfj%2FS7eVPGdIV%2F7hI2YFqnT5ApHZHb75AKQLmceWS0gZOlsoKsjj4Ng%2BGhs%2Flro6rjnZMcv8Q%2FN9LkiPs2VL8h2ULG5LxZPBLcebTnMas3NJ7YHpxPggE4L%2BQ1aSnb02Dl6VCSkYQVPIaECoOPqwTtvUuo9B2K0%2B2BOfunh4giCPO%2Fy8HVo14fuOUW7sK%2FL%2FrCe6M%2FOUypb%2FmOOtXTT5Sxg&X-Amz-Signature=3f7fddad6efa1c1a4ad0d0aef673bec9c55d7bd3733d0d23edf6b97dd4df46d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
