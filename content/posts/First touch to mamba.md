---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOEM6OJT%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T073048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAr1q9qaeoH2j7C0%2FhwkFdU4S2PyQ%2B2A6nS1ydVXlJSDAiB%2BMKvO4eL6f5GWUJKGu2iiRZVTuBqCCNeBmRITWeYPliqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0IE1t8scspUVNmwgKtwD2YVu%2BOvuCgYGdZTMJ50bNoeJiAF7jVU%2F1EnR7Ig2aRpnsL6xTs1i2wn0IH908D62%2BkujBNGxybhkPlk8vsLDoVmooF9j64S5rnz3IjI%2F1iXrg%2F2KpYoAYqVFbSu1%2FpM4Ks7dAMGQQdh3WSknlP9eDHZODtzk7WehBd4Eh9OWXrUNqyAyqZ1qdJ7enns13JqaDKZld46RbGO%2BxBTgjAxHfqvJZW2ORqvdgWmAUxH7W62mmrhNsw6EtRJ1xvajWfURQ91NXy4ouZ%2B2aHMyDUpzucWDsY2P4VFKoBSz5zZl1dBhnbMfZyMcB9D43L91asq2PXUQ9wwwll0ie%2BWPaRTmL%2Fg4sKD6aAgOpuCPZk2qLtupDi7cjpzYYEX%2BxH%2FPkY5%2FCIAY2dfmcq3BdI5afFIVCunXBFAWOTRHth5dcDYGpwhn6jTGCH3HB6WWl3JVGWjjQay2yyNJHv4KGVwd6uEQrbpeoFXL39I%2F3o58Cp54GCwAK5S9t5jaQVSzryxFqmC3j0R5q0Rye551I70k78tyalOoqLEyR1Cr6OYa0ckyDB6nz9U%2FZbTTCm1S5Wm12cKbAyVRFx6lkLxgEgiKgbXz%2F6AlEFrAWy0JbOiHt8jGrQJpgz7XKEBlz5qUYX8w87%2FH0gY6pgG%2F2rB%2BoV9AWeFTfjY2CjKxAH%2BNWV5u5mf7ov9AujbOm4PI8LiGAE3XFGmc7AmQDSzkjsjzXWiwSDtxIfKi8bBzuJQh1ihtbAX4XQIp%2FlDat3Z%2B9rcOcYCpaqT6P2wmBeTWH8uEq63UYdww6%2BITjxR1u8%2BnU7rW8iXRZaOTYfKFBdkKPtdplm41jD92%2FcFWQHYtGDJIFKjhFHzP9o4I3GO9n8jQgnWv&X-Amz-Signature=8bc1b88ebe263529997762165e6b6485239d1be2bb163ce728e523e4f04251ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
