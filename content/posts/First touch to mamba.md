---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I5A4EK5%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T132118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICKTMncI%2FUojRhNm46Grxgh%2F7pnMcz4vBkVuyeg%2FcMjKAiEAqDVDUU%2Fc%2FvkKrjpfqeJuYIIqemRJLxgzEHDjw1EgnbQq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDCt0avVIBQbDCVhBeircA2n1EEP9vtuMwwxcKNhJhrpoNaDDN1dQPmvd6op5STfDW01NTl0OZ8gTlVEfFwgyxP%2F1a2GoXlZgtRbicO3jDUKnuWYCp5xCwTVyMuohQvHb5tB6YgvoQaAY%2FjRJSa3NwRkf2ZvJsMVcLoKzwAT7QNkQ%2FszEbPPa%2FiUtGRwvSE1EWLqF7Y3uRD80gUZVsV9gEAZ0HvCP58ke2xA9v%2BKO7fu1EBjog39qmLR5T2KJpr75pcWPneUCNUlUiT1ka3BTXXQnQEPsK85kzxlgq7wmqAnvWGCW4JDN9V4PxQrIvNHaSZhjdPbs1Q%2Fma6p9ShrIwTNEIxjG3JPhJHhJV2ekkCYcV7MIspeOYWA4RmGDNXMN6oLfSruLi2%2FwoMkjJEVWflGqR4%2Ftj1k2i6zwse525IL1nFRG%2BpUDw99hpiYSz7DX03ndj0cPW%2Bf%2Fkytw1JN5x4Gw3%2BzYS1gSgLpJTuJYsWKipKTSqCBpwmUFrDuP1%2F%2BhA%2FDE%2BBtGEKEHk2VkP7T5F4D6zXuCdD9n2UxZVNJHMHhad3zmIqt6t7otVN9JIC5mqwcaMzgBA0y8AN14lPy5VrlzH5mFDVwAb5k5zIgwRD2GRCJYHQ1orFcc4dFLPb%2FFnyKuKXwkREEOJ4y4MLDItNEGOqUBmJB6byWMVihofi3WpRcGaT%2B4URP2r3OlmX1rpAtlE0Vg2kO4toN5QYilLtWVq2mYLTu45HmHl9YuXMCX2kAJmkUp38v7l6VPjJBnDha5HezKDFHDzE2pjBPwSl%2BrgAMLzisPqN0h1gLCK%2F5wvciOQLyi84oaLhLAp%2FhnRpR54J6WENX2nR0Z%2FLZXCGZAOi%2BJK%2F0kPUchreOhqOe%2BkMUE%2Btf2Salj&X-Amz-Signature=465c5817bed37069897c49de87e7dd9a8dbd549df454537771e5a594f70a9b9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
