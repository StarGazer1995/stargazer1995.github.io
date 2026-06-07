---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REMNVEMX%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T170359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu7qPsUX0X17PtwCnSYN7HFOEKHL1bO3TP9ebXjA7CpAIhAIryY4Hct2AR2RvRXMEC125oOQWYGOcYLKebzeLP00wqKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTHjvtIVpCpkGRum8q3AMg86NS410T%2BHcRyPgHRhPVj4ss9IZGfMSWb%2FNBJgilQhlrI7hLF2qZidrA0%2B%2FQ%2F%2FaSe87Bu37PrVrbI7weMLmsx6FX4tEjDNXm2m51n7g8ruU5BVaneOCOgukagaqUm7RnAm6mAT5ytAKrCtehcCePcG4rLOlDaR%2FBZ5OujQ4W4WeFn%2BIt54vvNhzXCUcQw38siGAbZEoBTK5%2BxACq%2FPY1Z3uCVj3SU%2BmkqsZ3r4hShqiyLNDTMXHq3VYTgvJRT5IFnxw47LE3Vz81aLtLBv9muZwr%2Bdk9IAQENOG4asTRZmbTKqjk9H16E%2BQby4hHX3b2vjsT8iqnua%2F567fN%2F7OfJZWoWqKOEvaux5riO3snxPxXMGeI2ehuFJWYfWREB%2B0wXjKBIts7qPIe5pg1uf9v5LJvsqOyHdee7d9E7K%2BZ80OW4qJcMXf7YwJaKl8vGy6Uwl10OhPruhjmEl7AMDlS1EU%2FzJXBweuGdA%2F%2FKsESMGSPl8geZ0OmKJz63tRXNSRFG9w4Xbi%2F1iPTZpuM511UsRG1JMlKrJsE%2BeJn%2B6FDT9qKUCmtJk5CjLbc8VvK4Riqr00Nq4MPFsYDuWvxAG5PirZnJsr3PUTmb6IdPI%2F2aNjIwbcCXXM%2BUg7bKTC%2FrpXRBjqkAQ%2B56%2FxGm5plPyc%2B79o6BVobh%2BF7Ax1ZQw4g7UlrSYdZM2kEbsSPThvGkXAJ4AHPG0ox%2F2y92VPIyvSNA1jw2ZYbIijS1ZjNOnY5PIOVaFEtspHlV1eEXvqH8YAfPl0ZPcYbpAbX5naB3sztfej6bq1PTl3oZEKawSaSE6kfE9fWdgmHoiOpbcFVlvwtgWq9J147SsCjoCQeF%2BFvqVgVWALz59%2FC&X-Amz-Signature=c5989517481197905fd65055ac189d3cc50e10978f88d638774e02df0a4db01d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
