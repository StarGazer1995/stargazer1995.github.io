---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665X5DOBEH%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T075121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBOitDZV%2FDcaG%2Fo5mrCOYdI7pDck%2B20ucxUq45QwBbsMAiAyaybOV9aj%2FoweO7WlOJH22FtjYCVWsU9yUZvLaXVesyr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIM%2F6yLKMveb0oK7xHfKtwD2Q5MeRiJgtyafqe2Eg0nt3PvPI7d10tY1lN8l877q9nKIBFIg7y9xXYkz6UHtl%2Fp8KgLIlR%2FysQdLHEWD%2FY8HznTrUjRGO8rV0%2Fhm8uDytf3WyZO2P5gzThB0rw9Drcci5hMETDFyF48AxOnhMJRoIDattJajQJzlR0qc%2BWM6hOgmfIR7KwNbPfox7Lmk65OM29BiDqy8YU73v3XwobCsbH9I2tG3dJP9PkSHi0GN65Q3FMmKaZgWuLm%2FinBgAKjQ2eKQ%2B4QnS3aV1QW6sQiqL%2BmpiUdEuKlsXRTeWgTTmcDtGHBJk6qiVYSI%2BYscA2GDt0r3ERc5cp0PWmTxdTLqIMWkYpPGxN7iOp3t0Xcp2kkxol6RAUBvBlHUxkqRqyK9quY489he23B7iViRzo8p3x%2BbT%2Boq0UDHwoV7Lobb9wFIlLLmP6M4mQG5BLO6P0Z%2FiOrSJ%2FaM5wKK7wq9nBxEbWJ0AJ3uu%2BbTpVKGuZfcdTmnjyCJCz%2FliD5zP2wvJiPptey8LRw5emHdWNL0YcsAPpAzmTA%2FDy4ABStZKhxbpOE5uZgfv2Ib5LNsYoeXxihoXG3C6ppn3gC8usEZvZbxJGldomCl2m8y9inGpDj59mX8zrO4LXFI%2FhJEUcwx7in1gY6pgH29MCQssxvA4JdZu%2FV61y1nSFvUf%2FIwjW5dLuu0YdN00jcFwX6voO9Gdm7Uix7%2Bs6mGxgKLr2GRRj9etFs%2Fb1WKQXr%2F5rBij863PVeCsAdQXVCoo8%2B7a%2BsEjGOOdLr6fnzp3HSN4Qr7NcGnOofd1WR9o32w%2B2CYWcxGAczrqmkVwltNLTfqZuFWx%2FOLgEeUSomoVjMzj5a8GQtf9jOr%2F5RIe%2B%2FJYO4&X-Amz-Signature=5ab0c693bcf9de212d58b6b8eab820c3ff360661a97df2b06f31d99a64979d48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
