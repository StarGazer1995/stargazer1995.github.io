---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UG2B4X3%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T051456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCorEqqbBJeezt5GSplZbvanldKP9ydGIqSlVa3pQ6KxQIhANuVhJRAVtaGGnN9gheQOU7TqVc85odY81uYMO24%2F9T6KogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw28K0jV44jZgFMFV8q3AO6TqaG5QOxIRfZ%2Fyy3QDc5a8A1r9YOEhHjkbOuJVyzp5GRtfnfUIi%2FFz0Y36pc36KsAE2oMyYfK4M%2BzPOcYKaH0%2BrAfpS%2Ff5zgXcnaeBJPStoNSIYtDm5kSyRFSw%2B03wBVpHVGlv9Evs8qan2NeQ1ce5%2BDpoEwX%2BLmKzsKCGa9eETWBOsmu6ww6MAMbmD7nPhuvD1rncw%2FJFO6Hn3Z6Ip6qjYhGhIQ298G4pn4oId%2FDH2LnoQVblwwL4yH2Ik%2B8nR6PNp42y6gRt%2BCpXn7ap1RggFmt5HKlxo20pFTKX6B6Wui2%2Fb%2F63kTuW6T08LJ%2BMtN46hK3OPV7noTRsyIg0DggNUCfbtZxPFNVGJyvVV6%2FchHf7l2urL5yuzmo39vdmR6%2BikZ%2B00d8iicl18bqhWdsLpJ3bJT9JtrYPnk67R8gINIVZc%2BdXUekTAWXZhA9BXVXsJyJUoC2389EflGXAYp1dVSfCHIkC5t48%2FfabfYVP6d0B9ja%2B5QdI91a1qt2oSuQ5weKdgopvbRWkeL0d8weZCCXuOW0Mi6VccE3v6wCajn4mXF9QOHHcppJspeWnWc5Ce6%2BmqtRAfTh%2BNYGReCU1kGFEzcq1mf6mU%2FAczvRnjymSjPHqYB2ea0qzCesczSBjqkAX%2BpPoqMxqr0%2FhpraouBsXOJRcKyJXQLaSsqq%2BFp9T8v2kpc0MrOaTHumru4E%2BmguOxN7N%2F8X2SITzIFbltsUeOaGwNsEFICYY83XKGvZ0Q7cTz%2BOGT35F0e0PNm3ksfh%2BuvsvTuyKXYH1tBGUoMANes9q7B%2BQY5SNOw1havsFX5o4EatMy4LdcSV%2BDe2QXFwHGyVzSg1jGvpVY1L3OXkiu1QgHL&X-Amz-Signature=068cef3f0718aa906f830c1f285314b8387ea5576920cf4322fe2caba2966a79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
