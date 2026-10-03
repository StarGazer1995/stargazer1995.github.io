---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JUYKEVH%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T071253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmlFvYzHWb%2BDDfGwGubxaaQW8p3xfooLwQsX1MMKGwGAIhAOBPdIbMXp6hj5%2FdPRSAZiHExTTJHAY295Kp7YeJKcRIKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTHKliaCaqRiIiM9Uq3AOM72sRSQtvzG%2BGMkzCwq%2FK4uz0toalerB7izZaFPGAKtF27S9T2JHi9GFlx1VyGMJ3CTeFzrh5ivZf0StgjW0odq2qXkH5wh3nCS4Jtra3Kk6VYycmYSXwfCfBJURZyKe181FBRQ6OEjTj73igVCvTJIp3TkTVTvlGa%2BXJusxJ3%2FP4PvMkXvpfWF%2FidfUM%2BxT%2BLcZQbB7ppRi9vAnnstGzarmmPDUtmm9LjvQYQLRsOtZYeUfzRCItAPnr446tJURuHojUr%2BtjCjuFWxI5orc3h2V4fNYQ7kCpNRFggKvF4Ku4EOX6JTl1O7kjJnpeF4z4dluMNeaElatoUrVEM3LnI4mUTpMQMwTb7KjfcUNNyrGh6Qvth78wCrhFuSl3rhaSrexhGs%2FYDlN26cTGEguKhuPeXkLM5apA3qGDLOOZt6mOKGJusJg0A3K%2Bgfnu2zRPpxFO96vQl0XItWYnVuCQlWUbmMzExMo13ymsqUdl%2Baw3i5gyucZym%2BCqXoZnutuYwCqrauFJOCQyCMxmm0yGgR780suPd%2BMPF8TvD9yLhFS9a1vuSFC9EJpoyHHsTqXTayjgFImzOaX7GFRRymx2MbIN0crJC0mRmot7XgsLT1IlGnTSH6nPL6wG8DC0v4LWBjqkAVuijZfuajZrOfA80aWkwUiu%2FC2pBoyLqBPPNVoApszCWF%2BtW2PJQ33A1nGKmXR8iwbleKMb9afYmSWgDTIwSYnPU9qf%2BKPksorcDbp9n6FBKJKQlrIKdIglWCvwuX1v%2Bo8howdiLougrFuKQGZplcTl3TtTZhDhdt%2BMiyXHw3bVC%2BPJ0z2olPBnsabJ7slU6jSkkwk7wzfnuZNrAsrsCSgdeCDf&X-Amz-Signature=c2fdeb5de90d8f90016d391dcd5a28ca56541359f1ce62f73cd1e42fa383e935&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
