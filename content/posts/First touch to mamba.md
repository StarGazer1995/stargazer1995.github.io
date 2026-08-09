---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W6SRJWY%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T142400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZti68%2Br6VlJSDbDdSJ%2FrCBZ6FW6tfiQvuc2auAroIYAIhAIg8sC7K8o0LN6GtuEO%2FuEvRYDpRKnwzR9wH6Z3jofN9KogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2F7PkLxvdpV4Wlcxkq3AP8wlaTu6OFinZJ9Ap%2B9%2Fw%2BFIaq7kYzRQ90xkAj1GXQIV1tFKBd2zmvjBGvwElzvOU7EUkN4MmAT8Mq81SKtd5ahJBbNgoqLeQxnt2iNxv2LoBtGDlufoFCQtJegWS1t1j71ykLhrOcCb8L0DSs7OUY9WS8r0%2B%2FQhYlnIew%2F1Hh7mhHDYPbGvlcsgnDVnFKnx6S%2FTOdNUPO5XnDJubKGJ83hwj4xGwc6NchmG7UIDhsnfzNOL1AKj53Q0wdB8Fd0YujO%2BfTNCeYMYS99yEQcTjfwVGt%2Fv%2B6aJESZiQbVrM9YPHI55SANWPiTdns2lDfTqegoehFmxk2rAikWp3J3vmUFRtd%2FM1RfoGADixgPIIVdzHLIJ7G81r9Cqo79lKZuFxivMd3D0BdI8hWwxjc5RKfhq%2FT6NyA0i40iCpt9%2FXrh0j5C1uMcsXZ6Gm5%2F9pFvIWBlMNVMQN%2FEuW9X6XwQ7bN0WlMHkB%2FT2vDAXeFU%2BJ1GMXu5d6aJw14CZvBbLbIcRDYo4on%2FsOkotg8rHgeIWu5miwaNVnvxbal78AekaL25ORTlPg3PFmS2CLc2us27W1HKBpMCUsm3gtbyxM7k%2FHcbjAeX90fgCh57dAM2PCJya07YnXumDo0eDaz5jDDouHTBjqkAeTNjQrejd3LxZFHqCmJzM2KjFpOmiOZkHJvW%2F%2Ff7nNfEr7tCGSoD9htIs6ESiA6Z%2Fm7WY3lqXBuMMVeszSmMCllIQ4LqV9f5udExhAjKfaIqOvrAIkf6T7hdeUNx2Y5Q3HHJbpDm%2BxUt8cwjN8ABNyM%2FlPgAp3TAIJBJjMtx7a09VrlGVRda0xX92JA0jAR%2FeEEjYiIx5%2B7x2aKkBhU8voSjAO6&X-Amz-Signature=3978bf28f20432fd8f76c7248912db1876c0785f60929999c48f00c6e6c59cf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
