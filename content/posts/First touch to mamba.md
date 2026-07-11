---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLD6KZ2L%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T045217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDR9fubn23k6WThJB9EErqTijQmdLelneO249TFKkaDXwIhAOf0SsPxuA1StnFUdOowF%2B8Jb3Vj5OA21Ke3qFze%2BRNWKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw68TFgB9lWylI31Doq3AO%2FmcM9H17EdreRW3EDFo%2F4OetvoAe1dHelnIVXQyCyUoR0i6bPmqSWXkGrQS4DQRfxvfZhmj8%2Fq2nXgA83rIedwE6HX63bCvbxJ2UI2EnTTjyH9S4iDiqrajgCVhzYhZOPRVzarKSz8BUiQ5WAk5QAzBtGPo9lZexiFnEWGWqSI4rH%2FjaPwkhVD5eHtbRxLDcDJ24fRhYXDYL8fB0FXe231pNJtqyJOQG%2F4lUX2I6afJXH%2Fdpx6ZtHl%2Fq9XXdbOQw6PFK7%2F0t3N8H%2B8J%2FMZRWhmmC1I5%2BKDUnN9iVSCKhiER%2FKRxVYXhY4ouin0cE8eIuZfyIcpYXsj0Dh3%2BuYtGNobTMJgntLzMYCUPczBebvKOO%2BAWIcrckjzA4eCbUSIdbNnMOSMLKirTrjVu0fLYi5hPMkaduTTukDwFOlOQahRX4x3h%2FHLehbqdNrHjAKgP9nL5BN1TpPt6Ib7ReIm1xxcqs5MFdP7HGsHE5y0AcoMS3C79NBbq1qig16VyTr%2B8Kqbrs0SWfgeejpmmIddJcXX8NPyO4gXkwhR497SdAmNcxIXIrY9SKO5NzfVfNZhDBkHRvwl2GqncZZ5xwIqHpv%2BjvsJ7krvxbteVesH%2BU7zSxmgivSzH%2BWFlAn4jDLy8bSBjqkAc%2ButH72TCpy34LLeH033Lj%2Fk3%2BLZH%2B3a1wz7UcToKDoIzgWx1oAZYPpTGIDxbZ6DRAXPvsNOoCZpxXlwpil6zBEDIBhph%2FIBjG0MrsuOmevrSv3sr2qsTy%2Bx%2BKSarOEIqIvlt08tcMRtMgDmeDcvzxfhtjaHs53Ts2KHyVmmp0pzOadf%2FHQgdLrTE84jrIGLigQ1F84bJYAP3sq7Samp5bjtbcj&X-Amz-Signature=524d494b315819b701039d3a10b40f07245a117baca636e4dc7244b0a7b54d25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
