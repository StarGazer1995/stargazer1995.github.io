---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS6H5LRM%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T185910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsYQSXQHY0jRl93PhTcjZl0JMh%2BVHoL7Yx213Y5ss5wIgKqs0EWJVGZyA98fSEAcvsMm0mlmOezeWJphGaz4bkOkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDEVijiAj2R%2FSjAybkCrcA8wpU8M09EPFSpJFXtC0zBu6uBfZMayaygnDUq6WsgnXzjO%2F8ZPD4F40W9LjSMBynVHzswI76i8dwp7lbss0tANkXh78%2BkeVGouj1xg4nD1WIY73rbvrC9jv0tjbm7xNpiyrqmhPBUIgXRGJhTyU99vpK1ng%2Fm%2FDo21Vs9g0PNPi7cmDUMBBgaw1%2FmkBWhTQerfM%2FQpFEyBxfcF5KnuJZMMPC80gq4p5%2FlWlFRKUn8do5NiNHpeKPsU5a7CwVAFS1O%2B9TI%2FbKnPcNiBz97%2F4oRx9lnJ3Qtb3dfx4QBWsMjUh2Kz%2Bn54G5uglNBzNL0UWcfB722CBGKyONWUD1o0NAp8aUg%2Fh6FfqO695pOuEVAnst4vqPKTddWKJcRWc4crbMezoK%2FGAArYrf3pYcT0UuIQV%2BXQVJJOfBN%2Be3Yrh9ZIpWnIHrpHu8z%2F%2Faiwu%2FXLFps%2BWOcO5QKGRbLlLAGwFmC0MKAVD5ELEOoDtXNeXP9ey4t58JSy9YQAiqr9MzjleSFQXZYnY88xUGfCAWMq3HDTXq1goVATW9PoTWFEt7o3FMCa599YBCssjiwxnVDPvZRM6upRZE40MHvT%2Fg7zNJCgsnSMBqFH9vQwILTu6pVxRvy73N5LmMR9aPhrmMJSHzdAGOqUBAV7LC7j0%2BCw%2F4d8BZ6MvcE%2BIA%2BbhVLS%2FAhNKiIiwepq%2FRHHWraYDm2Rgsz3ufetQ%2Ftoq17RIG7TKj3IA%2FiHoQI%2BJN%2BWPpyWav9NG%2FEKvRtYNvL2gB852oHnRPT5f7DYa%2FHXZGUqlIDuoNza8sZo3U1Auc09kQw64qpbaZOMvDwSaaXRMuvJRR6SuDpHBgxe53iaYntOIi3N3HQF2UUvcln8EwPkO&X-Amz-Signature=89057227171ad3c84683e589a4a8288cb7ea01756b94e58e5215f1d1957c7db6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
