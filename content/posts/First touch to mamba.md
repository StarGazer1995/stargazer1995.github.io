---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644YLJIKQ%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T115024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDZzamY09rjspUMznEIRnwFtxYReLDPzLkj%2BOjHf8vtlAiEAsqItNLS8e2kuLinpAXsFwlxCRTYJ04GsmSLAu1KeAVwq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDMR5l32SX7QIDH5eyircA1aktSIHFVOx2yxoCFa46AAtldymb1wk2YTFCKlEVPwFbL8uyaPPURA3Q2Aq8H9wIvwEw90NUpfpBYTllpEQG00MVjlOuBj8RMaxzNynrQLojydNS9JqAAWGj63QXLRK7iYfStPkQwsBtsftXcUPbEiLh45xbmODvZ6rAcpj3NiZoZPwCAuqqC8pgvMJnmHukh4Foldb6%2BrMxoaMiBYmjR2TBzP10Xb9YOSKQKATPuQ8GxxGsnVG5X2MlChTUVupzlN9FlKkcZHX0fNXCHq76PLY%2FvzbtFVzP48KWt%2Bf1wP%2B1su0Fe0Uuy1sx41YKCVgG0ztma%2BOhi%2BAfbF%2FMKkaXFiP%2B6R7k7X1kz6WBrN8HprIqP4eLK5b33KM3rFPeK40Z7UYsKrLRF6F5%2FLzvVbXXGZN2aNOO2yG3zkr3Ac7LFcWQjdz9Q7jDPCRzw65riXongSdCa4%2FUlVLkl1Qjd3H%2Fo0LlBL1NO%2FT48oVLiI46KA7gC1qFnkW%2FjnSZooIZJZ4xI2ZbU5LgXxY2xBm8Pl3RUjJGOTHKMOkA%2Fc4c28sBr7x4piVpGHpkoO32vY7kL507JqS2zO%2B9XxiUx3AktaXBPEFigH5gMnfvFIYnjjs6y6rfMVX1Wd9SlgCP4izMLOTotMGOqUB3dlsjTXaN6op%2FwTnDKj5z1boZiZ%2FWV8EqUSk8WHUcllzEdA1V1mwcPi2TrFa5kMAarW5m45in%2BF8hbJd6aFmdJ2KDlgnIvUZy0UwOMaJrl0ZG7SIGJNl5eINGusLmzqjftKdpogu9GCTb%2Bj9ckIcP11jHs8qEmNMUFRXBFonFXsoH4IMyHxieg6B0KOZ6srRFDvz8G8nRhjscFsoOR2XTis7Yjy0&X-Amz-Signature=7a547e7b1d181dfe570ca010e3463c32506feea5d1faac4e84a09f0e4fa02952&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
