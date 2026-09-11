---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB4RU3B3%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T122524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2l5H%2F%2BnSb7HuMC7p%2BObxY%2BB7p4KTpQdGAQVDLbR6HRAIgTgoFq1SmZFIE%2Fgpd7JSG63msDHcMiBzLgvaAS%2BmC1E8qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBA4COlSHMY5cM4vxCrcA5w8WIf%2BOd0wBy%2FcogvxvRY0uemduHk9QEI73OFTi2veCemTiC3kjJyo2GfDmp5xBwrUFr%2BWgoghn3FbTLpwdRn9y98EEAIGS8Ud1J7lb9lffVYSQKbRvlmch7Y2vh0YMpaBML4y8TjpIlnT4K3PVUczsN9sjsQ3EAzDyrPA9agYk%2Flq1ycz98gdDVp8%2BB%2FV5iOmjgvqKtUh1d%2BUVnMqOgJnbFSRY7QHBvOCGPtBFR1AnG1uuF6KNnkHbKO7n5%2BtZbgtNYE442vz7sym88Q%2BH8PQHk3hNke8cu9lqtIgjx9Ou%2F6QYXDzkPEkgJlyPPOuyNxy6wnlLByc3SyH%2FLItHImhKCdOMUlOGxIWdOWkYHuLCpPPmYpke%2FXe%2B9UsO4RRpc1f%2BfYFvE%2BH%2Fa1qW3dM19Ai81eSIMyxVeWWWsAz9tzGCpPqgPZMf9PuXO4DRQePxUBoU9dblcNV2h8QdbKHyezs1DBaarPOzY7285j7Y9e42T8Bvp0b32xazgUUNhmGLxc1%2ByhGMub7D0L%2FNX9WDyF7F%2Bb%2BTgA7RlW%2BNjYvVGyGNwQXXagzVFO4lI4dlWqKARrw43HAFUomqjs%2B1YSl%2F36OkOC8cTkpNzYwLip%2FPj64v1o6WVNcBC3uwGLeMOyyj9UGOqUB9w4JVXolursNwe%2FnIjodblGm4PH73EGi7pVEqrA4JYoS7n0O6%2FdLFIG%2B%2FkAywkcyABCqGwy%2FGENt4qDKHcvvPc0dBT0ZdVBcehlYZiUMLenLy14arNfLNOG7fJChliD6bOr4vhWQ1kpDO5MoiBgeMq2RZTQ6UlaWD3bwzCujXGhCzs8Q6KeHH7GHwR1UtPwIbfrlcX1NI4j9bmnkCJ2e9WPk%2Bz6P&X-Amz-Signature=525fa75bbf026124753ea42d9695a0187b9b6ac05f4f34eaad98c82e6db49db8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
