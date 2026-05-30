---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7AVPJES%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T054100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDVH8Oj9meLgYm3%2BSD3V3boj860v2F3EXOo8POtQV1BwwIgN3FQ4r4PoPpmowB9o1BFIsK9LdVA2p9IK8bLdg4F6WoqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDUX7mryA7Wx0FkuxyrcAyV26cN1RXOIEMG1JXILFq3Rdeebeg4sFA%2B1ISMvnltWwvSFyB78BbHFX1C3AZffW1dv8QHDYZUovn%2FzANW737haCwzlJSKMKMb9HAT1JhlbcuZBbjSaEtX59g91GJmGfA6ih04LrrexQZ7pFAq92lGTYlV43iF%2FekJMPweXzZgW2v4mDzx4NwyHRiNrNWxH36w3RhtsuwGPivZQcKjmGQGKof%2B%2B%2F3u34n%2FoIF%2BlI5gYE9X1qc0a%2BMGuOI8VnI4WGKf5dVAuBK%2FExpK01clbCkuuKvvkwNy5k%2FrwhXhOfolrqv8S8Qi9qDY9zFM5wdRXX3QJE%2Bw%2BA9vsJ2BXOmvmCxFUAlFM%2BgDMdNQo8bNCxk6ok1QV%2FNW6%2FHttPzRC1AH11gfAWruSM4g7R5ElHt%2B5blDcEnFukVik7hsYiQ6voL8A4wZ68Lw%2BTUAHJTkNVbjASINzNLTfs0jiHmGX5lIPVk4uVTgXwJxz563%2FjukEbLs72nsG%2FIJnSPkiOLvJDCgWmPfDhdNPihmWm7xV8%2BnvpCzgO901GATpvcSKoTu3ULy3YMmHJX4edXheMvfKQ2lzclP4Ch5gwBqTHaMbr7NyZtmjezL96RJD%2BydoN4jR7j2gVjZr8bfd%2B0wL6ceCMMDV6dAGOqUBspTGEZWMFLbK1IBQkoPtjkkU%2BG1znO%2F5%2FNpYIX1z1Rniy9LWLWVmwWGccfAHL6z5CecqzfxbE1by25MAwLB4LkED2e5edMesOhWojdy3oNVJM0YGQZQQfdzV6ii3KImd47856PYt1QbLgbxMUHr0hgbqWo0ol1J8DykkmdX5J4y6ectDL392iYwmNLo6MVorrd70CqEb07dKhxBG21Zh1ZTG4jh0&X-Amz-Signature=bfb8700b2e59864008bb339246307bd0889b8328292659667b6df98e32f3b274&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
