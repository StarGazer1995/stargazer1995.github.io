---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WY37NAYM%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T020704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDni6J61JIm%2B%2Fut5nKbsDKgrF%2Fr23hFUZzW7CYFTsILEAiEA9xQFGlGCotaamQAhBoozjvmjfxElSaoKIVeqJizOJ14q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDIGEeDxUKuX2vzRxWircA21LHZzEwvuacz%2BXvxyFF4AmbUAL2iFIBgfqLg3VDehHBggvOD6K2qElEGgoYibbhyhTaXQbYFC4u3GqOe0mF2RcOezTg7nbA2DrdaY6boPb8HXIWzH1%2FzvBcaVIymd27dJ3opL78nInQ1A2vb3fn3l9wryheQC0U5enfq4iPc93%2FFFJ1UTuSvn0wt4TXJOj4fCb7yS5a9UP1ihtwvTahSAEGy9dDQkXJ7cjycw8%2FEKCetJn07Z%2FmYvukJPW%2BRDaz8G5yo2V0loDvvRYycEWUS%2FEzd4aG9C3l82GGMWIU0LQWKUlrivA0YgIWFFLfPxr7qFuvkj2%2B4qGU9whV1dOPbpFSh2N7qzY82tNF%2F9%2BPb9u%2FVTBW8VIf9b7%2F9pnyXyDXg6VHNf6eAVlT7qjsYAKzseliqnPLnu7lCyojl3MaVQoSTDvX%2Farfuoi%2BcxTXnu%2BYFa1XKuDyocdCC3AqCRmPz%2FGJ4baGiK2GdCVQxYvtf9WeNjW9NURmIsFBq5CaTc0XK0dIY1H%2BuY68hCo7u%2FIt8qa4Cp9M0oXPjFBTAWnMFnlb48S4V3IVfEadUJLptpFhapsnRslLIbxsH4qBtQ6uQEl2XVezLUc3AIRQNgODdMTleriiSAhaxS6DrsHMMK0ztAGOqUBXvfWAg8QiixM9RWiTDKClWpHWq5x788jD0XSHVCkB%2B%2FOmqqUzS9cAGBSnqcBeiAzbKi4xo7njcveADlHtDfhGth1SuaZxsMd5YvFjVaVTpSyMOgjL3iyQWNDZUfQDZIk1LBgW2Q%2BEWsFFRqrdqpRWrQrOr2R3Nd3rRQvK%2FshIi0snNUiW2F%2FgjlQb00GTP0rL7Xe%2FM%2FfZBrQGfsg8BN41NnHTCja&X-Amz-Signature=92666024f818f25fd11f7d823c1c0faa4af307584eff6f2be4751a354e6294c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
