---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TQQFQ2L%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T111037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAb2Di%2BJyIaoH98bDL9Ud50QJeO2dsQ8zi6%2FAhnronGLAiBqjOSjZ6DV0rZLONtKn2whc%2B647R9uqLGGHlDFwMBfvCqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi7gBeEE7zigcjINwKtwDu%2BQtJ5kJ8H6KYvgWQ%2F%2BRA%2FX1T3bRoVYaMRw3dVLJTVcFiXH6CIC2pQK9r1w8TyIAjKcO8si5MCnSfi9antTGyy0ph1MF%2Fjg4%2FMD9mGGRVkjilk2IMHj1Ua%2BzbQFW%2BXx1p3t%2BTLRhoLitCmfgDNeV0EnZ2wIU6IbYWe2wa7qw0BOO6tx7sU5%2BSg7DLP9qwzBB7aMQiTf2hZkQyDjLHgi77LYcQxIa8uVmo9Y4ErW1R8LB83bOp2YZGK%2FURrfuVv4%2F0AajbmrHjptDbvY1k2%2FPDuUSqgJkVqt4%2FW4SUm6QVCCVBr%2FidvpgoTNA%2F0wTeumDWtPdxw6tisTQMXYOqk7nvraSVThRtH58shA%2BVeq8J%2BsFPB0wBWtaO7xEFSHHQ7PHT7PVsCacCCyErP4Sc4sd3nMmz3fhAzF%2BQSkSW9nw6C521r3cOHXaS7qWQMA4vxkhS8o2owTuhAtU6foLf%2B98TqYhHgVQfdBeZ1lNRZ%2FsqVtWsJu8hX2FclThN%2BH%2Bu%2FUcwgXx3JYZeKT3W5r6Whhje4CFJxeYHY3YTZhZlHdwoqdM%2FvwyQx8GdP4pPtBevakmAs68hDiVTqTq%2FZSP8T0hHXEq7%2BDr4JXlQZa9C0VE%2Bz5hh%2F%2FkcHr87xcmit0wk%2Fm20wY6pgH4YU8I%2BKehTdxFZENTk9P97YZIoF4NQb1A6ATxIygbFAxHKoYYCmqRqUJElKdY8uy67nprRMjh9QGajlK8ltzF7dAcnU38fo11M%2BlO9HNPRw8IkKNrGfx35apDxb%2FkDd9MXJKK4LOjGDz6yILBlYsPQw2h%2Bs69aaxTcWIWEboiJ%2FgDPmZLWdEx4YZ9Cbkc4KLiNLndfQgJedodyfWBL3y5Bz2CAyiM&X-Amz-Signature=f784775040ce517642d7b0a8ccac6f8dddf27441a3d20a27c4a1e3bc1d0cbf4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
