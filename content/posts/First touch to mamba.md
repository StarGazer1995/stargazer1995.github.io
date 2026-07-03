---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THHUAPSW%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T084600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCBdjQdsABnXb1VU2Um6iCgUKlHrmo%2BJ1cwJnX8EZ1X6wIhALra3DKAVe%2Fy0Ux8FNkPTtt0Ew3g4rtIu%2FNu3RWV4pucKv8DCAkQABoMNjM3NDIzMTgzODA1Igyl3h4HxTx8SlJIXJkq3AOerhrbJv1AhH7Id5u%2Fy6VxQHYYB3U8u%2FKyi2%2FshGq38xdSrdYOHZydxKtgHNHLL69XtSmZGEOamXHYSvdtFizkdQVhDjnb408JtNmov4TSE17Oj7iNeke3jKyZdJ7YizYYp9pevF7Zo5V%2BH3VxLMCF9IwgEypLh6JtxQqf%2FVil52i4sGH5tOdNHYMf1onDrdR3Jh3rMPNHn4fXfLhrywjrO%2FhZr4C%2F%2FjEPouxrwH7wIZG5e9t3am6rhmQJW1MijTb3w%2Brlfe%2BxqEKzsMzlKGaSbgdwmezwTkbg16qd5BSOBXK8O7FjHD0kWKfVuiqjfRH47wwqpRSNBiRGSy16og87%2BIgmfqKcZju%2F4HvHvF83FYdIALdl05tXqdZVN70oDWgip8Z2GI7RsISyd%2BcrWYuH%2FaYeWxnCk2EIfIQytTPnrqmhxYcR2gTRO7bfPoQPcpVxmZnT65Arbc2ceFkJUMVEjRv4MkhNIwTZZcs%2FrTgpwXalx37W5w24L8ffvxK%2F%2BAVN2G141VyerF2in%2FNeaAGdeJ05%2FZiW5AcSunDbk8NRbkkAxxR9qD3DtuIQMPxgrmXyweGSp1p%2F8YZlkAESIsLYtZ9H3VxBdKwDXt0rp1eQGx9eaVIIyf92J4tr3jCrzJ3SBjqkAfTz2QlzrDXuEMM5GQzA0kgi2f%2FvuIwaj9UgB7hp%2B1HuwZ4%2BF5vUbaMejLEeYlvMC0oIYdD708KBskdlmURPQ7txd%2Bi2B5cUkKxuRk2%2Ff92vbhAnvRorhEhxcXNosDpeYnEKEiwn6cRZc2baRGPEYy91T%2BNTDn5vA%2BSX3oGo11Iou68kpyrN%2Fnn%2BTIEwSTjuAtER0udlVpQO6brEdYrAjozJ%2F5vd&X-Amz-Signature=4d471dcd5f7c5a9dba9841465010204678f78e82e6964a2830d359fb952d9d52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
