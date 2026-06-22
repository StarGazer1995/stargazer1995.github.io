---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663S7E2P3I%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T191852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIGtBFBkNln%2FEDRpGdL1bgCenK5Qm2FqNxP6%2FxyfKW8lpAiBM0NPpF1FOJqzUSN5zHaNAhgRVFT7fMxVmiOUdTLx0%2Fir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMw2U%2FvOrr8jlreNKRKtwDt5oSqGN5FUO84nO712tDHudnQ7sAyHiYf9fdCgjVMQkCGwuGtcBBPXzWp2I91epN3atwj%2BDNpBs2eZS1zqVNI3DEejInFyTsDO%2F%2FOEbdpnluNA7QzO7MefCkHse27nJMRwtR9ngx9i8%2FBSof8MrCfin2Qa6HmSEvAcHp3qnlV1pjFy6t7CaiFTP0zqXhEsyiNThmC6sI1vW4h%2BZyhjbYbZ6e%2BjKIeN1taz1tTz91J%2BZQmrefWuy6JdA%2B9jA3D7zsoorhO0pdiltSrd4eOt%2FmNEBDJ6QWBiVeqJvVKCAP3JHSnzOdECgQenWpgpzgv1lOfWGkoPpEbuZDEp4qhS9xn2v5wzJyCruBxHK0pKaK18pOrmvys4fF1FE%2BvEDI031DOZ6Xh%2Fafhm%2Bf6nU%2FbkdCubdXJO2bmnc27lNnOubcwEguwSLgV%2BByDAAn72kSSILmkSgxFnhc2SimBAFF3eNzhoMRgtY6wMd8k5yAJ6ChblRFW1%2BLKu5YwMMpGCU6b9%2BjUX4TtBi6BOiHIwDTc7ltaOCTAgUpWBOJjhlKZFh%2F8Yfq9o5x%2F%2FYDbzp2mYPmo9d4kZiYLlM6PZAjW9%2Fvfh4sP%2BTC8OvDHvCj3RXodksW1E2a07aEJ3l9Yl1isfwwzZLm0QY6pgFixG2%2Fofh%2ByswN20pRehcLItX40YEcTbQlSFGICVfzaOUiYZRZPndU6GvKZ7hlZvuoVRngotPVVI5kfTlnGzCLcdgWpy1x9aWhBYtj234ECyZ7r59kArgnadv2R5vvXND9SIHjkpeMKD4UnLiug%2F3VvXpJUOVaafBebedT%2BAfNxrC%2BYo75%2FiVk1ndPKI9O9XInK2tPydEs%2F74XExHDlBMnKbDq%2BzR3&X-Amz-Signature=2c3077c536083487dc1bb3662062fe7914b3325d078174d5ae9116a6e236bbc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
