---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CT5KQZO%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T075922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWmEbbRu7Ys0InV4QroOVY%2FW0Z9JpOFzxuXVGIC%2BIlwAiB8fSrZSiErfW1mQmE2ZqTYM1ljSX2XPJjfTDAUQYT9aCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMLei%2BSgoWvZH%2FM2Y6KtwDobCp5aRbt13dlew8E2dFggoKSCjIQzB1SsLniMwBu17aKjLqy4b3YozUtgGTG6g540pAQHZrxFzcYQxkcTXNjVE%2BneF%2FXITmiIhZDOKDK0DFPXiczhbIND3UbUZDddn1CmZJEV%2F3AYTcjzizLfiVtOcxPb44vqWkUeKyCVd1SGyY7dqYnvRYZO5t0QTboVnBSyZEOGMXINuQ0TwjPKPtzNwhzeWnJ%2BnBeKkt0OyuaZXXaW6rvp1AdkLzKa55J3sVoh2Jr95T7pBv5M5jbrvQFHlD1mr3iC82VNNfUCWIDCW1zzTsqjiqhiE%2FvzFMdYQ2a1deDUqaF2tNEX7t294RYI0utZ1lDLrubnazJ6rFV40lLa4pqIzhQGcIPficBPlInh1qL0iWTbZSeWVSjX7HzX30kAiJZxnfBe7kmGPGpDHTcH%2FGGmLFFCN142rwJJG54gd8Jq47l4NtMFf0BYKv%2FNHLcdkdAVbuMejQdM%2B0V47Fx9LtZVFVFYgdCeHaTICObElyHFuye8Gbu%2FlbnHf8vnq%2FaVMaz39JV22NWn4mQMjPEku%2FdbUQefwq0oo5%2FXhiRdC3%2BYFUzoffMLZfXV%2BE%2FT05mDrNkZb8oWmhMLyAJO276yQNd5MneuovLU4wuOGJ0QY6pgGp0ybfLzUMuKws5doe6ph%2Fze13DtO89hWd2wuUTlzA7m8iTYukKJQcmLLbzMZ4IA%2BCitie2cJqCgG1opD%2FUstwgmO4TduEGh4PLRKt%2FvPT4yhCxyBWIdekVfgziXqmCuHhmS3OyAtjDygCwXZpcU9sOcM0lDIDyeTHNnydwsGaHAmuN0DJYrIRzDEpg5KzRo%2FfzLP5WhHDPVPV%2Fw8ZZusYblvbfJ6%2F&X-Amz-Signature=e7ee3dff87229b0836a2d8eeb2ff37e211df449cf5ecc22ee2af7ec727c41c10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
