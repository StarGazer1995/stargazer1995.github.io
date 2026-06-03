---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I6GO56Q%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T194207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQC0HjwnXwNmjOfDgaED2Nnp80zBXP%2BquiWsovJh4ommHgIhAOjIU8C7DU%2FuitLCFiAR1a1m6W5GuqFXkDVX5V%2FKrJZaKv8DCEUQABoMNjM3NDIzMTgzODA1IgzqL5SBpS9nC%2FCbvsAq3APSiv1%2B9FG8WfIkQwyDzDgCywKGHYFYy5srGDI4SKKSfWZK6qqKqsGUjuWvbra203gNmyKU6d3I0jXSxluU9dQ%2FSV9GeyD3Yba58pV0Ymwt%2BPyWV%2BIfmrxfHqMHlCwpiq74YXF8nLgERoemgTbnQJH8RD0kEQuwyTGF1BHu2YYGVLo8q7Vem8tkTczrhfddmT8HraGkMoWvTjPI4EP7w%2FX9K4Yi1QjpUZLvh4i%2B5cLIPnBkXd3b3qXDem95Wo%2F7B38DYpyIt01WO4RztjU4lkRqHnY%2BVLVQs5IzMlC%2BgiG2WD7TP4JmJDsP0m8Z0gO9NkqWzBAtF%2Bz8T51wIlGMSPIa%2BL%2FJFrwnaZUtI6M3C1M9GGl%2BSW0XkoUXEbc4KxjAFG%2FIEAddG6Zyt9MqwgrYCgwm4P2%2BIPEA08TN9CJvID6kAI6O6QevNSFcih9GrRXDxHB%2Fc2P0A8u7zSJjt%2B2H0B9ItDHDK2p0CY143tYBIpzaF%2FUwXQZ1xcgmh67%2FZ5yuzSAzVWoSe%2B2CMe60iTUCZsQ7XytxfiCjKdPCKAeaqCC3CCZppqCFzM%2BeszZCZD33L2semF6CYrzPGsmgrxlUlaemKbO5XHbPeaFvIG0hqTnGbAck%2BiThQPUMDqX%2FlTCq%2F4HRBjqkAfmF%2FtO0vQxqdCxa3jyD0s6btJUDrQwVP066b7WEAl1UyoHrE4IoCFKk1Xi3n6GmJAusM0siar1Qptj4kdGs2sIcqUJuXFQGHeG6xxa0Ho4IEe0qmyHQV5fssPs3aiMvNWBC1UsvpCWuZz3qN1tz%2FbJGYUDYON8sLpgMZ2%2FuJXMrD2bx08w0We8Vvpewj7KG34UtOkcGzWOubBXzMqHI8XI%2B2Yx9&X-Amz-Signature=b287a89f4e826f1aa687993eb2fd63b15b010a2d0257d24358152ce67f14ebc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
