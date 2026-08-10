---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJD4GEUW%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T164139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq1YemQIwxGSEkTltawwEKdyd8AJYyDOuJ77hWwCcnZAiBgFgGFCmmkErjOnDebD1w1bwDS59%2BhyOzh8p8rXWsWQyqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkA3%2BrY8CayV8IjqsKtwDFLwn2FzM0H%2BbFpyi9gD6EqzyQbqE67Nsf1ViIVHo%2FZ%2Fgcd5rLCT7ZlOJVe0bkN17p0ZBNEeQ4TIMZ0Bz%2Bvv2p%2BBubP7g0vZY1GqY84b3DkK6tn%2FQKknUamwjCgA31T75fZMMaeqgrabgtxrSPmT2Pe2%2BNh2jh1M1eL%2FkSHPgpRgn3rQm0rNRWWBQuEwkJczUjYUsOzzBPSP9aOMaC3zmpCGFZq48bDFHf47Ylh1veWcPJYE2DQbRUEuJCUQjry7U1OWp0YAoSKm1RPRQADmvSPNqkKBiIGok%2FnfYoHt8zoNnBpdwRbBFklcF7rRbbofyjnqv1YtwViqCBT1d90i1NRbnJw%2F82w%2FCe1twdt2gWyHiNT1LZJjB4lpn%2B8FrvimGQ4KtLLvekm1og82SbaqJ664eh6tTCVr2PZKGjNL3xoLMRb6kK5Pu9bGdQsoml%2ByybkyWnb3pdYp7%2BcxAfyHNdk74mjxERypxjREqAEW3nBnStv%2BagM7OsKOJCo54HIgcXMnrV9F%2FUp%2Fmt9Qv%2F2ZHKUd%2Bp2c7IIDvRsXhmEh5S4t14ocutF%2BpqwVYK0HWChufjlbdlyLuOjrcD6UfsPnRQ0fBaCny5BRZ6SPK7izI6pKpFVcd6%2BmlfI%2BDQT4wkvfn0wY6pgFS1KAcA4OFLVNNJ05VPBtBvbASvsTeXQTKV3PJGp6c2c1hZlgESl5Xh1dWbk0CDA82NmfMYBSrBJgii173DDMHBRE5k7jFrz%2FdBz5QvTjL9rp%2F0CVv8oCYgnsnrANN9yBOJfBRE56qZA3UYbGWlsPlmMtR0iDnYN8tQdR4xe%2BIs9eSNy38QiSrS%2B12vcgVKp40qDnNE9Mhin%2Bicv1icS8gHn6827VY&X-Amz-Signature=4edea6026a162778c25df5a2d5f2c10bcbab6c76fa2e242810705965f464c1a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
