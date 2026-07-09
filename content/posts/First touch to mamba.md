---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FNVW5KF%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T191914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAypeKcl6p4AXNHyD%2FtcUHhB0RflKlbuCqldaFSVxFdIAiEAwy2KCMhz3UTmDhV3z5K%2BPXbrWk6XEKtGbgDbctEEozwqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCfpbj30bUazIrySkCrcAyh1Ut6Yugzw5IxlFWno1BygwgUT6pvTuqvvkqUTFGWYlV9wU5Da7jXaYU%2Bj6FwV65fHURSDGAOVzFh5Gefr%2BK7oZUdZzqxkZXBPCx94lC1T9oTNBAmNyFaTfcSAZEzL39VBFXXgcEWq5HzSx%2BCwrI3exIT2dthal1vjKEOosZyvW4cwJNWu%2FmgnV5xie%2Bh2k9M7AeoUe52YFQZxEi4cruBG2E2gKDRH9Khlbz0apnhJ%2FrHuvSjFYa0T1UvpAPyzsgQXoQAmp4x4%2B44%2BifmfR3b7NToYPS2ONumo8udQ8DMXe4hWL%2BSVdUmrMZKpSy%2FhdCBVY3X8RXe6bub680wO0YWO59k1CDUdvkuf3gIp9HsMbHQRkO78y%2FgvhgwTBTpJFr5QN%2Bb%2Beq0AdRN8RNTIZ%2F13zg7VHDm1nA7G7X%2BFb9aazvUAAhWH49QEXFL%2FXBZ9f7cDEEhNKBzlkxcBirCT43Dk4Se40CGb5CDtXSftJ2yIyhbN8tc1B3s962kg%2BdYvZjOn1rbsVtCwvXkvgCBMRKc67TjQkjcb4b1jbzblu1gada8K8QsjMhgFBEs%2FQf7Cp0De13Vt4rDRSJJzXwyb5GD9l5XBBj7A9jRJ0FrnV8vXo1kT%2FNpA7v97ycrJMPjWv9IGOqUB2ypIa%2Fk3%2F26UOaenT2zIAv%2FNKGZ1A4ZcGOUV6bc8NSdGL27OFzq0BI%2BvTqWtk%2FwlfovGhTJ13z0tKShAs%2B9%2FE%2Ba3wNFRpDVjrdNBOeCPs4Cs5jwEbwpq%2BB6WA3mHgzMKFdnZAdU0XINXTx4VA061D3m1wzZRNIbj2nPpOHNGzn%2BD1%2FfFGm1%2BdhYdTdtmCl4B4sguXy60MWjKt%2BHiet8UQcsbNAjB&X-Amz-Signature=b7dcda487cd75f77aa0898f367c4fe6803838cf74e10d2580cd8ffdc75b89332&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
