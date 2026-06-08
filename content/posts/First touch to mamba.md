---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXK23IIF%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T084411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHRcfx%2FMjXYCTZibfr%2BywuzE8d9L86YGaWkn3KmUboeqAiEA57ICYt0RwqrxKNGyMoyS%2Feg3yP645kxfB%2Ffn86obaSkqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISQHEOtqmwPMbzTiCrcAzot97S%2FiKr%2FsNOzyVpvjJgXkEMiDyDznesTNcZZUlVmn9QClwDjdQ%2F2rVK1KxuaDmWDwLAHHvdm4XP83cGqbYwoEEL4z0Dl3B2Bz2ANQydvUBPcm6plJTSl9b9HejDjIsR0uzkCzjan89YLYBS4sAHKaIYqWiDfZQbGqbkKQOs68dhDLr3L%2Fwcl%2FMad1WeCpIOumizSRoxy1Xvg8h1WIx8kUOEQp%2BqwBYWFlvlNTq0mwC2hw8%2Fq4%2FhhjiMwL%2FElautoMPHuq4dqsYkLMKlub%2BT33we7AuDfWbe1dBuuk3%2FqVyXCNPUAaO9gu6IwNA7arLaguZMw3zuWE6Geg5M7BHB7%2BHrJAkiPo323DnoNgMbYdPUp2s63t0jwNFf1fQqdkQnrXKROwHrFc%2FhfN%2F8OdO3TAX915Rr6%2BCHGYIWyfSZwfyef1eV4lBB3YF5eCrMd3J3gcw2RGzG0JgAVblm03ETCmm7Hu%2F%2Fz%2BC8g8sIeydageqDPkiLSx%2Bq3RwxHiIardjJEyPeZch%2Bp9m%2FXgCwgeOiNlQHF3OTUtyKaUkMiwHL6fHJ3nQYS3wzNngWZw%2BSJr9pX9tVQ7x7hOqWlqwVRKIWa5v0zNVt%2BHveOyO4MKGg77Crt%2BNjLFEKLR%2F98MPLgmdEGOqUBSe6k9NCD%2BLs4X9688ILeUaJGYAcTr8IdK7ElyYK6a34Thxu2JmUNOWHDRQQrbvKDFPWHG6wJPKK%2B8ONSsRyNnvTbYgojO6%2F6uiMXfOcHBdgaMN5z8XemtTuHSxA%2BKdNa7KziFWrbozjuyAcgDnWnR0DblODu3xL5JKlR4WUsLahf3wcCanN0swa1pRpvH7XSbjHpsxQ8W80lXs5zdXHydWU6qJpd&X-Amz-Signature=0d3878a6a9ca5b4c27b06673996de36cd3b1033869520d227dd0bcee29e9cdc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
