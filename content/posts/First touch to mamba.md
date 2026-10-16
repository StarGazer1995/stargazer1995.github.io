---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYUXQ6GA%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T063459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQD%2FHXAehwSjgdJHJhQsk1p7zdXBter%2BcDKUekddyoopMgIhAJ895XTcMQLqVp0V1ltKsnd7bOFs5QFbdQ5Tq6uRLzC2KogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIAKGzprTeBYXoMdQq3AMAVwt6Zn0gQY1jPeH%2FmW1Tr%2B0b3DCW74E3CFjSNClPZjWCx%2BCszY2ker%2FsFXMjJXobZHQHFa8Miv8E79IIql%2BIqrqNeIJDaMTR7o4K%2BC5msWCFEu1zFY0ekKwDLFVZ%2BUDW7HrBFNfjLKecRWhLRbBEP9UN6GlVCOaLfnbpWEGGsX4LnTqWcciWFpY2Mu58KFzV6erFsyOI1CZaE855u7VgsemEqmLS6wmRBZa%2B6CTMW%2FI0lsGYqAyfMfDNPKSXCe6CJw8QVOmXcQ6K8Mlv0dKbK5SuTyQstQw3JcY5btLlCf0t0%2FjVOkkPIcgF2myg3bQxdUmB1yV45Gnmn69jHF4U6f72QlNcqhfdt2Jy60bHuLC8w5rFIJKQX1Oi3WKAQwWFsvPIYKGQkb1TjqOlafnJL5U5dyzWwUZhIriQnfsN345Q38w%2FwAnqvpk26xbXrIdhnrVy0IOQJGinLGksLM0AVdrjs7wkBi3xzsWALHHqB7EZpPCv0Xj8mPsti4YOWD2ferS6WhCGOT3H7k%2BhegtmN%2FB4%2Ffem6HKtxYaF9oMDl6LgC%2Bg3vlw7mkkVG3nRTCYJ0M1K4VSr6IPUDz769XVq3WCnVkqvn6pHuGKmFnNNF7dlcCvD1cJF07dFRzCW1sbWBjqkAX9mGeTDFzgH17qI4ZWgHXcq7p3QO0jslpEa2q7oxPC2dT%2F7cIgLDhLl7qc4CFfxCGZOrVIZ7vZVBMDVCCWbL3UizCrtFBFD%2F1b01311l%2FORSiFJE8AWsICxGAbPwvoJYIP1sSb79biBNz1mXgzoPjq9E1qfbTqomC8ldk509t%2FElw8CM70vGvicf%2FT02TlhfFdLFZ2iF6cTK1XxrUHyhtaIVWZd&X-Amz-Signature=57f5495a3a2395b3846461366160d39792475df12fdfdf6886e95ff5d55ebf72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
