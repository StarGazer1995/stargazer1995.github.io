---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S66GLKBB%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T202853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIE%2BOhtx4xwNM3xnnXLlFiyd6MbVgCvXHUHirm6EQyzoyAiEAsZUpLqr9xXySEZ8SM0TlQNzMnnX4wUgGe2CqBc56alEqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCoUxSqzoaZWhEV1ryrcA5Zv4zjWRc4KiX3%2BPj6FUzQmOTYzkAXlYYRhsx8%2B%2BnS%2FtLElS%2FvbXXvWpGafaHVFghyhi%2BAiGSzlmf2yn97lX9gR%2BLm86cHlcuiKF1c%2BRC7%2BmcBMxNnOYwv0hUu6gYhJCx2wRIciuum6NqAxti6nyFoM904jhG68JA5VDquckoaGM0ukbfcU1JV8tJcocecE%2FFdoixoGzDJEzhxtmHsPTHWp7MOCjnwVKHXPXok%2BBts0szNCCGx3b23ViboI2T8LZL0zVnTMBMOUiIPisXUsAC4r%2BdVKtgufTZeew3rAmye4YGaZU%2BflwGkID6PWaTEwDJP37NzOJ8HBxV0EXb%2B2U8UAzk2dh%2F6cM2KFH35D%2FOQ82YIuTbyH9BfW%2FapHOXRGiagVK25ROBu%2FBxFPqRFI%2F3qcdwWI9UZlCKsnv%2Bb%2BVDcIhxbXtOaRxuAu6bLJ1dKOaWPlYnLUq41DbQ1gAN%2FuEANmbC6U95iROWDz4hj55DM92agR2szb%2BMfZtaEaHBkjwzssWpTKz8lSjzOvQm0a1n49D7RAIq%2FffdCmW8VjZTzPEJiOAi1swgjWfVbaUCe%2BCxDYnjyzHYPmkcOrktTBH4gG90Wx7M8ROgQdAVWDwNVyXHvn9%2BLGRSvmaRgkMIaf%2BNMGOqUBq38cy5XIzjOl6PNGj4QOKDPE1NGF5Tm88xwLr4xKIqGUf37v0Rhb%2F5K0fMB2KUj%2FxQRHy8YD3JhvsfuiP9e6ARr7V3YsxcDvEVrexoEI23GHkgpxo2dQWlpwSn%2BxYKuN%2FT4b%2BU66mTCw%2BvrdhrKQ5xMu4qKu1DEhivAU7cWusXheTL5at9EIB0gMXp%2F4CgNumJKox7rNxcYuBb7EE7Vv4meHVcGD&X-Amz-Signature=01374b770608fec814b3ba1decfd4cedd31c7cbfeaecf99fbf3170fde38d0705&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
