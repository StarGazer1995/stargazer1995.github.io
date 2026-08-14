---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQSWXAPR%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T163850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIHXxYmLR7Wa6j898k%2BnSqNl7JWNF63z%2FNUdQHaVpX%2FA8AiBRI%2FOfZi9MRC9soDRqEa0uJ%2FnT09qKRot1sbNBii74%2Byr%2FAwgBEAAaDDYzNzQyMzE4MzgwNSIMCulJKPjyKEc381%2BvKtwDew2APtMXjKK2Ds%2FLr61ZSG4Yj2H2ZfQgHF7rYHIxVKaYyDn5J8cR26jptnOPtem%2BpabDvjhg66i7Yk%2BFVu2vB3IqS2R2NYC%2FyPtP6Ke9eF%2FvYXaG2GeGMbUeY5prUD0FW4mN2Q3KgS9dKYM1a3AGflQKbSZGz16MC6il4E95gG4CCneOBlhFUIMN73MMD7dX6aYpcqtTSKax6Q00tFkAt2zxqpfqCegLjRCXsoSzUnekb7238euSUoxNcv%2FrGxmTEZMIplLV4HTKanL18%2FdXyiX3lvyvwoEsQ0H8dgZkwMVegxn9iJowZYq8tX4xSQca5YPr8HVYUz4TlIqeeXmNUWSFIpUN7LDoaPwqXeDn3%2F9t7EDRr6jkp5Zo7Y0uMyZlddktuiKzxIS8SfgY%2Fxhs5jMhwIFngN%2FsCYFlIPb5rAd7Rs4ublGHoMIt31xFPFtNDrIL9QgConHvab3BDgbpNI05r%2B1u8FMEkvYZv1S5KEWViWhikT2XI5EwB5WEHE1SPu3H3S93BePI%2FZlH2bhTHnjVzDkDL8x9BU01OHz6rskh%2BhaWbGFhy8c%2F3RV7BPiDx3iVzv6N7LrildpWAs0qw0nDocJkszE%2FZR9Vp2soazMppI6%2FIAYc9Z%2BD3AEwnfj80wY6pgGhE7Ue7tBtmRq0mYjUsGtkOmlYSYE2sqCG8ITg4%2BBZfVt66gsFtBl%2FgLMktS80cuVo1L9QzXbZxkyAWWK0vcnEbwvi3Jurlh3fC98uobLQtmfSX2%2F6N0RXfkQcaiJ2KkHjpsaVz3mHP2A%2F3QjUlnIwpF0Zw7kYLDwY400vJ3EpPnTKHJnUVd7ezACAwD5PTbNhf5kDjZCp7E6rEqOdMwrrfM8HNH7K&X-Amz-Signature=176af10c6bcffc14bbf7f10968cf20a5d95a6bc9199a0eafc4c5e839217a9468&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
