---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXLTP4XD%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T132514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQCL74bmKci29pf7A%2B2%2FnVZ%2FfoD9rVwjzCP0of8M3MNJYgIgWgtioe99%2Bxom%2FH0%2FQ%2FhbsfDonPMFPvZHV1uw50szNm0q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDIVrGHs9CHyemBMvNircA5q%2FvovtZ%2FEekBghe16B1qKIxjVGd1ws8Li0YNGmSeuwKtJEUXS1N2BiDadd04w8lcJ9Q%2FPvLdrxN7GrLFyp6DtJWOkbpg9zJojZLGN6jrLLU6YPzcOgB5g%2FCGquH5OMjrwSLmioBrJjcq5iGskbORs4RnJ2ePUyDl7wZOJcVwVqZpzLBsuxxY%2BhAj1Wfhmm6oxZiuvFIyocKW%2FKgZZifLOY%2Bm3SU7tLHqp6I2vpfmoKLNs5ljmo1edqgZH9g42%2FZBTmV5Gj9EcduG%2BDVRUU5H%2BApskd0nZPHlZC2cyjsSJdsYlO8Vbln5uFaIEhymnmYfrlGOMm6Lu2ah3xDW6Cc1igmgY29p%2FfaG8gcXQxswTbtv7Q8sZFdrTLDjwyxFKJrVwDKMfywDYvrfWZmOYyNX5XIhghl4Gn0Npb5y5gBMDhlTDohpMTYGgeYuARHMTtS7sb%2Bt8SSQPMTnF1R3p0Kx1E577JMD50VUzs5idG90mtP%2BzOT4tFHaFGx%2BhWXMJGLmHULHpZY7MYRkqPDxTqFgunWIy4%2BLVul42LJarIdX3iR6bfYbDkMCLMP525xEJU22CWWb9l7IEq0KiuNRcsXm%2BCCOLAALYAVv7CxoSsKyuopNv97%2FJj7TF2jNtfMIXFudEGOqUBA0oAr%2FwPc2kA6hzK7ImvyAnByKsyaTjPViXP5WDt1JLwz9E%2FPi%2BrXUPl2P4hhAmblT%2FQgUMs9df0e7pt%2F8VnJBtH2jpgvJDot1YdZbtnN%2BsMWT2BOao%2B5IVLqSv7NWYDxpSKuvQVbbrUIA%2F92LceeD0mRIw6f0Jl5%2FwqZddjLJ390ABayC%2Fu0n5VStHxgT4w6SeoaOSCV%2BRPjZQuLi2chZ%2BY3lQw&X-Amz-Signature=8146bc5603aee107025817c057d2e039e311ac7a4ab87f6460a676eb0952beaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
