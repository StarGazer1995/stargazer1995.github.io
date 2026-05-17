---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZNV2IW2%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T054040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICMMtVySBVGIPTzy3ygjxcw9ATMOv8ySf3l5QYHzjMLoAiEAmyTnG1BOkHPPW3FCSHpZl8SowIW9NP4aBZGELfyib0gqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEPX3Droew%2FBl43xHCrcA0YeSyLao49dkE3hDNhrLIeiI3SEardQBfAOWMMZoYW%2BZASNLiS9fOKsscCpFGvM4%2FpTzFWbcrySQf6SbFHWnh4KzTAbqsR6tjwnzoBDNFc%2FP0S3iO4oiOmy60tEsyiCv5v6gHJ%2F0z0%2FNWz7FMdgfeufVQHtFdpKyx5i5ELLpoxVoH3Zqs8xfK9KTBUbtZc4QABabqxM6roz3w%2BpbVfTBz%2FuNLpznioYC9B3mbixZkaDT3tk48iQIJE%2BSctVYhASycUC2Kyrciv6h36QA3kdR2qPeGRuSU9mTctzvGTgTjD3ulY9N8mX6GY9hz2q8ZuqEIScJ9gqWYub3MdbmM5R0Biro4tWC8yYwbmA8bFjazffLtJHjJTSecApEILr%2BeOfW44bSqoEF55E5nlSwqVyIaU%2Fc%2F9ip0kmU0aBYBN%2B%2Fx3GdGfWr7HrTt72qFLFMUCscDIZ52sIDVBtu43s9XBqhyDXNXIhQ6OZHDoG56MORhLpGeMWeS7%2BiXmuarHrnNiZl8ZYOUN4DYHihyLeuizxwwN8gNiOfIhEfjpq3skeAcaSnGNBRC2vcdFD8JUyO8Bx%2BGKpqu%2Bk81U2QDAQeej5i6AYdylGnkxlD2Rvgigm0%2FqU0o9bfauf0bTOVF7SMKHvpNAGOqUBJ%2BVe5pVaAHwRS8zdM7lwk9YPMFbPoUQ5kuwdqjwGGiFealaIRpGIWz%2FbvEZTFdyC%2FdcZOBeDZ1CV94JxNVEz3uRceKejAfE4vMf3BVS%2BnuelbW2%2F7I56h6cpAFMmMBYgb23w9hnTMYSUgdgloQ4mcw5CqzOC%2FYf%2FVNat93F9hkwANyuK%2FeO9KWtT1Irr8uj7Ao4Rbkr1vFJdzqDFebjKkZAh6hjm&X-Amz-Signature=8192f58983d69c4fe4db66e8ac0b0bb3bfcbb4d69a64524e01b6b65a117775fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
