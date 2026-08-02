---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C4P4OD4%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T125410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQCugS9X5Bj1iWwa6Hq%2BWLt9uOC8lvYwwMcpeH2NyQWmwgIgXrQesetFrMHSX9r%2BZ9DVZv%2BwsT%2FfZSNMU%2FfjUI0Sk9wqiAQI2f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCi742Rqc3E5kDU%2FdyrcA4YY8798eY5gNNYr3VSjrtLdw6mOrLoAq%2F1pzJexknm1RxggYRs1vAkpBNv1K9T0cBmyRajb%2BFpixp5IEPZgXfeqMyUaiX1p%2FTTaN%2B2ljb8hnQRAZ0yostNQ0QzRMX66OSJmhZbP91eNyP5KaNMCrG%2BcyWbRrBskKJ7DkCCGPrx8pO%2FI20AM%2BeJh%2FzwGE7XvV3he3jP%2FaiTpFmr8VqLPemP5X3h%2BOIkISa68EfQnj%2FC9bA2IttTjSP9o01SpH0i2sTYgVCkGWBPHJuffwG0%2FjzJwlfj7ULSgocv%2FH1%2FX4qfrjZKpGeYfsIfK3Ztgw93zsom%2BCx9i64PqznVgH4sxqn0beAJSxU%2FtadMJgoQzC5JKd1j83%2FY9%2FEq2I%2BO%2FKRuGvmIMeHwCNfq5JEG6mmt78LB4YtQi4DGuuW%2FASzzH79oxe1mclWc6%2BZyOeAp91KAPhQcFg6Cw9kPYo4OebWoIx9gxE2%2BvQQSbny1FTAejn6LHLMr9E54DwpDBnFFhCdfQL1NMjSe19zLFt5mFCual%2BXy1xOR28DbT1%2BbCAjYUO082Iz41Ny3yPykRIjpaU95cSOUdqfm6sDtynswVzzlHNSkdxbm%2FPHGYH5ES95kofEpw78SFVMXnj9YC5j8hMOHwu9MGOqUBGh1LyESFnPecvAsZ%2FQxEAW8hyPbD8%2BHnmxbnB9043h1BErPjbpzOLEQVdG7KNhY%2FfVIVsDTvocZHJZfP0R6gpBqaEymW7D9pri7%2BLPXonJyOx8MRtvlA50OQHOz4GI8quYtsnhMI2546Zn%2FyuB1eKepeX49FpO6KTKHfF66V86G4IpIDeReMYQ%2FJABSqrWXd%2BE8PL2CkWIBBhqvENeZHjABGAahR&X-Amz-Signature=338a73f35d73e4fa69fab33ba1208265461b756d6fa5ae7ccb19e6db2ae933c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
