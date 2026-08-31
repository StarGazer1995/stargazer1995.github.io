---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHPTJCMM%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T211042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWRe2Au28P2blcg18ZqxQa6%2BkZUVzq3uDZ2%2BY%2BosYElAIhAPQP8TbelHPst62%2BuXQW000g8H6T6o2YKA6vkNiPHbfbKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGn7bHrlySQOI6PWMq3APMWahgZnmCVPyig3AsYaF8xlDwm6utExDetRccB9mbwwH3jGPW5d6Df%2BRpSNJspmOaDmO3XwmWs64mXArIVaKxs7nWB0hPgnWuvUPyp6yjT2eg%2FGzEEpLrzUAYw1D5NPQeoV4QkRDRbpNAzAJulCgpmpuzzEdhI816c45zAeObnLpSdOrIsfNx6N1WFnbRsVjP%2BYoHlWl%2FqFvBTF%2Fx7XAON8yeWkKU%2FgrvMG06X3f2qGLJTiNILdNXFrUuIMIzIQYZePIhjDKLFLAoapxXotNo%2BUzvakbuMFm%2FNLR%2FdpsOcTf1rYSXDgDHYavlhtVKWPxMq2Z11lSk3HukMLEG1c6kHYSlSbnD0yhDFH%2FgrZhBCpZPmVHWbzR9aHvuXxQBi%2BXQeKVhqdjSIlyCOuegcI1iLKOL%2Btx1rAo%2FIHlvQhJDPbEwXBNraD3scQLSmIFSzMy51tn9pm8KPEVJth1aujDDy1VQDYDQbM7%2BxN%2FfN61TPP6uLcU1YwQl%2BWUecfOIfS4pqKIsoDw8oKGWkmbS7mXYyJz0njJbOtPqXnQ%2Bid8aAz12TnMfMBKOlfq3uldulfGs9np5R2S%2BLpTaIot1Ypm4Awf5gje3LI1yIhXcqaKVjZ5rMAkTASH73csYoDCy59bUBjqkAYhozK24DJ%2BWcTGW6ub3BPY5FQ5uuI1meJ3sL9h4zvi6%2FCasFXOvsTASjGhaiD8rVDIYf5AZiVEnueXriRyLjmopPdbOk79ra2eyGLrMrtpG8HFnjdZYFjthd2nVFGIKfMwTgqxV17aoFvJuB0gwwTch2jxY8bMMdvGCcgVuafVOjSp9zcWf4HxxamcMUe2YqWxvpCrOCRkSrVK4bRquOGOlAFbp&X-Amz-Signature=d9ac3b5a3fbbe31b7f3f30a20fd0ccb0d3a6bcc2b3bd66f4451a7bb8277574ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
