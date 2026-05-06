---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCFPDZAJ%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T223937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDb0WGE1xQJtNG2xNra7wvqVo4jSYJgy96xVvtfA8%2B%2FlwIgfnC9wJGS7cvyc2KgfZBdIgPjKqZDqt52NufMQmUCKDIqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFTfA2%2FAj53RyFhjqCrcA0FCE2Wvoqx%2BgBpAl7%2FpAt46nJfFJzyIQ6wZaJC9tBdrTbHMhS40Kvld%2BmR%2BxEpoYgaHL7h4bgWNdB2LSQPpPxfvyTuKGaHki1BGKf%2Fl45LVbb5x83KpOSGYRRiwq9ugRUUae7ELp266BxFUCADs50ISS%2BaLDWyFGCqc%2BMku3Z12NitvA3aK%2B14iun7awXVHJ%2Fn%2BUfJi6MdVpgpFn2%2FxGKwKDT4%2BXNx%2FvY1b31UMOqQcV2J%2B77NRT%2BCdGO8Rl2FGLoS9UdlJbvPcIimqzXrRl7ldXZ%2FNdYcqU35j9XNt2ncn95sBXGBnatgHix1mKA08fNMXGeQbU7of9I%2BnPnVm0EcesOJoK3XCEUPLHrj3it0MFM2OeZLgOmbN4WpUR%2F56G09IGI7s7ZwOdrB0BOA16Sr2GU%2BkXttkGN2D37ukzO6KKJFVQu5dD3R9ZJVEAE0zEAYc4No8S5VaeezZ%2Ba6xcvkSIOFj27nlTLxVRbrug86iMUVgr3K1nh2tyHp%2F3fvniNkZTWB8dhgbghgveYTilVDOsdy86M0LsjW6dPh4XDgob9rhcPz5qI4mAxfIM4az54tTRzIXYgGmDqIBP%2BvwSt4QGOos5KfCgnQMaehRyosl2Gf8eNjq3H5ZeiusMJDH7s8GOqUBZDkAaM1MkULJnMzOMtQD5%2F1PYIRKaeh9g2DrndNGfp%2Fd312SjbL73JAWc%2BV3ZdTpossmAfYSq8OMZbk%2BtxgZ404VoGUtwDgyo65FVG9mFzNUWfZIEXBKsQ5QSQ8xM1s992IuNZFr80RSQ9kk1UVHAIw8n97dEj%2F3JZfvD125rRtlYuBz%2FPXG4AWcXsq8p7YKorMx0TNlSMTANccJa26Rbl3ZWkdL&X-Amz-Signature=a956c780cd288d034eba14141ad741838b9c2a42a8723add10f3dee646652320&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
