---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CKI2LAI%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T101714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCc7g5V10cveUXcOaOPfNQ%2BJo6uBzBYsMRf3746puyeEwIgUma0yBCDi%2BXaJC4%2FyFSbvCsjsXzXnsV85CvmfvBMAg8q%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDDLHgJRUnrjjlvrpBCrcAxxBGO3PcIWWWtcahPX5u%2BGpnVmY1x6oVfsZxKqXA%2FesuPt2hfjzPbHxTZj96DP8VGQfBd%2FJ8yo28ZlU8W%2BIdqnmu%2FTx9DTvHxuXiLFsESW%2Fqe2K6rjh6LgJoPLs38USfPSrCrEmbz9P3FlxaSV9OYBH%2BxYlR98dhm5IGmWqi0Yfpb%2F1Q%2FRmJJ3PCuEfe%2BFuaemhvvw0jl6ZNBHaBczxXY7OuQClnCyRf%2F16bkRfKFnL0JLeDHZngBSg1YQtbaRQQ3XO15HadYmaudOBg7slWXLJq6M2kxMAQpdTbMrPh%2F6mowyfTRGgvSvv4r%2FUzNPqAfhgyvVmc27jaC%2FK7HGyQDixZb6S9%2BQ6IkrE9fMfOVgAZUsL6rkGgrZxBK1XndDRvyPo53DEA%2BM835%2FT1IsZVWGTipiLaLxdRIQjnUaf6iundrsho8Ya2qDEbZ5pGhSIxaVOybDRizKzYtlkw2PK5DPvXKnexVYACNEFb%2BiahvGsY4Mu%2BD2sVJ4FoBk73z9kcAmrxEb%2BauyKZo%2F%2F0lvegkGuiruxsFOJF0AC9XmUfgDsvIfOk%2FqHD0HEXl4GL15t6qp3rj5KF6m6i7R8jFOM%2BonilzMhGVbIli7TnlrU0uitSMFGRAN21JpdHMNbMNfnldQGOqUB2ZgSoKNIlDDO532K2WI7J%2BXR2NpyrXGjHYwcn0Ke%2FnN73Fl%2BuiOgYXkR11oH2EAZ4YasVIrKjnjiJlu%2Bbm9KyEcCExE1JWvf8sKlEKQegbe6%2BaKxfLkUQFauoQBYQuSUSWHqTyl7Q%2BY8nU3oLbwUmH5CIjK%2F29NpUfc6AxeWn4wMHjB%2FbMqDun8rJ%2FTAn6%2BE81qBkXZzeG%2F2OBE%2BALlHCSkmaCqv&X-Amz-Signature=51803ccf00f1bb7f67a5f34aa9701e664d0bb6fb9909cc503fe97405c3e8619e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
