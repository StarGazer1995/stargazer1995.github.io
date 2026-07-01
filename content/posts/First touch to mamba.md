---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YWIPEAH%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T211620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIFvvuyEh4DRwPkCaUop8UUB2tmF5Ds73FIbVLNSanX%2BoAiBbtoaZ2qIdghydzo8K0IlNpBPJJjW89Er7uXMKbLIUDSqIBAjm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJ4aPowVQ8YGGTUoaKtwD%2BWwbnuEAjjk8Gn7Hp4iamLE6SRuVbb%2F5ANgQX8vCJhHXdK4Vc8SAZRFJNpcFQw4wTlVDSXjba9Y1rDj5ky36w2BF0ibYxOtjKjbezh0lg0srBecgSF%2B%2BFVhLyyp0UOvJ3JzaPlSZ1SYxldx0n5nGzZsC%2F0aqOdxWd2xO5RsQ2APs74jK33i%2B0MJD7Cbvmb0aVBgCSSLPLvL5iN7W%2FKLek4BnBElHMs7E%2Fp9cjVXL0TqFPjGVskviindMwDZCaIGTJVz%2Bd1xphzu9TYShbZxxIqVQt5OJFoFbiynfGkWN4umsxwa2Cyc09pfdLn2Y7uSsg8ylnybrC4glnreZ2iSztG077GhlBRwis4m5asslsMZarSYOlkr0KnV3tnrqTeuRG9%2FL0dwXm4mofTw41inZzEQHKqtKnqzzX%2FPNNAhcElDSOBktbVfBp%2BklPQ1Ol4NdFboHui%2BzolQlXWvsrM296f1s037OWBBVgCujO%2Fa08G4tHIj6ubj7VxNoPKZ3x6oB27p6L5iosYbI%2FUxOO4jGEbpnYN8NvYT9eJtYtFn0jM9YuhXhbgdfBogkn93HOF8oRAvsHhSqLJzJcp4S3bvGlIbjE%2BZIyhGg17wjftSWjLg2gRiXuplVKEiBNOQwp4KW0gY6pgGZb5kd8pbmVKODyr74QSnGikK%2FTfpklv%2FUc37axPu76kXHw8FB0zyRxfq9gByRGYScByewQfWDBH1%2B3iI5xo5uRHrh2UtoIhANvXFks09A6EYipiY4DX5CQ7VQp0G%2B0eGFlQPjT%2Fz2OMseZEJMrSMRhG6VdzJMhqTWM2sSCAIec5zEqHwQdEOSpmseU74DvDbV4b9Os8WbRB1qISNHCorap4419Fpw&X-Amz-Signature=c9adb0962206e938c3154ed4ce5faf2f0a7b1678fcbfc1d8472408815b12ef4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
