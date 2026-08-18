---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665USVN2Z7%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICSNph9IFfGhp9%2Bmnanf%2Fft2bieg%2FcvKURfwp0Md%2B2MEAiEAkaFha1H1yUCkSjb0rg%2BcRsJGxx0m6zYg5nfco2nNPg4q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDDtsSj8h2QZAOkfmLyrcAx3NHZKCwVYjNilo3oNsJKcMMvJxytGSoeGeGLvTSCH%2ByypUwPBYMc2h%2BsvHNxoM2nmQfaLatztPg8z1X0mPlTpFuNdQTM9%2BMlkNAmh6OvjOXGyPL3n1WZO9947dw4Il21GkUQFHZxovAdXDxVJopG8q8g7TwekGjfGuc%2FMudjRSuWnTU%2BZ0di4gHD2%2FvVT16Cs%2B7oQppBkwzr8HFEcJ3v2Fp%2FXhXMqP5bduYe%2B2ZMcJ0A3xebk2RB5fZynSQJyUaL4a7dkuQ7SMq2CmTurYXyupoXtSm87n44L2QumI0AxKMXkbd4mXTpc%2FRYQHfcNAdpF3CIqkKbqp1ko%2Fgbc2MsMtPgUmX6b7F%2FK%2FhKQH0uCdYx1HWnUKFerOvzA78XGsy%2B6pR7NLbddxClHShbT3nMtALYc%2Be5k6uqRfmlloW5qlT6gI7MzaXScApMRk7scg0yBXVDHwZDa82f6%2Fjta839Fc8lia3o4cvDtuSE7cm3bXNuFSvG2AZrqBYHNuS%2FEurTlYERwrKFcefjTGh7AqP%2BcEVmXqbL9HrxkX2D8oKYbHNd0hF39sA9krh9UC9pbJslYvzpV7q0RbgRlSh%2FDUzQ%2BsKUZdA0ynEg8V1kr6Pi9zpE9eG4qlep%2BR3OXKMMX%2Bj9QGOqUBUDw38zKoG9R%2FE6R0YPM7TB13zBwaQ1O7AETRPqwyFAHVfOSLZ0so7kNnWknnpVbW1nwQaWTDe%2FgntEbHrKMeXqhSO0dhZdxHnYm%2FJBO6iuIxPheU%2B7ego2ZU2yLYLtKgsltVbowDFgmldR6mJ6VwahltiCtfSQbfSZjxjIOuFB%2FKIDlLkfQhLTy%2BbdjHJGc28YtR59ekGL5PI6vnXZr9YPXOQJkU&X-Amz-Signature=a638e7e1d629b7ef2b9978364a0e148e795daed9d328e8b8545dbcf73e24f421&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
