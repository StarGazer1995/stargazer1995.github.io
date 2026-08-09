---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LHGHAT5%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T182236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVWT9Yoi5zUVeHCaBQGW0oGUKf8qR6fadF4eJdV48jSAiEAgtvTFOIbPR54pU3XAlp0Hl6VsfqRf1IVAlNcINjklHEqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJHcpudBY3%2BtrQiS1SrcA1zlLWwszy3mBMe3nw9z%2BogpipeJSKY%2FYz5H7tLuTDcPRG5v5qDy6r5vyhcQWAO93ccZGtrhxwWHqd%2Fu%2BAEkdrNtGLAycIrtbSHIT8stQwbIAeUCpGrU4HlCn4q6AuZ5GzbrRJbO6TLlSfHzCo2cnlNGK2CWRbhWGO04UAKqbFPFdMQZlR05pZzvgq6VHrxFPki4OA39ZDKEOxiw%2FXQnJnTPGcyx%2BOMJjzLhsXIWcbNf2ykDZMKSyxuMqZZ6lzC8TJiR8thWAt6gvi6Usp7DHZMQOojBq8q%2Bjh%2FpMQpkk9RgtKqqUfi4Mzmqe43wI52bSDPF9W5sPZ9TcZFBzw6vfE52%2BwJgmSZxEnaio9uReLKumd15DYR%2FWcVPbug%2FuCsCPqW1lgIntUPsRFL3NH40jdOV7k6F3AYjs8pxVY8q07icWdlcDdYQjpordGU1yCtBU%2FY%2Byz%2FWwMDzuQ3a%2B0EgkCCh6K89DrOccn7ZQDxTL0hfWYcgxp3yrIFigh5Btos4vAX7sIgVyvwZW3Xn8GQbJMVQz65ojhDaS5fEgZzIOXgIbjro22m9lRhtmMD27zIQ9iG%2F9MraZja%2FOD%2Fwpa3iJGaEankPlV2VuZBvXlML1ad4M19%2F2et2XSkPz76lMMDX4tMGOqUBY31fyxe3U1cxgWJx6B6NV%2BesF9p5OH8wDGfOHciysVLHUPoBYE1IG02zCt7MtkwKdxQLXVyNaiemln6XrBcwo1R%2FO6xLNh95iRcY6J%2BxMaD1tmyqRKCN%2BmxCCmnZYiZej7wg%2BoZQuovmuBaX%2BJpbT%2BEY8yh1bqbddb62b5JFLOWO1aDFbGriDP5XGhg8HMh8E9Rf71G2Q40mTyQwEVTg9hfQ4p7d&X-Amz-Signature=a367076e0b0e168e500fe71cb0954bbaf7e720485c8c0b2ef018252c2ad97a51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
