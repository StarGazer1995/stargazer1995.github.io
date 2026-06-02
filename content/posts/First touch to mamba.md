---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2ZCVUYK%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T232641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIDX9lNzqSGj9oub4hXNSCF7Ib4Ia%2Bos2fdabl9gfGMoaAiEA7fYCh%2FRB%2FQ1aaWjybif6nBE4PS9%2BsoY7PBnf%2Be2B3JQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDDYZbaVA6Gg1anpCRCrcA1%2BG1ZBs1kt81c9MXnYOjZyPjfNy11ouP4cMnLkdZYteJu4T6BoLsnq5DqrlN5YDapNdobES3ynnN6%2BQ9UGORiFhXf%2F46k%2BCQ2ss%2FE2vYphITHdDlL8Om5QHsLkcMf7e6ShSM5WUe%2FrjlqLcU4%2ByMyAjE0OjHAGDvc1ErDNjqVtzU1xfsAskdpnu85PXcHeCx605Oq1v5i1ojfbSETWFrLqz%2BKl%2BuhzxMOn8Q66SqY1P1YTKpaSs7AtWLqxfr1vkpLYFpBSFuKatZCQLAiXKvBWgmaSvSo1rpmP5q138DaWDOxOSLt7JKcmxsgRH9QytJA6yxtvuLleiZOSPmGVbiMbYff75g3tPVDHuQMH%2BXk6YypV2c9CjOjjo5fxrzVyfNXFlIIqZXZAYtceeA6Cftuig1DN8y2drxpoUKD0LPZfPAzVP7Qh7Ahkei6cJBuC5tsTzNSGTOeO2FmhmwJfwmbOW1W0e9zqc3Ic3pcTL%2BqcfLwMsSAszw0pTW7OO4A3p%2FHEBmqcEkndXBTQndc58WxlzYuquDJuKemRp%2F%2F%2FZbqCgZVdZ979Z9vJvcMu28ig9bhJdXKD%2BHRArLooTufsOHSLpNnnA0uvW7fud18dB9JIA5va6eUvPTpBoc48NMInM%2FNAGOqUBEyH8xgEUh7DDEGz0TjoCp6RT70jKWsZn4yjpdJjBznMSm2wXMJNotBReV50GN1o7VqyQmW0Gjm5XuEyILEkzcnxlHktNJsNLBnMfpg3fn4Qckvr%2FROEBo8oexCQVCHOszZGNsH0hdP7PCm6LFldFyZPxX27JfWy4ytrRlAxH3YGA1snQoqmGTkgFykCNTnc%2BsTL%2FAgoTuxo3r3IYHcITRZcfjf43&X-Amz-Signature=b667ce41ab18d050db9ef4ad093872d267e5144b1309800e45cbe585b613494e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
