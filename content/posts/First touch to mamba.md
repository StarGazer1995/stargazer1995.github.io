---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUCZDY75%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T013002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaH1XZBVhugSlyPNwDqsoUy%2FrnzgBs%2BtGz4w1UxVx3XgIgaC7ctrK63LHFsKXaJJMYsQ1tmW7mfyI5HnxNp2EyIWMqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIsZkCYV%2B4%2BQ%2BobBvyrcA1ltK81bl28gbW%2FPRtWAT%2BXhBfv67CoQG4vShxb22YVrouMEBLrI05ulsiwXENibUWFxsznhw%2BufVKpK9npuBE%2Bbq6pu5F%2BmfsYFSaAinb%2B9GxXzBdW9gRPEbIR7KyZkIzbeO7WyAE6JyKrnd6gAukyVqf2ezR%2FcL4Wrz8NdZusiFlDT3i7Oqnj%2F4MlDgeGQImp4V6AwQq8%2BX1c2WLd4pfj2yOIlRqc6wwcPesH4h%2FPYfYQ21z%2F1BO%2F1XGe%2FelIdP2iDYyvqQQAZMa0rh8g%2FK7q4E22dz%2F45e1drxNdR5XtEfWarSO25HOu1Qkrv0SMlMxGBfBpSBf1BoWLOJII8fXBLRHC2%2BEIvin20UV%2BALipoWLxMhHRZDHKUkpE8ECPSOHXWZxLoiieOPmtlqxOGi1IHNqYcHVZDqbs16yPh2RlsrRG6qD7GSpHhzIMrI%2FSK74LJke15cr7ygC4exU2jJOA%2Fl7mdGUzX%2FrmDlijq7lnXBFhCcuW5471r8HV88Tz%2FDJMiuI6Qe3PRav2h3RWZm6nPzopO6RGogkIr07ygR9%2FRXRstpcNAMTV3PzJGLXcGVTEtR1NbscEUEzRXK3Vl27PkNfJPozMGcvmxb1TIbYgOQEZZETCb1s5iqLodMNKu6s8GOqUBGt3eXzCRI21cPvhkFEj%2BBfp350XWo4gVwZvTywL31bL%2FSP8jzMVeB5JKrpn6cCd7zpLi79vIuTxcUzDz85ppkA41j0LMs20lIC0lGiEDaff30c7v9u4%2BWKG9ICQI%2B3hleFEqE6%2F08csXCmTk%2BwJAUHShaknY4KDvc1PBLHGPpMXmjdmZWERNFZKnQjfij15a223UcoWJ%2F%2BGhZW4BPLmnBg5FhspU&X-Amz-Signature=4ebe6c2da05cff6d3eb7dbe40e7e46e6f41a11e6c7570d772c961296fb43115a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
