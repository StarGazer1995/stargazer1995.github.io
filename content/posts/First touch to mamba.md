---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXSOXO5R%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T045355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIAMXjMm7ocxDmFk42E%2B%2F9aSiwMdpY0dq1%2FtMESe9FTl1AiEAn70Q7i3rCs%2FTG%2F5ilWDkIU212cJpjXi4eR1Q6djK4pQq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDJnWzAemIwpVEnZcSCrcA2DuprRf6iXHP%2FBVaqsHc6K8nij7wULpfFlOPT39mPBbop%2Fx%2FvAuA2Lv0rbEedbR4LMhmDfd%2Beg0cLGmTH%2B8YsYEbjHjuRML2k4cqeCR92g0EGwFFilNJfpDQ6QZvdiV9gpqGYEKgNDigG4DYOHGYkOWMyxNFPcwMgX9Ulik82ibGn1IlDW1CywKflgFBKt0jzD2nSi8Pr24XfxiFVlEsGnc5vX0EPdkcEbv5o6bGVk0OlsPVjviYZUeO9qA8JFnIXs0W0UWlRsHcWolqVLqCDRJdRZRPmoKK6cUda4tJxOcXknnrfrFsSXmGDccVk%2FBPQ1mzRgodnD77hq%2FWmxtgIm26ZEm0zbbHvFVve4hsSxQRnh64S2zzIsvVS1gwmZbrBNsVN8fRH8Cjba1UsKg2PAUere4G58u2G%2Fnu8AjUmsZF%2BWPMzO4w9si2vULnOkwwz4K5hIuVpwu4NX7wkuJjA8IdD7fE2N456ujr22O4R1fxNPUa%2FRCJJU02nbmhh8yvR1KejloePpkNkXY90sz2qSHNzIVJyrcg56RxCZftDliTLW5tLtd8B73quX08og2oVffRt2SIuG%2FUZT0dd3%2BNcsdy52J0HIHME7CTA9HtRUZUXh4ytXcgqEJw8qdMI2G0NMGOqUBvEwdtkVDJqNu770buHnXveiMkAbX3G265a7xJwtXGbpmF%2Ffhphwq9tqkt%2F4fSexXVFgCfmVCtYms9egIj9vkmjtMTaB73bJGxnOOOBX1889sGYGur9DxZAak8ZX7%2FIC3qE0cPJpfnFTEOXVQ9KGVe%2BlyQli7G7ghwoiStztK6cMNAdodzXMUa9363aRtbIX3PQ2jpkV0saffbkRi3Y1ob%2Bugz4Tt&X-Amz-Signature=bbb8c9673d52828bf63a6fa8fe288d05031c215e7ee1d9e29f8a006e91a3e5c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
