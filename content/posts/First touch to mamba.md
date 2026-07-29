---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPRIG3PW%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T170301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoNRRZiKgpCanC5CQGGk1QdfXWRRbMU%2Bu%2B3EJunNdF2QIhAPMGIwmJZAyvVs0sQHN%2BydjV0hD9y%2FL99bw4eNcDLixZKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzMUsmDcXbPpiYy8NUq3APEQmFiQrd4CB0dv12GtN24qxODFA%2B3MFIs2Dmjche00MiFSgOTT7nsGEEurd%2BCV0515eXDI08XN9r04Cka38d%2BrQ6UvnNJ1jeA3%2B%2Bko1y4okhh5fGpUyXgMgb%2BSoiKIX9%2BCRC%2FbRQb29%2Bp4%2BnDVyB59lqnTiGTHBkP6FDHOlGn%2F4fCI3aBiQlLohVCwYYgoGUiebB1nNgtdm6m71cNnChKnmhgufZYNCTznQqtNczt9185Eg7%2F9Z43KrlDtm3ajiOJlKGaRobZk032bZwl0Ts%2Bg2qwa6XeGUB%2FvTiDrZo4xF2Uu5nV%2Fm4Xak%2FRo7Z8Rme61tjh80CPAc1tJaWkLIQBdGw6kkuLAiqvM5aMRDARB90bIeyipPQXB2yBby6%2FgPaCI5qE5OKvc7fB6f%2Fp%2BHRWxBXRZhC94bE%2F2VC44SeSsWJhcVTTUQHqNvoNzyLEOfHZhiljo1PtjGkqXfKOl18PRMJpb0Tuk%2FEqVJXHPX%2BrEBITLTDdMfai8qvo7nr6lLE1X9pT2vv7ke66w8v49rki5BGdtK5%2FYpM%2FDg%2FOt9Y399IhwBnjQGfJTM0JnHBen6OdpzDNNleBVvZ52YDp6jlYSvpWP4NWceNRUZnTjH4qlivOCwg%2F3fax2afDOjCCwqjTBjqkATzggZAKcsUcI8ZiFl145ofVuJinag4dkezDQQnYuxtkqK68WrqYM5uXtxdvwK2zMfeSYUOxcOwQ5qbQtQZ9cPyJdTEe2XVjt%2Fm8EYw6I0I5pTAR5KiX%2BCknec%2B5pRnAGX88w%2B5aCsdNFn2P5Jx4sBwEFn%2B85lEjf9hqo8kbTU03Xay%2FoKHzHmQX6eUW%2BpXdeYNsfVsCeTjFYAu%2FsSkTXt1FDgbv&X-Amz-Signature=39a71c7671a592896bfc5214a7f2666be6d4a2e8e0673b07952fcab8804fba98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
