---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD4O3IZV%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T140010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8vwlCd7sdkzTNuikBlSldHcG6GyVug2eLMVVL7PVofAiEAo745uAFK%2BUJzT9h6zg%2FLkvrGypFPNNXD5VxMPEhr4Twq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDE%2FnLjh%2BYBMPX7VWHircA3iJNYIHQwQZywtdrAQikObfM%2FpVENKM8Ux7ubK7udFZPmD80jxBolFirbIh2B5mfrr3%2BVM9acTP%2BjXMZmWLdJ3zAlOdovmhOtW30dty%2FtCuJ1WqmOCXU0l%2FKCiqZJC1%2F9onxEDD5WSE83Z8NVxEbDSTwo9tQrm4yTko4BRopch1A5rQXFG9liuCg%2BlauZlqAx7det0l8v%2F%2FYMZcSM5dZ4bZ4%2B281KVa6ixUK1urO8RrgGB1AqlBIJgdxdpCjHFawqDlWbIcjD5%2FqEklLryn4AUghsp4MQc%2FN8uwnzgRf%2BUAeYtp8jH74yF85%2F1Z%2FD14ktCaTZsjwbtZUJW7akeSL1nlxhFzj2S%2FNK1EDSsjWSc1tIXBXeZhe6OwovMqtwSIPVm1t5cbLaxX5wF%2FQg2EhxPIEE9UudgKKDRXsDHlOv5Z0wmjX9mRjqiuIVMTKLe3RBfZD62WSrSc37bRcDAvyZaELsex%2FlAYaDEKdKr0EfkXSYKfEAhPAHXk2TWUGqOhBpUZJRUVMrsMKVIUf6bQCDD19rRhVHRDsWfEYjhdXmGVBsiV5VkhUFCjqqs%2Bi5nQ2sWWKmBRsZYUXUVDUdIt5tfRinPJmQCX%2BujFQzkVPQKACZz8Zwp7bEyPe8gGMKve9NEGOqUBA2q9EnafjXcfOoRj84dJSW1hq87B%2FXpQ3W1xapYQkhutAvOYVdwdoaCGngMWETAk1Rwga5eak2aCnPco19E7KoKSKfK9p40xCit6ZOre4BeiVKi1sYnbEymfoplPHStySfATsxoXgihZXRlvKrYNBTF4bjyXT2D4OWuHXEm3dbLEHKNP1sKOFfgvnVRdta%2Br%2FTpsffQYh4EVY7PX0JIp58x%2F3Ot6&X-Amz-Signature=6dc0c60f7eedc6104212b3444dbdc4ded662eaea36b1b363fcc8cf70794fcdc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
