---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLX2MOAD%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T172953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDvaZvfQiRR5%2B6rC1bBp5rvHDbj8msxBDh3smT2oc4OBAiEA0ZASNzZlDUhnsAIqZEOm20o4EFUf%2BHNltYLbC2kL2PkqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGAgKLJy%2F25MK%2FcJNCrcA1aLEuq5Bk3f%2Bjato90r4i1p00534C5OXo9Mi5wS4CYktTsK%2F5NZKRtdpYbK0hgD09%2FbDBBRGlaeXxRpWNtqZZYyFTgZ3DoeNDwIuN8LS%2F%2F%2BjN85%2FkzQPX%2BznJMhS2fGQCA%2F%2FiGQpu4Bbd8E8s7Zo39VYUO0tz8ajc%2BiM5G6W92geUuu323FvrXXvLe%2BvGt2fcD%2BNUZ0wv20h4yH44xPGi4Qs%2Fr%2B5c%2FpM3C7MsxSGf77wDagqOk8Qv96wybBBLQd70E1Q8LXqgej1TJcrOhi4pj2O4Z0W%2FXgyKxeTE3hX3i2k3u9icLld5mdHg3dxvRvGSO5NJVXuvcZ82y%2FKkwqxPDylJBVXLgVgQuCNzcIdfoIK1yz%2BPDIo9k0N0WmnXOV2f9DntAxtCepspQYxkPHBWOxk2CX7lPFzG3dIbBi9vPC2kEhAxjpdsL%2B8mlcjGQTkz9%2FplRI2v99eTeSlFxSlAiGWI0r0o88P6FC2PMaOeQXTxBH7b97b91li7bR%2BWE7TGuoYC%2FZub2VIGeM%2FZ9XmbGWlI%2FduKeKlVkLWAt4xiPsPmnZHC8jhY66fTc%2FUTv19nFCfMJQtRY4wnwV23p0KzXkMyk68%2BNJAJ5Nd%2Bf8kHGhL5BivPrUBWCnLmjaMPC34dQGOqUB1Al%2Bqi60EYujya1Y0yycLJ7%2BNtyH%2F1M1k131I2PEs5bVsj2tArrspMBtD2rWvJVAkcn61U3f0UGaftrA6IywTSHqVocSVA5CAUucp0PRUm6R6J3sIecloZoW7oEWD%2BtdFVYXkWU8Tw3DxLGxTwwaZ1lmthztzhmXjaVK8ucWdjFri9QXrpJGYJPdxO8%2F79nn17h6WVpqvzOPd0S%2Bzd72PFkZ5%2FP6&X-Amz-Signature=b739d13a664bdd61e77c11ab7a115160c4d39ad35d7869f56a3bc81166137a6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
