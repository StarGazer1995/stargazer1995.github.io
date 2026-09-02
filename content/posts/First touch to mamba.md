---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YET6P6F3%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T122137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDv6VJerJeJUGLSRkYsKlcP7ChXQO%2BgQUqgtAe3zhH7OwIgMLqVVwa00OgP5l6nFa9iZ7%2BjGJ5GZ7bgoMXyP%2FLQEfkqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADIxzGxly4oetrfjyrcA1J9LGSYiL%2BcZoTDJZ4%2F8U9AIwqt%2B%2FPYXuCEFspzof01mELOmGeqFu2OGSZM4cCDdLTS0y8icrtzzyIWSmm8vK8XoS7jDFbHKZReSE0JFvfHgpHI%2FM9LflBQFaZA6SoMTZ9ag83HVUOFGsJ7YCCiTE%2BqCMXU%2FJpwi2dXRsYY87pzeMfhOI7Fva%2B%2BtNm%2Fjwj5U6YIOEu6Gd2pojhXSdiOcxv7h89FrdKTbbFYeF%2FXQBJikxHVTu8V7dpgcTFTK9ahTmpAiQ%2F3hk2rZ6Qk6G8OFyOQkXP3Cm9JgaIjZdYHwMcyv9l%2F89nsyErWfI9u7n8veZjO26yve6ZP%2BlhYy9qsi2M7R%2Fi3CsrZmUVILFi17B33pEcXfyJnKgimFkj5viB3t8TCERswO7tnsWnSRf%2BcDFchJw0C8euxtxujsBNfQKY4kFNl6ahoVZBVYCixPyHC0o1vBJqtenAKypfFV%2F6Da5zMxfzHDvVX2Lt63Z9IzXHiLMPv3ubewqIcbyT5i2yTA%2BnJjynalpC5K3ixZWy1OvH5lXy%2Byw%2FW%2BpyQz7STh0wXOVhiJ6yAocfufa9ohrLkBnyYtkaMEnlqOMGIlYYtVEl%2BIfOl2S%2BTtfPm%2Bo6OLBkOVG%2BTiuu%2F2MuyIG%2BhMKLz39QGOqUBBJgJM4QACict9ugnSaGgeDJdCtvZS%2BUKxt82kX9OXg%2FSh26smq41Zmur6igN00NvF06LySQ3gF%2FR0wc%2B%2F%2B%2BgXgVlw6by4LonOcXrhW0t3RsmjJ7pgS4mkuzATw5Lvhhiapt3YX3WzK3PhmQ8Wy15HtbFaCMz0i7C%2FJhj4CN3a%2Fle028%2F9HVDkjtoVjsMKL7xIX1KEJ83bDojMnHdty0OvDeH8auE&X-Amz-Signature=7cc36753f2b42c0ade172b66fd973c0c5dc00c328114790b2386296b1405bb4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
