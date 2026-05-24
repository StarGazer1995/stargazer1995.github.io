---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LDPY2D2%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T204250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFggxqQObnVgHk9FiXRlKXR4FTt67opEoNHHjf0i71mIAiEAl1qzRMw4QA1K4zTD4%2BeOZD9NTP9Vjn%2Bmty6FtqT9a1Eq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDNQLA%2FBMwY2NLHkLjyrcA8YvRttfe0e6jmFbib5vPZ0Ceph3mTtLibji9F6ucKALBLNeeVEqifZlOn5SG6nFoN3NlSCOkFrVeddeCpR%2BqudkxybeM%2BtFP8bbiyRfY73QJNR1FU9CvmVxfw7AwoCgJ7Iu%2BwBNp96yx%2FIZDbMoOzlwEwYvsBiCPZ5tev2UhwT2mqnAEpNiGJ0KfrKoqpHPsMKdCXUIGwbCg9P3%2FFLTZ8O%2FYc9uFL4Vd2O1bkQMw1Xfk%2BYbjlnGFeRQa%2BJtkeoYofVxoUrGYn%2Fz4mTJsDa%2Blv2RnEhXrNtn2uQtNTRhLypYAymoMm2dW%2BM6Vqf3f%2BeD6KH%2FGT1ZHKiQbf%2BJv8ZYe0sBkI7SAiwQxpckL2nXrIwzOKA9on%2Fk2ftopDaT%2BbuuCoU19oNrgotlcR9YSN3ImYCJOAO863XVTru%2FZqXAE%2BL4hAYhZ0fIWZoC7tUB2wPov6XGDKsxJdk8zQRCMD1WhqjIRiLLJplM6MRCL07K9utvX7BVHUP3B2GJghWJ0giRzf70b9m343SBL2KnKnbolD%2Fjx3QSDUxBUca1%2FXlnhl%2BB5wZe%2BIKWCjUxTv8TN8HPWySOedNmmCCJat0zD0Qg70GXhQmagWxs69cTqyn0SOfNK45TJz9f7yRdoBKgMNKmzdAGOqUBPbuXUP%2FPJRZcLXoWDSBXSqLsCS2gqWvzX1V2HI1fM%2FEEtB57rcwGl08Wjfa0%2B%2BO90fBTVJ9K3DzfD106yhAmIA7UfxDFTO8OEoWCo0%2BZh5Y%2FH2gTKEWQcZLIcm1ZohutFlrbBWgT2pTmHz5MbHVPCdnq3imZpyCEvh0BtVYyL9QnLZ3DOEqtw%2Be%2F6nZA8aenkzbZxzA9cmhoLrXvdO%2Fp1ZvDhoSl&X-Amz-Signature=ad7fa44151c52dc6489882474258fe5532e133bf7ea6cadf97355cbe6dab0d67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
