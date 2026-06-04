---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZAWY2XV%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T123802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvao54brZ6BqczF5SmIUI7%2FGA3PkUDQrtlYmue87GpTgIhAMD4WMfvJpaJN2reAZ6U8f%2Bx4WfuM4CW%2FZIvyrqCDPKLKv8DCFUQABoMNjM3NDIzMTgzODA1IgyGHpSoqAw5%2B6vHemQq3AOg2Wg2rTfKGLZQIvBKPHD0zKgoLC9WeXEtSPJk9FF5h1j8oeWesND%2FA3xoCaAstX0uFa%2Bi64qJzV2q1dWsjM%2FeXHFmgbVFrnCUItKF1mB7XkXcGuZEO8bGJ1evt%2F0GKRYtf7Ht9E2fQbGchN53ALsW9ezokhu39HCRYctEen0MRasxx4L6WyuEFDLzBGy2FvtdZ5ztz2nqeNvQiXUh%2BJpN99nTiGO7azSjsDGsQe5AgqcKoNYcH33W2XbkcrNx%2FiIc7Bhsia%2B3N2gG3GQ1kjxyGLVUJU5poqT4uyYcQa6YKZtpEppk52FLtenxU26G4RrWxVrUBGg%2BiAWd11HwT7kfxlec73t3VGQr2lWQtM7WNgPAC2QUPw%2BpfdLhIikyMr2RS8viU7JuTfh5TiUH3%2FyiJy3rZ4J1lB4qHHIhzZ%2BmWKipmvrG%2Fv01Uj22xz5RB6NKCEikcMtaX7UFxNWXxtQFmcdEeijNpYmEv8LYvPIw8hw5AxakaL11sQm309TRgFA5z59cLKqYEEnTNXdC%2BiCjTE5yoVtRgd8tZGOna6RneWmBLi30Ra885VmH%2Bc%2FOMi1xcX%2BrjUBJ2CSOb0cx%2Bf05njUY99OXtl5E1sjXdJbC5vh8SmyPpAzbcU9RnzDC1oXRBjqkATe8T96cxWHThoKlR%2FIhZ%2FqpOjiipN%2BuCMHBIJnQPlDa5iAw%2Fd%2BwM%2FrTc8N6HKAzs6B%2FrcPydd45t698yGTYk7fpfIlrKfh2pMHGCxPMOJjW3DBL4sqAHpj1XLa9ipUYM3N%2FdFtxeWtm61GG0cmv6T9OAM4CtJ6FuEm0qCR5OVn77S6jHvRq9eYpQ4REMwDP%2BJg9dS2VEpbs1YfB6UIuGJXGT4i3&X-Amz-Signature=6a149087c57a36177c85e69676514e871ded790e316dac2b955297100f58c39b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
