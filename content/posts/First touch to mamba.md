---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVGAVBMS%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T054630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXicbhibUclpjA3RxARqgt4s%2BclSFawZiJoA120fF9aQIgMrS62PymzDoeE2NsAHqNvxsfJjBNgxx4wi0c%2BDlSgI4q%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDNpUL%2FHE1E4yiJeeaircA6mFyxD9AkHfx%2FJp4iz7SvPtU2NKBwUc9MAIF9EkB6k9zosuwPpsA7lanNgUGkLlf27VXY1K%2F%2FCf3osnm%2B1OUUaMflL12xxrgme%2BT7XpyEMJz5cYbb8KI9l2VmRans93cfQaXCfM4olWtu19k5LzdrPiklXE9b604XNctmHgE1rQiCS0HaaMcw7lyhn1aHNrp3ngjqmSqvGSnU990%2FDpH7FCY4sun%2BPlh5R%2FHhJ0L%2F4sg42CXkqDCLP3OXA2WfgymWFmazxGwMwueYzo9Yg%2F3smY7zq5bPlcCMO7O7UCaY4%2BuSYHQ2rk1z%2Bdq%2FU88QXItioI0aaSz8EPXtuVHj7Y%2BpKukbisOSgG%2FLp8H8ot5jaw%2FcMls7u6sCuKmL679yXKJcHvWFz8Gdv7NPkEVw9K%2BBXPhywzGMKGlwKoA0tfH016olIf3gYvv23hDk%2FfcimLttqj4o%2BxrpB%2BvvkrZe6ZMX41PctudZec%2FNb7Fv4WM1VTId5JdTc9J70lpkyh8S8VjM5w2j93malEwtS2ziOG8WZXb3duLnT1JPWqRJE4P4Aux%2Fjz64kgDv2DBq3%2BxnDyyS3q4YdqYvLcEMdF%2BzYp%2FTE58aijq1%2Fe3ciurunjlif6LBW1DxcCKaLS%2BVHqMJvHmtAGOqUBHd9lKEq8nLghb2ggw0ydNMoMY4RiW%2Fg9wcWBWFO%2BiKKkeLK5NdUUJA5Inq9Z4SM%2BrEXwpFZG5VlwUFzAMvWzxu9LLwWE7zfqO3PcHynXhaHbPdMecm39diV99q75AJI5tlDCc1lfAaC5MOvzfx%2BfX5Kok4nzbTxW5EJXfIQWuhDxsYqTFOB8az741R%2BaSguyeJkBjNBVyIAIHkOxB%2BUjr77DJssP&X-Amz-Signature=2be69d141145610c3053d01c17322da341ad8d903caadea6bcef95c462da3498&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
