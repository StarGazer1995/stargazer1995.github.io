---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR6C6Q47%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T192350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZNfqrtmQI4fXhWusWAfOHZ4FhxH1ULsNG17gUAUe3dQIhAKLR0ER9PLC7B8fxsCSley7yxMjmnv5TWEMai0N4sC2iKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCFJ90mYZBkiqarisq3APzE%2BElXeRzMMPZTpN%2FRHSLcoNLVjkZtUD3WFAD6Dys%2B7pR%2FUobf2TGXRlkRnoOcbneVC%2FGfjF%2FdCuH8pp2IQ4MOT8YgGULescfCfIzxu5zjNqaB%2BSQOyT2NlNjqPS5KpElup%2FaIulR%2F3HFROc70yTs75DgGAOyG1Os3Rv6lz2e%2B5EfwmggvmNFP0bimX95mRyLkgTvDjQqjpNZjRPC0kHOmMB3cf7T%2BC9lBdognTqq7m31691dNJP4uIljkXMd%2Be9X1K0mciwF1%2BUsCrEcI%2FhNk91yGvTI9HMSUd6ltHuu3UgdFZBP9acJ8nM8vwreZAVPDUjTRSfo2ISDzeRh4zwKZmvhbSLrUwjtT1bhqTUao6LDEi7wVxCUKHG25FXxppPwtoETNsfqttuOhd91NI1J8Hqz8BssLC8Ym7E7%2FbN%2BuVvpGlUWGvbsiEwhDjBen2v6tgogcLvRjor3uk%2FCwZoGrIG4PiML1V286eorpdFQb4O1Fc9qzg3gh9LestjMY%2BiHZc9ZWAAZYh%2B%2BVlwZvjeNAy1xKJ8zcijyPphzWIeEMj1Pne%2BK4JxH5vKNoRQ0x8mthVjLCN93WGqVjcJ1xJcDlm2R%2FZnt3eov1z3D4NEFocgbF0hpuTin%2BofMmjDqn9bRBjqkAeeE8IxfXc0%2FqA5PwLJ0cCIxSWNjd%2BNb%2FIFhHdEETKOhNPXWxS7mnMlSuns3djmOczwlMcQg170J7%2BT5PpRazaR3hGcw7ETYBlfFmosi%2FF38lxJeyIxF6uWZMkpSB%2BVdMWftDQDzwVLUHBL2IJSLWvIg8MgmdZooi7ex19mVMMLLwJjpR7PfWkJoMa2JuTaM6tSKfgHlhyr6rWBTXwGQtjyaVxQq&X-Amz-Signature=c8889861a06c84beaf5e1fb307e13b178bfa1a9486d6e66bfb1162ea87410560&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
