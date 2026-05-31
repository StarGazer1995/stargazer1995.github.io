---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMPPD2O2%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T130933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCrFWCV%2F%2BM%2FATnG7VNO%2Bj84i0ZraP2HMJtj2bIQsv29gwIhAOCYBj946WXv55630EowNRnLdAgasp5HwWIqG0T4zpnoKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuLJ%2B9RZUU2ituv18q3AMczTrreFGDcVIog6V6rGrrYGfw92XO3SJzH%2F9LliHQ6dmTZohQCb0QALDYEStp%2FIF3TKr6ykfKeLKSpjsQSu61ys9D7msq3GTXq8415Co39aWIzDVaKVxIWiSTTHIyn8gBwL9mMNoBdJdQ38X0Fg7HYK1GOsUiRNgEdNb%2FBAz3aPPT7UaMSPPW9KIvkv2mZ9MAztj2qi9prF%2Bhnb3wV008jOZSs%2Bw7b6qg6pfKMtADTy4ChobOqMy4jC2lyZpodWxQwGlw6ZVGWJVh1kykTAe6J0suZXo%2FHgXmIUMwrBRt2CBnt0WvcBqYX%2F2s8pwDurvW%2B8wlzyNxOHY1CpYLON%2B%2BD8a37XqNB%2BfAzrguf25PSWTXe%2FVvdBsaKTxv4Nct%2BxcZxvMdEXdpjQDlFnuM%2F5vn2DE9uvzZJGcQsqQvyaKjeBuxM4hpuB3DFMFPq%2F%2F7cIkd9Y0jT2lYG125%2FcIcD7s0bKMverY1McJixSo6GvNYP8bG6rLvIMIUTbaUc5HazaBVC%2F5Mw%2FYPE8h0HuCPcdMVAgy2S9VNMrsGE7JJJBeQLcH%2BA6vqMrD2pPQW9AJMyM3AhvV8bU30tfrnOUwebt4vzbR8FzFbDqIao18NOojOxIHELWg5H%2B7UlaPQATChjfDQBjqkAeDKwxoJEfJsUQFZsKCyHteHJrACRwlU4dD9%2FkZUjAjdYbxVaRJo2ECPIFSwnodge0x%2BW6oWHxRg%2FSI2Gkkq%2FBM5WcFHYJiA0FHrHpvj07scGsCqHrj3SivvYpIr6sNVAoe5Y60wo4rHpqpWWP1ikSy0KqJI4t2Rj8DIrabvd5LzOOUwPCzpqL2bFw9P8y%2FXDmHi01Uw0WYd3xcfEydRY3XEbRCT&X-Amz-Signature=d6ab86d65c413e057d34102108fc4620246b0c52e8d31d9c6bfa2c1a3d82dd9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
