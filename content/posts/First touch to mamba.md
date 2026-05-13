---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RE4SAIT%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T175512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqt1KKWFfwXcf%2FJIC4hSq%2FbManM9JKBqmh0Kz%2Fq4W22AiEAwuOzc8l%2Bj%2F%2BjDqeXsFtz47VQXCCXhSEpKKyTlytpGa0q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOeyOO0t%2BvpYbdt6iircA5TGLnbQfDZl7iF2sf0EAF34nHdbMZbHztv6NkSQHfGzIOhqjVVi1Bp0tEgptyDzzAon6IvY%2BvtzCDYivHa02Q383muV0u0LWHi10QcvF9bjflkvW45qRwGCqBHY4H1ASD7ZAGnYaqJ0dT6YX4D0D%2Bj2hiHgN14JJRKOmID4IbjjCyMw1uNqnJ9N7wqO0h7M0BHgCs22rH7cxf8qlcCm37sLwCpCAstRaqPrbdV4X7wC7aeYFgZQDTjHavhD1HQjv3FLb8lH287CcrB4QiRW5K7jPv0ZGcoP838i%2F31xpSAYTXxF1qyokngbY3%2Bin%2BWUYv3XWW3h8Afeq%2Br%2F1XiawTSNeyUzrDnv7D22l8rOzpmzku9xiNLfVluYpfaMn6%2BttoWCkDGYio1lVHjWdBA0EI4%2BtkBeueMfdzHd8hDaKLTzSYSWZ5gnygvXhNt5ZHPIfw%2FuUVy5FeXrjlR9rwLne733pukpgbiDkgGl66QGUX8wRfPLpmRyNvGmHv1GMq1YAo51AB6EjQPMVb9MlwlmGPGW6n1vRm6okepcWNEGkYmIE4XfSFlnn2W79cwgjfuOJec0oswChn%2FPThZ%2Fnf1wLEgs6XcAIPMSXNIK%2BaNypdRSZYeKqCuYSfMKd8wmMPXMktAGOqUBvqpxTZZov4o3XPFdy4RPtQU7iinuOHJiwl8FGFOSWYFrFQXyLUfIOzT0QpHuEeIqn6Kc4RR61WpXKqzSzLrKn%2BbbHjyGzezd9HaWAEg0Pk8rdnMl0zJqu3QF3yrwgUvNilSIFq3rRks4KMqduC7%2FcnyJHQhKCVeZe2F%2FVuND5IciX%2BX%2BVMV3KSdT3xIv4FT87%2B7Q7lUeHepvbgtoIo5vVSdvuVeG&X-Amz-Signature=4f53bb85fea7f1eeab1a1ddb294d71a02afd01e0ce875f0ceff619ccd81d1aa4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
