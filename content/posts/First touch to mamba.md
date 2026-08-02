---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDXM5KYT%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T204639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQDeUIP%2BsVv8apJrIvP%2Fa%2BwnYkQiLlOS%2BqCL6j8E%2FMf64wIhAJXjWm%2FH4cNA3PUH%2FBq83BW58N0d85uEJ4iHl6fXez6SKogECOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz54aa%2FrokCS7Ze%2BAwq3AN2WAJa%2BnFj7Xa7acre5LhL7fvvgG%2B5BN%2F%2FoCpqQf4SznupbpW1LWHoe%2BoelNwdfriHT0t%2Fd6MCdvxhygWX%2BoyiaFy9UDgm2jDvvY9zHzZIGPwWBmepCZhr601UjXelJGqkmwjHZ4A9r6n46Co2zVyEQ770oOYR3H%2BbRAUa%2Fb90PT27zUg%2FhfX4GiRkVnpzWFQtq8GP%2BwhJ%2B3sSmsdU%2FuhjrrLZY1Puycr3kAcrFpTl0%2F5mF1rONN10v%2BKo%2F30eKQpBB7M4ZuVkfhdS9umfHWZ%2BdAHsdMu%2F2qGafDPDzAHRb9T6hSyPasePcOYBd%2FoZuQVsr5pQfN1dY72uEQJEDgQIuMt1fl9jmy0BI04fyPbs2KJjITCDbMfYU7xQKHb42L%2F4JKGRftI0N8uacl8DG5HSJ67XukAyN7njBylMKcTLb3KupoyolOd2sG7H5vG61vN2hsRlYIdUK8Gf2uHkZLOxN%2BMSXGXqtRyMhTzWf7A9gJhdR0%2BUaSGZlFWjpLf6tO7mvLw%2Bn1rv7OfIFFaqEwYPMGzsQFvTHwL5Uj8oRIFrvrr%2BS1CsTEDAnF81crdIuqwNIgM2i3BGWPmewFC5zAAiDZGxcDrid0WwV0ZClYC7wEEbFtamQ7Lafhd3JzCW0L7TBjqkAfHy8nwW6B8j%2FggcwaTXcs0OCgo0E44gxciPAddv0sdP%2FW4m0Ajr%2FjVjgLSKTMarWQLKJGX1udbl5VcDpmBnRKtXFoHIrVMLZnALwihH2os4y%2F5r8btgTTq%2FRTjSPAxrM9LOWRP7Pi1ed0gpk9D%2FpVGMIvwRDyzVf9y4wPh43q7oFSjh4z0T4m7HeTRECXK0tsAoQcUMd3XCZQKxsnDo0xBF%2FF%2Bf&X-Amz-Signature=78b133a53431a3ef9b4b4efcea703321e3049ac86c0e99f02198a8cec85c5a4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
