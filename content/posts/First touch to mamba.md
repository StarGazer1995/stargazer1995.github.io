---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPUOZB3R%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T073118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIDqD2ZwQ2Y5Y8ZR%2FqqIEo9hQ0rkGj7OlOmYR6gUZBOUwAiEA4nJrLOKveKuwTLMhYOCe0Zlyfnb4K%2Ft3a9Wn4ITL0nkqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMBB6MgmjZU6VPl51SrcA8nL8b7DEFbmGYPDBCfW6k%2BJzzAEp%2Fma5E03doPGzRKa2gv7Wz%2FSK2IJf6QCuOk0rQ3h4IvlS3%2FGQIuv4d2VAeeIPe96vcn93cyQ9jiVOg%2FvFvScLhk4GhG3Wkj8MfbWJA5RNCFVvlPWM2IFSDMq9oYS%2FYzXKZACypedfBqyGgyXH1bf51QkHCqYQT2nf9yYMUH9ePqoIpo7nKFDewyDRVllVzEtmnhygpQNGN%2FZl0X%2BvT9Vl3LYF7KSClNjFZ%2Fm3kH9GNFhi3IIsTZCdCs5K0sAi96LXDHcLJV4ch2i%2Fk9B4acBUGI0a97BYXuM08UuRfo3noJSeVmdt5OvZrN9UjvVTLT2HEIfnZVpl1YKhIQN9WmDsq9L9x2rrwsd9xyHCkP6FLzC%2Fk7CpOy697jIkGe5OaZd4V10r1GifsNXtWnOJwbtb%2BfUu8CaXOYEUydNbeEhbdcAisGG%2BSMJRd62GelvgDS%2FLax743PtcRser%2BKhGKp74e4f6LE7FyQsBtm%2BBv0Sl%2Fmxs%2BY3OMg6hosocv8aF%2FUCJrf11Qhu0LeCPIKlEum5bB8GyGpVN9%2B%2FezF7bFiEGcCoBnp3RIQzeHkpAIhrzMsg8i6Fx3k1l2pnu5uR53keQ9LXg7y7PB%2FCMIbE%2B88GOqUBmqzVr9oQEmoB7M0oWamZkIa5g9V1AQ0OPJks3%2BuPlZQbfz0CRT1LtehPkQ0FvReJIHRc0puRbMP%2FUA7ZagUoh3Z7SpdxlFBXFv84PWtLBL1GWFcBea5KFThDX2tg2Ffty532ZZ7cmcdCUBWdEPdcufouzBHVmguV0PGYToFc7aCtw0a%2B2%2B0%2BAPGrILnabKt%2BCIk7U51oBPVlwOO2if7JCobG4h1O&X-Amz-Signature=c2571b84c472b9a1a23aeeda7e5d87fb361e5b4e0923dd33c1acb5460fe95e04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
