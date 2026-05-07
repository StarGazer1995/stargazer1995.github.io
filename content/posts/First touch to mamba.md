---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4LLKJ5V%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T132616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU%2FgJTlP7qAN2ClCRpHsI2eGiRzpjL07hv2q2p3jQj0QIgCR%2Fjz82UOEmt%2Bq39nbmUWgvFFsqUHme1AIWzdE1LNLMqiAQItv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFipd6c%2F6GFPY1CCSrcA5hZds8wzMw2xEb%2FIwt14tRbvGja7Z%2FnK9U1N32A%2B3kmvtx0FrqdV%2Bi4oVITgqMcUPE5KsuidYPsbQcwU7Z0XKcRqtT29WKqrWnG0AyXZ%2Be4z29HQwRvZ9FrnjzL4ypaj6QOdhyuMfxsZpycfNAd4%2BOjnfnvPgrW%2FgOAhiVdLFVTcspjSW59AqtIWB1LLBnZi9lrBBHzfVDmh96ebheHteefrTK9IQ4KJOoX9rSpL4UwPoMIKxedwK0ipF5ps0NPaYYO%2BvJ951SEuQPj4jQ10LypiWrJD45fhyy9Gv5rTWxbYtAABV%2F0xR%2BVg7PItzKJf7EnYFFQAHSmBjwbLVoydAn8%2BFH2pGDP7ENhpmOajpiCvO8N8YMPzgoQWkd97BV0whEfqj1p18VV7FOKIBOxQG4RZjdCLPqGpb1Gq8Xh%2FlRx8vk1KLr8OKt1i8%2FiSEubAjHnvXTBS%2FuDBtduOT97TxqvyMOqSmO%2F93eHfIvskitfxqZ5WV8%2FDMipQcSzXBOpuDoxrxt%2BWwYSrhh4z9lfCXw3VqykS6Ym4x1RcJcFYKTjqXVJZzy3MU4oprXHwNz0LisNVoVea3TQfchAPBjGr3XN%2Bv2mawKM4roqG3o%2B8D7Gsj3lK7qzhc3%2F%2BVi0MMCd8s8GOqUBvGz4IDzBdB7NS0PD7KoCwchZY%2BTlOs5ntNJA%2BCMAtSo2lUKdPmQ4qgxccs2ogHlnvMKUYRW0tlSEj3aV7OB3BCgD7KPqDYJhdwl4RfpT8L4SpuiVRQYvQWPN8OtyAzyx6%2BhYJ1Mb57%2BK4klgMq5mqRJhzt1PWi4jvIlCaSJEREby6OZEXmNu1f4yhRg6ABXRo%2B6Jnwt906nXuskuuxhrKbjo%2BzaW&X-Amz-Signature=3a61b87be19ad7aad079b87c7e9f4aede95f25287bcd08af9a6e7515bf7f4949&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
