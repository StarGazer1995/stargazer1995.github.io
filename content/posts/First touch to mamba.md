---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654HA6BWO%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T104124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQDlvcQHPHh9NOIEGFc8elOPzp7v0%2Fej7xT%2B0u%2FG5jBq7gIhALk2fNm%2FFMdMHJPpPnO6oqWBSREBNRU1gxsNCr1beHKuKv8DCBsQABoMNjM3NDIzMTgzODA1IgwrsU%2BM8ZSIKNjkGfsq3AMnhvgk7pRwPFccsn5sAf3CNwF%2FJhXrsUM3WUpy6N3llTIeDNfi2%2BqaOx4WsC81cdx%2B3gK4imSGGGaLENNohQ7q8ykXK34yTp%2B6uOk6%2FabDTNYb17nzCoqfXl0n%2Fm8ZPHvJHufgV1MspGGzNXTK1y7vX2KrsYj5PcQVhHMgWW%2Fagx9G9IUsHzWSONQ7rg7OEh9JY1qgMm%2F9%2F%2FKz529H%2BJrUrsLOoOwKiIAZNnWRGdCQ5dcm%2FfzyGugaQiOiHA8q1wPcSotlN3IoA9uu%2FMjPxq3pgXjv%2FvvvwlsEGTKwYdKrG6mfcxSbhLH0XX2mqITl6W8aT1MClHHR5mQtufgDu5gOUQnsU7WCewgCTPoQQZix4xBQO41fmaoesEm4kuAWkFi4ejqfFvFNVO1HwZ4Au9OVjYInn6W2PET4sP%2Bnn9Pbh%2FCTSwC9MWS9oej1g9deQdqFBkdsmPM2dOuSXV2ONs3Fo5yOg%2Bxw2TY95f2mzvQQ6RkL28iT0KWKsiGeq3VRlw3nPkeupCFne4%2FQ1deOMDScvUjaDv5L6IJRGV8lu4fh1LCG33lRm2OtwxwjCVRcOWoJFfGMd9275OY%2B3ePLDaTxPGzpczBbiaWfkDGe5fsToKOeZKBLCAN6J3ZB1jCK1MDQBjqkAXTEI643kN1rX50Njow5i8JduR%2BO%2FpIjRvv%2Fxmv%2BuQ8%2BHp1ZNp2qZQNZ8pQ3PpLB0v5igUq9t0iz2G%2BRwicFC2jLiNhmC%2FCwlSYqhtPmoPrGk%2By5QqmLl9eTP6jyqU0tYRGNpyuciYDPiHfCU%2BbjjanWwcShhmpzEQ3I77tRYsEN6Z484tTqMKHU3z4y8udaVgIXSK66ueWWInnnddlTasnyMjxH&X-Amz-Signature=efb4f157acae581b8ba7728803145737684c3b037e228bf9fac0658a760585e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
