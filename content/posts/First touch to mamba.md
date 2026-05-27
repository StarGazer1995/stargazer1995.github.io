---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Z2QW5I%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T230910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC4nlEv6P1XjVc6lUmi0qs0734ECQevOltrY8rV%2Fx6CCAiBa6d3YRBslKSyRNsfu0V9RSrSGVCc%2FFWhJturI%2B4E9mCqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD%2BKoKliiKr3p0mB%2FKtwD0BTvC9YxCRr1DyykJi64f1JUdpFrz95oYGFWXcZR2ElePJH5WU5xyF4W3HSt4uAVMwK3TWv3EkVvpeW2jtuGVenewJbmUpW9cKFwUldfocG59SuBXWEuvI%2BZKpJR1Q%2BMNvPIt9enYmJ%2FAnxjYz6iDHYDvjQ3uaRmmUcDsY6E%2FQJ8yp2FR5%2FsuV2VfqNG3G38%2BnRene1XI%2F6QlXOroBK14RqsrT1OS1ltVVsIo6iEeNSwWl8pC0X5YrTOWaiZgSuAagd8H5nxTcH30DqNxNCCAGHn%2BgSm6DIESKIsapwiAc2EbATGajBmRu9N9gPRX5Qe6%2B2Roplz1wI5zBMkA1q72x9Q3J8U6mifhwVhnxP5oxG3c%2F6qv4nSd4Mzqk8QXtlpPDyyjSj%2FUG%2FXoDzVegEtqR5XCx1SWy%2BqOvvlNmFnjlBPuC4D8%2BOrQ0KRKh8Hbh8oZxr5mpe40GAViprD1nw8EOEAg1U%2FqkqGTIuvtIRu6G9trYbssjTaoCAtT4KYLlCVRFuxYk748E0EHx%2FhjzC1VV6GVtRxAZFrmYdP2g9CDcSUGs91fkpzX9xOFzmL3%2BslxcQoU61KrOtrkORxOu03Pu0FJAY5nqi8mZZBAk5F5nvSA28qAGluyWAzUYwwuOTd0AY6pgFCtEUiR5l2PO2uohThgu%2BiDFd8rR4baB0LH%2FUayFYCdu05ww6jfI7MmapmTTZOSUcM2fsyB1RiRGWn66SZgbReWPS5YvpJ4xiq26B0SlWzaNqEeuhPV%2BLnGJyvS5vVK5jQs1TF6ywAkVtJr0%2BOsxE83pR3G6e4ksxxB4isn4XERNuLWA2pV033vr5FA2Uz8ZNEmcBFcJLSbIuw58KEyJUH3g%2BfBV2r&X-Amz-Signature=42548baa89c02ec90f43b17d3d68b65b056ed578b57bf092f50580cd3c9d15b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
