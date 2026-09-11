---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665RXNGMV%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T234012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIfXuFeEHrV8i%2FoPChC7sBHoymFlnzrUiUOP7iCuuCeAiAc0ma%2BRrhmzF79p%2F%2FeZTQ%2B8vadun6Qqp9%2B%2FBcjjx6DuCqIBAip%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcCRTX4cui%2BD7wYtmKtwDe3sRqSKgDLXmc6Ax%2B0%2FXYJfGP562fWtbBtI49pWC8xPeWL4KZJcD5yR15KVrYcIct%2Bh%2BWxAn8LD2%2BE2ZtvjeZyjtziNqRDfCsjgGsf5mdpbvwUvZEV7ZIFbY6xNBavb0usHvk9gPlRGYrgBlofo2Z2uYdJRsKq%2BmlFJKDSCzvwh7qQMeHcUVlqln7gExVDbn6P21OI%2F58MyXaqaVt4TohfQFCqOOS6edPjKzvHA6YQ2heOsxCzZ1kpoPYz6iW2DwFr%2BUivrHJGObffCD0zAC7uzVpNvcxZ%2BulWeA3MKaR%2FSjV9BcSC%2BDR%2By2%2B%2FHbjuuvQLEk2jJ5P2K%2BcmuUXLNUXDK3YcM6Jjmo8vGfbGK6pGML8RqzYCOdo1sq4UO8osHFxmYeawM3bQJsCJTdThlsryjZv74zpLvWvhu7ud%2BgRzi4E4gUpy1MsSwkHpN53cEdN1%2BhIjci46nyQZOa4TuerL40OM%2BCH8ReFIc6ojCyLtJWQji0kum%2BCpWjvMmxW8ejkkK6kjFEkUmCSqFD3WKfMB8yDF1jXMuSiI%2Fe0ZgdkMdcK7%2BKFFUug%2B0KD%2BVL%2BuCjWd5Ydte4mk1FR5VjIzOsiwbVKIFLKuttsq%2FOw1O11R5n2m4IW9QbUwdusz0wl52S1QY6pgFOgytQ4unmNoe0xq0K3xTRSaVQDl6zOD59TB2Wd7DYjez2%2BoxY03hVRxfRHEVk%2BVE5n08XkypcyV9Q7IAOTSgnZiJ%2BKmObXMCT6bFoCVZqQQB3Ecod9UUu29CN8deE%2F32WeF%2BsQ8KEtvgEbJqJe5r7cgsSxwiZt4qzSQ5dEPrT0ePWzbaCSBp659rEdQrJpYv3yVMYkPhawa3RJ%2Fo1Wn05SxscsL1T&X-Amz-Signature=a06f0e296ff45ba0ec36f05ba78e7361c7affecb2e41638aca5702522c3d996e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
