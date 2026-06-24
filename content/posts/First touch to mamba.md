---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFSIL2YC%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T225928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIGLDcC5dgILPj0%2BSMerhRoYe%2F5BzahXXMv26EZuSVvqnAiEA2ypERe9xtzpGxn9TVdUiBSDaWpTz2RjfZb44RrBMEXkq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDMlvzKniLPljkfstIyrcAyVKEDIUsj0AyTi5N7sdnG9FG1NNXXJ6m0sFtcXhGJyzEaTsfHcy6s9IG0lbso0xXsSmmNEnCdTNSvnPNCCtFKeMYVfZSoBjSAnm1I0htM6tHDwA7v5irwYu36SMUntE9MFWVPIZqgk9MevnrcRsk6ClQzr5u3pSebhuzScNtZttf5X5prtbR2WOIB5DnKRkthNyl7BjbOiugTdRSCOWkqCTwnD6CyJeeBawqe8gukSpJInOumFMGgJ%2BipfvpSz1AWQGrWN6tTxZCaEp9yxlq8TQryImXg%2BsRYs7vtIO%2Fev6ARDMaUlOAfKnZMaxLHLvspdV9ie7r56jPzdVjh3NaetHiAR8%2Bpw0lJa8MnbVhUiVuhr66X72gCxAF%2BprcEPCUXUPUX8edxOOsvZHrV3PGSWMcRnRCEsjUeBh23Me8cMddw%2FyJVYHwpEzPVgOFJYdCKFg7knYRcPVUamKAT5Obe7Yx23yWTl2cOBixro8Vt5jy2j7N%2BS0yDeAX8T072muPVUfNZYsbMZ7Hs3Td5QP9x5RdQ1o7GeD581TgS%2Bma8dkX0F6vH5kp4JfpSF7hAzOqTGKEVb7UYtezG%2BQyEZNsI40gog4svXcxpFNckVQRf%2BcMWOC2Epyabf4XLCJMMe08dEGOqUBn91qyA9mNQtOcr9qxYjBWv1lnDNBADBzb7hcgC1EhcFILDKlCvQbaVxM3bw8zhyahFy1hi7YUEWdayKChMUC9lJkWMCuBAyDAxznBbX%2F60XfzbBuLvxyDkzMDNLYuXKjXLMOHK2Wuin%2B1fw3xlQEl%2FWym32sYo%2BKs%2Bh%2BqJXeGIVCHDxQFnwwfZuwdgXX5BObZ2Tj15NYv6Axafd%2B8Erd6Xq0Jvi4&X-Amz-Signature=719121f86c4e5f985e6ff162033c2d2a981ab92d379d85bdbb034468c697e821&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
