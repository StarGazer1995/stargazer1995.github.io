---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E5CY7BB%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T172932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDuckRvPaBNR0jf%2FW5pFAJIjEOsJvGaDY0EVvsxlxKRmQIhAPF0hku25Wxebp2HP6gapYgk6mPU3oxu4BTBYh4oCP1YKv8DCAoQABoMNjM3NDIzMTgzODA1Igzp7guQKGz75n6O4wsq3AN79MIwWaCO7lNvVt%2FVnziXxrdJ4i75xR4CR6YFwnez0uoNGi8V9TAd2lpPYbAxwW19%2BH5UeTGjA6Fg2yoLSQWUbC4pfzhdfjqBKqO3KfBC5sgVl29nH9iNtfq95hlZ5ms7EWmTjdIkM8kbEDzxUan0gM73aFYAQ%2FPUBloHYR82hUlTPyYonlcQo98xEVe4%2B1zcvymkR8cyJqLpDPXuri3uFIGouf4IQVqIfoj6tNc2Z1ieegKU%2BJ5LvmUymZ0eQiLVypXw%2F4yXwruTWLpaZby21UCmG7A%2FXWfLH8jsdp3%2B6HVUJnuuftlpmBwRIfcgCuOw0YfRaX%2FEbRyMgMCVLUVskjtTMvaqTuMtQEE838U1L9vArpML04Gb54JodHAHGyD6rwzxqqPTCs0%2FFp3vrlDBz8EQQM8BwBLm%2FiJDhbWkoenMNeAeB0ExhdLD6viHi8Q9Fex1uo4rPzzQ3%2BnTYVB3stBpmR678rV9OItbrUyN3s%2BeeZePIum%2FAgPK55AxEGFGQ%2Byy4ijOd2m7vnaEE7do2Vh%2Ba3aC1QE28ENqPdLROJlzhHSWh2OK%2FbbM6TaYBb8RI7TC%2BuL3Id0LtcPpenTiUrO%2FFeckwTZ3RzfFTfC00rk9c51DDwlTvN7oQjCD89%2FVBjqkAXkhGJYrvyZQRN4cBBtlFR6r48WzuGntXxnqkhkaKtReVkefLr4NaaLqr0%2BOl6LmOBG79Vqtd0P%2BQXTXcrkB9UZvdLceYY8maGq3eGs11D4PaE0ycsmvqd2qVVbdq9bVs3k%2Fo7kAn3JHzRnsIKmd%2FvA5cDyzMQCVmf9zRR4w04AKvrLbD%2Bk%2BU2No%2BOruBFMRHOgWSbV%2FXec3Do%2B%2FCYLnXsjjNCcG&X-Amz-Signature=dc153ae5d141372122efecc034f72ed403de9c92fce0f575e345e5ed17715eec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
