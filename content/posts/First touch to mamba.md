---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WFBP44R%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T235502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID76%2Flj1o8E6Iedqn%2FDpcidwlNUIW0Alh8kosnB9ydTBAiEAiz%2BR5s9wu7i87E8fLcCuKF634ecEfeEg5u6RZSpGBJgqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaM9MPoOf3lAejn6yrcA5aFBle27IDtZIW%2BEWoFZCNBxRublpssbtT81L03NlSNriPFz4CrFqWMjlzLAO5hAUpqwk3zHDnBMlUyHiGEVwZ9u9tXF2NVGe8BR7Zekd%2BNnml1RAUo81m4pQtiuU%2BrcT6%2B9yD9LPhus0AIJgqY9F6Lfoz3ACO97o6G17D%2Fyi7rcIMyYqVd9RSOW96KrznZWA4%2Fx6a2pDEiyRFSjsU8mmKe%2FyZ3PcLyUqPDD9J2iQUFrxvUL8e6S42TgMdg9KDHzGTGi4sXf4cCq6qmXfxqsSZTuCmw8XlrmE6BNtuuKXkK1%2BP0pq0ZdpwPDn8Ir%2BKUSbY4zHaeNjngIv5Y%2BwRc2VHR1d0KLjRsAQz%2Bc%2BI89fE%2BR%2BpwFLDwykBUWqy0abxe5fO4%2FOeX3b9tn9pbpCjXG%2FJPtmAFJ1EwNfY4hCbgEl8%2FZB3wfJh8ipMODttRbIcKOGI23iO5t9%2B5xOSGzZ1on7IFQaIpN%2BlGMVONjDikkAfkvw6nuRbr%2FBKhUM8SPRB%2B1CkFIHjSKZwgnPQ3KKaY%2FOeB0XxblyZAYz9v2Sw1jvUbITEgoFTB4Wlh%2FBCigGSF6osKcVY0Mx6nJ9tQujlzQlVi%2BXy4D%2B7fIOxbfjkrZIVKDiFd3BQ44Xo2pOcVMJbWy9UGOqUBrEnRHwCSMJEPWMpWa3KBJv4T0OOArgCNrTbjOTPZVuTxOWF%2BelRJdZEXMdv9Ql761R11eSEl7SoDClAxE1koV3mOVhMbLX%2B8E2qMw1R8lz3F0cqh%2B0z%2FQdFSAAIPRp%2FPGm0wmn74azxDuRUkxMqdDSDWseenNvVJnHnjE9t0XHaVzuh6hxgAo15Ep5WqeVY7SkIxRU%2BWTmrfKEV91gcCM%2BOuNTE0&X-Amz-Signature=45a5ebd51771d5fce840cf5955621794c9d7f6dd1ba52ceb4ea1eff93de45de5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
