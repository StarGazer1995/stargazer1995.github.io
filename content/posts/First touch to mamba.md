---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FW7CLU%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T224841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIDwGV2Nm5eb0DsIUUeMG5bU7jZ5488vtRHQJzzfaSWKtAiEAqpRKI4uN0sB9VN7tqyEcJeISOeVEF%2FoVjcKJoZtN%2Bpsq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDONePnYu9BChhwH3CSrcA3Vcd1pQ8RqtPLWuHzQ6VxFdq3TL1Qe3JbuySbNAU92YdSapgLyQ3dxEnXgdL4e0gjnnu99VYtc7MY%2BBV0zz2LoEGJPT3U9r195EEyicPzK76mQeQpcgXX%2FNAOztwfelVqM271RU244F2OCQrp4qokikukbb3%2FZz6sfvCc%2Fv9Paxu1VZjnLsqPHcnmih%2BfqrLGLmnGV4VUiLS%2Fewzi40ofrhLf5Bd2d25AJiCzMoMIwHcth1hmHfM1dhjQTDWmieojYtKJ%2FX9S%2Fi3D439R6Zj3Sscox6Ygow2NYKO16boAmSTCjlFkrF8Upiey2RqROTv867Svgw6%2BVp8BsK6PBkLO73ZpfcDO7pUMS5s3Nr1bwPQr6ebUcNuPRuUGZ2it8g5XErsTETXXej9V7m7dPBjEusNh8KWD1aPWotUFZ%2B%2FT2vDq6vP3d%2FPGvVLfBZDq4LYmhHKlc1s6eewik0I87wEPSoabAKG5eypUX04NpBB%2FMu6H185PXff6OdmZSEHHmpXLZfVTO2Ig6MAN8esJ5gWyck%2FsPNVVtVzzqyLEEq4GlBod47ugFOb7a8tHJRXV%2BPGWhQCeiUv5ODxEv%2BLc5N3KaEJpPrcqCsNb0am6K5j49J7nUz%2BbKd88icOou1MMyvq9IGOqUBtxOPNQ01YonJYMisibClIisF8ibnPT%2BKy9WNJEs%2FpQ2ZMsTQpErgMyvHZfuEcnoImm4mJx3r6EKKf6QgpZJW8D%2BsA%2FWlL6MUiPKbyGVk2MUWJtVRmgg%2FBxQmYGCrRhfZyKMWhYrQ1xbSp6%2Ffww2cP%2BoTHu%2FTv0dXTAimWgnDbqhN2QwBIbgH131HasbGlmrH%2BmknMR26HJYxJ0P0ips1X%2BT0Eiet&X-Amz-Signature=e7d27c9e0b3b95fc63f418ebb325ad7369b86b2176a82cc19b2f97539773af0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
