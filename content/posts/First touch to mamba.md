---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VC6PWLOR%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T165323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQCvNr%2FmnBAbS0qBKg1SKtGqFLTcFdgHjRTnd5XUeaN3cQIhAN2EcDXZ9XIeUt0m5zAzM4CwkSdERarenJNAF7kI3fCbKv8DCEEQABoMNjM3NDIzMTgzODA1Igz1M7WLqkGqYHl%2Bw1Qq3AMXKLhCZA3cMSA0AGNGME8oVwLHWXHBGntJEAN7quow97qVCqez8iGP46n7VYIa09bues29pigOaPThOLGr%2BjdpQjIjFOu7IBRuiI4H5BwXnZJMCfLjWmW30BlWLhqfEOFIoaRTvLphX6gTmrnpFfJGaVmOCrRO8k92FyOmH9VdyB1khbOzKzQzJpYCWai01gK0AoqzZKYIigSPXy0IoN3X9%2BOdldtt9t33M9hI76ZrIJptUYrVsHxz8FIvto505yR6fQt0wGp5w5bARw9T1x1aRNfI4hRBfkSEoxvc2RRRox%2FOErVmBt9sXpmgKroaIyam4UXos8%2Ba4XseSof1o%2F0ABgqFH3NQ5sVMIklRfLE3yahDGB8TI2Qa2QrtjKZEwO21hpb%2BqxuPtyv6SzmXdNALNETG742fjsFTXf53cYDTjfxZp4%2FOJ6UjKtV8rAiLpfem0E%2FC8%2B%2BULCRd4JKmdZfYaT%2FotnD6C57vdPYjz2B51kBBLFg%2BogUaSrljyaxXxco7Mxy4O5XG36bDmTCrNuQtOwP5qlU1ASOVlFBjxmccJubUJ3xRZYjvt2IxnxOv0F5G3kREZYoGTKQbmwxs%2FsJqiweY2Lre%2BCeQp7dZ%2BePikoeitBY5jpZR27KBtTC59KnSBjqkAZHsdZBOGFb5pNoorSFsNs9liKRtW04pT4PkJ0hI8Ub7O6AeyBGHgL7amV5AngoQDtVZwivK9Bs0JN0NF%2BymxRdXlaFSwkq3OH4Yk%2F7FWa71q0NEVts3a8GzqZvDlvw%2F2K0PJ87Yg6lLvXhloKtT9WRIMguKmUula6kDxQUWLpx1vJ605ywsQQi3ZRL7FOwSB8fDg5RnDUBFeU7On%2B6uZjY8XB%2Fn&X-Amz-Signature=220e809688362821cd49a69fdf693bae17964ccdd7c6017a707afca4a6422c13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
