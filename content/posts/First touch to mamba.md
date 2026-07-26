---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SAZVMNS%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T164459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQCNctll8nfaxEdKMBTzOA2l3EO0KPBTGhYSi8u6QFIx8AIhAK76J9fA9kmpoE5XGNqV53WJeDsJIsgYgLXT5qvRcm%2FLKv8DCDkQABoMNjM3NDIzMTgzODA1IgwWHF%2B1y2IcZg3ZWswq3AO%2Fdkw70NE7cpzTfQw3zIjg6AYwyJ2gjYNydPFD8hOBGIYg%2BMn0VgLQCUen4otTTjduZR5Eckk0f%2BNhYPieG4CsuSzUvfk6Vn%2FH3EPILgUaf3AP4w59qK8WsaK7JhyW2Y%2BokSbWzQyiqT5Dd0sy3gxpjAx4bKTKEwGDjYC3szypbviTaSYa%2Fnr%2FqlWTY%2FwOkG5yocWUVBwvsgPTrdQCNUKajK7c5AGxNhtaXvoL82%2B8ArOepJBdWut1dwzKXHawMUty7Xs16IOSWhgKGqRPTYG21ieICbER8NCA1bYsPnENGFhCO8Z4ea2FXHjXm7ezdC7nlLUlIdCY2coquvjcDttxFillv3NNFvS1smngc2E6cr1l%2B1OUILrk7rfG6OFSXZGcV66RdFA%2Bw5eoGg6pOoek2igj2twixxdkgiFr2ktetdxoNN1dnv%2BiBVHivErCm9wVVHCYcyYKckULQDkUFaULm0YJAJzdmMA7o%2FSfuA5%2BizdoQU6LXfWfMOZdTVKxp2ORer6V268rYlv3oXP%2FlWaj1CqHidjKqnh4h6kkGtzLwTxIZUnN%2BVtgIQ%2Bld8yu7UWHqElBOwbQxNXZYoAMNr1DSmUm9bCvFzYpSbKgA6yNd360Eh5tUrNa7W7IvTCB6JjTBjqkAdMY180FrFnw5QB6bRYU8JWVt9IKbxNH%2B1Hq15h%2Bc16ct7Xqg0uslTJuLiklDNUAQlMkYP7dj2LBRNe1zniv%2Fz63nzthSDEHRx7lKSVYOkvr36cr%2BkXbuWYN%2BXY2qlUdO8ChM4LY9ZXcDdE0HTsYFgL6mCv4YaIC6J5k7crkOrOoTpANYS09WsGugOHE%2FY7tlSV6uQovPOPQnVEMkwSDXYn5Rfj6&X-Amz-Signature=119362c9eea7096b6514ce254a9920572f97ef945043bd7f0a053602d4e09e9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
