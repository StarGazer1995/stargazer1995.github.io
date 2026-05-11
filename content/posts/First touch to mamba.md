---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMZKX72M%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T015524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJGMEQCICo%2BGIO8BCxptymP5ZSlil01NAt70yFeKsjecOSAa2UjAiA3jfXttcuQXubvexMoPMLqUJcJxHxN3U7iNE64o2Ou%2Bir%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIM4c0tQigkMmQwmvrMKtwDSAJahH1M6eyVl%2B2fwitXHW0gNPFVK7z6N%2FQ3WdQkLPUDES4VmWpNlmQVZr%2BLPH07tX4%2FD3b9cLS2%2BsjE7TGTJhgfmdtCYOBmhESGLULytlho2PyMdFhOhPaISGJBD8lCOhNSmKVAdIrojoGuwrg8f2FGJ2MBZ3UArqqt5VX%2FM34rNAtloPbE60cVB1C5%2F71UdCziz4hxAb5fesFDlEG9yP%2FGs7HYDt3YjZZ7kpMJsOMWvXPLgVpvwtz%2B%2B1aV35ZEGlHI4HdLoHzQwgICzdnhuZ9EI5InfZAeI6s0VQvR%2FF%2FnekiHp0eepJGoE9KGOR2I1j8O11kORs0jSECRhzMK897d%2FnEDC0DE3nxfxCyCifVO2ckmr454bkSQV3AT3KVH5xPo8JyCvXzDHHJOqaY%2B1qVBwnYNHag4MPDh%2F5u0cIJ0J2lMcbxTFZNRReIehPPQ%2FWYYXSt3nrslxATFyOan4g93nDgGPIaaSBoCfUyhHadSdp%2Fzu%2F%2BroU%2Fjmitprg5i7i6wJvUGoPZV5U0ifIa6eFO%2BQ3TEQ2K6KmP5xEmif38pzE1dyuaR21Fytcu4w6hV6oG7kLNt6w6KfyncI3duIx3RXZlExjDbeEC6HWH7uVKLLply%2Fii91iXKCJ4wquSE0AY6pgF8U%2B94y5KSg0ulsgqumG9qhUhXnQZpVRKqOku6vwGsVAUpLY%2BYkv9wk6XmEbsqQEzBS1HO0lo3wHMf2DuBzZFCkczU%2Fwg9SNja3VRuV6anVMq1Xf0ZoiwwqruSXURPMM5GzkRoO9jvj2Y46sloAiKUgGaFkw2c1dhfhOJ34uAPghXJUUcLpdWvMXlOW3TEwtqoGfahll%2BpDpre2lu1O%2BBpLja6eHPl&X-Amz-Signature=fb291abcad861d2662fccb37e9d440abfa229adeb80ff922b6b7d63ebdd2eab6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
