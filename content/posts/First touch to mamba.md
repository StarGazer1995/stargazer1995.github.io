---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GB2EH25%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T110246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDYedZWWI3O%2FcY6265hL6rqp%2FhQ7zRsdEhiN6feHsQysQIgeMzYyhwRgaBCshTM7cPH0bkif7DwgDB1%2Fk8l7ozyrJcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNsrezfruL1McHL9CyrcAzb6W8YviG2d7SEkqHq2HnR1OUECTlnOKdbhYpoTWAjsr109ahm5dz5lKnLD3UjUuu25f5BPiXgUvMQ7k7xkwDbVr%2BIWNEHXy4I%2F3281MIK0dlePR7HJrgLAI%2Byqv3rH6VeT8Tetsg68yEG04FCR%2Fk%2Fi4QEdN0DBwC4Ehach%2BiRA1YlOHaIoWNeOgiKzyvdhXYzLyHTGeBf6qVNoNPNPFa4n1bMKOcRpiUI9TjGN5nWcKej22IJ1r2EN%2FKBJiK7u0Pj%2FWDfV1Z6%2B6LaTptIfqnKBMV%2BeekXJNrulLIFPs3%2B8ZdDvAgZbQwSlyBkwCwbm7RBTMFSnEzqiqomDfuKFqFQcfUjWlEwu9aXCHG9ZG%2BpiNcSDiQB3mxqO1fyTVSb0vHPqCq5bYLv3c1hHvAvyVoz2UtOonPFBrO5oBi%2BQp9WTmUhYflTuup5H%2B94Mc%2BSJImPW6e1VZ0cAbqTQDmlP9ttpArQitYOx3I6xmQbhkrMsAAW60fX%2B4k%2BtEHZcuzW66dP59y%2FvUPzSg4goT7PLMIqHoE84pJrUGvAIFU%2B0%2F%2B897MzvWkMf0AufS3HYyhPndP6sUKpequ26BS7ddycvsir%2BMKa0WrE5s%2BwXWBNbjjOCAV74vGsQbIo%2BLdfTMKjw9s8GOqUBmYw36rtpdl9JXcf1H4ViWBrbt6VWkreKJlf55ziDk6IjLjYO8YJ6jMWIGbiblfi5zV7hydqhhAwmysSdeIvCfl2rfsEsxvR8z97ZukvyaPQz1Hv5I1reD9GdwUEOVWBDHwdcK24fhZ0YDqlYQ33ZYAzJAURdHGrxsBunkRShHM5pYlvuqVjjdnX%2B0HaMDs%2FTiEd3B%2BnbFgQsZNnULPw%2BxFln9qt6&X-Amz-Signature=ca1fab899d95fe4d662a5a69fa4920e02ab7d5316510836fa5941ea6c6b4852f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
