---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WAC3BXD%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T164503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC2fCkpCO8QWHDU4VMmlQtNEb61JVOSqZ4KbDwXkUe6rAiA%2BpZHYoHQG4MZwp1XyqSVgNShXA20tcAKBtqQhpa%2BELCqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2yrFLDLBD0uC2r4aKtwDIEv19bxsy7CrTnbDAImkBPTW%2FTnfQhwoRC7ia59cog7%2F9QL%2B24dfRlQZbuRv8MfSwDlidHkEJ%2Btl6yJ1Sey0%2FMbSvnEQ5asytktpwjzxT%2BqNJjqcFtoODcpXaPH5sOhuyL2IxWPk1wVb1C%2FkdcDXNZa0OGiwAtb252FuY7xEGXXMNUpg3Az8C3SpD2ldHej%2B%2BO7n1Tz6CqOjwHSkpsxcUxRo5HJHuDoW%2FFxhPB5jivVHdPXXo9LII7%2BDAeaBuVdgHMJlO%2FDxR%2B4KCV%2FJ6LCuCBG6zimu7HC41dKRaY1eQsMaBrppC1IBYdW7MdiYKHEYcmZafslznp0kIrsOyt%2FC%2FAYalSQPWMEGu9FMGD%2F73n9O5FBMNIvyk27MszSuyxha9AnnIopbu2DEDRBjgq36%2F5wJkW1nIBJlLYnWF%2BnnId%2BGPmN1SDamADDZW6moWNGgxWk9PRRLdBkTL9SKZL4xP90YW2uYSeidWq5QgAdOp4LcZFyDNt1FWR0rj07%2FKbsapj7vAfJPyImTLBVhOpTgaxICLckQWFf%2FFbGlSaS0SMk%2FPBtaxPZGBY63hfohcFVSQZsOBZKeHnZwDEuTlNbYOawQSam36bKGoOleoWv61o1vrQbhR%2BmeKce%2BeiowkoXt0wY6pgGdK528tC%2F5wOGkbhKbMsp26Vmyr9ILTKdqmSUfV2WWDe4%2BdKp31zKVVkaHYfOGrZTR%2FX7iFsy6T49MfZtAyhloMmwHM9FV7lP%2BMdrYanZDSayGQgC6%2F0RH3HoEEWiFmx5a2q3iR6WwctT%2BokHPV%2B7G1WTGVmSJOFw2mEa3mHdaSbkhDk0VLrGtqw1LcqzElYsul07JFWdsY9u0z0kEUZgX3e7Apgkd&X-Amz-Signature=17696b8dc61918e342c3ea473caf6a21c82c32c9d832f91282612df0edbd7d8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
