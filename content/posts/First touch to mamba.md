---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JZMHPDX%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T120011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIA5aE90ZHCDJi9kdrfkUf21ZLoEXJhjbDlGq7Hht%2FIcOAiBeKu7lTQ4qlEAQ9hp%2BlzMCvLC1tne0wiXLKfOOlUlPCyr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMsmyPzZ2W0T0kuQPcKtwDYbUt%2BMzGyBOZJ2c3mKSWTSj6jqcseNjYSIheK271M9nG1OXG1%2B15UOBGynNgDyNajjJssQ91sIOYdva2pLN2RNxsAYv1%2FNDQZje8qQ7%2B9%2BN3LdNo1aOfYQBMeNnoRLo6fKU03JmIqZbKJM6IZLM4Wk7xhRPgFxaC5KK9KxswrmwvH4kW4nT6h42CZ0kCtR1DicDLj2byVX0mhI%2F%2BdDZl2eCorCk2fFpoWyClqTBNAO9RzNYDhij%2BlcY8lwHdxzRoTwgy%2B13BGC0ZEBQLTmiUEXVoMdWeYfo%2FuBgF1wsov5KbrTb1pak8svflT%2FN5qqDK6r7p6QalK4%2ByKUT0jefr9%2FKSEsdJGKbDt4uCL4jAA4eGZu0UnyOmIVBx39xcoF1H74TSZTGdibi%2FCLjP4uf7RtolhRQ5fcn902TxEKs61ZvudfGnViOmKhnAIw5GaPhVLMiLwuqn6mVupsNjOeNOvEtVRvXXNK0bRKTwfbnbgwwsoXxMcvL3YJyueIbYkdWJpILPZd3trc4RkiYVkR%2BH1boRxSneXDgSP%2Bm5zuQPI5QvG0pMpRtWVSiRmyu9j1yQu5xXzpdl82dVRs6N03AlnPocxJ2S7vST%2Bd9RUJcdjGJWTGgiAzbO6%2FCvWIswmKie0gY6pgH0xegOgmCykAYwOAyRhSyFbPUkQEOrnKENWxCxeWGz1IgFeypGJeoe4JqQ9BtYMbFM5SRsB5ibrBKi%2FS5XHAUbYodSTdDN9PVDMTM4aA1iYLPzYVMxE4dJXTEJgBpHvWLiBeW2kUNc6ppHLG1CZqdFncxslKE%2BMgGTir9Y69NIleUEZeauFEIy8W71FkwqfsbGNeC0kdhulb1cnE9RRKynB2uWYxd8&X-Amz-Signature=aaf3bcb0e050243b9981d1d9a51abedf6de0e3ed9a96e68b262e8bb7bdaff86b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
