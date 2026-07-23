---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3NUSFS5%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T170840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIGjh71HzuRI9rsKB7bHJpcY4QQEeEAzaHp%2FORsSJQoqZAiEAuz8QI7g3Xcew%2FNA8UQkyyYF8EeeBY9YQZNO65h%2FhJgYqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFU0aWWNcnnBmneguyrcA1TyrPE8psWN04q0eCoOWD%2B75o13ONupOKQ6152k9VO4WW7QUo8QkvP58%2FXz0gP8bil44z4TFoVuPomoWXFaf4uWPb9Lszs4%2FFnqAvablRPSuPLSKRgnKwPfTF0M5t8c%2FF6JRKyHnszCsJadEp31X6QjZTPu3m13Zu11YP3Q0Bu3UEAyRwmaSVni%2FJmMK1cM1iy0pA1Uhm2zzbICO9tQXt2phOcD3vSk1pe3IQ%2BB%2BT%2F%2B25PefjgqyT%2FQLUiIkzpSs%2B9yIS6JsoTzKEEFjBcibaPb2%2B53Pgy0ALoQhdxPZCTWMdzGNSkDxwYmddh5RnFQNMpUsR1PmTSaY9Nh4PAriRBpAmvIULNJU%2FgoajSeq4IEOlnx%2BZT4V9BCCSg%2BqeHHocRWvAT9FCheWvmQxwDj1TLgbgMrulg1VOcvoqwd0UDWlK8J62GJSBL2so4IWPoNSMr%2BRkA5KK9avVEOaHggjREkrqW4OiS0yWzQXH6sHYCbyomgiN2XXp0apdxOV18c0dRgHq%2FvhsfdXp%2Feu9iI8o%2F0yJYyCJKaynnsPuCRQjfSvMOi67bgZrBw%2BdIQudNc65EahwpOkNcLKKPYdcdRYqHxYsIhBiMjdm6mPo4PsIpzIpcaqzCmgn82SpIiMIuQidMGOqUBa8aq55Vqz7e758mgP7DwZr3p4CYDIYL5syeOYF%2BPZL4pxLcYdXL6ln4KcxXMRXKAB%2BBoUJwY4Y3dLAxQHJkuLVmt3qCnHLWJ8h8cUW0HfZnvFbEakdN%2F6TbNqwtRtGo2gBrrXF4lgMeTtBt%2B5w3EK5AVj85D3I1ZtTf1nu4F5PZCP0OGxU1BDjJX2%2B1pMaQtZmX6gOvwjRRD7bMH4V6iGqUwn9Bb&X-Amz-Signature=beba0d10b3b2082aa041c5a99483d60016e26b8971f538ec6b715fa555b414b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
