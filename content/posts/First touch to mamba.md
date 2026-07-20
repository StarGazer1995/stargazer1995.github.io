---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXLFNE6V%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T224554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXBAURqGiPJ0ig%2FKvJxhFPzbP2MhyyqJRZG5Ieb56XKAIgeEL%2BRdle4pOk5YJcC4%2FbRlUaws06fNf8NhsZNfU8kdAqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLOAOzkMTK7v26drQyrcAxfiuQoph6JHIwzRQhzsfpvilSS9AQccOhYXlW0bL8X7KUh5DRLq3z4BUYDZrhl36u%2Fb7zX0zCypz0r9Mw1UkXm0DtsJQPlQAAFxp%2F3DtxPrx8xp5GKLmoW6q2nf97gOWJMdBsC1FIIuuVqhSluMrgkKv3uqF82F00b0ii9a5a%2BdsYZ5PjitdgUGZGYlsLwTUA2Z14TOzi6azrz94%2B4RJ%2Bm%2B%2FyF%2FVaPT1UGFFsCN5fEoN3kNewo640qGaevgATgjZLVAvEASlxYcRhFurTDp6C40VkUc2d1NPZfpGH0%2By6k5vAhmjm8lVd1%2FLoUSfVxrizgRWRFkjFH24uWqaPx679W8j8FCdqMwXmiHvsyYge1Xk9mk6jsE93AiuQaBeg3tyc1SWVaOH6cgTfOz%2BVaDOFEtaVQHB3XCoYnpi48itdGF7mpfFmU%2BSZdnh9prS4QqgTFdgxgugVXKWCSoM7B0W8SehwuyZmtsEgmpns%2FneVE32aeR4PPiJdRoBgumjqXjIIAfaJhmO9xQurG1ikIGVI4RyE40tlaXaGvO0iLimcvjJI2MB9kvqdTF6ka2X%2FkY%2FHIvXAHT7Mb54mvTF5ts3Efl8Vd7v2%2BLuXEUQ21jjeLBcAx5S2qp9hU0sdWHMJLD%2BtIGOqUButQg2gfvM4WF2HJFj18QcHBfkY6EdzlhX2PJZYRXeAx%2B57xGV2T31VTFwxCj0DxwXuDrWm0wHZ%2Brbo75MU3auWNND%2B3mQD%2Bgpzpcc%2BgpduycJTFLngH2o9ZPbzqbJERNt2m3trrNLKv%2BQqLC3acKIZNZaMKb%2F%2BRQXF5w5NlXEOfvrV2CcAtXVSepr31a59m586aiT8o3Wm0bh38ydT%2FqUWld%2FZVE&X-Amz-Signature=cfc28d667d4229f1f2f4bde028ff4136a3ddad796d323c6e2590342f1998f842&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
