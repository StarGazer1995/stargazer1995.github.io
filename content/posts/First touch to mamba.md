---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYBRGZPX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T131157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEIZxhQ%2F1%2BiOV0pljS%2BQnn9pTfD1ThTACtzBY2a5SHAgIgS50cXEYkaB3CxSmM%2FqWroPA1eXWqbG60GJm9wQ%2B1HzYqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBi%2Fv5QlOUDIDJrcJCrcA2CvgdWu7VyyFBEh0UjXKmRCasaIfyxynLunugQlDLUPJ9jFaduRXHozysjVLawJXcD%2BC2SJQbJgN0TFmTFCoxCmUXh617Wq95vliPStqj7ZRXn1V2xnQw3ap0e82Zm4u8TqmgKcSMEGr2NjiuU4bRKx2bbMrmoUJbH4copOB2c1VbyUfH%2B%2BWweZ1YZv6N28AR7xbL%2FVHWMNXQeUtCPAMX%2FQjAfaEP%2Bm1ffaqL9fQMLhw%2F8XimW7poRIgp0h5jtMF%2FWri0ZlnfZp0XbS721ZnuK4rr9A7v5z%2B2vJVYSG6QrwHk%2B%2FU75faAYWmqCoKvKXUWkIfBFweouYoJd%2BIm%2BTgIj4%2BdXVObV5Q4XvPvv%2F6CX%2FqI%2B1Bc85h7nPM3QqyHwmCm6m%2B5COK1s89Y8BXjoM9JdXIW8Qsx2nWTm4vFSp%2Fwz%2BAWdvq4ydnfZwwZQ1ZTXnRQhe0aPJfN3qnORCJFcnYs2txd5n7Uf2SgGefgxxH%2Fak7otlDXKsEoHVD9BD2qW%2FXDM%2F1loIe%2F6DBm8H31ZPFCPpQ%2BTIeUnh9tXB0xMa7CiD6apAf4r%2B69da8xMhfItn95mzytxUvcX9Gtr61KRHSp8%2FfJ7dYciJPEx1hXe59PPsTu1t5r8xt8jSEmh%2BMPrE%2FdIGOqUBUFHVj174htjG%2BAf%2FR3KXuSeL0mtP%2B3j5uIAmEJve5CXOX6hBCVu0%2FaFf8B1vsnB1IiKiwSAgZIXJHjMex91tRe%2FiIvagmInDdwOeTg5CVCAUoXo4gK0vsEtIpSnQYYcrsm%2BefTc3lSY5GqIWDOQPSMQd%2FPM0j6O%2Fr51tK9UZFOg%2F%2BrI0sGMNbdZWd%2Bg5lCw7%2BISkSPVjXmS%2Bvx6w682bQscPMKoE&X-Amz-Signature=73497f8b5e95c772800139e6b9d49f9c6367bd8b1c10c7d50ee78a370871d59d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
