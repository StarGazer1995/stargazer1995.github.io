---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMEPJ4HA%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T175721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAEVSSUzp5OBae1stao50r5i7T7%2BZ%2BdTSqsjo4ia3YFyAiAWx6M9k2kE3Fdmdhp6hVFhj8Hs%2FTWgCU34uCAapGmBviqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoiYXqROkz%2B6cKyo5KtwDdj59qAl3RN3kapW15YEBlwVNUkXxIkVHsGoEI8YB%2F9XboM5BA6SEEVwt9WSTKtBpdwOUQxiw%2F18u26%2FQROXZkhNaefxGca8Ao4elMPWI0%2FVOlhxD4ISKROPA4lDod5OyBCKSMWBM9hmRnjZ5Gd3MwlJuwhSNRyc8NXdmbwinuHi7IVpL8a2uDGHXA04TSxAuSFgrQfZPVgLZ4%2B6CdqvxlpDew32GvdTMImZXCOYkR4rdb6PtcwaI%2FvkXqfLdfzW27dxwNQZPs54d4QjGp84cW2Qc3nGvH0hh%2Fis7c5PYFy4AG6ZK%2Bo0p3HRp9d4mqEsUe6Z6ji%2FtKLhY%2FfnBlRSUlzyjLg2tnb6REgGYhsdRXeg%2B4qaZyq7JbOencw2eCRnVy%2FJ6V%2Bk4Y6NiyeTQN0KNVMFKLiKhe4FMI6f%2Bh8RJcG%2BUJSjAy8TSpZfpLVoaD9y8sdYq3%2B%2FhAk5M5m07b7W9HXTMccaAyWHFo9b20OAPyEoRudgq6MNOVF%2FDYNsDZUeKlk9fKv1kOR4IOZA8Ppn87AZhHxwL0ek6fQuLPVNY7wP57mlKZfB%2BDusj2sNjBwpSQsA3o%2BUHjHIyzTBY%2FqLLjT6EYu%2FBRSFFa0VORS1UXQOyqIvHlkynjvDPgiMw6paW1QY6pgGdYlwVHw3Im7kW6t0kwAqLJWRWV06O66vHbkb%2F64PvdJh0w9sPCWq%2BsHUitTD15ngHR3k%2FqvU9f%2B0BmH5PvVl14tsGN0ErrqT2SSCLJoUaOAd8IME3q96UYvcYjHxAPzDSLN7pHnGAs%2BpNA7cJiN8JXjXS0n43G7GLfgFqxF%2FyxJN9I4eb8eKA32fkjm%2BWpX%2FxtExT1ePme7tfCQ1M22hhqx46fmIu&X-Amz-Signature=162cafd5d1e963e93ea0282bacc5a413f59a2273ad47eb82f64bdeb892192c42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
