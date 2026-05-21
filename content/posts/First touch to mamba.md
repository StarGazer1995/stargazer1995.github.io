---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAOTRSA7%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T143556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDxTBn6bStTxpAZasV5NVXX1qKgXMVEpnerwxZ%2Bbf7eEAIgOfH%2BGCPBx3OqK%2BvAXrRvLKz23LAWdzUumNMgP9zdC4cq%2FwMIBhAAGgw2Mzc0MjMxODM4MDUiDGGhmr3CH54t%2BAWMySrcA3RZ%2BpJuctCevI59Zq7NBsRW3altHHvGrXLEaLeArskfCAbVTE4wEhDfZi1CLEIZY9ay%2B8yjyaRI65%2FNHT9ipZBKxPXlYqS1d44KKaFLEFwxgP8KrRcZsJNPKFFneYQTJwhGUgqL1hkwOogUaILs8Gbh7P37U9r7M2zzRsGMHxUuyXPMQRHAeA1Xu%2Fb1QL10bu7S8JEIq3HF2Iq%2BF1yP116snsNC%2F1NbEAMgcWFUI1%2BW5hcsefCv0guRIaPK6o3uo%2FZZ0zSIs77uqDYq4woItC7flqIK5H7G9VqUWiADCYOnx47KXH5g%2Ba%2F4vm8wd%2FJAnK95GZY%2BhDWT2Z6%2BlMayxt%2Bz7GXNcJYSzUUpEzD880deZC4k%2FIt7obykxWEPGO09GWDxSRM3ZYbbRr%2Bdqlxx%2Bnf%2Bwlq3KA6LkoX2u%2BcPq6iszoKm1uXycq7EmTGASygMY%2BuABHY%2BE16h%2BDf0ucKBusgnY581uo0%2BgQxEx1oWf788AxeXwTWT4OcdoItZ2BGx8O%2BuXP1yr1vfidk2mmOKTaDpqqo6e%2F2cKpcLnVH3ekoTb9vlwm0rgM3zLVSpK3Q%2FgMuhLjbo6zciy7a%2Bq4UApflxApTJnA7ThfiUMuPNU4paKijQ2GZnNX5R%2FMNQMKH5u9AGOqUB3YUOE3bhMUPt%2BuvTRmlvpoI9zNemE6Vhfsxox2Ufy51fuq3xiEy%2FnFoC8uKAHLeWfD1%2Bn5mR%2FeM56nED1Azs3usHziSEhFJSOWJSIKCy6Q6EOhCBRFdztl3TussjwexLHdc97zef2w3tsj2Blv3%2F25isn%2BMiwoJKtrZnLFhehzomOKvO1O3Ir1d57LqI%2B9dYwuc%2F%2FubOIavscPdynnjyEUIBpc0l&X-Amz-Signature=608532c8df1c0a782b4532d1126cfda2de1e7454d9eb27a0bc90a4b83d4a5cb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
