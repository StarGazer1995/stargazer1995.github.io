---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IKDCNBH%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T060755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQDLRYSw648dZwT5DTl3fpJCoMbrc7YGF%2Fs4eK9BEz8CpwIgQFGtX6kuLJcxkKTmaNLYHAu3yEVpVBd%2Bgm24qlGSU%2BQq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDMSynF10onIpNU4RVCrcAz3TNdFl1SwWfZ2LZXrfJ%2FFemxkx98Ji4Ol0QNEmmy074S9XeZzergJekJM0rVCksvlAaMRpKU6UyipykIzHe5iU%2FZpFBdQshKjw%2BVEuatgZMB4fJRaO5yf1iTwG0hqaxL%2BkF60ochy5s6sxxlGuAJhhLioM%2F8ihFEDIRCJ2g0JIKu61pWtShGa5TFbcEG4tpB0%2BFYx0CmIXc6JIJXRM68qEg2OnvQnCwovCeX3ul1Ktc8KUHcqXbacuf3OGRLR7ZFKwt%2FXwP9CbrY6vl%2FBRIWZy2B9zSaaz8dXv21FxR3lySk3j9Bd5vdciErfjQyu5%2BedCZ29VAmQ6nv2kXkLuTIRJ23O5iv8XbhdoAuP%2BXz1E5l9gbWxvJT3ncrnnUrAAhW%2BJdXaB6A3yJKJhARvzrxn900%2FUmKSQTvvWavoZsDyc0DIombV%2Bw89h9dRbemxdPgRsA2GRnDzciIG4OgXtljrGp%2FTb%2BvShsT4tkEc%2FAi105pIDBHuDQg5vYQ2oArVUv%2F7O2IPtWaY%2BD%2BJ4bDSFxmNtDCofy3FVcKn86mMSVxJOB7ijCs9aGHmqrfZU5Y7bR2o0nv8DGqOWRvdpHSs4kGXRnRHbqVKWQj1N0Frn5elfEI9VgajaU0MZuqxXMLis6NEGOqUBPCUrQyXQa6jQNU2zg5grM6zh5vjsmDz2kJYV77zFcnrm68LZ1ZDpLbaoIFNi6ga76f9NHuZaIuNvw175h95wHabwP1n2w0xKiCfmXzVNLvTsRbA%2B%2FWRJh9fH7uU%2FKc9H8CuzePDpnX187Co3ffF7pT5TGxUtUWcGAcNwVRFWzk4I0QSVFIuwuA3c6gOBtpRxvkbgAQS9ZyhhuyoVmgmxIMQuAwnv&X-Amz-Signature=05deaadc08c8cd68d6070f09a7bee1762fd4f1989cc32a4c82e6339bba149ca2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
