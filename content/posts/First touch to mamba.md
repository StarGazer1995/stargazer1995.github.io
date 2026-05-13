---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZOZDZUZ%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T115521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICz31%2B7z5ccNt1lkx7%2FPtEHYlIRoOZHwTBEY7PDniBHIAiB4K9TMpivjOpIBxeBgJqcPkBXR1T3BPmCjQC0Otn1esir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMmNnvXLAsunMaN%2FZEKtwDKiprqEF5oJbGDLpI46yaa9AxLyFHjfoXgHpryu35BvjfmHxcRZEbxurED74U4%2BWTixnyhtNf3X91QWOKh%2FsLI1ijyJpVecWYSJ0BoHK%2F33HtpXwo53zc%2B1pQKfU6yRD5F5qmouiQf49me6sxni34OPni3cY6kPRDYDzMj1RwoxGD7DC89nAF%2BKT006wTsqmBlznEvunOxq7PI5rOrcOhxy517F9Ll8hLgqdSRYGcRMjXyeZXr1kiEEEqFTmZCOT9DPVGgWVITl%2F0I7Pas2EoPR2clhME6C%2FUhH7QbsxGOi0JOENQWiS%2F2797CsKl1zE1ZNn%2BOP6x1nucAUkhoPhybEWBEw2z1Lsy1PcTaUzsUhffLiA2q7MqHQ6aKpgHwN%2F7Avn1ln5C2QekSu6%2FT8FfO73SG7hZLWnOFXDZtSnRP0nsfi0A2duEoMUBOB3SXlZlG%2B%2FpG6ga4vAIRm4JijZ%2FDGozw9KmP%2FNH%2B2xMTxatmwnXCpyEmNwG2sDKg1ixg9YcaRT7M6xPI5JC3SfiTWAbb7q8dwlIIfslMsDLt%2BN%2B9t8hczzQEPBis9XY52zhEKHwt1O2T3T62MjO2NoT%2F562BdrN5RA3H9brg5MkNA6hpwelHurcej06hhsXBQgwy7mR0AY6pgHMfjaduCS0noPPHTxJ7hnQQHJDVpb92Hr0X%2BasA2RBes%2FGfAjFHBKPvEj6pgX71UxWuOSAPMqpvdfMWz5BXDBM6%2FAQttPp6Hw5sBYilK1JHhMoPMBsIwVfy9F8VGdiZzwxieqDYDgYcazLR1cZtnyHubcoex1XTHQy17ybuedzxyBPbJO%2BGRcJLjk43IKhBiw878lnxRDkThWUCYCnJ0CsTBmOuKCa&X-Amz-Signature=f319773dcdfbbbf2be2810bfc1fa7fa1f697c4588ff4f653c2f6a1db86e8e176&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
