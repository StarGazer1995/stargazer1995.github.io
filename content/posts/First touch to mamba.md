---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QC5SV6XS%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T225920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIB0VHthOXVUFw1ndgu6kKKwjrVtUXmGAUwaDEwGuRBAJAiEA2m%2BzZxGU2dqMHgipUNRCYgk0dg0JjzVDfuCwfPnFeKgqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2B5M3Q0BPkuTX0HRSrcA424I9hSEKwPviTWZBa4Z%2FIMnzDWKi13eKRTyhtAdYhGPdNsMcI6w6oEHkOHuNbOb2FN%2FKy1FvnIe2v1vQQx2I5QLnBz472pYyQzxlxwfQs%2BX6u7dzfliiq833WTJakLbE7QRLCRt2EXToDntnVDDH2810zu4%2Fbkt8zClQVyNzf6XmP2bHbw%2FIhUqZ20pRnzjCuOelb3lKIcFOqzuoiGIrm%2B1zDy0kQwD3VVDOPj0OF5t3oYLceNFKL5qqvAAT9caLwXKzq7qwxqZGL0IsNJ9D9VVTr%2FW0rwleOH33BwsN98C9dQh9Kkz5Kn2FUBqgiTXprBKP4orPt8toV5mfYTIuuRRMylnIaLEb8H08OBfrGlIUFs7e4pqRtTVj6L7P59j58cmBVedCW8rlCrnSlQZ78Cs2E9BlohfKXg9zvFeH8utvukHwSPC0%2BqC31p%2B6fYI3TqxoSifMXvMVqkQDCcdiTnIiNPgrGv13f0W6QsiTLyjuoj1f1uNYnK5rdyHXUN16PFPyyb418L5s6EOKmOOG4yeV3SdLx1Qw%2FBxnjPVn9Y9vgXyEPDXCVRgtBpSwPZtkc0sHAC0rAp3SBdq9geKOMDQWP4jXezebzq5xkvmDS2DYuPvDVIrrTqlcr%2FMNGB4dEGOqUB%2Fiax4CJQ%2BhHzeuv%2BjsaTrgHpvOLGru9vvB0P8CDU%2Bw54DrAdMoZ%2FClMcK9Z5qT7BpH4AwatfHl1rYJqLRsM2sIMKkocKfbpYK9azwwMCQBZ0kaS3RgJiXh1yMl54XUjmZRn47wdOBzjdONp1DAx%2Bbr2hXXD71eosXkx0Ep5V0MFdsSNwJuh%2FQG%2F1LCq7p55HLDxddeDbauNiOOuHsQsfQ69nsIcn&X-Amz-Signature=2dd157d4dc263f2ff6e7c1dda373f180f4675f9fd168664f32f9b2d673c84f93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
