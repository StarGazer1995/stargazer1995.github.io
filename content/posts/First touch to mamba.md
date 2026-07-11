---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEU7BFK3%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T012321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAR1vs2rqrBIn7HxGCZvA31W47LLxhu9E20DCNsiS5m1AiEAu%2FUlK4%2FJRSqO9XiiqqSHyNAEbPULBB%2BlPSdu8TUWr6MqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD%2BgFKLvBsrDTUspKCrcAygCVoRjBUzHyQDCMudeu0zHtwcinomZ1MkGS0fxvO6XHdTTG4hFjDGpG18gQOdjlcC4Vl8uK4Z1GxrADOmKL6jH6O4z0yEOx%2FTze3q%2Bo1me1US9rZUq12%2F4YI8mc%2FOALqmYB9Ea%2BWvG8f1KYRud2ZceCIWvap6vZczc07FM10Ou4f4fRM63tqTvdYO3aJsa9kp7cirpA7kjOHUJvkJJ3U2BfOYG0%2B8E%2FURckJ8zeT0g06MJxjHdOp07wvRG8m3j%2FT0NrIKpPqF9fUUtyUnBuBV2biE80SGQ%2Fg1zCPkAPRKquKIlxSleCEv82Me9PeB50KTZfYnB2hOQdu6kfoTNatn4AKnRUBowKBEFRjMcwBALY0Oj5%2Fua84%2FwGK%2FzJRKFVA0I4PiyS5F7SLxhVh7FgQi4vZVOzTAicEytGUxWW8%2BKfGXJlTTktMrr9hzRmwj0f%2BaooIFA9XxZwyTt7rRBOav6Nkc%2BpD1qfOqcRKsoUqrhKjKjYcEickSycpneKBejgHVsoAY4hIQVaLVSkxYTZzMmSk0AeuKDivj%2B0hO3%2FhhEHjCuhtS4iiDqHA%2FH00Pp%2Bg1wE1Y2J%2FRSx%2BZg8Psj5rYA6CZOGZ%2B%2BjkIYB2s9zB6y73UcOsedKp5Qyag2MJfRxdIGOqUBoHiCwqB6kfdyoJ32uOK%2B%2F20XHBC%2FJY%2B91GNb%2FrMulgvk87fbPl8DnYGDcU79GBOtn3YC%2F48IDmw74foZ%2F3AQHGIphwuouu7mtp8ES1IV5HlSrPzK3cAN0yAMLk2QhhWm683BHYGu6eg8tR644dXH9wg8sCkrAINFl5PxPhBhMWsiSHyXRD2ho%2FrQ%2BEX8ZSNrqePFThyY07a6mSiayjoRn%2BpTuNFH&X-Amz-Signature=01e204768d129e3a7718981f8ea767f5edb88eb9f339aab1f8fe13272bc51145&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
