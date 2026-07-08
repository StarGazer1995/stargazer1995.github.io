---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3OLKOWU%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T155733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBy8syMiVPLPues6LgJWiu%2BHhqmPT5R04z2Wq%2BKT4%2FUAiABG%2FTHBQp3DPjzXCd%2Bhrv8D6b9W6n8mNZWUnyLELkr2yqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZhvo%2F0MvfKsb7iJzKtwDW%2BMxfu8lbhKK1oWJ4aJchvW2jU7CNji%2BicVrOpI0KLHMDUVj9iZRSkxINGvqxwZ0%2BXbinGoilkbLNp67y5y%2BDpnF7R64DRvGZO8%2F2x%2FAkPhsNLjtv35udpSrufcf8VsHF%2F1XUwJh88fJze9QZUEMNLGQ%2FNJ6%2FG6RWNCxOmfXpet1tdUtdUNSaAF6az1rvnu%2FILQ%2Bm57vNexO1nHplr4IOzKNFe0%2BIx3mq3TOHtKN9ia2yzviymJ5b%2BHhHDmklVHhYdpEPjNaW4lMaEBUsCC%2B95RZiGKpCWnu%2FdShXKB3cNad9axfNnbKDS%2BfKyeq8JsUzOB6PCTZZ0xDOX7T6Ru%2FcrFkJbEa1UsW1xHM0%2BiQBdromJFN3fxZe86C5VUgsJYn9QsoNPqXztMWqGIuz57vU%2BDXVZjU0txtS3rCtvGUbv34FWgU8XmemKwkniAdTGzv2IM1OrcFRknFMueJad7Ea4ayq78NaJHTAksrHTYjxf2qRIFfWlCXYMnjUb%2FOALdJ4Anv4nVAUSAyL2hc5H0rkxy06cTuug4de7vsd%2BCcA5wTX8RldvrEORE30Sdnjbj2qq7N3jfsZf%2BEBhq5tcKkLLnbf5orSfLHMtRQQ%2BgNJ9yvB%2FfLRpJ55X1NxC0w59250gY6pgHAjAS1%2BrNjxR0JfO8G8z2UzoQIhJW4hD2%2FBwp4lSappXMdXfOtFRLix1VQzowHQBhcmTUtvht6hhQ8RXYOw%2F1%2BMuv3cSFIRRc1DoDvrUaYSUUfZwRjiECj6NeeynJLhIkNnktN0OlIZIhJkVWnqyAY4FuX6CAt36w58%2BZ%2FbGJ78sZD1JXtfvKNNwpDQZ0vvX0tLzJLHKAreTbMhfUME0JKthohWf8M&X-Amz-Signature=4f1a454e53215fbe85eea933ef7cda68c93252c4b8f4909523c0355001bf8781&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
