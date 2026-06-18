---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4XW5TB%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T124559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGJ2yBzmviBK6yFBc0dWiGyWacwOs%2BIbhNnHJp41GU94AiAfxFerbSxhHgB0R61%2Fv%2FxlioieLkczqcCOCo2ONr%2FWMSqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXL5jZtZR%2BCnc%2FpBcKtwDQ%2FmawEvdgUUGay%2Fr7v%2FtraIGt57PGJ4kIUJ2qfPcWNOsGm81iK8xbVfrYMbJIGql4xnLmE9N7ygTeDpp5jpHZvnIbm8GpSFcC%2FkiGuccz5UgciCHW456OSJUCgkP2KC%2Bm2vD8YQNAA4I619vriz%2FJwlvcq2noYXPs4SY6bMSScaNUwwnzKqdICAQtRPy0PY1sqfdJv5GDo%2B1r8WU7ehKGEikxpyqgTbIXq811lcTEt6%2BOXadvmKL1Uomv5HSqqiM52JAyxqT%2B5IhAMTKbVoupHnOnQQiSSe48%2BzMMvWWHdSRpH87u%2F3%2FFOFZDzpLIMWzpSJT9gy3%2BuUGJrX97MXAce%2FDxg8M2tpXanTeYIbUDZMmoqRPJEWTPKpSAF1akQYP8SkQQCwlxzeTmzuDG64wmHHSp7KTh%2B3o4Kyq5BLe9HSXdCJEEtjHt4aH6wMTpyg7%2BhaSxCT0zc7ylIRmUa%2B4MyvD5EuQDDWyir%2FO1riLdTqpWkNK3g989vzdWUgFx8lYU2ocd9Ob1Cb7ggZ0KoUYXmTAzXZKHz%2BAwaWDBrrRwIK3l5iCN8%2FX7wBMRS%2F23iXLT%2BpKHZsiUhnURTb6Ge2rv4eP0r4DcaepWzyPXHE1kvUAkyfiqGumrxGlOw0w1cTP0QY6pgGIMzynQd5zmlbcr%2FfTQ6I9pZe5XdfZW2RWlFWksgMHps9cQ93uQfXeElrdXqqUtw2ShS9Yj4K6lWbxB6ftp9Ylk5KKTFRuTjXotDJyksq4Mrvkjr9GGKEk%2Fn5jPglKg3LZrdlsgS%2BUCWnjpfRWbBrSmGiZJuFSU0KE1WyHR4XJYysdbASW7VZyPaxoMrpICxkHHRuyYvJPW5BI%2BjcAd2PxmyTfa8vl&X-Amz-Signature=c3985d6632105ac6dc9a3c73069f3532e3d6a918cf0151a8101eb43e3c0976af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
