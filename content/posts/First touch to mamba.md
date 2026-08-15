---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QJYU55L%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T220958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDsd%2FkHnE4r4i7D6sM0c2RS1i3uLyo72aWkXyau%2F0IXBQIhAIQv6goO6WbqABgGgGnlwCEm9EdYUVMkToXWQltZhZaZKv8DCB8QABoMNjM3NDIzMTgzODA1Igw9GoQ9IJvDFULJwo0q3APwIlluKUVSvLd4ZE%2F6CD3FDspV1WTJdHh%2BvorM%2FyzYIb0BQLrMqLjaDWozaa5HazqrLWdC6FoxJKTvDHs7qfysD8bdslyEU6Io66rwYIytUAYPzhwREcf5Ze%2BrjSZ3PPMXV%2FG%2BVdGB22VlVQPTKh1qgwR%2FbyEkSyO0uHPEPcDHw%2FAOGrZIhXCmlWGP59seH3XakdM2qJ8zRX8mFkgw5247jG76S6RPLciF6bQdTkaeJe6WC4HrsAYlTBws1IhvaaaH6XKRw6t6rW2TJzPu22NrfSN7ctd1f8DGDwehhsy5N%2Bb9DPtk4u%2BnKThY33GOXFrpEk4TJX8H%2BHJoVahvSTwHvA2dOlXE5%2FigRdbB7TNHVki0Dla4hdlAC4rhdt9daOjPMvku1lgDSoPcW0dD6S3VmVZb4f9RSUKWkVCIzubOptSFgw%2FxqPa5oBKDUxtaK5sHL8%2B%2BSwd8I5%2BWlizt%2FcaaMeELSii4wl00FpUNQVg0CurkRt4oYqdJTCAjoxTUGb58ZxJYTkvzR6r%2Fy80pZEQOnV%2BcXXnxV0VHMrk7kJZLSuEqJYd8Xi8g8%2FvzHIiVl0r0IsWt1Tnqi1K1%2F9aHVkbo9Eo3ndbnLE48p1tV8qUBxTfFA%2BC3p41khyK%2FrjDLvIPUBjqkAX0qt3k4hp1Ud6c1aAgb2qe6WgUbbpJpZvQW4wVB0OdNgG%2FS8tMPzG9jK%2FKIWsK0IBApJoSrboysW92N3PrMDqXF2tsCGVotQ9HPwyeZaw6m%2BnOnm3fBmAiJ66shd%2FtjqgnxzEoFytyEMyAKwlrSPBywEwQAoElWF2Qq1ocq%2FOD2nN%2BeuE1IkbdCO4rHOGKVAHMENVs1%2B7MV11YoY5BtTx4m26vL&X-Amz-Signature=8eb12d82adf04dab9e4d25e51c9794955b5cd838030d498e5ea0d8f986b631af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
