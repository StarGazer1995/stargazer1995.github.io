---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CWGQESA%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T115622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIH%2Bjp3gG2gDdEDqi0uVNewplllzZh6UTt4w28rACqdWHAiAinVXVU9tD84E9kXasH%2FtBjv56MtLM5ssg8pzWeXuDGir%2FAwg9EAAaDDYzNzQyMzE4MzgwNSIM7uEcZgGemi6oXIHKKtwDnuAbPBf6Ga9NaZpfg0lziQiHHSyQ1hZm00ahGeNupiunjqGeQGMIzHbTRIoZQkTdRsGqp1s7u6oXzNCt5FEj1KlPxz0qsID2adxQ6w9m6BiHzbTYVogRlebL8ICW59W4XWhV41J4OYH4odVIklYp6z6lOFQyfxBz9%2FxnbaBY97eataw%2B%2BNBujE3PSAhIjiyFrQaAD5w2Uf1xWxyxBfGPr13nUipL7ju5qVnWfPKhBIXmAMsP0XygRrxqZ2BNFr51qTiC3YQ9knnXZsxl0q4Erg4%2Bj73hxis%2BK57cxMH2s81JGOvdISjIUg99PGOzfs%2FFeH3WvOm%2Byg3TTQy%2BM2pLGePMDEGvzwhbF8UzH9BRu4E8nuj9lZ7%2FU7zaNyrU9NaS7QfwaR5%2FQn6lF6Kgqb2K90QngabmtWI%2F2GTdrpV3dn9OXj9459XxpiKzMO56rO%2BLW%2F0dj5JKnB4gTXmYCGIBjnMg5xxdt%2FWCmel1ZDp1DfRALOblRGKnl7raFHH%2BkkQyKkOIzAJHWBLa2Y0YLrXDonsjJyxDD5pimn3F%2Bou6JoBQMZn%2By306KrRxeExzNi9sn0yqAyjkOL75U3f4bUwq8t2qnUX1GUYbiB7ZuTVJG32uxJLsHXugqrL3oh0w6OrR0wY6pgFHXHePHHGGaeqx%2BpwDWHFNAQTKBIwDif4VV%2F8KHFIMkShDnFwJ4hFUrwh%2B4Kck70mY2s69q3P5hwZhkK0SeY9iB62P4KLBRiAj0F%2FTndpQHT0wIqEVN%2BTuK6g8CeSG03zIDcKp0aHv%2FQMbosHrnK9dhIv3hwrNF3uu7W5GNgUzfLo91%2Bve%2FZoz98JwmFIw51ccceax8hGwh78yZYBtrOHv11bPDcG0&X-Amz-Signature=bbe9d273756db503633ab733dd211251c82d18af5f5b7b9b6164ff5b70a7aae4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
