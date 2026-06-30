---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRBU4D4R%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T212251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIAdj8gcXsUy%2F30J9sBxopgY2kFJbFQ4uGZE9Os2KbojoAiB2MrjvHifc4ULsI1AdUD%2BGeU4NJjHLm7U9MZiOMEbikiqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNi1IEehbIhIiMC9DKtwD8LpS2L4QSXcnA5kfkIVhbsZPZ8ePGCyTbKBnelPlACcqF3%2BLpQhnGYdEjt0or8cW7v0htl7AeBAMm0jUPcv7f%2Bzdb73zXSr6U0u9DwsX6rWZs50Aq4B1BNqBhYSL6Y6sbnf3anQCijmx43cdRAxGzxcnJfjaAPICbyXwE%2BY8pjEPo%2FCMywFvUoNDe0pY256MwxMlpm2ivkChF%2B3ukMOz7gftMlvvvDo7%2Ftv5XUtXQvNAPxRu%2BJ0lSFshYgsil3mfY5iyxQItlNqj8F9UPykt5883Lry6sdzoTiapYujMBrpv4xLrx%2BMJHPnVGMe0DRhxBQ%2FwkzbmOyM14hL8jn%2FIDBFpWv7NZA03dTWWpc%2FaCGdbV1rNhqUbcX6pvbtWxyifii%2FSlBRLYk7O79IL5pEHYs9U%2FsbxsHji8YjPnefnewhj0JoeHbB9hnDDmb1fi9RlPKV7JNvsdhXHLZpqKQh62pm0NQeGNA%2BWuLybq1ptAPO12Eo07QuQGa6C8WcKH15Kvzl%2FGmdoLYBKkXMcoRTF6OTo%2FMCVyQ5RuqMOPra0AY0gpBl6DwJ0rgXs9PziyFOsGrWrlrMhbyoBYP6Z%2FhhzNArUYgj8%2FAuIr4UFhzY9iDTiBYK8MN27BukqPTMwrruQ0gY6pgGOqI4cBg4vKmBGNXGW5k3X8qBRa5qqEkpCfJP6GDy6bOE1F9FniqZeD%2BuN2vncnVljUsrW2067I0cQo1%2BI6n6KJHz9OUJv%2Ffb%2BbvzeXyd2fYoWXc%2BmD5hnHRMISaGOtr88wkotJVpdXnhie5v3374z37wYwVx1gwRJu7foIm4m45cY77ChgW0m5gdyX%2FSYaCMAn5IxTbXEa3odxOshutNHHKqvmgyM&X-Amz-Signature=8a1a4f7b472e51eac5ed4d66d85cf36c72f8d43c4c214196badaf88ba5ba9b43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
