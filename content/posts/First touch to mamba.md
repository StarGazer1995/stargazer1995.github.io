---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JHMONKV%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T042718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD09RYdw2%2FUT6ztWXIUQ341ADMfYaC9FOAPvl4cCYQAGgIhAKcXGH5V5%2Fuzj8UVTYkKY1UJfJgtr1dsKABOiKA7LQJvKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySBM5s%2F3zlGSJx%2F5wq3AOfbjb1HyRV6ibxsmAOIx22cleKpW6x9vpo3xeu%2Bm5rqzjLHRBmxJnOrtEm0fex5PFd%2BxNUufRzjb8AO22pD11%2Bl47v%2FakBA8LDesr6UgNuF3BIMqO6UYEuH%2BY5Bms61HB%2BG%2BeLl0e8ND4CSWd6wRG6we2hk%2Bta6b%2Fm7oun9KRkiNEKYpgadmWtfQABmjpQYL9WQ3SUYP76ulaR84ZF7jg957AaNWaN8v1zZQXsrLvMg1pIMiitFYE7xor%2F5upGlmffuC1atSm4jgaM8U6U6%2F9AZTTBWWPOvXJkcvV%2BdW4JNkZHT1NRUewHEwARcdW5DCdV4HzJY08hxCR2HrLFvKwbAC2UPXxAIp%2Fslp%2FkDwOMfGKF0RXGVXlAVP520TON26vHqn3OlcFbSVKbfCIGXdCYPb4O0rTXuga3Rcp3jyXzWciaHJJRUHJTEEdUXyVAubWCNx1gslrYgrtsf4Sx%2BJaylnxY%2Bw%2Bg5d0F87c3jKF%2BPk11qiDvNaWTym96xcF8TDD1bHvdqfTJRySTgQBylBQH9Ek3fJ%2FngQeNDja2LsEGLHLc%2B%2BNLvPmx%2FzzYz3nW3RZAYzvqWeZgPycYOridqCtRGKDsWfy2jYO3n5k82%2FKO%2F0UIL03SIZR5hyCBeTCM7p7UBjqkAUen%2FFaqr2tVdcWbsFAptwXItLa6KGep7MPpOUdEUmktArdYH8YMWTsicsouq0FTdC%2BRY6R96p3XhGNahBjd6OAbdVs7PxVFPKz2hejNkOXY%2BADiXqmkNs8zuGyMR6W1zRxc8t4X7YZDltCw3MU4qkX22rBnD3vpeeW56%2FU%2FE2h1rGdvQ2rpBOrtcOBf1bxocSbIyHLyfsRlcJQp%2F1LiVug%2F%2FsH2&X-Amz-Signature=ffdc1ce26d5307f6dd41098637ae70265fd75ab011f8455f903f9397a4268eb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
