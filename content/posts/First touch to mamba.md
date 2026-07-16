---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637UUUQEF%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T075317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQDv9wQsAJuLq7ZduHJg5ucwi5Nc7Ny2QUkrvaAC86VTjQIgXR0hdD83UUrgvDB2nopqHv31OaBb8ZctX7ftjzFvoWwq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDOE4fQrN3sOrkqfdJCrcA1zGzBpGXrNFk93KuLDMJtid21TUo%2FP50SmP3DR2y0DgPMZ%2BDhfYpgF9LPTzqy%2FueSv8kdCsnELsaAOXTg1Ka18c1kJCCaWFzMA4HcVpfVf41vKiS5ZyAdttuZiIx4fYzb9mUscSPnTEy3s53YXGlmCDttaijNh5N%2BerxxbE4n4AWFef2CIR4gAdFD0jjQML8%2B0XqKd5CajiBma6RUucuL0ubkqvsi98wWuVU%2FbSpY5BhP%2BVLshD7jxFOUi%2FzodHpIP1cvTqCoQ5W%2Fs9Y4aYS7gGDmT2wPTsvVkRKYdSEqUB4W3mGCnE2TuPxNPYKevTpTIS%2FCWsYGCVwTIiCFIXaCxmk3pL1o3UDXgIOibBcrkauB%2FXDkeNgMgAao4aZSIx7ns6h2VeRq8H72p8g5erxfIadZQrsrSerh8E1iO%2BoC55y23beiZE48%2FunnnLbPrEGwyDKsobGHogIL%2FQs9s2I0ZyG2%2FdldF4cUAzbt%2F1GSzSm9Q0MQbv8wR9Lf2y3JoeL62nW4KJLHAUVvBW0CHtvgPIMxYlyo9iHdIFjn3kUmK5mvwfeG8zJZ4g6X3yilJ%2BSxPsUJItp2kTpbgv2uFizqgelqGWnUGaTAcvN4u3eBudsYzL8z%2FJveRBUaxhMJjx4dIGOqUBoMWKgbHEZ4J0bsIjAo4eMKiRi1%2BlMR7TyPP4DG51YNh88O6Edr6ooSJHX7BxKDsQZRqz649ecaT4A89CSa5r7PQELW7FnCJt37s9bsRoI2dGq4fCnwTUHXPYPg7ax4w3p3ThQQhQZ3TD2eDNaeofjQxVv20pLtCdM4v7U5XaaPanaPure%2BoCiB%2FbqGWa8pkMZ%2F28S%2Bov3WbRHMnXzxxCytDrxCrV&X-Amz-Signature=173727accc84b74bc7a80392fbe87c151c7222e30a9369dd56762c4e2b5b7f49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
