---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA55FRMN%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T230744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSxTzhKrH%2FK%2BXQ4LixCXve9PsayS6uhPLmjFCzmarpBQIgFHGIoQUDtYi9Zb4zjXKeH9OV8n72gYwNBuN2Btu4d34qiAQItv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2BqeNx3O5XbLqivhyrcA%2Fgy1X%2FdPnM0ofJkyLFaV05V%2BsR437foRIlNIf2r98Bkav0nnNC7ddNGdcdpLiB0MXK0Mtk7Lzf2AhvDZZ1TXx7CcNg%2FOxsdm0xOI%2Bqj2QpGdSP%2F76ngv07UpJIzqufqFnVM5SmhVrjnelXoaftWYxXLLOrBxeXd6CHyPnreGSmASE8Ivo6bMAlc8OJ%2Fsggo847b4H4J4Ykd%2BxIGZkCzNK9HEP5HgUA0SXiOesHqXHRpalQsGvYXlVwPLCIf5eSZjYkboCav2StnsthJKEGvOPuHQZbI6iUyT0qbAYqCRzJOjQBsB8AjlpcsrH2s2o8f8dbzHH3idopx27zXyUQBNtI7yuLfj6iOK16dSIT%2FSPpD4c7M22Uz2atQgqATG%2B5LsCcSymsoWiOUkOkEuK4K8XnNWfvMv2yaajfxdLum29Xzp4lrm0C0GC4op%2ByGVEaz7OD%2BDGTK5%2FcsEVbMwyyhBAAKf21PSm1DG81E23sNDeALWC7JLvHn6pO0MX1Ge69aI9tVsO6X1BdQnbXcAWK8ol4Fr2CvbbeKtiP8FqF78i5G7RxsfNTedNZoXbL81PnHbqeRdrTyKDdWdHFOMeAKA8h7%2BU2OajSgeLuxjku52DtmgdGENPoi%2BW8%2FwnCYMOHc4tAGOqUBo6Eejsl0xhj8n0o3moqJ9sMvttyiI2%2BJA4oq6UFpDLW%2F1vpPn%2F%2BKINMZVC2177FTAELCqTbecd1sJqFCTiMpkMpUbQdKe9co771%2BbBoC2F%2BypK9we94BLCbFZqEk6hhWzCdioetBjYoRLLUBLMVazo5MnDYPotPxYQUZBUYklzuRsf%2FM%2FGi3B9gwGH3Ot2DIQGTsLzMUHRcofuGlkpzRzND5RXvz&X-Amz-Signature=332c896f6d1435acc131dd5a01ddb7899dc538d9e714ce5c1fef26f5a250aa9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
