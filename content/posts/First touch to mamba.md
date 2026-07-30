---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NGXJ2WH%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T205453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRHNsusBqzGefuzJh4Y5n3VVqzE7mWZ13ey8VQbdTlgwIgZeQEiAwFV3rVrmOVkrmNjjcFXNwFY7PtSB74v7W6LrkqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2Fn70oIgUZ6zqu%2BnCrcA7cUVkMaudWYhdoQd%2FyQKYgnoOB9VOSmdDaEfMuGNwdxOS%2B9Rxywd2unLGbQBI48OtnvcgHHxHW8ZehzmPI2JL2Cqc3odkCd4N3LIHnfnkSLJ59crwqLnl8vmE4PDtL6Spe%2BRGS9C0ojFmn0FKkodGJj229gAF%2BLqH5RLl%2Bh903QC394FUZFvlwnNAppDz%2Ft1DIwuko9kMkT14YA6XPRppnbe2KaUqTTeO32sWyoYgZLmquOiPL5KnvfNRbJl6LFcRqs1orTQEYS7qQoyCCmmHfE4jVVC0%2Fi95kP5a1pwvONhe46VXXi5nRCMI6%2Bk1ECzXjRF8buGvYm2P%2FLZiVDNGd%2B%2BJNLKEekmeGV4f%2Bo3RIeUJ40557eOe8dTqnwr9iWdWtmxlH3GsfzJYLihdoITBxODi8X%2BkiGSTu%2BSb7BdgSOpNDVpZp3ILeRc%2FpUBkzng6OlxrE9iBYd0LYrD9dugQcT6%2Bmxr8%2FmempdxPw4dF3%2BbcveSO79EORBvhHCUtYp%2FEhBao9a6EJ89gUEQqO4w0izgZigbvwAMRpHWJy%2FYa%2BxLzDPR5%2F3fdBnViRfgT8qV8Mj7BcPLoPiUSiKwPcPqtZj593sQsL6uSR2%2FOldrTCvN2eFiXtrq3d0pb%2F%2BMKDYrtMGOqUBS%2BRYPAPAgFuPfWm82yqO2DaVAkpvgCmicEfpZiZQSz4Hd%2Fyv%2FTFOMCeVL6CHe2VJml5EXCKztfq248oh%2BOx2oTR0m2Pbtv9vFs8N52fTBA2qe7O3FK%2FNkm7vSBvYOIG%2FugumARQDZtgf0Xc1rzd%2F0RwFdcbyL0XSmKl8u9Yc%2FZi4nhb2dXF1QMF8xP1deBNiCJ39vgr%2FsgaJ0La6L2KePcDUCKqp&X-Amz-Signature=f80cd365998c22a85f772de2556bf5e0e0cd26e1b80889825b3d91f16199c16a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
