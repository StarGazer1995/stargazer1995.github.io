---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CVIKJFB%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T224323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQC9IUc2NWQp0jVjYSegNWkYpoT3HPVwFtvB28y055FFigIhANXs9d167hvrofOz0goUTvDNNFNUf%2FaF8Kbo2x%2BbVz7%2FKv8DCAcQABoMNjM3NDIzMTgzODA1Igx0F8ukxsb4LHylt%2FAq3ANIahS8UZxJVm3uy1JlX4oaekMvDi52dhR47Wo2xGg4XR%2BGxcrKpXus0UyELE3NUiJ9IbZUr48uTuYy4YXHdNDOrPK%2BufZ%2FD7f6%2FLATyH5%2FXZhUMR37Xt4SF2VDikmQtzvk3palL5Al2BYPmMGm89x2vQqXqYdRbYIttT7RqUCrLObTzmpodXbXeSQEiO%2FIhv0AgpoD9alLCnb5ftIxvrC0OE%2BFkALi6DL9DguXXv1uDAff1TsA0Vug83zB5tMOCFYajswtwzD5Air79mfYOWhq5gaLyukhgn3YWdDGQy53iXkW3B%2BrQJ9SRaNID3PNeTKqbXyjlrkppgVsjSerrm2TeXRpELpe0D1KZcolWh96l9RiUztQJ1kaZtHkaOH0WIPaCc7iLlq%2FUTtD0wCgBgeMJDkzYQi%2FzV29gjZUPINC%2F8qUAlDzf%2FfyoDpkVfmw4imyLtqTQpwjMnXZGz41SF43KIOUl5K6h%2BVydC54ebwVoSJ5rIwM28lDHhqi3tPGjWOwgMLcceqXHdF61fd5sX9fN0gNh9X7PDSfGMv0oQdHGkfdaXWNI%2B0F9sPvD72Z9kjpEOnyRqSPHzo8mK5VaKx%2BIgR%2FDeyu3b8H9RP%2BDOKoGdD9tF3H7TlNCgoL3DDjudXSBjqkAStLrMzoh%2Bn6j5jYbbxCcgY1kHd%2FvbC9BLsMQB4Wo%2FFTH5lt2%2FjPlP17oB%2B0uQFz2IhREvL1usr9tSC1NftL1aiceboCGTyBK%2F0tUNBMZyamlnXaUtrwEEczfkr63Ru5b9SEKXrkV67%2BaOYCAF%2Bqpgp7nNKViXTBYUIWm08QAXSyEFK3SvjP5b0eIV3VN8v9a8AT1q3wiHWhz1ciio9N6hgCePrP&X-Amz-Signature=d4a742f935db6a6e84399c6aa4ace8fb33d72c583115a33dddf15416e813bec6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
