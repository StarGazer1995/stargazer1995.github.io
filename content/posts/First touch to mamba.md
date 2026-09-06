---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW43D6GE%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T194214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIDt8uV5uKiCZzyNxhUQEf00PQntBAT7xhf00C7xgDFpBAiBNL5uw%2FRjBlu3Pj9vhONsJk5qE98GJSVpVFMiTRBIF%2Fyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMEg0h6sL8mItkuW7RKtwD08boH6cSYloX0N3PKjBoZubzsbi3mB1KwBh9qRpK1QFnA8aYTyIBTWB076guLpU%2FB7IlzDKKuFq%2B03CbP8A2SREJia2cZ3g2RvUWIeEtUlVS5BqKvhirb7XJ7A6Mrv9jng78FTiulzWCJAs5Kha2zrLVQ3xvcms3gS4DoBgCya8pvN4Fbe4qpOtxXYa96Cmb1qIbiIa2dw3lvld%2FJ48H7P2dUbihTlYpdvUo5UtXvg8Ztonvkc3Kz3wgL6eqsVlt8XUqr6gC5I3AEF%2F1U2F9G00zEHhqmk8VLE978XXzPJx4xNIivwDT0gqp23d9WoKQemSauOm4nSJmkMWF83z6pUocnCtKs3%2BEiQSB6SeDP4nSg8zoXgvo1t9KhszKyLKFHGei2dpvfTOq2HOlGIJBkOFCEqXd3r7jnx0CHiYVtPURmsX4sYaIFIorSxB7okGV4VLEQA%2BoeE3OfVYs8yK88GvjPfoTiCLTqG38D8tGtq3G6p6mI2lf7Vj8Qwf0SREnM66Us07hExW2E5%2F36KEqKtp7Y6Pbxk%2BhNRtdHQjNox7HO2aLrQIoNjvSrin8P1WEvncpJaCD1K5KN%2B4bJGXRrCL5d9OeneEIHBwXzgL9Tr1Miz1JFvakrAqhi0UwrO%2F21AY6pgGkehkxNafdjZUHgyTUlfG5m%2FeTnQb%2FOfJag8h1cTcgblnELP3cwzr0iwvzQPhc1yBMHYC5TQIyZc8lfIo0GstEiNHWJnzXRIx4yW0WWV9jSDEnSggH98ZXndhMy2vmbFUGU1aVs3dHgrlM52SLokNVwiyXzfgfQDGrnTcWpE5WOOHjujw0mAJJtJTYucOB5s4vT51WFxNSPJKHyuVMMU45zushIJ5Y&X-Amz-Signature=35f681e06fecfa88687aa23b8910e6464742133fbf8c5013041d04eac19ca2ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
