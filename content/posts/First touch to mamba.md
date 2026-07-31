---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FHWEKD7%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T171822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIRsjGgcYuAVj7BtmZhpJNgRV2oMRosIgZFPps29avTgIhAMEFNYRPg3x7UmhhKV3jywJwYAOM1RRL1IsozvAkyYO7KogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYmTp2Fy%2FqBikUsgIq3AOvb8a2qzB26UwCiWxEJO8gba4dw8yR7k%2FgQCujL38HSaTqhRTq56%2BGsm2H7bazP1AtzCUBENCq6HYLsaAaAj6ZdgNGYvqCrDfsU7nUulMYVEpvhCBoaktIR%2BilmILXXKJYPrLcmjM4PJQc3kDVZOUG9NO3wbNfTe0Sjl7hL4jeV1zMapD4ZH1wrVKt0xp6fMmgInoxlAZbDHnwG%2FreBptjwP43wb4tW4doTEO%2FI2o4V74jJs4g673oh96bCHycJjOFFgivW3fm89OnJs5h4o54HGzeymHyMjWx9k5XrcTeUzkqDF2pBPqZL0KMFLniFJmHg5naE7QwowGoXHcAwH03%2BCSlJLq2U0WqBkcO4gzxFKrg46g4loPXJkygMlyEsrVhYb%2FE0YOpqsmvvzdtUeY6KIV4Yf2Y7l6o1d%2Fvr8h37Aj9kCOSWDsrRvu4KtFiZqbY7UGGqvM0UfhtcsdpgJpQImsQTkAOLP%2B6rbjOOJwNFR8sVexezbJiC9%2FiJI7KuBZVparrrzOVkK9rMOQUU2b5SIRnzqeBsKe%2BcLH0LGaCizPJnh1%2Bs%2BMEhacDyVXShd%2FipqRxaqhwIVQTHLrxImvyvLtu6IpBNc%2FSKhjC9iNg%2BPsaeN2CvfxRnpvENTCJmbPTBjqkAYcBFUld52KtasH5vRmYcsdiF0EPyA%2BS4wcEqvGH0%2FpKO93ccVsBDI4neCtA6th845h8bRm%2BXe0L6qJZr22nTYB9cmaDQMR1J22sUjOCRHD8q56a%2FH5OZFv90wrAt5AN2oeZU9Ya0s1ruL%2FbtR4VdX%2FLegFCZOYNkp2hP8Wpwk2QPP8vW0KHTqC%2B9NSRuQLh6h%2Bqy0MsqOkQMany%2Bz0Cr6ne5KOI&X-Amz-Signature=995bec89fab0d9fa1134cdb2730d575045e7ace140a90cd5dcc044f7552ff161&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
