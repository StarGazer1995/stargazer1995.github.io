---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ECFQPVM%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T124551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTHR1MRPsozZFbaeGdJGDOu5Es7lp%2F%2B%2ByXfsKR96njmgIgH6hn6FKV3p8XsYcseQ0XbQwa0Dy9OcnlvSO1DRcGJ7sq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDP0bjzerfOCaItjsCyrcA9D8dg9p5cVeQxXd3H3vBzZRuR4ZZ2Lt%2BTwQOYup0uAdL6KFf0AxalQGh%2BjYcBdDx36lqY1OhkhQmVdJ%2BmYZhRfkLcv4j41pTCk6ACj5c%2Fo65aWiLFMLAkZnCtPGWK9WOwvxoRQFafcsbtMpOve9MaOo6CkEeuKc0bbIJ9pqOBGJunyCxoGFAetPMjFHuqcQv4DVTOc1blenTopqApmBNsnuPTubzvlze7ZMLGoMICByaS41jkruO4x5jg09oXA0aaXqT18Pf4rscVKnBeT1pmED8eVx1raena9zhkTFV2u0cekIHMZKtAug1GNUVOj3LXuNwGMbIk5jQgQm5BvUvGroj8TDc15I1wlI%2FqyJF94TTQoJ0q%2FRcL7Sxa4wvRgQCT58Ed7R0EosnsWyeAZc7wiT6JSgeNx5QkVU1hyXzAJccuM0NuqOc%2Fh85zDJlK4oLGj1wMSygFxxWmCi32stxjg3C3WRyA3f1Bp5J8Ia8UHXjw6fffdz3D%2FUDtMSFitKTYQYZne0VzGMAhPk%2BO0%2BnmqGH5%2BsmF2G%2FrzjqE%2FrJcQ152lRoX0reHvL9SkefdLh0LVNiQeGZx%2FDPTx9RiYZ3vLVqjHBdmlsQipMZSLh%2Fl19WmYjcL5ok5Ry9eNeMKai7dIGOqUBDu%2BU7aUXemOxYBSjrc6pBLlewz0M%2Fcj9rf0FqdOxmZOqlzsX0LdICGCYtKw%2FZEcftLdwKdmVdb6h%2FZ4IxZmfp7wysjYj1w%2B2Wqbnr%2B3MUIsAWtAfTMrcTxTGmNjOCiQa9xNGqRcqioKpE3f6B6Jpt7%2FopCPQ04%2FZLKxDWfwMSluj5O5qc5X%2FZmcv1ohBiPNrcEcWA6wRHh5dvyi6Jer%2BJkpB%2BN6j&X-Amz-Signature=a2ccea1258a193210b1f1fc57d485538b153a1f571f7cfc4f81a4bbb1b72d976&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
