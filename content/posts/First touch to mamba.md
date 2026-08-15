---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJSC7UH%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T181218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIGFxZwyqCTuHWb5zmr62nTeMBs%2B34LiZ5HTkdjN6PYM4AiAwmBlgdKwDR3OFpYOgPLTFu0FvvdYGe8QpX2Z1tUQiWCr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMQmQGxwamtkrA8XzzKtwDA9AuyA8i3jHg4ktxY9e5HzUkDfsVazrmSZAw%2BTgnfc58BCHpTkwEMz2toSqHXdkAUjbSrDQLg4Dk%2FixxnFQDNOtpjfa3soAULM8vK1qkoI0Mkc95%2BZHGvqVYtQ3xm0fkH8aYLa9tSVe5o7hGkRHeHvX3dLMrGAo0qtkhXkjwGXJP1JToX5dikDpm6VLKrybKAN0b896lFccYijBtd2SUf0vJEMoF%2F2q7HiSSCAIllwg1MgSdnbeC%2Fhj63y4ypwRfiYyE5nUSOtvNJBg%2FTc8GvChIQkT1y5Oiw%2FJZ65frJvIDpOizEfTlTTM56kjLb9qxH%2B78Fkr%2BAJkmB%2BOB5YXD7tFzPus2jwxiEhwgkDTJpwwIScYq%2Bqmje5E1ncXSqMxblgKNuJoeOCtkCTJ5yIie9qW40rHnkOoP6FRdUmI0qpJkMm%2FM3lDvEN0VbiswGfBzCDZO0z36MyySGiZfAaU4T589Wf7uCg92yex7pAx%2FOkBodp27jbvTxchSm0xcAaF0x7jtXUBTzYLL%2BroSwQYyMyZzm80IvULGy5n23ubkwZ9vO3aOq0nF3GNu%2FjAjBBkhcdQ1kc7o5TIdg8bCDcKvN8uIFef%2Bj4QMSJrIku%2BJGV688o1vUGutSij9g10w0ceC1AY6pgHO92077of8uVmyPySNhKSxmk8QtlpU1wYqg1%2BgQFHnrZDDiSyVJomJ%2FBdZYnd5ayYhSxbNtioO4xRCVyVr59f4VEofbwHZd8rICul2yr8vIfJTGqDyFfOKAB%2BxZYC8OZG1rq357rVdpMm9GA3UYV99t25svY%2BQUyPLkS9ZjiivT%2BndvKV2%2Bn0vCC%2FxpyWAldursQwxA8Xm7I9LvTtUdrpfi09fNm%2Fa&X-Amz-Signature=efd9e23d7a12dd37377ef435a352c532ea80f8570e56d7fff49f6f0cd502f6d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
