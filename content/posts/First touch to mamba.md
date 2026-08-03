---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EPGLRIT%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T161346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIHyItDOcEIz%2Fkh7p2Ma7FPJjpgi2WoDciTAwyzDjzj6mAiEAyYeFP4ouoDisrQZ%2FLuozrJsU%2BAMGxWdyTaL44%2F3nhrAqiAQI%2Bf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwgWCgLL%2FoRgSw6YSrcA8E%2BDQdxAiVjw6o6nl0DDltM%2Boxh1HGYK4Fl8YYwTAmzNbFGTITOZw%2BSyGAARsrI45k6dbD0JlCvCvOy8WrXcGbBPl5%2F9bOUCHe4pVxKw9CF4XPdRY3TfWCOaLdFOu6%2BpjhdnupqMTQFVUHJhsjNlJCICyM28NFEHh%2Bk1VNNYuwyb7Rh8xNWB2cNPXmxpqC2l1iPjDheWeMDbRRywJ0VUq0CtsZlQF8%2FUZnvwEjLjxhF8IYbx88gXtMhRlHCx%2FV0gKGXJ1yv0j8jae3OOA9EVgxN3hWdJvpSVVfPe%2BQozsO2q%2F8tNiAvBksjlNUiPFMJD%2FCTMumDoQVs79crc%2BIRZauuJPZ9k%2BOzptZDP8IWc2ValmY0vmFpBvFs64JmCIC0dObp0pBukUYNWW%2BlKHXY5nIzreWIptQkngAF1JX%2BrC2BFQm02NDLkfYTXmhThXP5flDRb57tuzjDOAd1%2BdrTzl%2BVwBkbt95O7EYEzKJTzUfJXgqrAAJiwXBaUiSMXv4oTG9mJA%2BLlA%2Fuz2%2FX0EKwTVrzfn5%2F86BK4FR116IRSgvUyZs9qriT%2F4%2BAn%2B5ITn7UsGS0k6NIvrBzb1oi4dvFgMdxvoIAOEpGSiTrVZu5SIUmv%2BdZidvi7dxMlLcWMPP6wtMGOqUBY7zEFv5xPYXHpOz62SamumdlptZb15hRBjnqPGpuMDDZCXTOhUmkIJP7WLL4xcUWusrC1mboqJHMYuzOocj8hS6H8LeYlT1bvdkA%2Fj9MALlskoxScplsLzTCuXdCWFTbXG50NQU6KiN7XYxYEIjyTjOrQcZ52jUaaW0oPEAi3foJSp3EB4DQRGlAWO74OsbNHE958pBO5Szd4dRTy8NaQcy3AJWx&X-Amz-Signature=ac9e78ff78ccf0a8b08ef64ec6b8b83065e5904516ee27eb34384cbdf2f5bab5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
