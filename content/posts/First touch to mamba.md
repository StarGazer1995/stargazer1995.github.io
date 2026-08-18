---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IXUEEFL%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T122357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahgfu7vClmvnHD7RaBIEe4SCdQDMZ%2F9AWwFodm%2BvbdwIhAMft%2Fe2ox6I7cCLRwWMxWerZijqcMC28m%2FTFLELyBQTnKv8DCFwQABoMNjM3NDIzMTgzODA1IgxLxhcygRb2mVsgiIcq3ANRco3n2m92sq%2FlPgHuW8K7v1kvQGf7tPs8DgM52D71A0reu0UYFFEwxRqqFt9PBbQWY6GV8PQWnPpP1Oa60oFb2j1cfGxkaP1W9e0g4ztJIWvoE2F7JRJnRW5NQLD26U3sFFlqjenIB5hD%2FXQUajrLvAxCMwt5RxavbHOKqSf90q5p1BkYYYfhhMJt875jws%2BuFj%2FWugtCgkPCMK4yOjzFpFvYjx3q2UtRcaxpTJwSkXqWR50JriFszBsm1yMY7%2FoccR0WlyDPWO02EgegKOYwJij8VtR70WNrefEFnf8W%2Bi50HgkTJx%2BZKh9thoG1iMNRyvu8ZQiM2MjMlldCH7vNNB9FaqciwMLYKxcENGYFg7RBF2Wtg6i1BsSMX4tRu1SVE%2FrPMKydTDGih%2F9UFAw%2BKIKRhfv7N3IOpDvwVEcJrkzlttBwokueXxvNdF8aEsKfCD6FK%2Bhz7NHKlSlICTZkO23q7g9lOw%2ByI%2B1I5sNY7nfWORDLdLNt5xMpmtydbafi0T%2BJ7DmvMkZ8fgYjUai88GFe4KiIrMRbg7QGcu%2BSxt04tUK6kQnUbV0ABJNl51S1kuShdc7f3H0w8VUTf01qSpupGFanFkoJfxb3nkj%2B1%2FMleDlP5RT2yKnLnTCw%2FJDUBjqkAf9BFucESRCuELHjrzZys1ll4FA1BONokfMNfa4CZTIN0jwN1mLaHTurNpHC8qbwm0RtkLThYySED6Me1Gzhq5JUSXUd7U7t2fBEs46PHus49KzuTakrXrPa%2FAqlGwn7dFOjJ26fgPFNZuaj9ngy9znNlaKsEVQPOnhQ%2By49aIaa1heQLqtYf8dynfGf0M2Qgg%2FNZssP%2B1wj5ud358%2BoqM%2F23v5W&X-Amz-Signature=d23f8c3a5740ed72c6a71d0494ac563f4ad3a828de404f724cfb930db9cb4d31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
