---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJZTDH4A%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T223436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGt%2FnOf4Y8NLSt4CtEBb%2Fu4LzD0U3fI%2F6jiIp7bL24k8AiEAwfgHF1w8lmjlsYu9q3eqKyDG5LRkg%2Fj5Lh%2FZJ%2BIy4eQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDO8LZo5kab2tq4hN2SrcA89UgVxaU%2FpOVxmRuCjNZJgLM7uwo7kGu40CU8VIoebq4kDz9XgdZaldto0UvXfqM5%2FTbTVOA6XTPQdkwwGsrmXrWTUEPRyn5UUPn%2BqnzQE3zNg6Emp%2Bsg0t%2B8rVEDHY2ZfFUW0L8z3gVCcTlMCvYl9IQWbVMbcnVY%2FEtNqDhfpyYbLnkPGnsVbQxnO9k5giEAco1L5EyH6gNbg9SW9KsNU%2F5coiUG9Z8QIF2%2BsSTXofnL4kXDWD6PeR5cRjX6OjIKn3FvqoUdTPWEsHvB%2BNonpb4ushRzvcdAKI2ZzbVT5wbFCwAQl0b0GHwYK6txBGQpm2tkNrHE8u8L4%2F13K%2FDlqW%2BicQmzqnCdydwwXv1Dpr4p323A%2FWOwCxDIMGggB8vbHIOXvHiLm882WYEu9oUEELGh1LFm%2BqP1S%2F1r%2Bc8f9BOI0vPciEJ0kMPnqVT19VMP04WHNcJpQEiXcHe4LhhfAF3U%2FUojG9S0vzTQptv5XLAvXg3PhsIExOkVFn7Z3rSanpC66ZDYfDNnBistfOBB56A5v2j0YSVXKBYNJ3tASfkmnXy%2B%2F78LaMK4eeFsaG79wIgcEtHGLD4sVIWDRIaIkVS0pjox7m8gF%2BoTlMP3D8EeIMWGPl5wNPfjSDMJOvvdQGOqUBoINtdFDDp%2BbmKaaMJLC6Bbee5ynmCM2NLOtLV4MUe7BH%2BjNfz78lIrnTgBAsHEm7OWd1OZMotRPJkWUwnoAJ6G%2BM9Do87T4tWBMU2pXds44BmiBS2pJOcpqpoiBq%2FhNfaY74XUbyDtrG2KdDaT2G26uRlBjAbvUusHE22FQoXIocM0jbjlPn%2FfHelc3LyTku%2FRJ0J7XjYlAW3RUOHhjVd2iuHpbv&X-Amz-Signature=ecc258b87a80e61a582e43978dc6ec39f69fb544c752a79b60aeea1550c9bf85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
