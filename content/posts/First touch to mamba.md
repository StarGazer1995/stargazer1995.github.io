---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OJJQQE%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T180024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDR0qiLdwa0rZIM2IcNkcWfr0n5%2B314OzKKCSAsNVqT0wIhAPLDL6stmH%2FM4E63a9fBgviSxM%2Bmluuk8vqkpH8wDxm7Kv8DCCoQABoMNjM3NDIzMTgzODA1Igzl1ahlZgT4GYvuBeMq3ANTjHhy%2BJ6AcALUKwndYMXBbPsVkvKomzDGAPvYfMMKF%2BR%2BL80vJmIgGjSoVxushaxHwYdRculY0Es%2BAi74HWpWLacuilQsAygyqtMtluGzPKoyVLdq0qZUuhOQjFvEQbDpJ0QX%2FzwG5BV0VdlRv27BugFz2yaSlI1khvgl9B3lJbOSuutPtFhdAjQYWNssGgSNWqp1AS%2B65EKxf4Q%2FQVqO5FCucqMgHgW5lOVMmUjgD3KH9292yfHGHh59DiHGsVON3c9q4Qm4nhQ9Q7ls3jDhNUzLjiQzri01%2BvmAsgeovEtIy0qPq3y%2Bpv2TOo13gi0YUUwcVy936MuHaY4tlBe5Fq9TViDo54rup71dW660Lh18mRh71TJBBaLsZ380OTqq9FFl1sW%2BzLXAtBpTITO4Z1WHh9bZaUHs6RddemIg8fSSXxFVOv46uEe4iO8DHIg%2B9UtHzSomCGC2KEBaLwhEI4cjgSrjqX9ihZGCMct1QSG5kIfBPEC%2BY7Xcb20HQx%2B2bpWTf70GwCmYGZxE0PMSZoxvuKSKkcJzortybyxoDWgic8V%2FdPVMOlSR0b7W9K1SSY5wgA77oiPcgVGKOdAfwiFjaT%2BXvxN84cUQn4tNINHgUqzl0QyxUv%2BfmzDIo%2FzQBjqkAdXia8ljUXCmJpb0WzTQgwHcPpEcuofQdzrhxHBDsEoGc6Jfch%2BVf4ZaX1qsGqIxvm22R0TsTZNabG0ukTEZcePoHXOzvmUfLlgMhQ6XvQZLYSEXj3JC0wuG8q6Ywgj7LZ5I%2BRKNkaHJh12HTNAOFVFB29BSztPHIIecoF2XrfNnBoW61koGcpShSKxSaIllBj8kbPhUVk3YF%2F7C0ky%2B5Cl92OlK&X-Amz-Signature=1536f31eaafa62c657fd290b1ff6dcb342fe8f067137988ea03fe0a541724940&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
