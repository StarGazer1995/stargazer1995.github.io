---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCJWBT3W%2F20260914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260914T210808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIBi8lCpaR%2FdabSpyBX3sT9BYBIgAk5%2Baa%2B9%2Fsb%2FgGrnjAiBDFJpdE%2BR9AVxndv3amJ3Mo3%2FIvnJZiMK1zLKPiXJFzCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT%2FdTeVSsb0piJoLjKtwDl24lpZhoX0N0pC4E%2FGmrBrGrOxOyHyE7zEzP5rbeh%2BVj6TndsZZXgvJOIFHyolePBSVq%2FYhLGNs7ijI%2Fu09LH21sYwzAuF7Gg0TOO8Nh6FIycZYmI8HM8sqZfObuRqQf5zJxaf0C4vvxR%2FTU5AKx9vj0asPmPCCvxArleNBx%2FfLqJktGFI8N3OB5zOSzDIIeUqD1rZYHcDHXF9%2BSu3IKsG%2FmEmFHi%2FK%2FRwmI27Z3m1ZooxOepHbpwPifoKFoB%2FSRov3rLYwfd%2BPDCt6Rktre5x3yw%2BjWV3KrXNpdtuifwwCOOC5MxJwxwAqGlQXVZBDou30tPeR%2FaIx%2BWy3tUdCjyQU1lPoIVYunVlxEpRnsSMI9JNVq%2BMKm735ViRwPNbwyms2qDZR9y5BntPHTaUbf8HERgzd5yP9%2BsM5Ky7ClNZnocMrkcua09U4UrOVMq%2Bg0PLLasnZiNy%2F8KiCra%2BXFqJHoQxH66enPVRi9XK%2FgmiCH1pODQhb4RJWDOyh7z6j2oh19EhdpskmML0DgPKG%2FywZbW2xNmO0uOUdkX%2BlDF4yB5nYQ7G6nUq0NYHJueQNvgk%2FCzD1i%2F1z8AzwieLETDMMR7CeIaIEtjRGEmtCLW3x9Mj%2BDDss%2FAwsjWDwwrKWh1QY6pgEkZTiCuz%2FiJzfqLEbU3P41r9kiUVMEQsLCb5GoZLtlpjjFi6geMxwehrbiAdi749f3X%2BFE5CMr%2BrO1G5wNpXNG9xGrCnhPG32ir62wdH%2BJEB7w01vu%2F%2F9FIC1KwmNdY5uH%2BM7uNJHaxeCqIKS2R8DUvaA%2FAOZAI86tfJAZylLgxSmU50rbU%2B3iXyTdzxb7GkWi%2BpNpy5uc%2Fp9v0CF8OPaXTdJnqaqd&X-Amz-Signature=4d40b7d28ba097a3e3241a957b5957ac02b3a5c6b55ceb8e8640ef17e6cce03d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
