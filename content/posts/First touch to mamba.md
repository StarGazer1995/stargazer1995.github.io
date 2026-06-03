---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVR5DDL3%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T222401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIDo2RLt0mQ%2FmLM4nQxkLs9HQHRALFJSjYmDcevW3ETAxAiEA%2F4DP26OaZKWftiad3SneaF8m6k56%2BtfdgMJgAoIEJvQq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDCk3fn1T3CWhGImAYSrcA7KGWB%2FAzwP0K85sj9vHX%2FY2rZ4WETcfY2HV9%2FAsrw643VUc4JLvBVnJH8Pl57g5IAnigY2p%2FQ68kF0B7qsJpMi0hpPwp%2F8JyJmzCFy%2Bp2rQUHecVuBlrb2t1CWaqi1%2FyMyVRnFDtmIxCCSnfZ8PMLP5PemVNOxFPucda8Rl0HJ94bpTz%2FDNb6lBzI6a3oAagKqstUbPSQSGQmN0BTHZBsZP%2BHrEOTp9YBoBPzNiLQxALgwFgDPKLHJukn5CzENQPV0Jzu1DEX17xx1Wnu8WeEHX8NSeurvdnROEVXOmK3MwfW%2FVLvz6rl5BDyABVvdX52IdCMs4tgdsoHnbZQQwUwTwjkBRZBIuKWqZKC4HjBtUr87QNXgRmOChGlkoTNeiaBnT8JQHziW7qYmG62vNh0tN2AjUoAq7wKwXTWnvJx%2FFA4bmT6pAQQbfTayJZ%2FuDJU5I3t9e0U3Agau5IIanWw7N0AK%2Bq8hPg4EiIqtMGS61FOGktdTAniWCEOO77jpR35O2o993FFjX%2FTktF%2FdiDScNFgoMqjGMEd8siT%2FqHLrkHpKHLw9xTmGHEt%2BTww%2BXKpLQomYCIq0JNkBIIP3PUnWM2LXNl4LYG0UEB%2BqYVHX7ESYXP0RlrvCTkFlLMNS9gtEGOqUBn4wVmcMZSUYnBgiP49EFmfEoJGSGuKS3X9YlII5%2FBxcOzQnd%2BbJOo4PIHkMfRZMg%2BLiTCGe4sUszGuzesXwly5LTyM6hNn2wRc0V7CTCmdcBRr7HGK0%2FjrV0Fsq9Rydp7cLd1Sp42pwvApKjZMP4qfhkDZj9jjaDfPDFnZk7U6QR%2BqTo62hN4BjiUb45wxEJO5ocFxJpebM8kcxf160ZvWkM9y5j&X-Amz-Signature=0c4e297e36a5f80ce68de0d4f1e0438aea0406efcde1b69f128b0bb56743f847&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
