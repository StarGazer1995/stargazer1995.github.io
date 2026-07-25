---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GT7A7QP%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T184741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJGMEQCIDR5MmarP94mNahQI7bZEJCbo%2BjiupCOt%2FEh0llwVsRtAiBrNloSJoQKgwTKEDDW6gEzLGSpM5SL6ihSwbiAHwF2oCr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIM2C8c8Tk0xBz3NlGfKtwDjDbGZsFN5DsBKJLnoOFQXmh4sMYCZtiEzQVQmGqrIeSwOmCepvIcSpjqNRUPxkU33YY5%2BFCpoK7xkRjqlq8URNUrseuu4YyqEB1HQTj8b4v2rtMfsMLP6x0f4vBFT9Dy50w7VJRr00x%2BTXMPM2mx%2FqIeCgfNBNEMeMO22WR6i%2BBAQcQDSAaDxyuFTMBFtVKRNM7G5VkiKdkYS1GzCJs%2Br7feUCzNUDlwZPj3QjoOQoRfYNIyxZes31znbrL0IzWABp84%2Fdjzz1SmQLH%2F5NAQLK9zwNJ2T%2B47soj8D0iagrUdj4rKgQTHGHQ585TZ9sjl5ZQ1RPJ1Gt7dIEW2maZpqZ64%2BaBaw04%2BnWbVQaVJ2ltTMiS5fl3oE2X0yXmtCEfI22ZYli6Yh4vx%2Fjhgv3xVfwFxp7KaRCocrnHiR7X2ThKGXHSg3HsmEfIcW1zef7OkqjE4ZletXDxCUsszlcpEpNrrAr80sL%2FCNeOPBv%2BML76wJRLVrS%2F3sCOJMBotYWQIeLiJSbK3bSz2j1ehpknJLzj0TskUuxbfJlf3OJy0S%2B5dnfBpmDUwgwkHoonJaWkWQkET5O%2FAgjR5aCl%2F9Mx0B80qPK2O88uOxuPbmnmJiOMtmyVq84aPu7rXUkMw6fCT0wY6pgFzf9CY6G%2FW1%2FVTrsDR5GarwNteaKTIZKCjUoFInzVthu380KIhFEAHqNpz5WeMoV%2FXdKWRxW5aYfGlXBJu%2Fl5m22RTKcFSyZbeG%2BBXpOAydEO%2BhB3ZS5y%2FvVU6BXdYp2EFgaj2Arq32g02aj823wOEU3ienNIgKf35%2FNuj7%2B2fJJiDIoWPSw6DB2MIPFSyIDG%2BU8ofOel2NPNls%2FX2utFDyzuWbFPi&X-Amz-Signature=c8d427bfa4e63acdd5cd7eb377a74ab72ef550baa4dba50a3d2c1cd3fad80698&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
