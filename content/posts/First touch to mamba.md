---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663NQBG5S%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T212302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbP%2BLB2OMj29ez%2Flcz2KB9Z9fK2qy%2F4rIoCbsars35gwIgDJN%2FSEbOVTOQOlMBcdOTixlkRR1ivyKrymv7OuAIMEEq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDDOVtxzrEah2r3JUqSrcA0y1A8jcddWbJAfTL9jepsaeUpmjocKHrpj8RsTjJ%2FN1F884%2FXHyJHD4vtxFKVpzyYl2dwEs%2BNRq8mxJHBSF7KjVa2nSjmdweJZIagjBHUST8HRqLaUxyavQrlwUA5T%2F%2ByKfrmjfMpOqwhqMV0nKq5kE7YaQaSsscMNUrBHoguVItsO7HL7VBilM6TB6OotmiIyzy15uhGn4qCrKX8IJ%2FKNYKUNxYYXPQyhE4IRlLPe1AT0cnUeQcbF4ltCNzO0tWOP%2BM2AW%2BTrb7mcjcV3MgsQ8rSQVoztJtJD3uaLKuNJI2Q2PVSOlG1thTHX%2BNdgDFetu%2FrGDdjHi8majEhe5DGcGuV0br1P1nuT4T6oI0xGSr5C5pn%2Bdf9PJiUxbIhQ049eFZ%2BKx8EgCBtbqxD%2BE4CRVacbCoyov2INb%2FY8kziG%2BIGvssqJNB08WPZ7fcsL9QjXHU7UOOC4RosXJXvO3u2NlYWtMIHtUYpj5iEAIwTESEwjhImRD0okOVJUXv43%2FrLwm27%2Bt7GZ17PPNWkD%2FaKfbPYHH9ecfuedN%2FU98WxIWpE8GgaoUjQeARmQ28Q%2FeaKHGLVuwZ5HD53iBZg4WimvtUzHffx5dqQHGFBPRUBz%2B3mo8Z1ygPK5IW%2B8JMLGvh9EGOqUBk%2F7Rjt2tuMN%2FunZl6ctEMI30pxUX2lQ3n8xP6UhhHnVm%2FBsDS%2FIgteR2I8LvgilK7Bygp3VBS%2FWhewW3DktJxDOmERSczCtybykNKcDxAihWOeSkJwVL7EDCvACC3HcSMnUpgoFnf%2FJULiNX3fP0lOYnuLR72ryKiD7SG2FKSgT5mjlaLzBHkxIr8yJPnM1sLoS6rI1ULTGRMOZiH9yCElkZdRwP&X-Amz-Signature=8e1e80ca2deaeadfe61e1a6a09b9e8cd500620c5453ece97a548ae3fe05b4e81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
