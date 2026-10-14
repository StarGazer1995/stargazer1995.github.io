---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SGPAVO5%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T194935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBsedZnE9AohdYFlL9hLOHko2PJmEwsQ31qOFEKLiP9EAiAo%2FPzNABur%2FDcsQ7z9hNUKMDbc1HcgIkqvUhctqUyE3SqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCpMJDIjUkJih3ALsKtwD5WK5bSJOOnQ%2FajZMRKmD80lbFqiR7bEDNhIaaoj9LipQ8ky0zBdCefkf6mHijkSPK5zqCS%2FYpkpENyTPBHn4tYRdlFiLgBjCLwf8DWLHMKk9nkRQRudG55jDmmh%2B1ClSLm30Hx78mfWQq8xL8JfmWut3ggS5Ug%2FhezQj76lCf0VBR749ZelLHjdPwqdnH%2Fd4YtVC8XgjRSnVY%2Bmt2iDN8bVUh8lpCs3ssoJfp6h5lFPiy%2BBbzbrAXLy50Re7nzyaDlXA7exffIGrMp%2BrJFiizIajTOusKxGkbTksB1pCe426AmPXCddzOXrvoq%2F1RFMyM7%2Blz0%2BkSumG6o3vsFvCOSetqRFQaKjQQmQ%2Fow7GJ5yAJSTY6CRlFCWQ9RVEbUJPPuQrl3vgR4KsMkgFTgDp1je%2BL9Yw98pbJcet4XsCBrYqBmsb%2FCMkkZmGXnCJtiYiaeCO4cwGh4v9hEbLeEgcz64UPySf98bW6ojfZA2sZ2ATrnJS6%2BHSHaAUkMcLnE%2FGdzdbuNJynbWfDgUdsAgcTvhyr4CL5qoi%2BoTdj6Sb6p1CNAvqOlQ2bS9XEqz6RGvZmi5jMIa4D79v7apKKs8In18oBkReHMXIIcq%2FgodhQAbI1%2Fl%2B5e4lOzZN3V4wvpO%2F1gY6pgHIFEkIGpKTHiwdg%2BXPUpfu0LaEIe3o35zT6KHlytAESEgTKJLZE%2BbGMcumKUqIr3bCMr5TIP%2FoigkNK2s2Xqi32%2BSGu4o7HA7seDgJfhHDPuyFbPedFMT3EgqphpfUlGZWKO2IZDR514wdX5kKEzSWMO21XbWKqgctNdW7IUCRwUpvMkyyNksp019AMDPBNqXpnxi55M96DC9F2OCcMNYSYBmysI8W&X-Amz-Signature=9342e4b781f8589cab6822b87ef3f65a4c3805445ad2297f27e9259057e7cf9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
