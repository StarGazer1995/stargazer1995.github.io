---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMR6T6V5%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T185114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHJJSm2G5nYSsZftentOB4vZaST0sLu6973zQOSO4SEJAiEAzhls0gd45Ry1AQndpJ4R6h%2FPDmPhd%2FqfobzIOo60KvIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDD2YPx4J5pJ%2FtoGEhyrcA%2Bxns7sI8AAj5tf5fWV4Mc3HOxBfx2Chs%2FF8qPxhoJTd7euJ3mPCtemIU5dnuMcdAo39iEsk5ZjJcAI783TWCYGV8krVmALrsAOon5nUcmTIYq6MdM4%2FDsy19SMtUEbXSJc9dzN%2FMf9ORJWBq6ndxMpzAShzKM%2BZAUg%2BQoBc2vv6VMEKDfpCT5u1tVTRLp4a7PKpBPJAAma8xoqxiGoldcv3t5U5CbS%2BwsaOuB%2Fdf6PCsxLJICehK7It5vC5XT9YvQNqXH9q61YrdaordhoJ%2FGwQDoVZISnNwjB5g%2FOeNMYR3kS8YvVeO8C%2BeJqTT8TGvqqrr%2BUYZ4djTqqnjpMgEPohnVS2tkb6cpBk7itx8TUBWZwV0%2FacWaxOMtP1RBoaFq2j5Z7QHDof7Zf4qyXQtOKQBQOsx20g3CTBOTFUXFCaaPjbxfN2Wc%2FSDMXQlKHj6R6bxOy0n4%2FCwilCsRPaBMBcG9ngfL7E02Mvd7wk5bf0o%2F5gpnMs%2Bnz7k6uxB2ZJiOe0ZWD8xithyXNsYjp0RI2zMSpII3ZHWRwIG82TCG7nGWBgzmXNap14m8N9xJUJaTs%2FvXfJskGh1Q%2BHLeCAXK%2FNeEtnJQX2MGW5wYblBMRmRPfVr2ciyDCUGdyeML7N6dIGOqUBQL7ymvDHcnKY7uRupF%2FwlzJ82A%2B%2FKACKmoXlV4TApLrnZAF%2FeXse%2F7mwHAmf6xnYCOM27pyU4o7QtVFXllqo%2F6LuQEjiWxKsBuY%2F%2F8UQJw1qxk6GRqwg0p%2B55LSoyRe2UPzoFynbBaMWew9ojTjsz%2FWlFyTShNnvfSO7w7I%2F5uGzfCf6CI4bLy%2F0r105eXhvSFT8TMhl3gw9F5ybAKLjstewIXMy&X-Amz-Signature=cd45bb50a07c69686052fcf5de2931760f600d436583c1304ef6da304e20b7b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
