---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWGQGTKG%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T161209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIQCz2BCrICplQPuDbliet1U6WioYulfdhW5rm4Tu%2Fpd57gIgPWf4DavRT0paHVQLr42Q1XhI89e7onG%2FNL9TDTWK%2Fukq%2FwMIMBAAGgw2Mzc0MjMxODM4MDUiDEMdYo02VePrVtaZeircA6wNbtxLHd4CkmkAlk1jt3ZW1E4EHFqqL%2Bf7H1cnnp2yTXtV%2Fp9KjVgSYx7w5t6t%2F%2Fcedd9dNWJyvpLYtZ%2BSgOQjuLJBMr3WIZCqDzkQlKTzLaoTR9poTnRGl7Y1aQTbZUU9kgRoJCS9WLz%2BPbqoQwtwtXGZFw8Po8w8AnGfrPuvtVEhsQY4bNlUJABE96im8sX2jCbyeqv87gAEHIF8oJHdny7XEwW2mU2iqdJRc3RxaRAn8qHgEwCf07cZoKoMBVus1pJ5%2FL%2F7XaBXPbQODukVlx8Nfe1hipMnJAWt3EGplgIcMf%2FLkwbMFeDgrtvRSGykSbQGDjJEGd2yEOBfGIw6gDHTUqpoOfSL9TBXOLvWGefAFfvV64GQTLVOChIIhVQl8QIPJjSSdX67kyYnp1ZkHmbPmHFmgdDrEDkS2bUwVNVX6GKPDvkxDyMoz39tftxEbQDau8GoQinboG3z%2FIV2KdygEXH2On1uZTa7J0cZ3g6Nvfwv1A7%2BR3fFA%2BxWvXpBsuGdEL8bUJtYilJDqfMS5F9giqoZo4oMtu49sCTm2Mx9LfTxIfng94HT8nNcMUk6NFLb49NA1LHMlAyLl2AysTzBnhztQINvP4hegJQ4AGHcCtoU8dbqFWxeMPGeh9QGOqUBLv23GD9qK2c5n6%2FONP0aDZrFKhi3PgEellzNRySvN%2B%2FgAz3rMTNXpmpQ39C%2FrPkEdQI2PsQyMzTtQxpjIWPHoLqDvMQBcLG31%2F196fcTATrH7lvOu2SFkwbMqvRKNlIF3KttPCfIvJFsorvI3x%2BNDz7cerMUPAmF1JSo58T1No641B9DemUC636BP07TvZXpGxcGFBI5rsJTXiShUeEINHo8jjQf&X-Amz-Signature=4861f066d76c6f0c6634a8ebc27a7eac770495503165dc34f0387ed82776c19c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
