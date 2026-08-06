---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZRP3V24%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T081223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCWD%2Fc5lvMVnkcw1WBNaNgSq0bz5TmnEicw8qhh70Yd%2FgIhAIrzKbEN4IAUkQVzbdIS%2BRfyxbwpTODRQ59p4JREVfuFKv8DCDkQABoMNjM3NDIzMTgzODA1IgyFvXK6KQS5fvOvkfAq3AOSTzOr1r5QKdZ0ZvyjDSBvDZ6zPYNDTJ4p1P1gslswENs3kna8viUZXSqNgC1DnG98yo4m4IYgmTZNbBEZcRnees08C%2BDpbgikeSfo4C3gaa1WQpHbPtb9U5g%2BUp3p0uwJiBtK8QF9QPQGgN0l7ldTSm%2Bg276WI85yTqDrAz6UpC04YbWk8p63OyYyICu22pP5pMYooqAuAkjMVskVc5TiJz3zeK4VuruX8bTYnn3JPxI8TLDWAtCMzCRHXPzF172XcCH%2B1C5U502vWqz%2FqEWbs3SaI3LuxAQ6o2ouZut81U3AwpLM2BAXEEIHxUzDy3TrN%2BUW2ABBFGT01NdVkzOQTwQkA6YSTszBlcyUF%2B2cQ%2BP8q9ynQdqZmIdbmkg7ii9ty%2FN0XQghBydd6pCUkILFo6vDWMIzgo%2FMDwgTXJmPAPSXIJZVi1C0sQkJWwEJ94O10u8eALCJ9PC4mC62u3jZuTVWZUp7HCWkiWz43hwaxRlwyqnRNQNmM5A22zpoiz6cFxnMkxBIAhAUf81gw21S3VPibyXjLVf%2Fh0BALsk0h8r%2FFq%2FQhSoMeRukqHDSgWGoPX0Tw391LEkbNfWnT30QW2a7aLFZlsrdF9osCDCDGfSLs%2BbIkBWX%2BxGcWDCX%2FdDTBjqkAXijoj7irDHqGf12mTVIVS1OYLaU1ytEAR%2BriZ8iS%2F7tg2PZ%2FaW0htqeSK%2FJScN%2B7va542LCzu2yQzjnC%2FT8CR9HeRGFitrKRsN%2FagcPQwjjVKhHoX2fu%2FqVJO%2BeaHSbRFlPc9ne%2FSHRyFlVoZ%2FyWk9JW4IxNUBWNIP7%2BE7H%2F9VGvHI4A3aLpFGLZN9u4YbhJTJ2WuOSvQ%2BxUDUHlnw6%2FHl7AIQa&X-Amz-Signature=c2a42c2735c70ac7aee1d86b2cc925d51b6b2ca0c98bfcfaac033e390c130257&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
