---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZLF3ZPV%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T051936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCPzWjApbR0JBLFpZHSbPg1hao0GaHHkH5ZdTqqwQpckQIgCull6KEB12774EwllcoHNT6UTNVl1l8Cy9owF9Q0WF8q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDN4y2gQI1GAOKOV%2BXCrcA3VLSRHj5lu4cXCGa1sZJVgM4qvAD%2Fa2j8IGqwBcH8rZ7O0bt7uQdp788Xusbysa6JFQgML73Zt%2F%2Bd6E7IpyIetWinfsBLUuVr1jXy0Jlos%2BnSL4HzGYIDPBtltRKs73TmvGhU4swlT21fy0Cxwg801NMTKIcWy5mQv1rIv55gMk4l1VxIZH0luLx1YxInlRue78M8%2BIAJGfPC6y4VHpp0dkCQnKeS44p%2FwFaHDse3BMm5NXdO5SzHEkHKY5674WZwEP2d2dm2yeQDZZ5em3x2%2F7qmLYOWG%2BMrtswMyR5WOZR4k9pOuiWu7UGg0Q8ZOe07pxSwZCTXdZpj1kFHZJXGl5zOkGBynpW8q7HnJjF7sCZk7isagArMv7UDif5tFSAv98E8zhePdaPrPNr2qnwP9loEWIsRwrdgmLVIeo2LoLLDUDMHDBZWFy2RTg6oDHG3oFkFfAjiXRB6bJg6Rozkie%2F7ZkdIyTDjwMz8UcGDxDWZWJYwz%2FLIDpaubb7a4QGOGHpLQC7JrgKl15F%2F2FnYtTmxyoJB9SN%2FUiOLuZWL71etCrHW%2BUhmMLd5MBJbZJjAaASXZYwNgCuEF96Lu9%2BU%2F4fMMh57938K5dYgX6EtRwpFZXs913lPx1yQBuMO6BltMGOqUBK%2BW268Nwv8m1uvkYV0rNxKZi7j3Ru53t6Ap1%2FxXipv3kzCRI%2Bp0hYcUT5eta2Wvp4TIJVk1BaNwW9rkjabvOq%2FiNWP8cOakjA4ryNgL68PxGEsXuHfk6%2F6GFfiVFKtRC5oCV3pd88HmGMih4oRSNPpXs9olQY6Ar2e6ryTauwCnDjUg%2FkY5zYsfdkRqTFOS6Nt3YebAtaRqwQoAhL9%2FyIG%2FwyyhT&X-Amz-Signature=6d520b8d4ba26a867c01ecc29b47f470ce0673db7e71ef12b20fd5a729a61265&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
