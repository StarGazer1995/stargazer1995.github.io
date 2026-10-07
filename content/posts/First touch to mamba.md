---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWHXDCDR%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T011042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIAv9zR%2B4HeEHJRp1HkxqktwqsuhBgG3y7T529guIdmFTAiEAvwUMoOBZ7%2F1X%2Bq3ozbbWfzQ7Kkr8gEeyiLfZU5e6qvYq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDKds7TY3A6pGAsenfSrcA0BF9xY3nUK3Lm5v%2F2g84lgMiGWbgyV31lJcbTCJ1WGS0Flua7SMkZscMDUxtP%2BeB4n%2FFKQoKeKAOp4aRR2ujHgvyrAI4iV%2BCofN6zf94fHxYikSg56eGgC4shpRq%2FIecNBqkxNlrEdxhleuuyvTjskyetlOxODda%2F3Es67JJpaqTVEM6mL2%2BBDQVrCvLxPYprTfMa7u8AjQ36a0nzWyBcWwQgBy%2BhZMSdofjizaXCt6DlU6e9DqrytfZQzrh5yvOFv8%2F6dhS55pQ7JuE0a0B1rYBIJhlXaM6Xwe1tLjgAzXTwvu8N1B4EebgQQFD574bX38ZTe69rBKGQ0rHSuQ7ojaLZvDTt%2FyOFGQSFMZWpZ4oDQ6WWxMpXXRjYowQOlQlKPWu8nF%2F4GoBiZgrPeSKz2Zm%2B98SPQuS3N9KikqPRpBMWLDKBGIkOtbEWPPMh6fsq8r0S1NKpxanENvZQWpuMVfpD0m9UMY9exN8qZl9eu5NL64pEExC%2F7rwhudcBMPqrFzlZyA9xSvRz6Pyo1CUcxCgN4FLkUedpjx1UsnJ6aiN7rGst2GgGuH0vmCYw0p0L%2Fqp9ht3WY5QJ5Zh9TFxvV%2F8e2%2FAXcUyQmt2QwaDVYSlIktqVtLaeuigbX7MJKultYGOqUB8KW5k85MG1akTqXMON0UsKfNv%2B2K%2BgXXYOH24SwXiWnaXpvPdRuvgd2zEHV66EY4E9HaLiLGfOpLMAO4Zdl%2BiTTJ4kwWjnMQQatFMzCelre4lE0ANViH74P2zaJDWcAVA1qoBGE14JP60YZaAlrZjkG9U5dtKGzAf1wx7eenlw8IVpsl5mAM7grouDOBpsoapRHwndOi1AeCUHPi0kYsGYIF6zh7&X-Amz-Signature=9b3370f8c6e15df6493c7b9d038d4ec67dbfc66ef1ebf31804285f8363f6d3f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
