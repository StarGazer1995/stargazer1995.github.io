---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GAV2MAF%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T061906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCBs322dDXvozD6icVIYw%2FVwn7cTiVAzjeLyASrAMREzAIhAPZZpcq9Iyyn%2F6AGRU3fc80nMScvttaYlv8pnXLVu9t4Kv8DCA8QABoMNjM3NDIzMTgzODA1IgwfTkU5ZmNT%2Fytpy3Eq3AM%2B2LXz9TadFnPS9hg4BTgkRwEJlJTamQ4yzLg9iOd16u3CZqkAStLIS5w6GG%2BBtpmNK6nfjo4ZdKQaiOLt1dvqROFTqRwPcBWnW%2BkZpPnGnFtdc1BM1fn8CcF3bBAEJivzTtpxVKW%2BczSYfJ8OIYFvrNTpP5qpsnxQraW34qqeujBqek0vg5ZoRHwhCUEjes8J2VEKzMgZim2x7gwqpNZ3t2bW8Jq2N1DzSXcIROzssCNuwJtLTiuif3BVetZc%2B1s7%2BxLbx9KdMkdIkutpeYEmcMByoCGwc0XkCwbj62dzdYXbFoSAoGT%2BCpYohJPVNJ4WXhoqeX8OVA3ujsUqqBOsjriQzHUf41gu53iAn2bEqmnBqwgjTtsr9SXLzAvcXbcK3O4TvZs5YVzGFyod36HGT3sXYm7NY9apRSQ4X%2FEiaErtG%2FPQ3WW%2FK%2FLVzkFpt9MFdqxgrqVFJ31ZAOtMfbgYsA%2BQ7ateTsNoZ0gdF6gkU24HTqPkG39yGHGME5rVK8a6JHpzBLd5ZNStR%2F0qG3dB%2B9FRLfcVVpL%2BsZInTB2W18eZgs2MqNcFktUJrUTtpoZ69Ynp0fEWUiGFXUGJbuPv7HI4zkFLnlkTDIejjQeYy3bM6jzc8ZF%2B7SAWmjClgYDUBjqkASOpgbIYfw9twx7WmZ1zH7ci2ob3fSy8us%2Frfc%2BmerKXSjVeSmjPbTz4ZTjeKjLVjf1Y7tcYybAaa1H9PPg3oJABFSHw6%2FmMJ91KrTGMaEeL1MAQdVaxPnvnDP2WaHjxrcFcGRiRjoUWWAkiUlBiFVz4XYUkRhPJWQ1EvDX8vUMPG6MaylCY2Gn9nh1KXrmPQyyWTMU65a3doV%2BnAsOxdCTsorYw&X-Amz-Signature=1833b0428e09635f2267354b78e1da1442d2ab1f26d3e5af4b7b988e48a46d39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
