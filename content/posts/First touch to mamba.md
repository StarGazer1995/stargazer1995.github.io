---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5NB5Z4R%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T033534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIDHETHNMeCDQj2JcEwx07ss29oldvOv8zpQE%2FaWWPkXvAiEAq6TsCC3sgBA1nTokOMRnzOv1CStIINgErb82jwezwVsqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXKPLOtcv6HU5IkfyrcAyKm9m0WWAVCC4MF7d6VX0G68kAlDrRhBvocOwQn%2BF%2BJ37lb%2BteVNqo9Op%2FClRLXbdKX4E%2BYhXQUiLAcSASGKl7ZV3M3BvoTNCOFC4vlT3%2Fn4zusKMZeFHc7Yt%2Fy1ePQuCiWneqJ9NQFrY3r1BJ6Flb1BJCUmLJJBa7gkHowN2cX9E222Lt%2BAdTzcFd0ItwlRoFMT%2Bzx5Ta3lfwHI2jkhNG%2F5eKI77gm%2FCkl%2F%2FLNl0mANtDHwa7G54NrWuGhTgd%2FcQn03yWJt509Kp1tTu1mqrZs61X5R3OfzEW6XrmoBsK%2BC1eJ4qEZAEvKXrv%2F6TG1wRPb3Yar9c3baEj34fRG38z%2FwFrgY8H6%2BOQ5G1Dv%2B28h4a82ab3ZzGC2VKGtSPQdB1KU8UmFUs1iHUsZyWFdpE9UoEeVk%2FCdFDMAnmT5VDQ9D8KbUcy1xbP%2BzyAtr9TwiiHBklBBsu3m3xLoQ9Zl3SHXmbLBVmfsol7r3RrJ0D3HWhVCziqjArceXM7QmpY%2F8up505XL24R0wzl6rBMn1iMSLBciF5d7c%2FrxdsG56MN8KZh4sD84J4P%2Bz%2FoGRTYSZI2aWI39CxeqzJqJTRsM7rUG4TS4L3%2FG7Ag4hyqrc9LoQbFfDjPPM4%2FIrm8UMJuzkdYGOqUBdpGwj7jNjy%2BvnY6KnS0lWxU22YuFno3KvAiS%2BtWNyySJmsK%2FXMhUHvFS7omzVUXF6HNILW4VxOtp6FvlTY1ueQS97a47AlXxKiPtkuh%2F8M4zcQbzknuespZgjku9nIUa9bFG%2BjfPKbVgXKGPTEc%2BheiOEi0ru4JhNLu67gU0RWuU8GKQ8HWqM6CQIJIE7Nj5YxnCASJ%2FjWlv3oFMcQe7kokUBnU1&X-Amz-Signature=f544077851200400c7a04af6bff14665e603a5468318006c3e91c1f65810bc2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
