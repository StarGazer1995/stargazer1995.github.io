---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XY2BLUZK%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T012856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDK7%2Fx1hDJGAejpxFrQaF1oPRzt7Isx39jXhrlFgDFK8wIhAKtCYUvUI9qKuKCD4tKKXMC%2FPWYGu8%2FOmM4LQn7oKS2AKv8DCCoQABoMNjM3NDIzMTgzODA1IgwDtt3BOo1dBR5A5FQq3ANucVH%2F1HBqLt9Lojk9OqjMgSZdXQomAbQuJ0uFvQaxTBLPrA53Dfpta%2BugcuobXkvdP3Bn0kwDDpkSW6Hb9rKCPVh7oYWOh99fzm%2F5%2FJokd7JteZ5azHg0olyHVH6%2F9Nsl1aurGoCjznubbAsbHb%2BjZPM%2BOHPcQ9FibpS045t8KK%2B6QOAdfgyCpde5MfA0KrMdOAKivFpCx6LQzWHBFXgKmoUnct9prAQLFRLn4zIBSjpgSUJu00laqVgZ53TdJor6%2Fp%2BfabxNuM9qitvGcxSlvhEdQX33jwVDjPOcg53%2F%2F1t1YDIaqClDPtsuDeeBWaZ3ls2pPVqy3SbRYJHSqKyKb6agYGOwB1nEhX%2B4UT7rWGk4Ds%2FkVolOTsTqNbNFVjPTajBT%2BHqFUDc2%2FwUNEl29PXFpk4oe77y6bVk4mqFha82yoQwPBCiTHuZ4KMOGS%2BIsQNtBwI6bXTfGtdagoO4TKrjXwkpuze7W751c8tlxibGm96MgnxqWwqgj08Q4vLc5WBWUvoqOPwSPh705f7VqVmajvIQgRmVPHxZErYUABYuX0rDcsIyCcfB%2FwzSPgzlmTklyIUbgTRQoIupcTLbYBu6Y2cgv65SbjyNPZPNXflz53qbb5muaOfkw6zDKqZXTBjqkAfN9SDMY14fjUqBfJ8xWLNv7LHKf%2BNUmVIVKfOg3TUItTP0x5Z9wactYRXLnUmfDlUW0Dc2LsHC3kj3V0YbsorfXGCigbuDxnIME0FizmEIiwNw5rxA6tKYoZPnXhhTgTFU42DKvnQaih6uSTRIrbxCPyIGwRjpIbLjQ153gWHW9cazAC8H4w1e1HyfFNZA3KdnNxSznc56dv6MBWrUGofh2vBy9&X-Amz-Signature=f944030db39e387b3cf311ba1b9d545cff2c03c391c07196a16abed62ea346ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
