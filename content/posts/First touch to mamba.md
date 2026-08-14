---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SOP2R54%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T202105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIFfQ%2FNszP0KKORSUwWy7KnO85Ss7%2FAdR4MSZTnxNS3s3AiBfEgXjGRL8Sj6pHAXgdWZRHN6ltuO%2Fg7ZI%2FkREIWp0Cyr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMnKTb9GnCpyyCHKGRKtwDywt4p1nvgHMptztgmR3coZAiBeVV0%2Bod8ILnLHYiiP3e2Nfwsb772uLTznPmfhjRur7ToS22fmeCAxIQClI0Dh%2BeLKHVnITev7qoHJa9bGXlEuPdwBbfGmdYEZcX6XGoTSYNfZzh%2BISgDaf7h%2FN3qq2EHLgRq8I60edU7NUzBRzVoTD5twEgmLr1GI9HDAkVNlV5KZYzp9VHLFRD6hkscEiDzHN%2FlKi4WzNYoBcpva8ay%2B7Ba%2Fm%2FKBqjB856LF9f78u9hnzNMHsOW1oz2%2FZft3IWt8jdPGv5npTwPpPDlXRIs3MQttxkcjgReckagoC1wDOhkdx0yG5iiHbZgdNHMZO%2BiNwsHQ0eLvgYd4jQ0VdCC7d%2FSlO62BALd9yoSKYgYhtNtc3xm4yI8Ls5XQu%2B8CtAn3sL44JVrm6ITvrbg5anxj1JdT5ULtH2BLO7X5e%2BRM0r3S564HLkqBsH%2FBiQAkqObSdHoooMQ0jV%2FUVZJEpa16VixjDmQ2i5M0w7fLdumuuJ9bNIGFt%2BDYNoOhxlWiW2hUx2c27g0cgID1OUbWyte5M4n7M%2FDCTmdudNJapUAtafzJpYHh92E4ZCJBC5mZAHXu518n8tzCTH06WLq%2Fetal9dnjq%2FkhdceA8wk%2B%2F90wY6pgFzUanZstwosrgphG0nuWLlXFeoVFuwU0Eoh07pEfrmGMZiaEf2UrafMWf33WOPDYEtIabSZCB9N84H0bFERyUAY%2Bkc5nACNmTFr2ZYcGOTPkKRbJ%2FC6lAb8ESEdHQ%2F7VTh79OKqjO0l6KsbtXfsCuJzmJkCthacmGwh%2FJOKFggzKfLQQiroSe9eR9zacLuWUM6AeHp6RS4cmFL1Vnkt7Ohw6q1TiwU&X-Amz-Signature=e19c4c00c5121a6b47e8637260c4e48e05185be42c27fafedc37171903f99218&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
