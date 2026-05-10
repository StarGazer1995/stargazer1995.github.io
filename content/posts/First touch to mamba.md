---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BZ4HXML%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T092120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIDKtiVq7zbZ8mwsGmFV3i6rlD0g2qlL2JvZCfu6t9QjLAiAgT0nNZds99quB5G9TFjReALgcLwkTzy6FT6ozqJkQiSqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcb0XELt7NP3bMqFhKtwDFp7FAui2uo1qTmr%2Fz9Jjtc8vOm3h4p%2FBe31X4S27Nfn4zwoP6yLHXRQBmLd91Xd0zGQ5b6tjpylp0QKmCGM1EeTy27eOH%2F105XSF3vHwnPL%2FFjidcNhRGkLFIN%2BHvyf7Lp8yQpoQP0NdmuD0S33MEQECbPhiMbheTqEB6%2FaHYWWFGAbcrtcnSzD5SPuV0WK63MK2zMvgxklBNIG0liyj11O%2BqhsXNdLulWzzaS4invjQTVBAxX5EHVLQAMl0GPfdWjLaF5bD647jTPIO%2FrxfIy1%2BEFxtuyn4E6dzuXJmhJM0Bs2J7I3mOdwqQgUx0VMpiLM09YKAjxBtJu1KEWEeNIkcXBbzSdoHwUZh3eyHKfb3yfBemDWiL4FnISq%2BBImt%2BeZse5WJG8Zj0MtOIbtjqH5FsRHaNfPKc8ehCIYd6RzSiAyivyLLgSKcOG4aV79T%2FUq%2B2l%2BFt3qs5rDHt1oK0Ytv0UF4V5d467Lk0AVRglkhOr2QpnuwcAd8uLw7cy0zOR0WBeoQPIpxR3wK9XiitoR8%2BnJh%2Fef1TQR9gf%2FBF9al8eLPqelAJKTf283BOKR8wrvgNQ%2BQGAccCOReFtyxeX%2B0EEOQ3D4Dte5S%2FUW4EHfIeZujqF1a2VqN9NEwt5CB0AY6pgEqAzTa%2Bw4rRV6BiQroS6wiIkg02UAkLeYa9TgQXB1ZK0ze5azt8VOL0mUry%2B0mEWUxM0i2SlYtRikyASDmmgeSmooeq6myalfWQ6LMYoRckmxshukCsR8Um6yp7ldC32flN%2FdoIifvdTf0b34VuW6u9t8Jdp6tYKNDPJEqPLuZnLLXpv1K4m1RHxQRqDnalRZpnMGHuPDIwWr%2F5sJ56xa4kRHeaKA9&X-Amz-Signature=04b2cf8a8b322ed2693716013f57af9048a75ecd97276fcffe95baeda8ce8d34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
