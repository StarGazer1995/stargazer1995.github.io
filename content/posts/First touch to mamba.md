---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKBOXIEH%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T202336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB6IX%2FZGsJfIghC0Ijv%2B5MH6Z9SuXd6sDXuKHuWXjOsEAiEA8pXHKeHuHOm8hDdlr9QRFfve0hk3PZcZl2biFHB392Mq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDEsAM1yQ4Y1uLVZyTircA%2BWys3fw0LZWmcFu3XjA0MqOF%2BvdJU0Px%2BvK4B4wQf3kgY7zwJSNqCfvR8YaTR4jiGBfpX4goqYC2zGpBdwqLM6OMwpSyVVK85D9Wi4U4zDffSbgnZs8qMMyLZhfmKJsHu%2F0kRDYab35t1j%2FIIFiB3IFI9sQ41G6NaRwD32rJKUqlHTQMUj0PfTJwN0UuiOthlCIPZ0IpF%2FkiWGFKoTjafBvpYqs4LbchctD1rDAObohSaRFltmCa1ei4D53ViJaQo884Znedy%2F52WYrgcuVfsK2J01Qubyh5if%2FSqsAwsyAtYQ3Iufb3i0%2FALcBLbobFnjlw2HJLVbRajS%2B%2FIGjvBiG%2BIG5ncMbvBgGhAtvvb2P%2BFzfnIZcS0eNl7gSnqYnwY%2B375QjdkBcVMtPFsQRSfe0Imaf67RTg4cSDCuOrF9b8%2B1iVAPCivJ5PLmoZmPCVWoUzYYV49%2BkYMtFH%2Bz3UWrqPjuOAt8VAQzZCxJf2teP71u0aOlcOBtk%2FSIgvKzwQhvR4npSU0bzsuZoyiQUFs%2Bc%2B4g%2BjsMcHaSNlIeUxUzIqagDm163tX49CxFi3v2FDu0akva0nf3GXq7nfQhqp%2BHosv6N3K2k5FI3aWD6ZmMCU9Op0T7El3MulUouMMra9dUGOqUBtAzLggy1IO%2FCafTG8KJNOJqdW3AMyAXfH0pzL8x12e7lJ6KD5vhSuFTd5iVFWSzNW55SKJ7wuUPNjPZy%2BkJ1MiT8SWI1lBkZl%2BHToqzxo3dtflmyWMmABxxzrUDgv7hu4ywnTDeQRIlbIZNcSPYagYvqKZcpnWyGlQDzJBW%2Bpc5IdlaJ8UQ0vGpt3eXhcG2OBYupxAD%2Bh6IIaCfHfnDcoccDz0zJ&X-Amz-Signature=d4a8e339670dd4cab6cba1a1513daa9d0203bd8e418b1afe6bea6f9514e49d64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
