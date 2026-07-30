---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6OT3N2X%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T190728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWYJFyY0mrxHuviOPHuIy23hEXDABeK7PioU3Qa65X2AIgbWL29ATItB6GarxflObB3sKeuvrShIQrWC10WSGwWy0qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDODt464oUTpZpjQ2tyrcA3DQQy8RC9I%2FlWkFb93v1%2FK4crsGNezl4GcZX%2FhC7RvabTY2uMOBD0VWQRnk7hAIUbpIHx13xa8I6QV%2BLgCxSECIMlBaMpdcwOJiyGc59OfFPAgLpCZQT64jwSf93%2FOja2hBdduqVB%2FF%2Bd38AwRWqSrSfMbk3DfG5TIOASF0bvaz%2Bf1WjqW5IJiQB6qNdKjAbE7KGtNmumEVWoprQNGmctLXkac%2F9CD67zH3v3RWCpBtWj8nLw5Anu5H2LIjCN5Y5g%2BHZBvPN6IUasw%2FuN0a8gXAn886z0QTuL8GaCHuqyUDzrxwVi0QFMUssWd5Ycbs2KKCfcBCnOgZpGY21RHhdOJfx%2FAJcNbKVdyri0UyeXNp0FnaGsoAsR6Na0k1GA%2FiHQMiMQBPVKNH23I3cRVNh6gs801q7ygulCXbehAH%2FfHU819ff2L4xsqCoR7H2nE1DM3Y8OdCU1LnY14ipmtUo9qpZECTreH4dsXJaB87m4s8f2LPqNl74TfveLK1k%2B89Wrxwi9gj0ZAoTT9JlLDfOQb7qS3uYlGg1jQIyjI7VOMLJuMYATEyQtCzeV0IF1Tab0xkbPfD0ZzsG0aiG2bPuwfmVTOcRo4tNC6ys404DFx3pH3Z9spxH49JjrYEMOazrtMGOqUB5CnLgZohtjv73uMMm94M2%2BVaP0jhWsOCwBn2Gwmob1SrVBKtIOpuoL7TDs7LJFXAjGMvfHk9M%2B7PPLZALizBJEWs8%2B0GRtn1IAaycTfJo7QhvbAeKwuoOSerbC1AbI9LOZwt1Tr9poiGBYk8suEoaJi%2B57uziPxhSR4T5lKI16uq2RDhLvYfBoAdIk%2BPy5GL%2FRIRy77Xs77n%2BnLpVjj63WjnaA04&X-Amz-Signature=7bd2669009e65614b39cc8788836ec823dbe7463224edf75f117d6ec909a22b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
