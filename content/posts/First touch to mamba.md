---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMYB2S2V%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T191614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCvKt9IpWa6Z0qxJM3ijuNpGTwdINrmAMT%2BsTbH8sVLmAIhAKh%2BtQgt0nI5VLsP3%2BQUOiedjXmXJF6GZsA%2FViJXc%2BUCKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwI4aptG7aT363vraUq3AMYMsfZ9LoO7wBBWBVEGfC6Et16PWwBQxdetoPzFGBPLEKEt8RStxVp7hcWfXwRl9roDC1KKnLlyNikL6tM4nPzOpwuW3UTLrZ7BLl73fCkEfEyrebFFL%2BpXd2WcCBh%2Bz2Az4QHED%2B0HgPhgXV3Fs%2BvJy2vIaEtl7Tgcugam7V0n%2B1iGIiwgYH%2BWVcM9L%2BO9c%2FUqwpoqmH78qp31lZYGa4EgcFiPNZceqqJt9Y%2Bi%2BeTh11yoAvCreSrC89IG9xl7VE6O8M3LKjdZTDMueu9HjHWwTkZnvl%2BTp%2BIsyULzCzYF%2F9lMOwB7UTpim14br7%2BPhxRaxXquw9BXnrNWOS5Sp%2F0dlhz2t3HaDLn%2FCj0vqz7devXnOb91IkJWQ%2FEFESWORssp9fALEAiNyc%2FVqOS2V1LjwjgGHdg1jZCWIeXOpYEteeCPz6ww5ikv2KAHQdxVRI6v%2FKjUhqSlenv4NnZjRW9MA%2B7Yiu6DOBYH3CWstjMWo1oQ1oG6sg31gMMBdlR5iGEJZaOeOXmz4tlJ57aL5Z%2B40WFJp0MM3x8%2B%2F%2F3dlFPMSEKyc2ckx7%2F%2BEpwBFxXxNEVyg0pSq3TWBhK80fXa78igfgkteq2d5W8dtpw%2FCOWHBvJJGlmOLm03hG59TDIycPTBjqkAdjWuPxoD%2FNXC4YNLiu5pZHgMLXKJSVh%2BbnzVf39WivZGM3yeb0VH%2F8bpeSgppnjJwQBx3fUq1uuUze1aCx0lonGYmSbHme%2FnOYnI8JUjGHyCcXsWBbnY16CSi1ixqukPYO09KXTR6ESbsCwmkZ0%2FIFkdjQAQt9qQ0%2BS6rFzZf4uZQxTN7ImXI5ORiovSwjuk9HEunYIdUGX6PjGkbkVe2ZzuCiv&X-Amz-Signature=9d1f82f79463486d066a9ef62bb0de1dd76afb15e89f2aa3378c453afe306c68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
