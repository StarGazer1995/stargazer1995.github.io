---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QFS6274%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T085940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICeQ1WF67Tde7iF%2FLzd%2BYwY44to6DqUFAehnHAM5ApTdAiEAmkRDBSfg%2BlLNZVHbOdHIiRy87ht8KJzxc6cbyL83FyYq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDNyt%2BiTX8uDOzWRabCrcAyfWVefznsRtt4X50kLEup9xZF9a6KS5lUzJpAvdyVOVBekhDF8HskAkMNpccYrF4hBb1jfhO3XW%2BfEq0Cy6S9oh8JsxHgnIoKVk8Y2FiwAk20NwGddYBWVJb%2FPWxyziAOG3CCF2vd9Zw3PAoA1mgKQNhvqzyc1fnGW0NS83KYc9%2B8QNUmGTHEfoGGtxEqv8rwc5VRRYTP%2BH1hbTZ3VjJ%2BTsxbNsl4OoTcSN8nEBwQhce8XCaMYdmRnlmWpaIESQC9XyaY6ho8sRgI50Ly%2FojB1%2FjbtxMwdClH2RSF3XlxVijZ3xnSG2Z4X4K290TWBtpc6omeyzVIH4RBRCRx72I0xvwkgnMpfEUmX6VPfb7fCMBiodjAtOPFA9EmHS7H5jWWhn%2Fy6ZXAex%2BRZmDHkIlbZGjnZMFoF8blEjH7aIwa5m7Iw5zwegwWYNAKa2Ab%2FCZb1J4kH8OgYHAcnaaT%2Bt6Iis%2B7rDnjR4lZUWWueBh8acAz%2FYL0PBh3fze%2FJiku3GSm60hLX9I25s3FKQ5h7fSnR9ff%2BUIbTC2OcwNqDx8LTCMCGIk8ZsFQZuf1w8G%2FlfWEHtGjTxnpTvRIsXl%2BFatyZBNVJrbhe0fu2YZKrAAYqF11sVh13y60l3f7AxMMfOrtUGOqUBOSZgtj8LKaoZwJdEr%2BjB4mxb%2FdKeYQOrkbQ9uStdi2QQIPGfftcQi7B%2FS5s3Mag7kVPkgCd%2BR5iXZoovOgluSifqQlowrhfDl9YUW73rMbvpoYQujuil9sJ4Hkt7NsBegjDbuA%2Fvvy1IM9jJKAUfHE%2FfuY5KsSK9baid0uITWuicY3WzrWoUEMM%2Ft0nhHunQL9JqbSMRjCjWRx7gecGtky27Jf4z&X-Amz-Signature=3e95f142b83bf0f89a57d9df52fe0ae831dee43940cac97488b0244bbfbfcb7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
