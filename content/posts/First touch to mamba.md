---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJGMMYPF%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T182410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQC0RfusSznedJZXiBlbnjVRYywFMnNO79ROiPzbyL7%2FuwIhAOK9lvcwqG%2FUCNmkfVvTPCVO9Fk7TOnnJgz0CA1RWVkEKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyoJb8TyA5j0NqYjSMq3AMyVFLQwmHWflWmOW4shvj5G7xUWTJeyfK3QZfM9CKnFJlSs1zg4QJKpxmdG2nWcIqWk7MxqPnStfvTxNlGLnotSN9P6ITw32bYRZ9IXolt4geH2%2FGTw%2Bs0jwVorlCFSCmCVlHw3W7LUqugbh7OMDRLfnQTyeVq8%2FECwx4kFq8Th6PrMGi4ZetR58B%2BpDQ2uG%2FiQ8ysMfZueZ8%2FRCe7eLvwLJ6ofq8c1VFNqt3x3EX34%2Fej%2Bb0Uaf1nRWTvGy1flO98SgB03xiEWA2UjUTDMUPIH9ljziv7JeSUhd4LbMwgoigDn8aPDH673v5StJH1nqq1SMz11XBrGAje7Xi7yXp%2Fk5PNDsb7lNTZ%2FN0nr0vurNwudaV4emDskJnuTfH5T%2FfMh9kkUDiNF5b3m2E9Y6lL8pfHCBL%2BvcXj9ASMxNMQ8iMGxt%2BPTCMOA3svupV1MD5mND%2FRjjkQud3YF2yvho62V3Xl7zz%2B1BX9FQbV9J45OZKPjTDjpuYWx8qTjTeK9%2FeE7nNngDqxN7GodYpKyowV7njXjbQpnKxBkSSqtu4MwKY4DXOPZBZtWF3b%2BIaGYhwLWO608o2hiCRKnxgMdHqecWSvHD7F9eGFsZGhq%2FSzOe2N85SrvuAMmNERezCGvqbRBjqkATolN1HwMXGUzKcBlbF8wlr85uS2Hsv2vH0%2FGz7Yd9XMTUCpxrbJQAFRSfzNpJ6wPZalB4yURjguFy1DK4xwKE9b1w%2BgKK57JmfDosEG76Env0bdSrbRizeCfmZGnCQ4UjAONgPZlGSBZU5qjlPJTzOmsB5B0DPmeia1Gqp9qzokjTJZy40eJG6%2FxIofde50YMF1Lam6bWx2FOGC6pmolP81OKFh&X-Amz-Signature=c6760f0e637767a0ef96b3984ac57feca186066ccd63bc6c914564bec955375f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
