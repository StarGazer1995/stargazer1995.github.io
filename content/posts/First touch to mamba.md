---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOBIXMUG%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T062421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCe1xnB5LAOAXsotxJ%2B85QqYgAA7yJY6OiwmO8Non1eaQIgO%2BhEdZNQHweZzRucADaMhJOV6xTQEN0nwCkSiukcTfMqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTmKePIfhE8CAXQBCrcA5HknFXQ5wkSNsVpUTwkKHneRTT3ZE9DRihYJJM%2B6yWSMYf%2F0JeN02NAk55CxfNCP%2FfQj1f%2BpgX8n%2FwcJVz%2BG246VaMDo6GX1mbPCfUY9IyTWQteaeQN9srJHk0eSozbWKEoNornJmEDFj69I%2BG9nXlPe7iFfT6yyK%2F%2B606J64LQUF4yOoMx75xfOcsIYUfvgDA8sk8ye99xyQ3%2Boj3J29VGGpUb%2BGESqg1Gf4xBW6tFF5EsC9dLiSgwGx6Q23mzy0bnn%2FErOUIFXeec4K%2BoS49SGZizsGMbsiXrUIO%2BTFb%2FO0bLPagHKDeJs8F6WiW10woVMlTB8nfuWSRR%2Bnyj6%2FRBLloXWchFn19DeLEF8RaH5N7ySkWK5Gjv3zWYDXllfK01h1WBe4vEoQ%2FSSblgiVVPeQbsFr6mHKjj0QHl2dJdqZWNZe29BUvW8tabikVafYmIG24%2BvMmX23%2B2fCW%2BUlvn08K4wer%2FYETyYdM%2BZpZP%2FykKiFxhPkSCVIOoVuFUmo%2FMSYFpDJP%2F7gneCKNWRPBOce50yepNWufvfVKmDxcuuf9Fn2qRUYekZGOMP%2B29%2Fk%2BhfAd0dAZDclkBIb2qtEJVoHhmVVXBwwnHe7PcobXWoCZCCSFyDUlJYQf9MLTTs9QGOqUBxbtkPYYzst7P3j4MI3fjxWrgbQHdmYAdUyndySexVuxiLdp2fGprbkOP%2Bq4redhH69Ecrj7rFAp5jSm48KCxHztsmUHIO%2FJn0Z3%2B55xX7YYzAb5eob1TJZZWJdyA%2B5RdXjpgkNaWUzSrR5OWFMoEmFrn9RD9TfEAT3JAIJ9GMEusel8b7%2BatJ12bJYNyx%2BdZe4EQlPecslVEXJfO28gFgNJWpOdo&X-Amz-Signature=a2d479fb71c75c2b36d27c5674bd6cf9993901484841767be8232c7067ea2b27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
