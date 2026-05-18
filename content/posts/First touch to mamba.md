---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663N57OZJU%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T113709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkuMNQU8zhv7vo97dyz9InJHGrGibonJGAuqFBKEiw1wIhAMf1CGtVkkUg%2BZnFeR%2B%2BWuVNouc8kcCEr13f9bvvcAbIKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrWwnFbWSXqk156JUq3ANU%2B3qK6VRiaHIY2QAQCZYp%2FqRIJszi3OGMvCFJx6LIgfV9J3W%2FxgXwFYAGTX7s2U7xXI4az%2FyzwrQg9ZGnSFscgIiOwJO1tUXF7sawRcQ2E5bmK%2BL9WmXmiv0%2FQKKTRsIKwiYt%2BhU6UfUAtVSloX0CPVw6oGVKSq5DZ2DDFqpTRPX%2FG5l8pFTuZGr8dBJau%2FKgrjb2SU8iC21XbEFMAe14k1cwhN2X9tpzqoUAKaR6KMOoGJemSw22nf1QU4XeIgGlep0NvGniJu7Q7OyZxKOAolBLhbXjmel3LuSSaNCdwkv8BNWe2J1Lrf2Bv7%2FDyr7ycAjelIFDR4L0Rng2y%2FmP50D210CpmhsYeUgFTuWhipxDWDX54lJAZsIp2mQS2y9B7GrYH%2BTKZAs95hmN5UA2mnP3UunJ%2BOzyt1phxXdU2PFUOPCOcKh1B5vOFgfQH9Zytl%2BbhoreH%2FAxI8LBV3bBa2%2FlT3gYLpVEb3s4CwU0hgkZj4RxWD2LBYAF8uAr5CyiWehk%2Bf2fe7aazOQjo%2BoWUxDuzPWJpG1C8ZXFflT4ZsxYxEZMK3LGA7huR50H%2BnGoVtlKDSuBpmvW8l%2FCZSP04F%2BLXfnFxlFMsT0uWT6jwYzCbTD1Yl0xzgyZdjD%2B6KvQBjqkAS9LywxDWsg9A2rZDQIeRil9%2FuZvI9rP3xe%2F2Kjq2RsNcQgYpE1Fn%2Bs0CadTQKRFfGbP3SJjU%2Bt4krtRae5pFhpRqcYnnh7LhUzNFsXEC6yMUu%2FEX8InLE%2BBKsojc5sUcSraW7phVFmiOqh8sKa%2BgUoCLS%2BFUD0wSAKw1g6eAc5gfke%2BkAfP0knLJo0n%2FCDHWRJ1Onv9Gv74LZaK7Nx%2FOaBZYbVC&X-Amz-Signature=9d3ea29c9b07d2321f31b9e5960129f4bd70a72a8fa92c4a5280b68396311830&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
