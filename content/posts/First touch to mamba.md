---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GBLHOTD%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T142307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0RW56%2BC2OkWK7aR%2BMlJXL9uxq%2BEWKwTbIVe%2Fd%2FXH0AAIgcBdSKlCk9TsDc9PlX8Cidzw2dzXo4C0HZjvrJdyPw5gq%2FwMIXhAAGgw2Mzc0MjMxODM4MDUiDGKU%2FkwPQMsooU9mlCrcA97svsO9uA2Vz7D79ydbiNN7gz76tSt5KTvzserjOtdloUWrSSUhuQehMUKIdQuh9VtuNof883WmOLdtY5grmZTH7TQiyBkQosO5pIlFImpYZhj%2BiZsLNS3V5oeBh3Gdfp9ucPkEPUDAbweHzOcqqqbqGgW1XF504eKmZItRRHveV1Wst9gPNKNtLxajCZCKrrZJ3qWhxAmrNFGWj8uJYsGm2ms5Whj16KFwQ%2FaNUYsbuz7wkj06VefxZmITM%2FqHQuH1mstYhGzAEm%2F0EXX2X2o2eAO0H0c9iv4UQ%2FEWXpKbFT3GuVinJ2LB8uHEeTjf%2FPctWB%2BiyLjJqh8IMMjAsuBgHNpqKyW%2FjxOlWhsN3NxerOO8TZgsShz6CXB0hMAI%2FuwADW5IkgWREcmzT9M7sM1coePzVATonCkEm64UrLVn%2Bq15DcaJlVRBb%2Bawv5lMyFbpILsFj6qz5bVCvrfN8Z25RdE%2FWsA2D2Iyewg7HvDbQV2UsVL72NrSsp4I4qSTLARViY%2B1AMrFtHGM2oQP20Ujwp3RNIUIoUA1tGg5FGF30wRwR3rdJikygFT1HlpuFyXiCNSgCYffvKYs5PRIV7IbS3%2FUKyzDYh0E8V%2BxmkjGsOjDE8ZL3otmbUwLMM%2B5kdQGOqUBym8FxyKJ2DNM6Bxz0UCNKrSPE8%2FH7giBlTb%2FsHVz1h5V%2FZvPb2MEh3t1jx48HDFGl3ZnaegzhFngMwsymIb9UK95W0udNdZwiULypeVGogsEHl1cEpxGIyYZVbbyT8Gnxpd54CWmEaVhVvGuXNRUpRU5UUIkrixP9SEN9YJptkCFfCnmnNHg6rfd2srwKe3e4RV2dglCPjOzSZLIBoJqTwjVeyj%2B&X-Amz-Signature=059c9987721d73b2056df90c619ae21616f5c91423e8c4e7d23bc6fc1ff07095&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
