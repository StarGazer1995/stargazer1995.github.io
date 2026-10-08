---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAYPAYRZ%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T080658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDjhMXnr1ZlwR5EmXNRZMTUBeZeOSb8sPIsBUuquTqgcwIhAPt%2BhYxv8H93bG0JvoIM43TAzdZLsjG9f%2BZWQKTsHCwTKv8DCCEQABoMNjM3NDIzMTgzODA1IgyuxVJgzxWceVuFbQsq3AOucbUPs368eEcS0mEFiwbJnUyjNm4dfkhpiZGSQRL37yNTq%2BEq4%2FIJyxyPkwNhM7pFiKR0HY8aHfpTi7ZqJ2EQQWuElA8olPgbcCyWMvd1V667AJnFE0PNav6usyOLZVrqBXsx7dMHhFMvqMUD5tbj3R9thCBXCMomW%2FoOeESf2sH7zF%2Bb2HM0huqFI4o1SckSiZSqEsCeshwKMmEozIQ%2FPRslo8TkwnQiIpdgHLZfaGOPaSRaGGqsxgGoEWqydx06VG4rb88cpPPu5fbn3kK74%2F7aVAjAYEnWuxLVagSkfrLi8dVJk5TofCCd7UntcqfqcBqphIHspnOWRRApNJ%2BS7vFPm28tqLkYypS%2BRJdJBUbGnR%2Bw%2BFUZxvlskDBFS8Yby1RGDSoKAXQ%2F4euqA%2FNUao9%2BgHs49ffCQBxOS9Vb5dK7fm31AsPqcb7p6BssJOT1szcNEUbejo65YqfZJBCbNb35XnozMIGAqsAIw6dVLlZZaReQLGY1kNGXN%2BB69qiTHRyL1TtUFcDYditARFMLrFV7uWhewVsLjSHixPVwPcgJvDNzwvKBJuDxjemTV58TTcY5jK%2B2Ezr6qZS2kQadviDG0E4PuJ1q2K0sYGtlB97QM80Moe3gPTKo4DCsmZ3WBjqkASfD4ZCyEhiD0xndauUr6FFdntQb8noJvxJJprvJsGjROcPm13o9HZ9bsa8KIIcJPuc5NucqsfikgyGLJC5xxGuEpVSktTctdRbZuxxo6MdrIWR32d5%2B09Md6gzyXiZVuQFPpM%2FeQsBCpJyBtB72RZQ9D7adzM3sr0abBQFCItwrEzFpxpHwORfiHeP9RK%2Bzkwc8oVUlRKxTBHpOGI%2BiVnpB5dSy&X-Amz-Signature=464df9d70154c1f242c7d2d1ee43d6165d0356a7e091303e567308d45b0f7ea2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
