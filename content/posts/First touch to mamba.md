---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YV6XYQ5T%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T114853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDq0RgWUrSIom1QGeykRpZ%2BWbHqamQGOrER3mgO5Ek7cwIhALJOgCP%2BaX8KFCqS44HTHcUusaJ8qEJwq8woisMYrRFOKv8DCCAQABoMNjM3NDIzMTgzODA1IgzQ4LvkarHesXz7%2FV0q3AMh%2FmzOP7JSEtwtdDbz8QJFnFzBriMvXm56BaF0OyvVr8IqeS1jIDHbYVvRgAX57hE0OvmPZsT31fnuqyu17y5bKn%2FScNdpoJS4V8DzLAmKLqB1q2kMeeJoPT91fBVg0vI754JUXWNznrq8xtqgZW5ehvbBs33eL7BoLBT%2FhUcxbbwChp8FZY5e5rZ55u1oOhMQbDSeI6Uj82RDNNZoJfz7bh%2B7vE2Txw1QU7SvDkPDpjq8pLEIXDFdV5oarGooSLgA4MvBAhRBud%2BXNgnVy9UHdWJ4MB8dk5g%2BOe3DzBWgsGhnpegV0dw7obpgCOPZOdM1%2B81v9rY7avNwoFKXBE3LCSoVgn7QsZPPDgh6MHALyiam0J4%2BUfiCKJWwquj0Jn2IKwPQvh4PCRYgCCHyFM9Cu980PpdzFkGyGXC8g1bDn1t8TqKvB1F4z6KbZ6iEYD9BPSBqkmqUm9uowCiZylGnwBGIQpWGxkGB6WW%2FiColweWqEECij6zYxeNqbAZcdK8ZQNxF4MDWJUJNbnrH7f%2F5KBgDSAj3wIo5XZKYW4jVGpPCq8XzLXPRHo3TSPKGJp7ewgs%2FzyR8cyMX6sc9UgzjEQewSQO4F2mLfGZO7D4y%2BVH3nEAfSZm12ci61TCsovTUBjqkAVpDBtX5Xc65lThj1yW%2BG1P7JpvoHSQdIlwWq%2B8XWU6caJHYTRFAYZTnIe4ZrdK9l2ydh%2FIWPn3ryEsxd4IdAp65DLmHCZrOIzWm2zkkqxNFc55xVmhGM3cwrmpeY30uDXLvcKwsnhDGw7NVI9h%2Fc%2BgZR4KFqd7c4nH9vC6YEgMJ2gTsJUrXK3PzMJ7N23SqGp11x8FJeJsbsaHu7kNdsQh6yvyt&X-Amz-Signature=b6ae06eecb6328be1e66002987e7bf6fd78a887dcff65f33aa06b10a23b9bd37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
