---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QL7GW3A6%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T015335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICJQwclxJHGyoFxhwyjemJLQF8EK9WcPd7zHQRaL%2FyxwAiEAydQKtO9%2FyhN%2BKtrsmCrYOowQt8yvJBQXRRD7fKdz0%2Bwq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBJwt6k%2FFmdIOIIeCSrcA7EqVTIjZVLfEBHuehzD9rFQooRz2eZL%2FAZgAxXnbcWZV9RS7yJBzNtF055ajcs5qBzdWbq7wUllNe8MUpCiCSonkUH1%2BxCNANhq8G7QNb7%2FbpXhXqF6bHV1AFLZWnWBCAmxYYDsFsNUPEergRqbfidPuYA5MrA6ihiLgyFFFecFUQ7MbgbIbN2w2wLTTrPa%2BM25RyUOJDcoJbd8VnPonrxEFxgfvoDp1TNf2qjl84XhpV8RQn2sp6UXHdftHNT%2FZLcTcKOsohlB2rtGHaW1Mq%2Fk7A1FjY7cxuyfFaNlLcqrzViAFBRhcAcdyuOetk5%2FzXELh2xduAsmBkj36wukXYytLQoOpCp9RgI08tUFBK76Gch6k8VvvifrNPVGstJykV0w0W6I6745zUDIb%2BaYYbc1IfSK417r%2B2VdX0XSyM3vkyOaX%2BvwXx5Hg2JADdlVCZlv8pU2HvfXsdRC%2F2Ssr%2BCNePsneyNgZI0d0VvIk2lqZMp4wpXr3vVlZI6HhrqRlha0YR%2BTk0NSCmst7VlR0Vcc%2BlkAoNkpm0ie%2F6gNAeTfpGfytFUlTNjDPkaeutHVXMLPorO0iTugoQ%2FJ%2FfSBF8ko2k2pMl08Cu%2FZW6mkZB6A9%2FGfa6t%2BmkyL1Y5XMJD%2Bw9AGOqUBnSNw%2B4HPxwhvcDRZIADhhk803wgHKhE57Np%2FwbFBOra%2BW7EFmZASVZSxueEbLeUG%2FkMemFDDmMnbNnPRSLssydruAxizVAtSPj9khazDUiQX715HJPmGXL6oxneZID5jugMZSMedtVpclWI0TyjSkFwxwhhPYgQDKGRGWeCqF4XbqNz24pl1pfmC59FAPjezZVVJCTLvMmRR9xwuk6giTJLrZ6z8&X-Amz-Signature=1488437090e80b173b9472ef65a6e8c4114053f919bc4f855b725c7d1cbbfccd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
