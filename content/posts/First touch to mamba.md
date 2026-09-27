---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2RVLRBM%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T145358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCDhN95C3Y5MijB8zgobiuHQQ5KGUAx5e1Jlve%2FjN%2FHxgIhAIOHBMP9%2FNnahuo%2Bw5Yw2TTtf0kUkpxoBLnTL6QSglx7Kv8DCB4QABoMNjM3NDIzMTgzODA1Igyge%2FYFTGe6WVmvviYq3APyIBma4qCbgEJjgKkC6QSiTutKA%2FjSmbAyXukgkIXKGI4NV691Mk1AqI9SOu8MdsR86xe2SduEX6yGRfewZzDNI9dckOIf3z1bIwk0R9ZoFl0vc4JC0lvohRLWTUZuYQWZY%2BeH08Y3EI8AryrdrS9Co%2Bv%2BloMPvpMFHKdYXHqQ2yT%2B16QEJ87qeBZpUqeIs7yl6c%2F4sUqHvkHA6RjPmhTG0h2xoSWodBe%2BMQviP9IMee%2FeayEDqqQED98kLV46iZaIFdH%2B6GJUezF70vQJA6wWoqMxg%2Bleg6E2srSBYLrtRVwtdUeGQjLYU60QqxTdxVIwdtjvjMPu7%2F%2BwlKl5agmDjUnsAiH%2B1UERhByP5g%2B5Zmq%2BzX9m75pcVkBOe9pHkIDweImLQqcL9rsZ6KrxsIw%2BNDKWw6c3u4Hcl%2BsJUOIyoHdYguooQ%2BIWix9qcFa2Tu%2FzdBZUkxYYASrQlWkoaEnsnzf8Vk4lSMxdUqorQSIx2SP9GE1A8bwy1Np0OQ%2B3MKsoXvmonvPrqyCRHUIq4eYAX0kInaENDNQN49FMMRPldeVASMm%2F3URkWbhJYqoKmjwNBfbuHb4JvxN%2FD3bAduwSZdnVP8kT8MO7m%2Flg%2BLTpy0F0wGSGbRLBEwsg9zCnqOTVBjqkARj1aeRr0TOG24iuCMW2Wgu8wqyR9MApO6ENu9OllnifmwUW931eIbY2Fjg5gA%2BG8fBKGnYkOuDMLwkBmusHnh%2Bp1zp2JVrBXSJBP%2Btto4J5JnxUmmIIx6KpaeR9tBOFom1P9kdUVA%2F531c197LqMMriipSHCp68O%2F7y4noVjZv3hUBb%2FUzDytF7dHAhooIafXPrEi3uImL2RdjG7GPQpBTh%2Fa8K&X-Amz-Signature=70ef17aeb28deb83da119b167621146d6f7cafc74c997ee014684510cae9257d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
