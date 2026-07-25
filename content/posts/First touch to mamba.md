---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GNPN2VG%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T125629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIB7AMtqgCMlfvFw9vlYgevE1pkxoZjiAzAdTtxCCDVXAAiBMzbWV0LqYwTSzXtEVZaOSCgmgG8BlhnCOv9pC7P2Swyr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMaS27CIfNcef3zyJDKtwD67hIfgCrlqXqr21Zo5XYwrWMKqnf3PmGMJpIrjvh5OkRPaPrMzcCH0WBVDMnYa%2FBgXdq3mvTT2AZnLyIjQ3vA5LIh2e8KA70HibiBpxoNlZlB%2BviV72e0%2BDnLXYd6V%2Frvu7TUA%2Be5IHU9kbyFp4q6iKyf1UPTvbOmec0VJoGjD9udB6VW47yl%2F0YePOf3qihpWCgjZv6WakBJuYFZOcwzI5wlbHYHGfL0zkjG2xgfAHvFpg%2FMyHyNdFsqO%2FKnOx4VAdKkR3ZFPROkumYcgy9rRZJrkTTGYpHECZFAuTx92OOfwzywbJ%2FHhkByPWs2trYo0FdZvDBqq48aC8UiUPHzCBaaGKeWlRnhk3Q7JkSjubcmtYKQ%2Fkz9%2BZ8%2BgULqiHCXC%2Fcmfjiw%2BFVm3wB8G6gOV8icRvelyyMjwuR075zlSdrQ7NXAP7DjwKXLaoaACVsOc4V75beIlfT3gzXf9gV676QJCJh%2F78HXD76KnLDA3YAvNMq5%2FX64gCkepJSgcFJJV3ZNvArKmfdkKOqZp5iMjF84ISneZSI0JI4IMOLZySCAGpLktJfmIb4yB7ridWJxoLaHPoUmsNAVBL7BVOT9yDpWMpmRDqpochZfCejznA9o1ge8Vcy918CIdoww%2BKS0wY6pgFHY5YTcRdoCl6AE%2BXgcMfUlh%2FdT84XBZAo4qGwGMA96sTrgH06HlWAJgZJL1191SsgEZXu5VphwvPC5WdYmSoeoDVBTsr1zzhW8mudznENci3HDQnSaebjZ66WKqVDxvSMYkGSNNr1eEsJxBcu%2BW%2Fs%2BzPJxnv89IFfaVogplcm3mHfsjQxZ6lG3rJQcYAFNLYVF%2Bhix8MQLWb8MmocwxGp4op4eS%2FH&X-Amz-Signature=bf4804698b50a5dcdde228134a80027be460c15e0b644910f95a2ba1df797b8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
