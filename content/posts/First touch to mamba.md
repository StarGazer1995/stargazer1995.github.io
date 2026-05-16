---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVABMSRQ%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T203813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGYjixbrmuHoEvzKW08BCqSv7wHfL%2FDkB7bJLzGo4msSAiEAkNKKlKVcbMxf2IoczzTKNn8c8OhwsZ%2B3DIi8iPrVMd0qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPJOVCb5kq5cXQpQJCrcA57p06ywxtTFwcD8Z0e5ApBqklZ57kkhw3FZqwnjbffQXh8kgcnbej9pOaGBawv11fgRkydyw6goiU%2B20JMSDTU%2FT4wqfzETeWGDs1pkq0DATyJ8r0%2BWp%2Fp8mtj3fHxMxgA118Z%2FzCKs4Q3bWVlwkxHQME3AywHKI1lAB8mhXpI4WJuNLHlhQ0nC6SFGQrJRC9rnSvqKUTe2kOQ%2BS1JUV7RS8emwDIHJinfLO45vbc4lsPGpmhNCBEPkz1sbptJ177lAKslLyfojrdQADnAKAIzFKdxFjjsB0LtoUdYwQoGIaS%2BjQJAoOp7ifJNaQDVu%2BVxzN%2BgryXw7XGQUUFlmfw%2Bg5W9qQkH7LvjUG95GA%2BipdrYNiUrFGpe%2FcNJbK6kGnMevWLoGSowdAqsVF6w%2FmacjuaMOR7sbowWLmUGajBQWgYVClgyzCAZGzegk%2BRwamo81lUcu%2Fvf9DmXtGDKZM95OadVgkQJliOpIxTKDLl2kG3%2FYYFN46s904dQAUJJdrU3qogZDfM%2FmqCmppuEoNhBswVDLiCSywoqtWI5bCQnHL1grm2eshKNdXQ6Bsh3juci8SmKGb2FlX23RTQP6bt6zkojqnQoL4BxStgNk92Ke%2FZApct1xtLrzr%2FwJMP%2F9otAGOqUB9OYzGushqR5CByPdRqf2TP%2BqWokj5ZCyWweFgc42MFrUJIIUbherKeJ1nYzZs0LZtW3esD4lo3kI0EQ5S2OemJWrLfrRpItuGQu0SWUGY7nYtjVOIFAWatHK9W1jFBmRkYFSBH0Fx03FLDQ%2BxcpqDhBNfGAHlBbd1uBVjXTZNuuhEMq9i6zhq1Xpjs2DPa4XeEom3%2Fqp2kB5pP4ONhxHc6qZLCWV&X-Amz-Signature=a301cc99ec2e6aa98b2c9399a94aeee71d56e594d85ba85330dd791f80bceff2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
