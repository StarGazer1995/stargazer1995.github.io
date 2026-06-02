---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TFUT3MZ%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T082007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJIMEYCIQD7eTfTBiSkROgLiuPclNkF0Dzkmm7au1dVRnVYp2RpHQIhAMZRkXEYYzQXXJmjbhlpD%2FkbPvnt4gX3bYdD%2FD%2FeXESdKv8DCB0QABoMNjM3NDIzMTgzODA1IgwdqADP4tkBlefZxsQq3ANhMNP0BJII%2B9W9D283c0paQ3ltA4%2Bs6tBanMsw5EA5Ss4uC0TCYSIDCy3I%2Bne1IxjZMU%2BoR9j%2F36S3FrSTGvdsE79FdBqqw1GaUabAJrcwp2XKTZv%2BHKNnfif8NvR9bpVtoMaGQxrvt%2Bm%2F9LYQuzQKj3f1P8SrB2v6skn%2B6GZAoGqdqgHvT%2BzcsIusV37jGq8HJ8ITOs5T%2FqZLDbFhT12htxTu%2B9zvQwMt%2F7G2fBJ8EyLRva77zG%2BVYbdf5NA12gRzYdDnjGbRqd2rYw5I%2BskhwbAUEHhV7V6bsAYl45AOrbcTWGIWmSNsbnfLGJ9RHk6VRay6VpkvmL3VnadmgoZsnCCvgVsx4Lv78KkqgtLoa%2FZOlb9sQaVRxGMAyLsBrw9UA%2FfEaRip7g7kdEi9wHAoIuRZDR4aFEkUmV0tA24sEA5cE4iOY303uzmZ0f9SwGrYI9EBPNFhZIOXWioEpx8Sk%2BOqzY43VQ46tNqZzynUo5wCMriu1iLdy3FOCvmRsraVKhb%2B4d8sS7LC3J1YaJKu7npKwWpzrvMJE2XTNZG6qzuMMQPc92x6cXaOI99bZl%2F6U2fGQIjDv2NcA45gtz%2BHEN2nKzDTcRgDJLyYL3U%2BwwBtkF5%2BoP1eJvNX%2FTCno%2FnQBjqkAZ6eDAulT0h60ZSFNAIbibFCQ2t9DVRtqdFSQEZF7AtTb0mcEuOQOvegKrn3J2RxahdODk%2F0Yf%2F%2BC5zKH6xnVcpyVZ3pswZk%2BcA6%2Brge6Ver4jJCp0SPXUCI%2FeZFxto2ZdChiKlMreAePAxxcZcSQgrWwciSiKgTeEG%2BY8FG4timrF3oIL8duYA9zj91B4qghW6RKqey2ATzkn5yiXP5vFZi6gxF&X-Amz-Signature=09d5ef18d2da377fb869a158bf33f4483aa40a68b63bbd0681c609085fb9c7f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
