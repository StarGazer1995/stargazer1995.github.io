---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XF7CBSPV%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T081444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIGD6ZIBeS0HbcnXmuiD%2FHRoadPnrakE%2BoXNoO6p%2BPnWeAiAAvEcSLvxacJAnbPihf3K2TpAQ6zwUk6CuMLRlO1yWuSqIBAjZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW4XZ%2B1LneAFgKW3ZKtwDmiZtHeNK7cbxSm0XhEqFxlUfj326KHrOJhNWNOLba49aa0wBm6v7cHXCRrsY0ukqKlfif3Y8BBr27tLo%2BxXrHH8p%2BzvXMw8%2Fgvz5X%2BI6nfHLzYBxAg9nwhc3Xzm%2BVEpo%2F56PIcGrj7KcfYTfcKEqrkXszoLo%2FpJEqbmXPmLPoUUxX7BHggD0W23sPv%2FJiEwhMvVDbBZ6FSuBvZArQHlGXkmcWEyiKBLN5gD%2ByFuLiaIcG7Di8yexIPZ6lHCD%2FJRsHqTTWs%2BKm4UfEL9gqnCG2OQPhddBFk1H8e%2BTvts0L61kmXd9BP4roYdPH7McFDLsDNYBOp1PCxLtdJa0uDAXWZIDSQV8yCcG2RILToxAxXlYwOsli8bYkFhdQTTp%2FPdBwQsqYNsn945IG%2FrKfJrHUpix%2B1knG%2Fl%2B8Eo18cmUtO53F0oRkT6ngQ6%2BQHDU%2F5WOhS17x59LaujfXMahX9b7tSClsYvd2tAsWo7p5E7OqzojT9Peu1rF%2FjWWvP0mDuOOS61vrNN4ejb33ga8f8LPFLPWJPUzZRn4qqTld5wOxe8h3cQPBxPg8mmg4rcTUq9LQayQ7n6P4CZH%2FvvraX%2BLt7Gq34a6%2FmboPHnaKTV5AFkbbpay%2BzWdVsS%2BjIcw3Krq0AY6pgF2cK8knPtx5Vof57%2F9au1TUXKz1t17Itdo3YN3MLt5sDM9SKGOEYKs6HzUbODPQW5f%2F0PmHeuHfFzfkod1KzI%2FMxiPZ3l0ujTWJ%2B1orYLxPtjnNFlyPSvGlpReMBV1QVU2lpuF7bEgzVNTQvPAs3EjulDTNtiWQl6ajGIJTjUUDMDi46rPyuQugK5Na7P8BiTYYTlk%2FTHie6DbbSwhfuh2jR%2FaqvCl&X-Amz-Signature=16bb4452e9023c19124db9af5b01f6349647df5b0d5c73b3b1c76a76426cb287&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
