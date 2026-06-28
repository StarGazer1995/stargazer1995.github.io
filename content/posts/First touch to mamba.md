---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFATCFXC%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T151105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHvb2GlPIVg4TZy%2Fkq4wvLSbVcl3gBH7eDwxQJKaHWe4AiAGar9yY07zKcq%2FLQS8ZBAg3f3Qjfq%2BaLXk59AICfeLwyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy6ZXVZcAumjCigs3KtwD5YNmjGWRr49z6MW4928bTQUcOVZY%2Fd0OmQL%2Fmm58KWowJBid%2BTerPYHYEt1ipNr1ONs29QeP15efDmC2ShKuj4w0s4fdLdc%2F4y5uauCOQUrNOvLG8sa9NJIuQZD%2B9YSR1PqMQ6mg%2F26aKkSwiK6c5YkdHF17OgbLH37SaX4odPDWPOVhUFYjhCJITaTrcZqgd9ICUfoyla%2Bj8hAvWbylK7XCbeVCex00MMESBiyau8bKuRck9GF6BL4eGiIphUKYvyN%2BLGlk6gxiJPnqzUvHRAX5V5yebr%2B0nh%2FMARd3TeGthTAJFFuVJvqMOwypmgqF24F2cRCU3jTc4EC4a4Lz%2B9QiPwxFJQeK%2BH6KuiVz4TThj1BOqPX5VaZNVA6PbpQ3kqIBBbHPN7G5bYBkJD5CA4YtSpCWhfBl9V07Z0HIZTRSwnCr%2FWqD6DxIn9cIj%2B51BfH0YpB2raoViBg9KkhWEEDENqtu22OUkiQfIkA4odb9ncN0dUnoWfIurZEOBUfB5YMeOh08%2Bdh5P1V6qBKoTSD%2F%2FbSqdZjOx0xaRfISx1zzezT3EUL9IMlQ40Edg0q%2FSqMTt0r7jgkAq7U64h%2Fmkckqmt3xI9L9wG%2Br1zqGudOxFb1%2F6P3h0fGhVeMw49CD0gY6pgGlBoxxjX47LvwaKly6nYkX8OYm32A71bvLq3M6nBmkNbp%2BbCRdaNPoWnPEqJoeXYWLj%2FQtOjFSX%2BuydRt8BVPxESjDTl%2BGzsfEMPKIol5m1%2FWbSSicj8A2tudVXYskLr8o8lJxKLEucWc0jbrr1VAsPoxl0A4lEeQU%2BcGDIxRK1byvdfSJcJbHYKZMZ%2BH2zh%2BF%2FSzftDHS47%2BTzEIAcUDRK%2Fh4PuOT&X-Amz-Signature=38fb3fd589e91f7a800470448e92338aa7b4763d68c047893adfddc09c015b09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
