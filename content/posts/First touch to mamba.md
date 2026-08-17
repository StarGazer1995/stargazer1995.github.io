---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAVLN6LP%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T161406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQC22GniqufwuaCnYvaW1Nr8waweax64YQER2KeauUYRdwIhAKnyo8%2FBFgo3NtB888Q8Io25pZ1TDn%2FZ4H5DCP3XJppvKv8DCEUQABoMNjM3NDIzMTgzODA1IgzUIXRpDZ%2F0rsALbxAq3AON2777giupESm%2BtNJwLzWKxZEfbtUzEOYj7mKN%2BWxNxdHeKy4dc9f9kMTRarZlBM03Ngqvpiv8FR9tadI%2FEsVzxXQgHfjIi4xSy4Z27mZ9ggWRVABRn1%2BaxljUOTUf%2FOZ5f3Otvl2uq1qCgzuSjfpsmapG6oi8BZ%2BTppjGQT%2BVq92NVS91y12U2Ta60sakvloM8tK6r9VhaCoCmyMKDKYmcOxKgHztUkPBgSDAlZyZte4ZB3BjTe%2BJsRMnPCcOlAFNZ1JILpslzoJOqrZnWvkE620QYOd8%2FRqKOK4WvqW7m%2Fvxkx8j7yLW4IhRj2Myo1x1RZxneWMlfhBNGWjsY5mNHdAZxlSZgXqJwj8qDHlkRoVuNJS3dd6GXhzlpDw%2B5i89YK257EigMMSYwRHxpN21zza1Ra88DX1s4TQxWAHylw2ryV00TjFQrg5NXPZf42jHQA%2FzcsPlG0g2zzIeFcgCu1tJuNbI2DB8qnChO3ukJlv3C6qNFsRHebI0%2BG8ym0k1syCAm3%2FI2%2BizIdxqRGyvg4ta95vTC8EPSugn8fGa55JKpYck3rvHsMpbYf8jlpbVvKpdhADWt2fkSL5ndpXa9LI%2FWN3OWTzeoXwe3GagSHL1KwARFAE9wCP%2BKjD59IvUBjqkAROKgGDW65B0LSxVEX21y%2BrQrYOV0cq%2FTe4v1IYLq8RNugr1RnaZrrgBhWrlFMZi7FaRe4g4CQ01h21FvnKaJiX9oWktmdt1OKM0G2eWsNm9CfITOJJtMODO9qEJngPXmWhLhVR2trfACcZyN1JyLM3jM4Z139Attm25vbYEirQg3isw4bak1WdfNzQaBhzsI3geh93ow5YxXGD6beqsjmCH5UgA&X-Amz-Signature=93a710d44f350e3de2046e13f19c0f80a1e1ec88e5fd57ea67f03a4f38d00223&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
