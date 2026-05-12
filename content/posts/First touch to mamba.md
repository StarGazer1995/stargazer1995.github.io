---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKLLDEDZ%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T211307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJIMEYCIQCZDhceO4whpwWUl8ErpNRPY4eFk%2B54yHWkyNVTdGI1FQIhAInREoXF%2BzFgFlmxaie%2FiUbzfCUGQE6dIy%2FjFXdky0LAKv8DCDYQABoMNjM3NDIzMTgzODA1Igy5EC4dsq4thHWmYh4q3AOUdGOmydBDxKjbCIFgqkn6%2FRmfIu2bynQs0SLsMpfwdNbl8rOYAZbufFF71L0k%2FpvhNa5m6bZc20iajgsAsyc21tH9xeUHab7lVt4FX7w346YybdnW81hjx2N1sJFypkix2R5gAn9b%2FFd2bhxFYyHMqfwGqGwFmohPZ7yTgvb7%2ByXxvrbfxfuU%2BS19LTFf9O3mAX5i3xY0VoIibo3B5g19cLT3YPREfI3uGMWMXWgzWGw1LT9e16Hfcd31BPOqNZSrgAA3gYuMBhhJMtNlCn5RY49s903%2BObvCP3Sx4oAo5wvNAYnDKvt%2BUF8Lm49YZlZdR6M7qmqY1Zw8%2FdvJNfjJTonuEYAn4yNpCdv1NJDJDuPL0Dh7UlkKPWtTxnI22MnIs8MhNHAmoCI6FVdcgtTMgPxlgG%2BqoiDtgIM6jJiv3PPJQ26JldwvqLVWYEVj33%2B%2FVzyQQIbWRPAe7aLc5s3WDjJqk94bFZdcVoXTQ5dqjTH3Um9Qm7dCalE36zJRCdgsYjKhWW%2Fz21d%2FYhP0llTMqXPce56FmRHoIWMGoC27%2F%2F2GzPP1EOvc7xOFpYiDpuW60BX6H73E9%2FoX6zalv6kmv7xEZEXXUV2NGqyKz8Z34RzMCbHIH0%2FbPM8XlDDgm47QBjqkAQo15jNovEa3tU7HoNykg%2FgwTN54uHG60YMZPbzezQOeoyES%2BHS9rp3mh0hN3Fg2UEP79Tj6kArrQaoJF8A1NwknBwJ4AoiFijqx%2BdlIHOFDjuXkQlsXIkQJWiXYoBJwdd1VUibWYf6HUzaF3Xu2BodIF0NC1dlX%2BoR0jW%2FqHXNU1WGjdY3l32ipJHI7Db2GCm1%2BPCdbGTT%2FKI2JDlEjuGmzH6su&X-Amz-Signature=c8fb5f6306523d62fde6a686a04b090018266c350f7969f859ad2baed3d2ee9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
