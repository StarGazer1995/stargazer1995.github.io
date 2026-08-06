---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHHFKJLU%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T134238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQC8JX1prIuvNl6YxsTB2t0nlfA6D10DrAyBY%2F1ZgNW2AwIgPLGgAt4RU1PETRkIB31UU1qAoUloy7korsji%2BSINsr8q%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDJ8qfwh%2FngQuvM%2FGOyrcAxDP3sFOZhGWy8qUG6%2F6vegMectuVmrQ220NriGbvDVSYhrcdx1vOZ84K8msq4CG%2FndRE%2FIBG0v8HjgvswtmdDBO5zPckepezirHkS24B8PezEWnUmbk%2BFvPwr5H%2FRpWtRPemx7v%2FfMVGS9%2FO%2BSgb%2F%2BKKd%2F0y%2Bgo2SkccObdrYZKrjs3rjk82McWWRnt6%2F0aayD3Ldcdf2qsKG9y3nKaO%2BuAQzxTaUz%2Fhz%2FXIqBGv1d9cukV%2F%2BHnSjcYpQN%2BesM8FI0csmMcX7%2F1g%2ButnRZjPBoPKxwgm8lGfTqQ92drsWTcs8Qy4jKIXPYimFQGTHPQ%2BwkPWNxcItK1Wn5kjB9PQFRmMfnK9yNv1es71Fv3WTjO%2F9imuYP%2BURnikSOeK6LxadBM9%2FRawSvKcwgEueqvfUeGajiFboD1X0xBHUx9eaXl4j%2Bx%2B7sL13wWHya0BBD3vKcii4fC63CkTL3hld86mC6JlWEhzIx8MpbWH8Aw2GVxYroGUz8DRWdSgFlelQMc8h6DxTkN4Z%2FV2AfWzKkQA7p1qAHnlJbGeMxXkxWwFDldy7WJvkUer0lVm5%2BkrTZ4DjEm8tcTcLKUbJQbT4b605a%2Fy3%2FRxYZhoTFb3O3Q4GlxFBWjBtJzAtaOulkyMK2K0tMGOqUBkXSptTqQw%2FDf94fkP5nIMG5Qxjrx%2Bxv2jdUJxNfGky%2BD41oBAXYcr5xzbpJwCX9k%2Bs67YTvoNf5YRt0ADELLWs%2BhS%2FkbRV7DCuekth7I0fZhG3%2FdxKpPQ5jxLZuKhqO5hChEWfnqkddr%2F0iLofli%2Ffr%2FMUyjZPfRtlB2AApAl0kFCJD16Tds20bfmW7U3BT3BBTpgwP%2Bj6Sz5V%2FlsMSKLLEgGdyM&X-Amz-Signature=81d8793a5248f660d61cae450a6c0afcd06d69affa10308ff4f5b7b2b0707411&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
