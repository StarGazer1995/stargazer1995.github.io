---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQE3JUX4%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T144610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9ZEZbxwVAzSgmt%2FRfhmDkCGudK9eRv%2BshsXXAwxfRwAIgJ9NS4wUTlxC1kH8MYxL1lKV0ACmJhsZAY%2FLuKvomEIEqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7OPVsGOvsZJxV6zyrcAz1t9TbtAikzFyXRHnItOvFeTaf0XDXljAXVyKH%2B%2Fm%2BjM%2Ftmxv5Whk0q5RFGKLM823WyUM3X4P7NdOspCqU83WTWCgxiMP8nwQzaC87VAHp%2BzvYLGrWMOQhkmm2C5dmFiitZzFyT8K4xgw2f%2FMR0nEgJfiYdy3gtbdClbUYNwkFPgvLj9CqkkVxOSWEWUlmcC8L6OlDhHpIzkG2RsrHTMFY5K537Dg4OWtu9VuHZn7P%2FA9KoaXjMQc2wwlNdL%2Fp3Epavnl6Ya6jfMoX3aZe9Fd9%2F4kOYEcArgcMS5pIyCy5Ug359xpBJagcPU0GIe20xNcSTJY5sjsPnQkzUkAihK37ml9inNQrmrB4lMClWkFoJAkkCw6sxk%2B04oZaAHRKKFM36PxcQDqR7WLn9JmDIouKjDPfrsljdwJ0J8SCX%2FK5uVLpCkf8Uj9MwYRwqzbKWgCMTloIBspz86jezSmnE7pTU2lXVHC5hP5GKAtL%2BItzTtmNd6zC%2BR4Adg%2B%2BcsQDvEmhjTrqHG%2FPnGfdNy1JR2cMv3TICR3A7WYUvKw9Jn%2B0WrIwcB%2BWxg2h3I1JtVFPNZilVMYhUQ7gs%2BdFMvGSrpBqFrgTmtx%2Fwhw1xXvQ4Rdm5UFfrV%2B2Nu8xduRVTMKSk89IGOqUBL9Bxe7MoPMKrCwloIHyH6gMWXVwiANOxYV5cJLkBdW6XKQKSbkg%2B%2F%2BkOd0z1Faowlvh54kbmkoWs3GYD3ns3%2FmYMsEj2%2F2cdSSIp%2FKisywUyQjyXC51h6weYQMdZtKsgj7EtLnv6sfa7HkqHU7g3PUOpWPDIv4uSAp90ZRlWkuH3D4G%2F4loBPKzUPsxYBuftSKm%2Fxzh9N8rCbLb8W87KS6Nhw2GF&X-Amz-Signature=60e4c39012f11086bb431581a3a535f85f5490aebf6330d317eb7b36814c0a07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
