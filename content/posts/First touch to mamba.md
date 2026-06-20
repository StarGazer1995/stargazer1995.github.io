---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTTAIBVA%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T171500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCrlHlUO%2FtQ57I8UdROWvOUH%2Fa8Zfco8E2k99bdYorsWQIhANyfSYsHjYKKgcZYiiVNzYgFMwn0Qq8WdviDRkJRyudcKogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwNOMYGHivl3Z0eUNoq3ANMJUVqsPZrYScskKE2Gy0UxUQkmmHeppA2qwFLyHifjVgEaAzwTeqEzibRFFL6I%2FImc9kY1K2fJ4SjeStzV0On71i7n4LcdBfk8IuuWHUmxoKo9IqVrEw0VZM4sih1J12KIwQRQmVEBLMg15TQBEznsmTjh3VBjBTXmAoTpAu1ijD8lF93hIhjXohS5kGVgjALh%2FH46D7O5MB8KVaVEcqX%2FTZywKaL7hpOh04DDTuhOulnd2OiXXI7wJKes%2F4YdnQMm7koDGDmCvt%2FtanyTd0%2Fu3Z7wCpu7%2BHQ%2BYs7CP%2F48n7XYZqx25%2FPqKiygrxAIxPPVtrKgkoMZ51rD%2FaakQvDRhwy6UnarK6VZshwRM3pAqKIRRNC5%2FP97uwZlk7JIZKfh7YIk%2B%2Fb1FN%2FM6u2sMBiXE0gvTdap3kq6f9zoqdbaM70vV3ZRNyIdfTbcFkZ18%2Buxs5zxYL56BzMnMZvF2D6nqpCceRLY5jRDIx2zJxxuRCNhmMN%2B%2Fz9D9%2FNThbTPCywoMrKIv9kG7bLJayCSxQSkixF68W%2B9azxrgPGi2vTsXV7HPF9BAmx9cqMe%2BA6V6vd6z%2FQPXR0UJgYTjA%2BrfdojdlmaNnMCgSLp4pRASPt8bQV173jByAa9QiOhjC5iNvRBjqkAYZ5EUYGKq%2BpqEg8meorfpEV6XgvO%2BGiRAthj2N0TS%2F6ZVqZbZOv47V6mvOvmLG%2Bkl6WLEQ6eqzU9OGfXWZ4xFpw%2BvhdThsj5ArWQv8hpFBZyEvgP49bc3lwMhlrDQC8J049vxMAi38z5CYVcXU6da4i%2BTO3h2%2FVX4KKJ4PGjnjHcZN1AlhshvnGiaQqFNOCYmMUvv27DqNA8fjoScovSkKN0RFh&X-Amz-Signature=bb6979729c60c3244608995a31095765f9f800ff7f6a3e38313ef5efbb7c58f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
