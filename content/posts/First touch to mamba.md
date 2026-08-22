---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JCWAPR4%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T042124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGI%2FsrqtVA17uDiRvUx%2FmmS%2FcIdnVHssSeO4o%2FdWn%2B%2F4AiEA1OCufFwcM%2B5YAvmii01Qvm2tC3dxUACpkLC1wvUE2kwqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGfTIZuKAuLtyjt5NSrcAwREDV0laPMsiaEnKWmA9hs827dZHAKDlCAd3NH2GLoXvPKW9JrTizJsc4i%2BGOBtVTSwXQqu1ykVXki144a8%2B%2Fu10hdwXob58iaEti6gHO%2BbuFqoHNiSP5EYk3dzvPA71CbsPoGl2K9HVSVJU%2BghrXZdByV5SUu1nRrmdn06Qcal68Qazu9JQAp5QouDiEvQp2WCgPT01XgSYzpMEXa8mYO%2FfT58ICGo7KXzv3Duvz6GnCQLDt%2BSIs%2FUCaAmFkN%2B%2FeLROpOA8zab6q7r3gw64JYR0CmE90K%2FKZa%2F1Tzwe4OgLMm9Dp9VnGYULnLG%2FlqPhe%2BKH6WFxybUnPprRTZdHN8wl0M1pLZXZnqGKlmZq2Oa3hpVJqVHpGDFo4s%2FPtDpLneWJO85kXVgjeZ%2B%2F1%2F8HGAgZGF394d%2Fjh7O71iFwSSP2yB0OaRE%2FfUbtebC3gsRc4ivb9MNAGXY%2FCG1PB13CALdbVFTLwwCWd%2BC67MK1nZzw47Wdn3vz5L8fbKo%2FZweeD3gw4H1edbX%2BG7YEyF1giO%2FIi8cRuOOTZ0dMBb0yaUEe4ks6P1f86oImhC1Pf4j1xnKa5fHDl4%2FVVlM%2Frl1TG9DzU8QYoWnkFAFfffm32BVwCXgaBktkyMaaheEMN6%2FpNQGOqUBHvPMxGEwikVKUo9oFYoi1RBrCCZhyzr8UzhDC52HSQ%2BoGmlfLpZ10JfJZX6XCG6BS1tqlkJmTxP6JX4KMfrhoIyvMjqCZmhcwYpaHF%2BrGRauS%2Bcxg6mf3j8Jx0Bi8T%2FmVtHiDzypquPo7Sz%2FAQzmkAOiluzuvM3RlbRYM0xYxst%2BBJ5MxJIfNas9%2BlTIujVVoJON4iK2wi7Q2z63wTmYJV93TGLt&X-Amz-Signature=43727de430a5da511540940c2aa41700c5cd1bb94efc4564c93cace7cefe518c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
