---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCMTYXSF%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T192332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIC28zLDe8gBB3eO%2BnCvyAtV%2BxWPi0p6PHxl5fKg4N2GEAiBPT7g%2BoqLyDceL%2FUR9iJdb6eI4bEB7%2FYztRpNJL0Hm4Sr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIM%2BRSi6WFY3wTQqhwvKtwDX2b76IixF5YLSCfTlHCWd0HV760FMAuIjKHyivKNASMrSLRoyPa2tgQKZUEax3pxwzDoCwrnvTMgk5aZmJwDAjeGAaSRMUeKwwlMJOXgWRv4vXFFcXUvULyXpRsBqXGV%2FAOD54i8Z8mfbi4R%2B49Vpkgc8YtcT5vELhCOPkmIEd4yBaEVCymIf8NJVqL7N%2BJg2AQ3y4rR1uOC%2BC8iH%2FYtdD9w8zMdNUqJf4NS8nmhAk6olZCiqqd9Wx99YxjKNu8p52Q%2FoENuuR5NUUudNm65mLbryvkZR4uq8qUybkKuTTvBuMmSXfnF57rkDJ1fybbAnAyafQtg84zmuA4UTu1fpRd6LxwTbQSy0wlt4mXuSNpW1nD9JQ9hdcubmwYeC%2BNOgkf9bPNo1Fa3I5q4GUAX574hEN%2B6iQ9%2BhxBJMl3edmciir5u%2F4tOZjnLfW0jzeYsongk1zsS62usFUJB4M3sImhlhVm6ncLIlhn%2BhZeeUignJ%2BEuKLnwLIV2uIAKuhMW4d6ea6i5BBueiA720vH2POnKzISuQ8bRSSRTxeJpJrs0fZoX%2BIJG0i5HbkGmbPMHiu2rXJasGZh5FR42ETbb1%2FOUdOE6xq0pTNAD1%2BC3YymkuwRHc5L6mypeZiMw7cbl1QY6pgFVY22o%2B9YN1SazhT1P2mg%2BMwIUd9ja8dUvCDAklhA8x%2Bszz973oDhtPBVrnJZ7b97Ou6HJhQyT8A4UqGLgxJVevHAyS36fExg%2BFJKbfmY9TgXsz5lSluDlZIqOxoknomYNx%2BCRNoLAaISmU98fGpRuyfP9gKf%2FyxNf2z4Ffw6of4Zb%2FjVp6lYT6Xavr4At7fZOio7t44VCy5r7y0j%2BJxLcpgRhJTwx&X-Amz-Signature=7cfb581b8a272aecb0f4dcd76761b40331d2e98bb8adc1a14b75cca86d781b82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
