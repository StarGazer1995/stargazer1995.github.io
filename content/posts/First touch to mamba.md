---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HKO47CV%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T165251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHoSo6xPSunLNIvhjldH1buaCbj9VKBJd0h%2FDlfEwIyJAiEA4l%2FMPlLqNno74M7LBS8onWf7dIPIkmmffz0ryNhLHAQq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDKe3%2BE9cR5tLOEy5byrcA0BWDyvaho6y3rLa%2B1SDQQyd2ida7zPNmNbdumwsOdd0TKMkpzpigVRC46Sg6VQ1UudFWbDNViU4hGJQkO140AHPB0l2bP2jq9jsyUTAKmE7WUBK%2FDzG3Sh9BrAQ%2F%2Bmggi%2B1HbF14EgS8x2ej5SSqTqYGbZM0KPkRdyr2Lxh436CuacosBRxnMX81kSAxFe%2BUpuOy9vSfZNKDZceFOsw%2BHBb9PE3p3nntO9MRBIVqpx8mYHnjI5Wb3y43prlEX3SpGpSbWmMzJgOVCnq%2FejDvyAPkmH4FWfRbmR8luqiEFhdUjg5MWwNsc%2FNlYjZiqkzuvurB6GVsrAMvS3J2UWQhCqPwZn1Aj3u%2B9tNZqrHKfDAW9P8JhAg342%2FPqzYYewYXDrOyojruEo964O2TmYEFNm0YFm6lw6LwtSirF40tBYsZPVlwwqsJfQ1NpNjkqCcRwCjNNUNcGxGLyrlA%2BLN03wV0VcMNLRc4Ck60nbqay7LbV7M8%2FinbIcmKsrToEqqMErwQ2J3EeKhVge3rBKXDFULVG3rLhCVWV2qgPFxmpFFaBO1VbAWKJPqAZmXU22EK7W0DKU6IL4JCzmzIjSFVBGUEznmtNWvDNygLdrDz0lILqJoe5zU2oYJs0OeMKLeutUGOqUBV4amYbCiebweQ8tRZ6jvQkhPkwS7bbaTJtmu6EqwpbXe5xUl59%2F2sBqjKlROBj2XW0nKeRHkB3ie%2Br%2F6o2PqNOEURfzwor0i%2BpXbxSgkI3nVrUuGPgLwWJPXX9qKxFdc%2F%2BxUmDVj0O4srUoaW%2B5iUtTM57VFpiNP2eVsaUFgkiPboDT7PVyGBnN%2F3PHgDaqmR4WrzAKYxOgjmQv56KNepi3b075i&X-Amz-Signature=402e3e88908c3a029f055c6d16c1452740ed56544ef5a0f50f4e3af4a9bf6d9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
