---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z5T3ATC%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T201016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJGMEQCIH%2BtJCbIwaWCFIld3eqEkKjyg%2FVI0ZuRDGMs0mCoPKefAiBczPCnckPR6H6v23mjvZLeheOUUYbks7d8UdRgw90S8ir%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMWioPgb2anHMPhTaAKtwDdAqcDyAKOFuiUPZdpCSLSfWsbym2NQyuu8sMABmhYrxq2XzZwktIIru3vIFIm5p8uDtVekzwtcqGitUr%2B5uwV6HZWAzFfbjZ8tfQDHub6Jmqny%2ByElaHQkQVOCJR%2Bd94IdNEi03WoJHzYan7UMM3d1x42ipvOB8kPX6uYOADzFDR4Y%2BqSW8y85ZkrkNnlRbVCHUcxYc4NeKxbhHqFVEa9MkBcBPFioiEBnJaQtpw29Pd2O9za8qG%2BcmfWNuCsIfw4LnpEmVwvpwmjCJ9k3kTwVeNlx%2B0sR7Q4I%2FPJeeFCMox3LnCVm1f4nuqncQ7ew7o0r1vpegT5C3jj36yWFnNW9M5UJ09eV7YosSD%2FmxWQErTBrOPqdKlfr56VFCx07qZdmhPgCJHwp%2FTWPI6UD58TQU1C%2FKX7y7hzQKwHirUXMtP0Mv48AmTa48AikMX90CtNREEwajYEIamnWSO2qsd0b1uhDIX%2Fvqr9U2y9GbYT8OVIf124Q28piZFGTcJ5gyoIs5wIDehf61Sl1EVysvahNLwEQ5HQB5iCiCm4ncDVcsutDHucumg6k5M1jVFTrNCaZg0wVjI2VgKSQ3WGE0EGI2N%2B2P8av4FEVr8JhELLx%2B13MEsi9k10dIff%2Bcwq%2FiC1AY6pgGyme0N72xjEfnR9G3tVvuPdCuJJQ5HzeUxqkGir%2Bch3UnMaO4UezQdWlcib6MJ5FH%2BeBPlE%2FahxSuu1OetrP1f5WVRKMP1QgWAlbtGPSEEIibXh5fPfPdIEjgDbGc53GmYmc0xBaN07pG32RCqX7C2QMrouc5%2Fy9A9pjj9cAIPdIpYrzrm3VRe%2FAcwoLXIgrklfx5LAhaCLvToSYR9csxonVxDMvsY&X-Amz-Signature=cc1f22b5beb511d8df5511d7b6606549f16dd39fcb9de95a778b07f25ab96541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
