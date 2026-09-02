---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VG25EIID%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T014210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3qVU6ZU4JwjZkwC1obfA%2F5LeU9vZGbf%2Fgk8S4se%2BhUwIhALlQ8TWyyIfMcFxLpil4HiMdtY%2FduxspfMHfaSf6KAN2KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLtsP0OAs5VBGCLaYq3ANrfpEgNO1zaYmBSCaLBk%2B1ACxBzkxfRAIZF64ceJlt65CWido%2FSspwW5Cl8yBXxFN6FH0bcRrxJnEUXphOqA7oKiX1t%2ByEU4TIGMSpYMJ2kBcsLMA3pOnIdOsXVHKWjXWDz4GaZS163IsG%2FdGGjWLnqDsIaO0JDJ3dUaKzFbQ76mXEyKYvN56NNc5v0qOUJQ2FDof6bWb3i1N%2B1aMj4P11tEWKLpoRFgj%2Bpnc0jInz2bLVFDwE6BpcwVt8PH30WsLOTXBU2L8yvVak8RuQgjjN9L1tAQ6xRlrggkhTb2ECPbBhs9awO1cdo6bRBDc%2BCPXxzh4kWooCGxalUWiQWz88Yh5QMqgeyQOzt9Qeeb4RFiqP5bdFpY9xixyPJcKwfp7lWsegp7W7BIwc%2FK5I0DIEbU%2FxMiImhgDWQVXkQ7WGn5isBc7x9JBbc9tER6b0ReOZdirb1dECYhZd6k8A5lKBXh8zVGorYRWQi7YE3NmmjOznFTtWA4BZRTuNcJ%2BaeHJv06VEghOlOz72Rfxm9zT9B%2F4FvLbOpGErVmqMWrASWHJnANEHENR0X0LRFT79Wafk2e5jMC0LR2fVeE6Q%2F%2FyZsOaAD0MIf9JQamkTtzlmRG3Qhs4%2BxYiMA7aMBTCu2t3UBjqkAXJb8kc1x3Y7Pfv%2Bqd9br3xQGFaSQn%2BkdCkCbn08xY4kisv03b%2BrtO3yKX2hssXOGfeo9ru5RJlkGzKMcxhRkV0kctUlR4nrSZQRpxw9XKUBPH55yHRJFdoo6uDJBIgUvqdN9FfwM2Eqod9EX%2BzUx1%2FxtMvOYd%2FfkBW3HIJsJr8Gyz%2B6Usy4FMZVTLpbwon6dlEyw4RwseC2Avz%2FoymwNoFMC8Dw&X-Amz-Signature=32e024ac551f85c92f927b6c9cd10ec7e9d831441527607d335a78add6c1ad7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
