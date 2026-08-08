---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHHUCNFG%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T031627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoEJ%2FsrfQ8vBC1T21AA0TtSV%2Bp1iNiW5jlv6syNiZnGAiEA1rXv4a%2FlH91aSpteZUb0BvFCUrimGcmU6A9SmdB34Xgq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFHaLszQbYDFnCIzDircA36%2BCwvjp1QaNxz%2BPEbL9awZfKaJN7oLhnz%2FAf1dODw%2FOgFUxmsGznEE%2BN0uC9wpjISCdqmqSTErKXycGppCcgWKOC3R%2Bw8r5KJVB6NdrRIwOCRPTUN2cbYFvWpL7ISFKd0o4i5pyEDHLg29KfN1TZRK4%2F41bv3zQjr8OveNPMksqcdv8hPm9A%2F5BEmEtnKIeUfC1DdxzNUJvNQwMz5OyNaKrIwjk0yMkHD80Be6kuwpTy5WuPRwBa0Vb6Q1DEVv4oKNEc6AskwTtXAqJSK7mnu%2FddNBv%2BxLiiygrBXVCT69Yg%2FPy0YUdlbWaM9%2BfrNiRYHv9W6nPWEvF721sYwKp8iOIbmMVeehHJ%2B4%2FL0dxh%2FV9WZNcwKDc%2BXDcQZZuyP23H1UPlkooPwW0wi7RV4p%2BmPuBFPAUFSmQSxEVfeA9JXSW30GoM%2BJv%2BgHRnv7%2FEsqYZ9GG57%2BHrHCpirVW8lqSpguOb9pbt4id4Lk8LIy5Ww7K0nEwgr5rbgi2uHnRp4ex%2FhBdf76NGr1mEc5CnOrw%2BYK%2B8s48wFJ4SfkESFBNjgrP%2FbA3BjNLvyIbFSuluBi3mF3OrOZqmtUmqOWdWaQh2ckieeMrmMuyG1KBAo4ubFGPGilNa3mdNnpyB0wMKit2tMGOqUBzjnhM5DioM6PaLF%2B%2BuVEfsOS8WaHQJTwpJzE98oTxGLrwQ6eQsb1beeujgYeFIVxCKY2RHec9OV6nMFN%2B09%2FF%2FiQukEOnmNaEUBQRwOgumKnZk97DpTKeiklREBX%2FGxx0EfWJxhJBpSXy8yd0nac7DQksss9QCTXO1w6HKcSAArw4VXpyWLyFi%2FTDvxF6R0Bv1D645Q8eWGm%2FXvs5T6PvJ9IrElt&X-Amz-Signature=90ac2fa550536580bfca53b7c6fe84c08d7c5dffb2d540aeb2fcd25f6f40e08f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
