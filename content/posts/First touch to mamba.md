---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPHXVLN%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T020026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV8NNkMYZwmhS%2B%2BK4syui8SV1gL57beo2V0oSdddIkzQIgUoC0R6Phi%2F3intD1Xf98pyYToW3zi4rFb48o0NKsiwgqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwlxh1yW4UEiYup%2FyrcAyFdobf%2F9XybytzT29naLKuUWl21baWuCcOfIYOmVVPIEw%2FAI6MRDs2vkklYVD%2Baka%2BVaJehPhf22hWeTP21gkkRoypmMhMkZl3ADrImguDCh5UAdgQO2cs78Lqaikvysa7y%2FmwQHDIB%2Fp%2Bc40K9fi3uGgjqFOmsrmjVyLaJqDirXXt%2BaJXyzhYFs%2FzPB8AravCNz5tBmIJqTg%2BY23dQgBMDtYQc6lb1rcesaIjx%2BJx6z2hw%2BCSmU7si6KvDgs9ZuOfbgbD8PHc3admntaXGdK9BgaWXIDwoMh3P5Oy8wBHZP85gyUUHjSB1pJdY2A0QPeCl4sQkfti%2FFB62JbhEOjbIyMAcctr8zGfcH86pVH8y5skzYrR%2BXJQbmstyB8cG9QkLO%2BamoZkIPJ0VbSuSMfCY%2FJWiid29FrcfazwczbqDxOx8zlUfzy3fkyH1Xv6kp8WDIlG%2BIF5%2FrQRhkN0KYLeP%2FIcC8GLt0fHB%2FkugKSNsQZBJaiwgcN6VhqbWKCkSAS8WCi91r3aBZfvhxbcnYiCrDE%2BLfcW%2FQEzVAxnCxCxgjqG22P1gyPtkYBe06ZGgFHjCwtqsD%2FOV00wWgEiuWstxLXorJ1ySX3OC0AOEXe6NCrvUYXCMfaEFCLnVMNbg49AGOqUBSubs5LCbbnfamp1oXnH7ivsSI%2BCzY3qG%2BMr7nz3i8OEG9mZ%2BTOUVSwjn0LE4URo1MLU3dBmFoIb5om9R%2Bh7POgT%2B7Q2HpFuCewzdZlfmrj3mxec2VfJfKC1YOLCq4%2BqTJUnTaVTSXiBrm1SdYC3kgRFeXZoT1agT6LEmfhXBDHVYUFcgc3qtvduDF6qdUFOkABXXUGdPVmCJM2fTjJJm2ZnZ8eot&X-Amz-Signature=1d259c1a36b68ddae092d9a6a86bb136168bafb37b14fa540eb504ea16a3ccba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
