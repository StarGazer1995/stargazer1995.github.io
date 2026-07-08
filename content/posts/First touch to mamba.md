---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2WU2XG4%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T172005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHU%2FRTmUz%2FBG7iCK7WI1n4afl0FLnsjhBNrT7X6o3dyqAiBmlS6p33YOK6KvA%2BKuDz8dEiKs%2Bw1lHt2%2BmYzo6AeVSyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMohQk9OdS4wVjs%2BsLKtwDS%2Blclhw70lZvBDS7hLA7BDxSDqGg8hJhV8XLW46sAuPJgpRxfmlmCXx2fd7eAnjR216XgL4vNyfX1hfhgY5sbQM9MtuA5gSU20wLUe2nM0ufeSgkptlvKrUYCZSGo82A4sFBbIvCpWnVgMkis1Cdz6sL0uJnjL58jWOsLFYaW%2BRJdcBFAmBK%2BUv%2Fu3p4FTRXalg2fuk9nr1mwWZYk%2B7AxUMcMNjjIkirmCyxkzFyC13jXFcqCUGonKmSdHMKkGuN7H19xZu%2BuRPcmBUHPyVKCQemWCMnKHm2pUZNPgUlI%2Bf6d6tr1Ic8dIiU5dzeAxZj%2Bz7qoIiATEHSOenaXnZ9UjymP7hhHQ0tXnTLf7ztSidnEGcKtGXD0QrBiQ4vWYaLGEbgJtyeGzrJi5caWsdMuqqZ%2BRNWaBok1k8SNWSq6Ile1e%2Bd2agUFL5ReJZmisvgL5eJ3xsApSr4E4pgaF94Z9k6PGz4VKi274vAbQBd74nz6ej5USUmkchyA8ATWsFzxlC1Bu5HDPfYkOAi604mFX7bYVjY9I%2BXF0s2RfSpBzUlak9iC2NvzTlsgbrglsTagpucHGMIW5B%2BeQKinkr8OAwSdnwfQ1LdUuyiTYeW7g3IzYSQbFMjRby9HCQwtd250gY6pgFqoe%2BYm9TrcMGZ8Zl4Svie0IhWgn1IDDOew9sAUuNR8cBodMivgz%2B14yYzzGUoZxdzUbgB3fP27YvzQwg49yYBor8mYLhUawcw72njCB9neophboFFIYEIyIoydU7xK6whX7FQBP9XSqOy4qbCRzNhzQpoZe27nmWP7BpO6STlCT3IN%2Fktb8e0k3ReMPfHcsUGixh%2FurSSLZf8CBCM1YXsskurej7f&X-Amz-Signature=6d127b0780694bb51307d430d70ad4908ae762c82cfdcfa500f660a48d6185ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
