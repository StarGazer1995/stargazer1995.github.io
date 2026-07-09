---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDFGKKXM%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T055414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHe%2BLildbhKHiDxZYJXjEn%2BVNqddV8qY7j7ewUcyDXVQIhAPehSYhnd9NW5H3uVc04LbEOyaYVkHiPU93EyhIztYY5KogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyEcW4MRbbOKeEf14Eq3ANkZx3c5prLMLuBcrto2aMWmNIa6So4xGAOxnJJaN2CiakGPKPVMHeGwXVZfAxtwmz22IYPvfLThKFGs14li7jozdVlLmbQ6JbjQEr80H7jDm1N9b%2F%2F3Wlw0Phg0rVDF28USw3jpzS%2FGpngQzOZlsMKTy9QmyCXp2hndSXdHYUBcZh7hUg74xf8BsJM03luMSrTKu173uqH0QkeNflvq5PzWHTd7gNIJBlrJeq%2Fh7IiZBCRdhWV%2BhZkKk6P8owyeJfZU68quDU7329SlEADwgIIn82gEc20UpMu4cp4V0vnp4%2FTPAlA6mH3wyysBxz9QU5Xdab8WywQ7POU8iNxXCWbHY9Ovsb%2B4m9VEeDHump8t4KEFvBs3UViiU1VWDX2aJm5gkGYhAgTrFOgQAxG4rIFm0BBDtbBNFADxJWGzRD8bdT1EhNKoGT2Y1dL%2FRWA%2B41mRpL5kzQCwnPJQKc4gyo6uMSvt5F9aH18c5xcWy2WCke%2FiBuQATF0a%2BQ%2FAbHITPwSZiXTjJCVkePUGnnO5scFzZnpztsM01phdP%2BrD3OE0%2B7Qz%2B%2FGYUuWhbmsIwmDP66nOTSVDwwhqrkI00STWdHnD0O3FYklt7cGRSgLZqTx9yB95Izhf4gD4IX79TCt6rzSBjqkAW32LpyZ8QqHDnsde0kVsrjivJuNtJWGefF4dsYI%2B7PPFAjX619hxNVAX8HPeLy%2FFCWO7LQNLVHVDHarXMz5m%2B4ieFGF2fyrJfAiyeBgmg6eoewmJH8YRWj28H9dlooQbRoQk%2Fdigmd2Hx9uiQcGKAIV2Lm0s7OLmmeSgwR8r%2BCwp44WhjlqazIKsk%2BK9VI49m%2BF70iKaqAXEOCiF8VMgtBKzrOu&X-Amz-Signature=2e2993189488a85a09e89d374cb387fb7cb5f1821641efa8c96b8a75b226d492&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
