---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O3R4ANO%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T213014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQDX7CEzfNZnTmXGZ85jqOoeyPBfAW8%2F5dI1mPfNwD0OuQIgLVNu4NCPpJMNvH2FkRIIKGHcGnRQK5WjETN7kCotU%2BoqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBdQlp9zP0ND3AZZSrcA7X%2FYZ2VeL7RW2QEpUs%2BppntgoIanflzZduBte6ee2fnL0ISVMSauZfltQ0ghPhCW3yAl3BJPtGBtS%2F6j0xdsp6YFqTAUZu6R5UHkIRoWxp%2Fbd%2FAujpMgVLGGmpJOxTkUlWK79MOdgOwKBDSDhYRT%2BGUj5VlDWH43z%2FoKU36u8wFQeiv6ekYGkSGewv1if2%2BPOZXG6uPoxvLoCm9Pyz8lt10d1Bbxh1fx3HeLUiBbNnvGQJU%2BeLrcaGXXHRkDaB0HjcHwPedpPrrLu30akYdt%2FQbVvY8BnIQ66mh5NsFOFoaLrX5vlWr8AyGoNRyoxgv9DVcpaUNYmXNogk2eSHJcabbSB73hN6jgEK%2FnAcItnDqimhn1%2FWsNkaXOtKi0aaAU1ffY0A6JoUaayx31aAvl5TvNJw7RL5tQHcScTXX%2FclVTin4ibr%2BeRTwPx7V1NH26Cdcx6mSzS8TjFc5a%2BjMdpu0q9AVb8QA1f2VmiqnTyBPA9LAe0QutD9gDxMK0%2F41p570Y1x%2B4YR3x3icbUSm%2BE4cydyh3OYR4YQRULrjQSbOPSQKS9%2BfiFySl6%2FicJE2JShWaAu0XgY14Glxv%2FNHrnSDZu7ae3akRM7%2BwThhOJE4pBgdBRYyVJhMLuXEMLjNuNAGOqUBWA0Fm0YhjFlTSzDNX9udWnCYao0uLYkWDg9LQ3U1aft%2FK7ltrj9R6fPEamIsOoo3pk%2Fg5B6CBSqsESa5jQcTVolJE3yrNeNp6Bc3KMRJuVaF%2FA%2Fe0Q7IGwQkorC3UWsSFtDuopMAu8x6duJ2vjcN9Js7T6R8mV7edjsGYSsfyC2UVwW6CyqJyF40htm3rcQJXPSsZGtG0M5RepNK3N0ECz0jM5v2&X-Amz-Signature=773c5f40bc40c808726b5130e719ba5896fcd521974925a7d06371d951b6bc47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
