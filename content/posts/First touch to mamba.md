---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6G4EOMJ%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T135042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJGMEQCIHEIpyxYer1a2YdFvzP9stkXKjFBgVtWpKqudEzEzRj4AiBLz%2BoNxdFGRGK702ZaTPKRpuYMAw6WFnk0KLyz6fxabyqIBAj%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMa0mtgQiCa%2BLc9eikKtwD3tWkgTIl6CwtxjlxSthm1vuE10tOrSc4Kk32bMfJGW01MVa4N%2F%2B4Yq1ve%2Fl1sEloPKICLWFkWDRwPyg9KbHLFo1PsostuL7UJzseDVdNk8asAu0yRaNV8zSN0WuLTmNayWxDoRBI985ktg2kgOHQXkx7SFpCBEG%2BTAw2VM%2BAywpR5DR3611uwf14jek%2BWY1Ojia%2FF%2FLdGfwmWLJ9W5zRhypqarHQt8tmsW%2B361Cbdn5%2Bce7dTb1TvphYJSWZR9qQiHKCkFXNKecyia0W6Inf3SHb5YsYprgKn9KOb0dDByVl8fye6%2FpCfldtxEJinQJACPNKeaBRoNqigMzuXbcGKB4rRYRMOxw5ivLH4k9FaLAmGF0xsfM1yj4%2B%2FvaBXMJHU4q7p%2FbGZcOizJXd5u%2Fm4NkrXCZr5muOeJttj%2FVdyR5JZ4gesY4p6R3B5LxsCLiR%2Fvm2RdFdNl2FW033TqGdmBesNleJZGa3zmlX%2Bb6Da0KZ%2BeZWA17nQ9PIXDNgyrsZgaUzvnPtQ1ApRmODyaQ1Fx7Xau0PzSBdmi3Sv6Ve0O06C0TgwJOtTM2b8nCKj4A3jtmQnr%2FxBSsUPOnDd45T56B%2BqP5YCYmIiHmL6SX2eczqioUyBbfxc12hibMw39qq0QY6pgH6fd4d5qXwW4QatwREiPXFpCOLoLRfG%2BqWudETdnI9vdEfngLJMHjEDtowPgNvLengVIhh%2B0U%2FmlVJucv%2FoxL01AOsrLe3I5VeKFcOTTVLfNMnuCpIjXvhJz0esK6Yy6xBTdS%2Fy0N5kh13irJ5QYjvHV%2FN0fDAawKI6TGH9c38uGWVMslDo4Ro1AVIKOws5PzWf77IOEurYaKHdnA34TMgatrNXtLU&X-Amz-Signature=60d848201153e6614bb231d2d45d716ff74220d5583dcf4cbc9a98440a6de3b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
