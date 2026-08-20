---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIQDLQOX%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T164507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICo4qTo7GsNfn8wjmPmXomaOp6dxQXxBl1ls9Tm9JLV%2BAiEA%2B51E1z87gX3hp%2BPTfsM0bf%2BQW5BEx4SUJD9XtIm9EcsqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJwALVbju%2BCqJHjSyCrcA0D%2FYXBH2qSJljOn4RrNOeWppLj5drxCeIZU7HbZhJBLnvw6dKs%2BxsOoIhdzbnyfLbdgvySjufJjFlB6yVFmFILlKLofVd86%2FsADfXdw5cNelrlbW%2FHOXipjhIAmmQ6AJmDEJkyN%2FtX%2F1o5mAs3CC2O2kg9yFKjiLRuHTTItZfCKSoglvOxlpSFeNKjqPg6wx90bayRbtjcbu3IkhzfXLloKwVqwntm7GTuo2O9CbW6ME9Fik4guLyMAHgvRCJxAJ6wteK26sbq4R96L%2FFgXzSFci%2BSSAiIC%2F715PjesF7Wul08BqDaZNj5coVhWzDy7WXMNKk8jm9CjiqleoKnDfV4QzNHnm7lF%2FBXQ1kzb3qyOr0Z9Rfd4m1BcPFaEZKLpIlh1Nt62Mlv6gcbygWGWN7PqPsDusM%2FCpvxyDaepnryXAx2IMnZEmlltk5O37zdya%2FU6gYC32p7CHI3NC6fVD7hcPLSdkDbBGI%2BwTN8K0g%2BZ1tLnITYffRjIoSw0mGXpQVmMLdRzKK%2BqAoVsKEPyU1GvOVPjI%2FHQbcFxMZTRHNGdpXFiR%2Fo3fZR%2BeMrorrMI%2FleWEq9G3uJKF9aqBq4kh4suRhhCudZd9B0mnZnUWhMmKeVVGAzaPJ4CMprzMOSqnNQGOqUB%2BXcT6zcjvyqMh3zQyy3jCAzvRMWxmSbCrt2Hq6tx68T8Zmwi5AKGWcnI5fN0p5kKgvm3rovE0moJtUiCr4%2B9GuQ3Fq5%2FieRtFke%2BApr4u1CguKRcVtoPuIBPASgUVpx0nSVJ64XZJq14Xp3aorbVRnmPtzGbqceQ5nGea0Od9lx%2BbgZvkBUXl35rNEJ66kAaRQyQ%2F2d0TTkwnguD759p7uAZBul7&X-Amz-Signature=f4770651e0f98edc5ce6288e710cc957b3610144b98bab31a43461b325e4221f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
