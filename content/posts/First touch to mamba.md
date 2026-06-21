---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMD77TUY%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T023016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDtEGIXknXXBJiSPCFn6Anj6epjmDfjRPmkIMvkoKpS9gIgQ8hxYGwhD8SHf8vquy59jvFXoAS0HBD1fYXRdVIYNh0qiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOcl2PPChop79H4LoyrcA20rzBhqhmeAmVVr%2BHCMk%2FJ46s5Vmy78JrwDEd4VQvEeyK3CVtlFvr3PXyysliSm7yvWfcDbjc3y6RjbUVrjzhYX%2FMS6WY73h%2FkmVpFY9QKTj3redickCtlzGS5WcZ7YS7SG7qYPfGzwRJUfw3LKopZZhP6cHP%2F7PCzeoE4EQQyid1l5taI1fj9AjEPUE1G7a9Z1BG4357DwQcTXvv7NQXorvYXPVrIA6oaToo3x5KVmwkVB1FkKxlpjC75GvlzsatXJxC%2BbvJ4wBtwvByi3pSRA2l94169DDmihk5yrn7rqrhTo%2F%2FNw1sqPJFvY9QBKjRGBIYMrB846y5GkTYz6ppdjCeU%2FHnwLpG9svJdUPIz8FTKnMI1EqQj1n9QChZwQFgsaS%2FN4hoAqC8v1AVpyawBCN4Yo4IxhU43z222hi36DcrnFAlpsYuimX5MmFTbKJE3P%2FwC%2BAh2YbzkvGA9qMjkcDOFleQAjmBXadnU4oxWg07h1OJZJtsJ5KeeKPZdkZHLXJcFQMav0bwjP%2Fh6ji81P50PzYPUR8hBkG70O8eFwpuWwuk2alHBICFiCynj2nq72tQ6nBrFdyBqX3sDYKwv6AARjgjKPzTL88yNOgAwZzrrRCauyjqX2Cps6MLqv3NEGOqUBgvV%2BcJ4hpbI8dcaCjkcw9QDJ697ey21teLtoQW8%2FB737ehDgGx2cgarokAaAcrEz1cx097T34DIbrRtCWB3IMhx%2BlkfwndxauuUuJ6thgkFQ1%2BaNGXZUnT5MYR67xv%2Fptyl7XWbK%2BDmgXD%2BiRvHP0XlSOiLQACAAeFNBezTy57hLcVntGrTsP2x34HWAwElQ2q6aHen253h5N4srvD12Bgm%2BNl60&X-Amz-Signature=b49be8ce724708026a93ad8839b6401106c6824539b4c54d6fc5d72252968968&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
