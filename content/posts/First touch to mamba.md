---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROKXBVUT%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T162052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD3G%2FDhY0wo14oLNgHwAfvEtkhYgi%2BGoiegjf1ZURkMygIhALRFUejIH9skUKkK8odyywjLcojSzahE%2BQQ%2FeEE%2F9oO5Kv8DCAEQABoMNjM3NDIzMTgzODA1IgwELjP7%2Fo95rU3GnJ4q3AODrLKMTCmxTIwt8nxmAXnTBOAtQNpOUnRhgKHR0tnpleQCCr7wMxZ9a%2FUeGXCdDlckgwPU1IPpcd%2BKSsRQrNlsKw%2BcOcHZ2ymFzkar3sPsm0U7Gu8Eo%2BxvJOOXJRJMz22%2BSVCslWxDizwIYH%2BFIgeNnHh9oDmpZFd9X5wonoFpvY2zANrOoHgTcPFeYfI0wuETqPBq7fWGUHuQWhSiPRyTyTrD1XcDVafU959pU6vm3MNHYzGM4JCNbd%2FOD0JJsna8inPU9lGRYfGmS%2FP%2BOsMCwWW7WjqwkuvcB1C2kgOQvsxX9fAdLuIgot4FViPqjiCkpnpxeuJILW43PgeSdgpASN5Q%2BUq8Uq1gEO3yXHDG3Jp40%2B34S2ZHr8CCKidD9t2AzC63yZWogyg0degLIMb3zILR6EIy4TAbhRtT%2FvZ529YOx%2FIrR9YrGjihs7mVCIJR7%2F3Lu54T0zxYaO4vCnt9TB7Tv6THIs1ygWhpDNMgwkb9UksfCNPOF6WNs15G4zxe13dCXDSTfpZbN3rvOxxLO9wR%2FaFS7qs7VQxfXCjdfgmsL9SD6A7YbonYEFxPFNkbCQhBXm%2B6CnqmkflmWMJr3lQeywegk8ieoumdQq5sRtljYNF%2Fb%2B8rOKaUMzCrmdTSBjqkAYeILxSci9Mo9qL7et8SUP%2FSTd0Z%2F4q0bqAiIhmdm4rfeinp5ZjJmdlEe0FHr4%2BdHpvNZ%2B8ELXV1RAo7FmJJHnvuUHXNRHXKA6BNM6EW7J12oB89H6kudBZNloj2D9ARQFKyXqPCf3PjupXZbI%2FjHWWyLvAgOmg4KHHQHFPU4aSz5le2CZhur08U3R443AeK4YhoK2e4vDsx58%2B10PJ7%2BEay7QzS&X-Amz-Signature=bcef3f2cbb5939aa781f2f8baa419300e64b796714167c44fa0446768035cab9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
