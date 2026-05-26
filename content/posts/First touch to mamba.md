---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LP3PY2U%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T212729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNwT%2Fs1nPkCiqVpEtX3CghQkRJdCqUYhm5Quavl1BsdAIgflORWCxoKjF1OdaOs48iq3AOeghtpZ%2F189dgnbjkhfAqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHFdk6s%2FEMt6VHHZTCrcAywfYD2G05DIGCDOhKLRI1wWxMbSzGNvDsiiUzc%2BKS0rvJ2SxQrjT46unlIzc%2BKq0G3DK3tcJXWmyDc70sBW3FixMd8VXjxDxA5ANlev5sccYqkGl9ub4IfsvIPL2cyK8hjLPBGlYUiAyPsCids6%2FI3ey1fiAWw1KaBzahuxLjCPdbzN3mTUbNhM0rTXRudNOHS%2Bonpq7uTnIQFCxGYGuL73LoiLzifhM3KTHVpk6Xo2%2BwUQpK42NEWrdBsY%2BU7%2FsV4uKFgrnTGFvyaZxXFds8SRaQYPPAA5TEh2EKIgdhJom7r%2FnbSeCeIoGf9Lp1Po7cZHRHGJ42qvBr2qdrTEX8UYYq0yVgbT2ezzatZieCRxtrdPXpaNwzmrBmk2k4KOAND3Q53E4gwaXHLDYWixUmH8PgjP2WGYq1VHhCzJV4r8KtO9bjEWf4eaetGKrCDJ7G%2Fgn7thXYKZ%2Fki5vFoC8Un8hzTfNa4YpRQzqwEjJJaNN8r%2BIVrU%2FgKJ49peC5A2%2Bqrwq4Mc40gIN9%2Bw%2FzlR2eHGI9n%2BtsMRgzltYOgm6SRcHJtnImAcLYvEtHDCVx1jMCFtn9i%2FieqWBz8E3gOxKZec%2FXlbQU5QeCkvEkrTfGKnLFyu1b14Cx16ArXWMITv19AGOqUBrsM3vyMezDOWjXyiBTHTAVNEAAp13kswhlkJ4QhN5lW5sTHdj1w9CD93oa4pb0IbWpK5%2FH6FRJvr8yvhx7Ak5Yz7WQzi7YAeF5rt27FKMfUzpD8aTjE8MNJfxt6msboxOa8q54ObclJy%2FHDziLJx8UPDWcsMh%2BelqKYtbt5PEIHdGDUy46yYSQMRI2ShNmdK1PUV617TUVojFZ0oqdaellX1TdZu&X-Amz-Signature=7925dc0ef5fd7132fcfe6c739510b7145eeab6759910bb6b633e70ddfbcba81a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
