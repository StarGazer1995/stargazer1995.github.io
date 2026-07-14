---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZNVGGOS%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T204913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJIMEYCIQD%2BrljcHX1NJhoj9ltREOXLvifjdzKjSlh90Z11CRI9mgIhAPQQom2OTf0NzyHBkN9NTpOJat2KVtFFs0VLKkdz5An%2FKv8DCB0QABoMNjM3NDIzMTgzODA1IgxfobPP3YK9j%2FDRxmAq3ANYvhBOcD2dHaSKfOBQ6Fc5LzHftrpux4LZBbDtCXkUnIudhpbtM3fPLeQ17fdA%2FSQbh29XBGXkSXJeyTdsFFVMCw4Bfffz5laT4B477Xz6s1F9llUcwily3PqMMs6c8OHyulA9U%2FaryfK%2FSyYrqPn0XguU9o7YtYZu%2BuvQtzCuqxTiy52V4oJQppxRPAJdp0qPkpDWD9eL8Pmux0walNzk7RAahczg1gJwbbYGlj1%2FIzw7DFqBujKC%2FKa%2FU8DFfGykHX3u%2F1NLfdfM4q1PtvaW60UkAUIAyPTfaG7JlmzC8alb9ivtgWsw0u5iCgCajBTQx0WlTifGK8pIH8QI5vUkjfalHqe8dO2VoKvNHKvKDmND6vYFQLGqvmOsk71TD58m8WV4QKYuOj5IHQSSeTR9ksj9Kl73B5i4YmAp5F6uWxTDzNPEEtRLMj06%2FQ6Ny91lKJ9wye7tr8CoJlr1ACB2S4uoIfKLXF1aBPgpUsE06CifV1J0lyaAA9RTQ2DJE3104RiQq2a06u4%2FKhhfsuhvFSuryVGoe3QRAhSYR9%2BJFyLVXrGUHPLplQ0uGbD4LvxtbcXDSSRhBOx0OfUBBPsv6dk%2F%2FzNz%2B%2FZus%2F9svK2ndApFVHebRT5YaznTUjD8m9rSBjqkAUYEpIcO%2BdWPb%2BFRt0told5GrNh7tWVpnEIczz7FHX6TEVk6d0hV1JPDyKDWk5kyps9xYT06zx4Xt%2FVoW%2BcFp5Sj94GWVATa90FrziiuQGJtmzGjopKDl7EirQwmcRzjRTNFo4ilxGD8JeN%2BfsNdwDy8AjDfWQQVCDwq6gODCVSvPxYb6hljGpCibIwDA6kEmgnglpUoBKaC500OxZLNDxGf9fz4&X-Amz-Signature=833af6be16a2adc104a1483f46ddd9516058ac84e74139c5812a8350eeecc77e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
