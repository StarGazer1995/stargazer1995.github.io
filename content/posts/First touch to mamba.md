---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZHOFWOY%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T073927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQC%2FKCEXAOFLYdabeaA%2BwtuN33of9a1fmIHzH5TOUK%2FZ%2FwIgedqRBUROYuaoiBJZzrG6wWuA8ZOo1rtwUe3K3glRvbcq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDNceXULqCqv7gIdxdyrcA8FP92qiHuU3A%2FF5IrLEcKiQmtJkA3FSDFnRhs%2FhpwhjE%2Bm4u2HgN5o7qw5DX5f%2B32047PXewdB1f7dKmm6Y3gt18hsWP%2BX0IraJ0UW4oZ9bK95svuWMdQ9Hr9eMosL91tjDx%2FM%2F1HDDIJiQg3d9k%2FoClavupVCVixkLzMB%2F1pPNKWTv6LOXmeNkJ42LywI14pF3e%2Bw1E6JTvC90rqEnKL8uElxovjk8lG8BQpiiBObvEdt7KkrGB1KhoQzkpCjfwPJLTicWBc192G%2F7r%2B3VxftPfR10B8ysBlW%2BZs%2B00zq5cGV9Hdoczc2y9FOHFgwJ103p8igVYiul68MaKOyCZXj%2BIgiIOivYG%2FOowGeL%2BJO%2FNaM3co2qKYKyJVMxdxihom5i10dXWpVB3XayYkgoknTDwrvZYnAi6%2B57YpHVAkKPQfynLWCImX9cGkRfZ40gpK3J0k%2BQQnTLmEESLiTRzTb2gXJ%2BWT0ynL4TqAw9PCpCd07b9T2Jb570erkFAdHbXeOagxgdfQKgrQ%2F3BZ1PaZXwaXsKyE9H0v3WGM8DmJ4K01I79wnPza%2FFuXilfjU3CIfVJVBM9ThDO2baKxWg5AYN5NiZaM%2F6HHU07tAsFM2TUNc0HWJAkBZpLiRBMOzzs9EGOqUBgrOlTdrNSY40DubvCo0eAm7KttpXKukNskrm09G5nnOvrPu77JGDRUJmioe6VAAZBREfXih%2BnwcKVfTH8n8PkMWF%2Fet80Yo2Wqs83dach3vbCIgMbMd0NiKefOAm10NCUSlRaEpxRBn0gvJtmv0niW8VomloKif%2BbXvTfPw1iPeYCiEoyAk20SCizLAA1TCdi1xk0B0ZVqEjswp7tCFfsEXVOEK6&X-Amz-Signature=db4946c47b21f5f5a987bf1d4d54d48b6983769a5faa13047629b2fd50c32dc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
