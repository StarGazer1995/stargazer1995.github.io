---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633G2KDXS%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T130345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQD7SVAU1O%2FqP6HyY2C3PGRYXAcibWdd1F2k%2F3%2F5kXarQAIgSUBN%2BW%2FMoGw6%2Fr8%2FkrImkNrpI698hkXMN7iwREKjFkUq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDHGCrBHQ2iTamZRMLyrcA5PhL31V7N80msCkwAQxVtKn4VVVjvNROkjkyNBtstlyF38yn7cqyWRs2M4NVrh%2Fq%2B4snWyLSVs46FFVZZcRy4cwZdHlu08FXwfFK9ADSvd1d1uGK7KJ2V3OnAkeIkprcvkpvrCIA8pJK01yR2O7y7KqnG%2BCyORGOQb7vNHQ3ZIOZPPNc5PY52foTV5Bkgv1%2FAx6t8mcLinGC0Vsl1dP5eQCgfIjYAZXo51RBsvaWUSNwKVoJfsrB8feAMA3N5yMgW91zj7EYdTkILoO4vv6kDB1FUW0AuoY%2FfBhTKWbesHaA3arnWfmdblzmDGvpkf6cYjfKpBPICN8udIp%2FU8LTiysna44EuYS5Pr9c6iIdcpU0O1r7XJeMhbH3u0%2Bfns4hoqoBqBPHltsNR1I%2BWl%2B%2BYZ9Yvvuh85qkNj9FrNWonLVHjGW16tx3RG16PqnBNCaUJJySBRzSUG%2BFxC3CV5Lbxe2gvqmW1Hj1zMt8AtnPFCkNqBEEVb%2Fn%2Bjw6yLsi4XPO%2FINkWFcZ5vPmAxT86mbWEeCPCyCGNkecOK7S9eJ9InzA6GZ5fPM8N1i%2Fl112cvUvUUI%2FTFesIBRuiEkLnigypvvSuE%2F8peeHL4k%2FqGHZAFMbFbq55krPn7P1sXEMPKbqdIGOqUBVmzF8%2Fcg4CfLjsOqKb657%2BGoy1Y5WEj77c4S05xGRhS0Up1wHRS5mbibpOjhholw4wv3jAub9%2BPXRzYaLFuEwUSOfaUjF8GZNBpSqfLd4Q4SnEw5RPy0KyMyDOk6YdJoHaalkVAuEjl2eJCvUGiJw2UNhQQ%2FuvuggJ6RanlAWyklinqqJjydAGWjRkeRFKBFPJg6g0rPRetvMPzk0SXU4w8hMloa&X-Amz-Signature=e36c50ef934e9f6fa073e2c743bd80bad4d120a9604841562a3e7ffd8902ca4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
