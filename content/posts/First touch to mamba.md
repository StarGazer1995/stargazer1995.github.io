---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6IWFJN3%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T142237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8P4lE3YyzQPlFeOaQpDU6Cisnj2vlHRbc1gu16S0ohAIhAKRs%2B40oXvSySK8spy2sjyn572%2BKcl1TB1EYT9twat4AKv8DCG8QABoMNjM3NDIzMTgzODA1IgxmG2ENfcUh8y1ys%2BAq3AOWwuu8rPGm3XNOMVyAU8BYOFOe5KyXme02mCApOQcrIUOWz5c4PxXlCk2GnP5KOvBcRmBQdiIMxcRwi8HAm8ozpW0r3GC1Q1ep4l%2BttmP13i6q5OPmTDg51OQ9hMCId7nFQf2Kv0vH%2BfVlj0%2FSyvnEQFRBUfoQ%2FBfX4jBBCv6bV%2Fv0vWKBYnA0E3kF6Y8vJUzxsIxlbQ938BoR17B4bcULMtHGehXnxMDoVIMyuZ%2FFdc%2FsWKNrz8Nbviwg%2FyhWF3EdrMIpQhyNerhh2I93x17hjbPhCmzaoeKs%2F52J7dab5Ol%2FSQQmP7Tb6%2FxiBosXU24eftwP3vSuPf5zJfhbUVDiH4RDFEtsTycfCqJpRwBO2RDzij2M1meT4sqWr8EFw%2FRNAKVUs%2B702du5LvN%2F4WKmz80RMs2u4kR%2BJSgpNu98q8GaT4Z3eXxVh%2BKNapch38iTm0SjJ7hkvwNoOzXyReaenfo%2BJJ1N3klkW2mgeVi786PRXT%2B9hMFNPcd%2BXZCUCOndvmmqkMYFgQ3%2FJz7iobTKPXNSWvme0eFdVIc%2BLq3okNGXHMvPIzSEf2aEHdaXh88nzTVhmdbNsgFXJTg72K6nrHY0evxyG8TFBFkBbcZWunVLo6oO0Djdx3cfhzDD7tzTBjqkAf0GgDFUjQIGSg%2Fo%2FuyxkzCGEfsZvDtNHFLXsl7T1nLuDykpK%2FWbPaZww7DZNG0t9pM%2BhZ%2BNZ7%2F%2BsLxZbBlEqBMs3WpdRU5U7Cbm7O6H8L9T9anuNAd1A3Aw2R0iWRGYbBpdpCDC%2FcyD2oThBhSCCZ%2FEtjfdzKmc6bLCG1NqHrg2iQq43Lo7NHeLL0QjA9K%2Fycd3SKIEcqNKlC5ptSmtP7jOsuv7&X-Amz-Signature=e327ede2e9faff65a5810df4c1ec99a702af5b6829ca940b066879bcc099be7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
