---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDU7PEE%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T083023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUu9Qt7zNykQ5313Orgzo%2Bg%2BzcEgSy1GtqnVPwGbRqawIgVHjhm9e2tSmcKc5lLJUR8z2YnZy4jExgsGViXt3jsE0qiAQIqf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2Fy9MzVv6w4%2BiViZSrcA4Z6BnyBcNihnXFuGkU98JKvz36ZJX9B6HDBSgr60S1VT%2Bst5QNouwlHoidMD4IdYA5g%2FmRSI2DotuX%2BISb6hqRZ7tsilAWkWaCc%2BTZvhaOxRWkGHBez%2FhcXNST2NUtBsbyIbBFt%2BrwRKF18bZgkZ19gJ7qH9jG3kj8azJBjaZc4eLGo4Pjf%2FDDMe%2FroqJ3NRT%2F%2FzV0xEJccwYC3VPuQ4t%2F%2BR%2BSRIoSCZ9H4M3yGqyOcFKHGbSuXVty9F3b60cb7SH%2BpVnFxWkupfdEgFwadu2zYFX9E4EgnLuhnxuc9W5gHMATbWBEkkKwyB2XS22GZLSzp%2FveTqhiLGyANa5LRQAa%2BsYz%2FVOsgeGMF7QoNwrJVojnZy7fonmJaVenoJspTv8E1Rm0JBC3Rv3sRqEHJBziVSXEGy9wsfJLBnoNVQOcuxgfZXrCIXaYhr6%2B8%2B%2FPRlXPNWsIvf12Qub4PDY6EyjWIf8XPmTKDOwiqd6NnVsLOptGoDNfxBsuUd3EEBF6vKayzoCyuV58E9qHIk0gSzO1FtREjZGVOtx604vA6Bozz6UfevCRjXHi4ypWc3uASMatXuTtR6NA%2B3G4QFjiGhk8fkXgkMwV0kOW8QAMz47OheiNy2TOgDM69lcR%2BMMO2sdMGOqUBhwVPf28KDbq%2FWk5fjKriKkwFFzvP293tWBWjAkxVTXnCeaFekAcF8O9Vv%2FOq8KRICseimjHHJc2Rc0%2FsdPO1QSFQJEq%2Bp7TFEEIYM8YMvK%2BpMmgk%2Bhbe4T4W3QCMChM%2BlT%2BXuRxDjH5%2BPUGMxDZsBmS2k7Y8mygMNwzxnLwkVbErhpEc9VfYbwZX4wO%2BH4s1hTxvqvfOoQ9ssYX%2BKkf9CfoyVqhW&X-Amz-Signature=c5a963e8aea8799e5c9f463ed69f9608a9cb31b5057c80a0f5d4814ade3b57a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
