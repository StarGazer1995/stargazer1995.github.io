---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6TAMUZJ%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T020729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9ukCSoBoOgInQ6Er7TtX7%2FEftrKxr%2F9xq9Pd1z3HezwIganXSc0rfdn68IcMpho%2B62IAqBFCdZDjEuaUst%2FWXpeEqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOBdZ6ZM08%2FPQUWsDCrcAzs5L8YB6h6XSJpPmMBzLboFbxBdmZ4p7vH6F1LO5beJ3qeXDIGPTTtaY6TOY2i0uHs2N0AeGrJw7LZfpOdv68AEoMCogc8U1wjFTWFeBcvUUYHUvpdfld9dBvw8nlITtj5Flyx8pzsGrWhl%2FaLj3xqLz2ABGdPw4PSsXE5u1GQ4oMvNkGYu0WL%2FwGv2H8a8%2FGkETrlT7anP63Zw9428jIORv6d%2FvYR8mgVGZ8Ubw5LHbvPYpOG%2B9VTymnHilMJg64FycmhyzFmVNLlPVfjyeiW7igMawqne7ZT%2BVOgfFCy7n3eBKojeDQIFwIQ480smI6EdrcaRSy3aQXrRvXT2GyFjlWmI0LkQ8XyRBSztClcx%2Br8X8k2bC%2FFbk1Z%2F%2FR%2BlNlV8StH9wBRMwn4Sm5diwpJVVelEHW6ikgIW%2Fu97iyAKF8EoTNu%2B8EbYPL4mXeXaStO2cIUhd20ebkniyREAajuwmWcZEj3nRSFSEf8xeryurqpWZ4lKZ%2BK7uCpbxQK15lTNAAlWnyDH4iloB7uL1Y3tflRDQwaR54pm9nCMuHrURnSH9h3W7zHMn9m4J20mHABUV0WB43iSEnBkpZcU0WJ8xZNUkwOeUbJm6nQr%2FUcHJECfAj2Xqr%2BP6KAGMOPUy9UGOqUBNEDpcXjnzpAoVZSNPygLkuiVUs6a%2BX9%2FWWI4tVnvTjRtI4taUJQ9N254061L49TDbAz2cPTSkSgvK4%2Fmim1Cw2XGw1sAzJVzutQlGUMJFqs8b%2F8e2EiOSRLKZykPpL1oEfKyXolgtBA5mcXBFRWMwtTvgsoFVPq%2FoGLxLXYycKVlXUNGCDxRkJt%2BmCkFMNnj7SeUEx%2BmiTxQofM3JYUNI4VIh%2FaI&X-Amz-Signature=8efd27fd8c21a455cc13ce574812c52317b32a91408efe2b26f7f45baeef6531&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
