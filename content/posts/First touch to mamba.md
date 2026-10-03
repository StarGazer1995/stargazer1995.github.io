---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLQAUW2P%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T174126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOeqgp3XdbIpeVcPOSFhNcA4qJTKGIfVp3ZHMReQhB2QIgV%2FcDgo7w4nbyaT2PYO1edl6fmniZRh3VjCOVZpVvqosqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN0ljaut%2BLkYgmv5fCrcAw%2F9r8oSpTSjvXfSVKqvh%2FM8rnZ0djbhj1UCc9jodaZLOlFVVAs2jU%2B1yLS0wh7Rqy5ul3u39T7E6B%2B%2FUVzfX99fTdMuYf%2FoemP6px25NUkq6gEBno9i7qa9k6QRd9pMsvr%2BWoGl9Zz71d%2Bm%2F2N6uKNZC8B1fJLiPhZKY3%2BmsPItxAA3ObFgxeCE8CYRbC%2BXMtHLiJ%2BzZH%2FAPwiTItrxPKStPR%2ByCZYsKQdhR3jNLrseRd1SDzlO1MkL78bDNru5or7kj4ra1n9iWlEp0aC6o1kevsEEe%2B9MYdA5shdZibQtTir7yLg6RSbPzkfwbdrYwUjxDMA3mpl5MyuBgr94oTP8rjCSaO87VLvXttY2ftp0%2Blibs%2BZNrH9xJqiZfk8IM1bKSLqAXCEcXi1xQEg6A3GgP491Qyc9qFh%2FL15n%2Bq26g%2F0Kr%2BcMHxUTHXytSeCV8TokxrqDssZMFX5w4vFMY4GDAldJFpZGzGO812w6fFTZlSnwAqRuoFKxkqHo%2FncV7UrNUf3fEJapNw6VH9Q5PB8EOkEZm05f3PJiBe%2B1nkllB4PYJNEbYlZc9XP1QIBvCrNFDSPv4zF57rOQ%2BdonLdwGkhcwR10%2FNZyZorZNCdiLIxz3eT%2FrzfYzuXX1MNfzhNYGOqUBUS%2FEWtpJLhFoD5vsPfo9IXu75go9j0RywhDSVcIfD9c1hNysPJNUiQBgAGF2uwU0IjaiLBzzWS2ABqLxlS0T2iFFoJohU0%2BU5xKBaEHtlr8LwSJB1huWcAf8sIqq6nigAyzwYChr7seWlxz1fhyQI%2Bp3fW0ZOxRXfdnSpvHpSluA9b4x4zpRx%2BlsASwLlNvcvsGVTr%2FbYKX2XKcipPuI%2BjHNAU1g&X-Amz-Signature=e1f5938458b76bdd314d5aadeec9dfb48db13f12a49a8253b577779ad7ff6364&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
