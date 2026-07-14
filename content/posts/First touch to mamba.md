---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFFXLTUE%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T170110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIGMeWylM%2B1SanNP1a1W5vEoYlXUMWDZDxhOHulmSg8wRAiEA%2B8uE2KyaQYke7UtU9I%2FvGTQguAHIHoL5a5jLdCxAxuoq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDNycFf4WoB4RXy7YkCrcA5us9Di1ELo6P3EGY%2F6WXKrLO%2FD9Rh2dEkGbhL8fzF4mfV8zmcNIJc2LICWERbUkRBPuxcEbCtwEHI5Y%2FFgq56a3cmb3Lx3W5ieeca8EwO9Ly00z%2F%2F4f931%2FUjQr1Ictk6u%2F742JLWEyhxkxK4VsqMB89ejawUX14gmTHMU9qQrR9p7sUO5fQf2FoftzOQ9rBI0NlJ8ehZRV7nBpjb3tOtd0RsziIo%2Ba0Xy6rOrY5Q126xys%2BGLtfxAH0yqGRNf9boVd1dt0gCMKLd45esO4dFKRmU2fEWF4j%2BqeNPzZshZwmF5n%2BKSVseMloyqKWESYa%2FXaYLxoHJdUYxlM9%2FGu4zXAwx0bTXNhqHuNWKgM72dyTgxwJN4g9gCbgGSWzb5RLZHOrDfnY6jeUXyGbwyyhGERe5FhF7TdBVF%2Bms4Ag3v3R2QsfD2UeWo976FFZG6GIfYOsDwf7HsEiZGi3cEGlkoINEp%2BrnyP3Anv28RHn4%2FRl8X3w%2BuiqG6vOYz735cp%2BrfEqwpSUh3MEmwlk3C832rSmaZjKflpGjvCJooE%2BfwM19%2FP0UNvLV2aJ8JxIm%2BpsWtJXo7hJfkFFjeMyfBOz1DgBuLUydOYiGh49TS2mDFWoAdqv9sMOBliYaGBMMu02dIGOqUB1KdWELACpuv5o19aZ2R6ToF0cfTnMJ9C4DztdvD3yeGEeh0QtQBNVYqg4oPJOSTif7PvDzYhoIVJJi%2BPuvJPOauKECr93csYTrusjO3xxrC3VHUsXEWvJvKeaX7TSUKTAiRZooWWQtyjfVSrO2n8waumkWSK6%2FHKNPZ7XrEg9evR0XdPbUroIWa3XbhbgIFMRZwxxoPTgGdEYMYFbO4NNZe1HZee&X-Amz-Signature=8f1a8f992e07a50d85013f159f215a1ea21e366bf482395e7bb2149b6a38ac8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
