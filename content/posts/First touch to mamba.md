---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WU3FZDJ%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T195047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIDWvDaNMjEGIExKxCS8MjJVsGDXfLznEqXCKne2ByStXAiEAwc9SQ9FjJvsRkL41Q%2Beop2B%2Bls%2Bfit4wvL68wFdTNxwq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDENB6cp%2FluAIMxg13SrcA%2Bnkf7HN9vZX133BoYlJL0SSN6JZrLlhCs9UZcq%2BdpyJaHq8yhbwTHGbepHeIJg0Fj3QVYOraWLoolZEsrVBeroZexr2oVLBq3ryYihL2ScX261667zRhFtlZ8XfKgduBfyAeQMTzn3Bxn%2B6NzBc7rB0A49qcFMnY6axpUR7Mo4o6gyUNxb1o6apIkFMz%2BqZl9OSvbLJEKezfLM36Qkxy1GLPU2anDXWcZ5WkEVzMra%2FoNtwYTF%2BfRx9xGSMPIkhfq0w9mLhtD%2BjysAgovkp1m5p6S%2Bn%2FIWXXlNDcejVGXl7%2FcJY6RnPMtuEwQGfdybjAhvYeUhgXAZ%2BErVS92RCBoIYGFpV1G7BwFNzy9jZAzTrl%2BhE4lpl3PY8U3ObyQCzDmiUoeUo5n%2FIdSGN23s5tqJAAUdytWLvcaZ4dW85XEcPGZUebNY2xEpkvw5%2BqWbUJAssker5%2FnJuGfmryF%2BfxaE8a4dAY1GOcwdU8ArjR94PIZcynl57jiVOW8IH3yS9W1IUqloLQv02UtTRfDnwQ9pRt9s8Ed0q9TIiwnktMbJNjc%2FT7y6pXwsgKqECzzGe8vrz%2BukoETe36g8oNbhng6D%2BvxLG%2BWtb29OuwGxP%2FVapcfnu8%2BvqWP84nfckMNOVsdEGOqUB7e870tewwb%2F0YUgxONKETg6ErXjntvJ%2BltfsorkMvk5%2FsqQxG8MZHMZyESCIEYeuveSohXTCMTnP0BD3gZIaeyDIvzbl%2Bzc0rC9qKRIo%2Bwz9Gc3Mnk6eMtXiVwttBO3gGH%2BkEVUNlRAesHDGRmD%2FDGvK4tqVdtXHbHqh4KDczc7nAG76Kf7Yb3q%2Bn3upI1BLgtL5TCA9Q1awS1cJJY3y49xnoQsF&X-Amz-Signature=a7ac63db70aa2522fc0f0c550ab7900f61a40220e780ca06d65c04a9ab5b054a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
