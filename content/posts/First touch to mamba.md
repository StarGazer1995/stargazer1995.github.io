---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMGZNVGO%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T144737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDTSbMN0Brb%2BefiE%2F5KTejVSy%2FRZLpihlxDJwrwIIshOAiEA1y0%2B12cXzTmPqliaPhJrW2XU4Cn3v4t305fJfPAmhI0qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ1t5qhltKKSxn%2BkWyrcA93itSXrQp0Unx39fpNDndMC5qMKLj12Ru8wizdUt%2BWXjalbygfnBMqEDHqXz2hTbWkWPZi9vZCAS1uA85rHCdsAL8EGGWCJJDNp9Kz%2Fh0ss2wbZVIx%2Bnk92ie6hDIel6YOCP6hD7nw8ygxCFJuKm%2F4yQiUq%2F7sGsYyewiKb9E9niikDMpL3TjI7STm1y3S%2FtULmJLI4jOYfgdhvCQul5wDSaMXtJGnlu8nogFYm56Rjeh%2F58GNaLGoafFLDM%2FRNV10xZuF9ft104JtVg7z1IWp63SCy7H40f7mzERBUnwMp0zIvuFaA5Dyh47p9dTs1oI21mEZDYTJqUGrq0lTl2N%2B0t7vUCGSi1A43hb0ZOyFHIZSUwNnHiX1irGEFRE70CpmgI26X4bwWEBoIDDdQsWZFG3RNFGBNkNg723iCz2bLZbL%2Bz%2Fu%2FUS1ibmIac1wabvoWb5mzmDTtDEb%2FCbGuVEf7nfWPQ9R2%2Fs7BBwzJ%2FKV3Svn7RUOkR9VXHTCgudeVn3bEwfxRb5ITsSwoMQj7RzUkmLRXOh8dZK94RJ0lNlsjuRJtfp7KtRp1FYorHWv0VYa8u1%2F3MNX3dwOasabmcW8AzQKC3fNa%2FbFZNb%2BQbaoEmsud3YMUUuXJGFmOMKHpoNAGOqUBlQQQ76B1qjWKA0%2BgG4WzXiQ6TdqxIgNY1QVChNTM7GUqmnbmhRyUdgGn%2FrLP%2BsgTIgMRsLtCvv9HURSk8JySzeZeH9XQsfppTG8mv6%2BYiDrx1Qffbzvb780by4cnJ2ZsbL9nhGgdOZhgoKsWkqWPz1%2FXy65azxK3O5UIVZg65oyR%2F8uDOT2NGoLHah9TjPnvISHKkyxKkTUOaitShvOz%2BQhY9Fxs&X-Amz-Signature=7c8e1a00672af4fb197a41762768a04c0e2cb6d0297e86ad5dbd8641b2e1d3b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
