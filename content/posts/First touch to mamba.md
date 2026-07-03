---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTLOILHF%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T014629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQC%2BeItBRDcdpPSM3yYZFmfeWIfFaBMGayNzYnr51PhKcAIhAJoYfGXFQNu0RP4xWkOxCtjutoKQyekvmwsPQ0CcEum%2BKv8DCAAQABoMNjM3NDIzMTgzODA1Igy5G5MY9OeOfzq%2Bmm4q3AOi%2F33%2FxbZx3dRigZdbx9CCS5GiH1%2F6JQvvdevHYUQ%2FyGL%2FzfHXxVmMaZ5WvdX7Vaui5tnAzIU88Z8Lfy%2FnCJ8prpKW12Tl%2FMlvRofUZ2xR4U4MmVY01ErI4tIcc%2BPUl6Y%2BwIeIHyZf1KtnXT0zx5swt5QRnhVX20Jdm4DclGjvR7FcG1L%2FVt956x8RAWBki5xqhHO4Yg7Xi0%2BNrEWozVQUaaC%2BbANgxBWH%2BxoMOfdvJnR5E0phRl8ojNealxkwi9yvAUE8oEvKW%2FQkXEPLnSXuMVglGG9EexBXPvtvi%2FfFX%2BT%2FU3rLDUzLHfToWlb79nkgCaadISgZ%2F22RYfXF4NNoRnXNPKcbhxMCQeWLVLtX1l8g9yqDsdfVs8f%2B61SGvv17j1MfRgX10slHyv%2Bq9eeOgXpOF1piTYUwEfqaRZXnfmuy71Y1k1bf02AZZzjwKoXj4ElW3%2FXvklKrM1RVj0KDBCtCRkwlfUMZIsOsQPJlufoajdMZqhWK2YkvSHY98cz%2F3cl6SVsj6zjfXY1%2BRgYKH%2BD1wl88OY9UzLukZvKJvxtAdazYqEQCqbmHxNSY5%2FvP1aUl6AF2DUh18zJXdHujgzGavSudqq2D3lje8fOojO2pt%2B01Ftzc8uEHQzCj1JvSBjqkAToV3aTMv5o7BQq2y8bXdyF4H1jC%2Fqhj4h%2Fc7aJfyJ%2FmHspcUM4qn%2F5NzpOr2Dg4IV4xpZU0FVLH2fbvt9487C9Nh2ev3EhjuZd9NwzggeNbfk1o49oTJjKrxGgMRXl9JtEwJbNaQaodgd%2FwIs1%2FvZ1re9n%2BSVsduxuFdug%2Fa4GeMgrngyt2DBdkekrGRJ%2BaTpvBE9Y%2FNJODB1b489HX9TG%2BoDdd&X-Amz-Signature=761227d51cbb211b10377635600046d2695ab188660821799f2fa5e467459aff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
