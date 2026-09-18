---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKAW3QND%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T172112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2B3R8%2Bj%2BwtSEtzUvuZJSjfQbISJPiDfQYRhHPxsg8xIAiAIBhYkst7sR7jxyX6DlPNvLm7UhP6xURB43dg1h61vnir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIM6OkwdVzNViimE0M2KtwDbkvwMa%2B3tNpZDq5D8hqBkUyFChFUISJezq4YdB1KD44bevJx%2BuZosiyfrrrl0EMzAJftZeK9rfC4GiZhjwooz89kUA5WVCNILSEWw8h0g6UoLnI%2Br1JrVP3bmE9bem7MkVSXNxGPyGaTeWM1CwlL3mnR5Tcnr2UaWVA%2BtLhkIG8uX8iXYgdqpSWUKwwQPnFhC7EK4BsV7b8ZE4nOL0aA0vYEn3gO%2FYj4NjyEXPBH%2BvkETs7RKQPRYyR9xvHmTMiaBaKIk4Yi%2BorrsiXmI3opydEcMLsotQi6Y6XRTBOBpIeD%2BZrVMNJd6MYrhYkS5xXkp%2B%2BiT8N1%2FzIt1ZKewWENn9tlmllsDsLUNjrVL%2B3JD1t2F0Lc9P1RLdkBzRC3JO4wVvpuoKSeFZoTLvVnBnoeBFVg%2Be1wJSU%2FqiEGfBtR%2Fgi3oGHyIsLsSRMda5rZ7t7sJ1%2Fuv4sAgCBvSaOoCaFZY%2FRN5l2bxlpIv94t%2BJXZEd%2ByRtfkEicqi5UBboKV9E%2BMdsLjXEF8BkzwZ7hiPn2Zu2fmi7Pgrx6l6ZIlL0skdT7T9F7lA8qa76BoLTmm7d2YCErOKUEjpQ26fkgS2%2FzWop%2F7cwhzxh9SNhcftjAE%2BaAbxfdjAYqfv5h99qMw%2BsC11QY6pgGXKuQzyTwBd%2F7vh2jkWRRMcTYS4ayh1%2B4s1fMAFkPBvoRiUH9XSLUUzKs078ZolHKdMJCmfI2p8P63LN9mvCm1lN57LDd1DYAPNYrOI%2BdwyB0QPZyURQ4P8SdI0TsNidGNu%2FoXc0NfYMavxaR0Xr%2F588Xx6oBYMu7WQUrd3be%2F3Y0qW0opCXMXB6yAQmZFfG7JHfwSOBmosnbYHtBJPXqW5qYT9dSv&X-Amz-Signature=0b6e9377e88363003cca3a8c830abfb25cff8a92e29d3e4f832ef9b222d3a6c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
