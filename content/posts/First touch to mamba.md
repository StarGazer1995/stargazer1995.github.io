---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RLWE2SK%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T102732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDBhzkLopyX%2FquWe0frqCHEqYe1GEcqE3Xn8ojgjsYWagIgexpVGr721%2BNCWkA%2FEkaWcxA9UEc4EJ0cpFbgErfOhJ8qiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLk76lTYpfuEgfz1YCrcA5XvE%2FbXnNh3606oAYM%2BYKvLc6NlJD5tI%2BPVW9alrV5tDOe3v2E7pHO6QZOuZHn5PoY4nJiH%2F5zIQfqF%2FE%2FfE9E%2FWlataxsKmo77rF83wREYh%2FQ1s41u8o%2B5Vyg1MO8yx1SqPs6nBvou%2F7Voipk84buPf4KExZdwiyGS8rGaMB9Dwj9Y85ruB%2BuFFlcFg94LUG3i4sGP6o6%2BONhP7RL7O3vVMmkIbnDK2aztnJB3Qrvm5nlXdfQilQiSEBCMh6Ee0WHPPE5EeHan0ELkSpGvZwa6G1v7U1URY2e%2BJFSn5zk%2Fpfl0iPY1fG3u4qm7vOtd7L408R%2BCFJxm3%2BgDnQaG5633lULmGPWtVF1y2GdYhe3pO7DuAOahH8tvDSzP%2BG%2BRxY%2FSgKGe3FlEMTXd8L0kq6ubzq9h1Tb%2B3r0pjT1Lw8%2FB1fBywHSPyAULGkbLdicjAnTiKdljU27BprtQmOF6wQKXrgJRboEdpk%2BDpXzqi4OjqpzPquGOFc%2BXQ9o4%2BciK5qHkpV6ggAU%2F8dq9T3XZQsdQ1niEJcMOMcWe8TsGvNXXT2HTeQliFdMQXkT847Mpjtc4vGhezh%2BkSEBBC5xtVRwCGxaYNg86QtdpHQrBEgwYampF3tPShVPjVIgNMLvWmNIGOqUBwHCgoFIvqTV5oZThlV8Iz9ByCLHWZQq7xziCUw7QK9VlyK2puEPr%2FfuWy5eznmGNx6Uk1SSEF5Z1odXm4xxAZBo2S6k1jMB5ifYMGjLQSQvtlyt%2F3DV4W30b7FACE4eUIpQxf3A7X454MLxQHngVJPAVNWNyVy5Q9i%2Fa%2BzKF43ljnERf%2Bkx0cS6xBnnZTfN9THxCFFwnQDQwSdaHkYsLVgNQnyRP&X-Amz-Signature=7118fc541fd6adbae9df5339a4b702a559bb70f98d0d1557ac88cdd72cda6cbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
