---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZMR2BNI%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T203122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIFAW%2FaNslCC01b%2F%2BWiXVgQtaAkXmrLIUpy4VuzL2%2BoCyAiEA%2BU6anjyvf74x7K3nmcoE3OANCqL8cIA4mATspoqw3coqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2BY5MkgRC6ftAy68SrcAySlevfmsTQSGzv6cb%2BtOADsvpHRyctvoF9hEWw8ATbiel8CudBkJSftmjWAX0kmYFJrCEbZFZlbfTsyjwG%2Bl7h7Xb2Ty1%2BsaGx45C%2BKQsVdIxZ7W8t4jjyv3y%2FI%2BO%2BPMj0XETBVEIIXGIuGPCHPz4Z5BCVfNPXjIW%2Bd69lzdgE%2FQRZEQrmAPfJBHAOJeUsQLyMW%2FATghJT3ejVrNQEV4XjqY6o%2FpU3PtVH2xZAoq3mHP%2FEeOBGd8nJwCNsM2pTaDHog3WC0d5lWdaTrUrnQMXDUZSeWmn3tNTRaZ7p0IsOAVGN%2BKW8u7TejzBPnJeq9BaF8qBEBi%2F0ZhrgFBZP%2BimSWiUGgal1vysvzs9NcPyUc5EfeSlt5t3REEbRGBmOb%2B11SEJX%2F1rJm0ZnHS9fDYcjAlsf%2FK2x%2BH2cusZKq38IP2828ALWHVOZs4EiqBrV%2BBhH0nL33qzQytpOKDqYWI9Zui9WddsmUr2EX%2Bu9zXTxVJv4ADgxMQIRi%2BV88tyNHOXmWb6RFbBbSUuPy6UwLIS6hDmn1hwN6V7isqsOFJ9c1MeTn9Jt1GanKE4wthO7o05W%2BKYOAjnRkOy3O20S7A3uYVRlNA1lZ0k4YSroAXwC3GxD13GDy3Ic6VmiZMOaG89MGOqUBAsNNVdFcnFBCEiLLBqzN0RFA7s4Avt3iQ7lHD%2FmsigohOPoGDY0MU%2Fz4ZDbgX%2FqaBYLiSWHeeEvTTPox9gzY1tbh%2Bp3asA9e%2B%2FJfmc1NqPPLuWeuOI90ErchCh1THYZBTdDiPj8afMk0ijDj50qx6V0oDMy26bgfrcBZsrSKWT2xdr6Kz%2B65daP6hlnyF5u3EutWi9eHK5FJUYDlEl4d7Ftl70Gy&X-Amz-Signature=fd70d0871c29981c1ff02925920e678e3a6135274ebf3aa0dff612ead8123b6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
