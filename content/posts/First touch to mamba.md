---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5DGKAHO%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T003309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIFXw8brXTsn%2BXNSBRn2iNmCAQCucgYqgtEt1dV9lSx6IAiBbD%2FSvaJ9A7WJIIjnSQoEg%2BvR8PtYJcH6uXlkVHz%2Fuyyr%2FAwg4EAAaDDYzNzQyMzE4MzgwNSIMAaj4O3JXd4O1CBbTKtwDjnoTdI0zgd1ptVizlbkRT%2FDiK78Up3gfoS4JZnmhVUm0a0oVfOMqqayfQocbpdTYGocz6bR%2BUP7OcTy7oO8%2BDPbtZMQUprdk3y%2FB4zewwMfWAloEJYR4T0sJ7EE3HRIencsqtjE%2FWbk4RY4aIEx7If2SJS06kN7Sd3LMMIL0Sj7Fp1lMjJnEQO9En%2BGvJjeUIazb1nWku7nQEfWUH%2FelwMNdx%2B4ARu15nyTDGQDKHDN%2BFl3aJomvAls%2BqsKkn44GS4MQzIHHMb257RIK0fyHIwvN9HVpbvMy3a8wihnAZH9gw7OF6q39FhMJiLWqKZiDxQK0upI6etyh%2Fo5EC3tJBXIfjZiuYFfy9%2FeRI1y7k1mFnTqkQybjrnqtAMhUxKUMzXMwi4T6%2B3kmhFVwEPLIIN4wyHpbyRlKfRniOltdGvnvToMwm25G3ByUtej%2FglF%2FVRNnSqe60M46yOi%2BB3KigdMGbIZWWcPi0M6LG9a4kWjglvDmKJw%2Fn26uxf8LM5BHsZjEXqhRTSH1jobONmbCOlxzS2remvd8%2FVEvUADFIbeJKsQz806moTq%2FHA4D9kiG2K7jialQqbmkMfv%2FUMAE54Rega7FPf%2FYvH%2BV6CUvKRPWemBviEEofoIcN44w1POI1AY6pgHZZTYajoGwdB9tBs0zVPEPb0Y5zsHmt0pzlwKCE6BzXQsjrIOKGg2fl9vn4M3yVdNwCooJVMt%2Bj2t04pMcfJQ1CwzyNRTVN9EXIE%2FWmkOkEL%2FCOlbOAdDQNB3heg884oU06rm2NR9NdcmthI%2FJb8knYQbTTQOW5%2FgJxFnJV2RabKsWqAIJ3Ezo9nQXR4uhLdRSLaLnclGCzq7rsNTcUhBHdRl3Dqzi&X-Amz-Signature=22dafd681099238f1f28ca4ad63b72529f17c650ab7fd264240fddf31883bbb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
