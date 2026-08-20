---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO2LNQ4J%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T142603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAF4KEykaWbIceT1rZTGCccxlV0mF6keOLeKqJZ0vzYNAiEAzt2Mm%2B7CJkS%2FxNxedneob6pc%2BSrdIBSrZFmZt28KahMqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAW%2FGxkmapids0GtRCrcAwQhIMFtSWS7Wx6fEWLtkWt49Kajh6H93XIt%2FeHCQKal6qX7CN9TUVJcUerSRRfNUwGnmZX66%2BQmJekL9E34My8dy8Tp9jmHhZt3LW8ikv%2Bdft6sYStG6GoHomMf%2FC0H24CuIVCCDJJjRHtQ%2FpKkMftU8dHjnc9sClgkBKAvOGIb%2BWO0Yy%2BSi%2BdyIhwloGvaCMBkzfbkrmBivCz2iMOVnbdoQaUdmqoMZHfqw%2FKAqFWuW0l7mhYoCuVXNvJLtAofjvyF3%2BCUj8jOHTiRbFO3s5q77qQTpTdukiETX2fWzBmRGOI2XhzByNPwJUf%2F1x7IzypxXJ1wOG7adh7BZozjgFPVnpvzzhjMK%2F0a2k4G6UKGkG2WHuJybwlIPxC6o7ILUq90TKtD6i%2FAuz1LvWJitgbbunbrTszLibq3BKaMJIwpUp9kg6vN6mUGGroV8QU1H9wjHaq17zcDI6O8fSOYlmfXSj6gnNhD2HKRtrdB1N6aptrQawMhiJ%2FX3vs6%2FIVpSGJPFslFXoIDRXJYhYcVIkm24%2BH3Qu9fiPgWgfW2wZAxl%2BrMrNoGWMJcUB5%2BJtxvmOPbWJcUriXSS3SCv7OyN8AmbO1ZzhDOuAiqVWfPWEQGjeXADnkOdirMxDKgMJLrm9QGOqUBHvT%2BlJrPU3KVjYswoed0fIwBYSk7AePoQx6s8f0215N8Nwuz8v3jJ6QB6Gvl%2FRUoQ%2BxwBz1bLqEbTtv8RKXcXpoCRBP9lIbirFs21389mKP4%2FJtUqI%2BLPBm1oSAvYp2uUTjUdW01SrBept3fdz0Y8%2BYQ3yc4FT0affY78avyDpQ7r1H7KIk148ozwkZ71dlksO9PA0Z%2FY%2Fj%2B4oCsjnD9G1pJh38A&X-Amz-Signature=94646d8a926192d0104e030854cbd7ee63bec76fe9dc5c3a0213360a531a81da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
