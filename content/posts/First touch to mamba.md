---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAJEV3QK%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T043840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAKnEa370XCF5PdJ%2FwdsH4RSCKOgmOxiteOnTKX60EhwAiARk5d77EO6fxoiUr8MSq2C5Q5xYriwYDNdnkaBemc2ryr%2FAwgNEAAaDDYzNzQyMzE4MzgwNSIM4P6bU2dN5J%2BGVBZzKtwDrrZDUakIs%2BGJ74eECVSA9jJGbOSsbmWY5os5EQL7Ix4126KWA9%2Fv5cWyqDfUsuF37btW2dpGALeW7ADuQm5DZmlEHrDzWkqUNIcsD7F51TF2spc8O5QZqQlKuSnR8cbaTwSS9gg0Z%2Bpnz2qr7vy5F2km8tSGTr2bc1l4tzHZiPBxZn%2B%2Fiw91X5btzedi%2B4%2BgtA6kw8DL3CNO3R7ceuq1S8CgGhIlArrO17RR7n%2F2t1CTH5knnnpExsSM2rDdNm58kyQc7M5lfmEpyp9iyliNFBPKm4RGFMOeu3R0ILVNtBgMAHIvMQKDT56G6BVJ4pAQdSXVQ6s5UcPKDtKcH3xNnyxOEHa1eyX%2BR3yBadedglvSfKXp43XLHqBSFyuIMz2AfXTAHwHZToULXWSWbyA4tNxnce7JTgiF60PNfSyFbAMZqBUfFHXLrt4b6OM4vlkV%2FWZZNfgQ8Agmg3Rvp8i5POFX2bCwEtTKyPzdjKlvnnh8fnoZFM%2BOrMxy1xelqnCqy3nELPA5I3HNZ2HOb2r%2F1g6NXPv%2FUXtpMz%2BNWxl%2BCiy3T5iR2yNQitwgZZw55Xfef3I%2BeN2bi8gNY0jK1fpmaVLOBiMEAoCQusZfYOBbDrwhpb%2FV%2B5HtAWSYigwwuOHW0gY6pgFFiOJeJIAw9Z6m448oocluhjxK34lnc5e3llmCY97NibBBRe7F1EWSG4wObHmFg5l3wUXdzHsweexIyxJJwPLkU61a6VcjiNUqcNdqmLid4ti1lGnAXryd3kZFXIgnTX8TdqDDZdyUFShp8PbEePTXOmPJaU1UtqzkkK%2BdY2Ovbk9HhMLoVgeeCUjJFtI2kGfarozodj%2FX5UMsIGVY%2BZAzOW5xu1Vk&X-Amz-Signature=0d314deddcf79cb01554cbb6d269d05e4e989da892e0cc7ea63da82b65ee4293&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
