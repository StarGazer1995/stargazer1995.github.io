---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMRUMTRK%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T115549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC3PBmh6UcLRCh1IPmv1GNDZnyRQNpPDEtNoPAQHqdd2wIhAMtl06lMl%2BLh8gDEGZuWQTR%2FEGkvCVMGRdz76bj%2FCd73Kv8DCA0QABoMNjM3NDIzMTgzODA1IgxwMTGXq5y7zge80nUq3AOQ4tg1nyptf84w3YzjQiifPc1CwpXPyY85KC3f6V4WJhMFBbg11Kiji2z6b48Zr0tktCEENoh0A%2FaF%2F49%2BNfDPDaTxaFQEuROgh8lLwyQuSV4fX%2FQVjeiKd8A9BXxJhTNcOqNXPY6WzBwhCVLBKP59mfosLsW4L1W5MzQyfh5XVGEB48EgTqrcsgg2CWuTKHuwiFI5kVH3jYrOlZK0xlBEG4mdASdtbEgF%2BN0Z41KUsRBLAQmK584jJRBAEfOnewSh9EHMTNdFPYTclUp%2B9Fy6O6ei7ikhq%2FvZwvh%2FDfRkYhKjHYXHuwyjCeRWSy6BdHIxhiw4jPtspb55Dr050LekDa8mx5SF94h1v1%2FyDl63g1UjRSYH4T2pWQUpISTPnH6f61dhX0Qh%2BJVIrmzwPs87ksWXXw4DPEBoDXM4YilNtAr2%2FPqSyipE9cY4uN%2FAw7fWmIh8lZx5p4Q08Ml%2BQ2aJHu2KXiy0Fi34WU4o5FI7TG7%2BOKLBn3MF50at%2BwFsY%2FebiCjVOvibrdefIt%2F83I2BUaM%2BwiKbG5R8srmtHwFimNin6m4tcMSTfpbU4%2BWEuCeTFN2MBXfarrA5wpIQKn41oDecnhjY35REWZKcoQArnCXkh0R4NdVt4uo0NDDsm8fTBjqkAVI7D8Mst2wJRIkDh40PzkN3qADPRsBUYjx6cFkHuAr30sKPmZGKYlfA0mRB5YMde4uwnYTZD3%2BVREfkSx8ge3rBzoKgx%2FSvWVaxcYdQbrSPfV1Pa8yyWZUHYsCXutMCr7vSwm75CJUtek%2Bog%2BvEnuUii01itdTrwmlHRHNUnj6vfRbWLOOEnPH1MTkJEwtbdFelrRV8GDi939nUCJaZgNfa2hbW&X-Amz-Signature=1a89c90e5bb7509b983b29abb45152bd5ca261bccaad9843ad9fd1ca31016c41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
