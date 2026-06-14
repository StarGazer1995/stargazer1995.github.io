---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZM5TLWA%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T190643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDDNbqlwFox4%2Fs03Pm0Znanc0OOvuN8Q%2B3AX%2BEvaqBbWQIhAJoe%2FChd3mCY0wAW6Gmw6%2Fc6s%2Fh68ZOoBI%2B0%2FHac0i4vKv8DCEcQABoMNjM3NDIzMTgzODA1IgxaGMbNmKQvhufJUcgq3AO0curUQmb3wiOpSDfs1DHCqlIeRCN2zbPFdtelFCMxzklJbFAA6nbRZDYQeRRaZmpoISD421u9j4MAflPputsU%2FnB%2FGbXDfmXdEjFrT9umM1vBG%2Be2OJp1VRO52VP%2BGw9OIK557mNe9ZPKyrM6mN4EihMN3fvpLjLMAmOrsNtTup39Vz0Hov1o9AVoZOOcvc0ChwRwKQ1JnrMg4Ah5l%2FnhfSHVEk4ygI2Ujjjgf9cSLHoUjPUFFSKZxqbf43HOqi5CuG%2BYMjNYXrAnFi9K3be3ERn%2BGt8zEnRqY0o8wKEVQXurjoxZ4MU2xBdSWU0Oc7oEd%2B7Wd7z9zQHaHLSBHsS0s6np%2BVEUTYEip%2FwHGmbALGCRwhoIY%2BLaFnQTcmCfKef3jf32UGZwe7PcI2l0z2dyuGOJz352ND7nutI6hbxqhEMWSc5K0ZsiZFDgapww%2FVtDMy4tp%2BlLmS2aoJ%2FhAHAWIW8Ofjh9VKoMe42IIFQ5poJoE7rqhWU1jNkdP8xGBNvpeX%2FxFqdXEqicE2GLwgcIjo1SdvFuqzFR3UFAow6EWQX29UKrpOWLpxZ9w9u3PlehZhaaBOrVTkehHRVvgDcXCn5jMJdV6pWGO50BkfH%2B8X9DcajzevxfdULKmTCA5brRBjqkARbZlxRl0k2hDZUe60P3rQ1f%2BrNntn4Fs52ldkC4WP63%2Ft9iV1b9vV%2FhdGg28kAogEXbEmCHc8tHlCyJKaLulb2CCBrfGN1YJTfilGt8hOgdPg1Crd3mH8Jm9SdPl6vTBTziVuPscFjCJoHplwgHjsYfbjTvP6R%2BTJ73USvwpuBA43uzo2sBO8rGSwJp%2FzWapvOjt6FwS%2FnTlTqDVG93DoNKsVf1&X-Amz-Signature=55ee4144469b46cd3a75375f071cb652721496cf37780ae2d87ba52f254cdabf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
