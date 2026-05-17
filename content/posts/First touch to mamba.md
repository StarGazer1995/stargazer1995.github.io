---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY3VXZRU%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T105927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1MhQ8s32W7a%2FOOEKErA1gbLOPFJqoX7W1JivGAJZvOwIgJqmklwF9Hc2t70HACNrJcmwTzIMh6diiueRjK%2BKDWuIqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAePnhO4Lg%2BSALHRWCrcA%2FGIJTAj1ywdcDCLPy%2FBdfdKXv4xedFTgGwtVNBb1iWk7GpHXEsJShxafQY2RymX06cp8XP%2BLlmkiHsu8Gc4e6VD4KbKfs%2FUxrhzZ79cUTtC9SB6JsgAY%2BMQn4M%2BQnnH7FyOSOJ6m2wwq697guMt3tscvB%2Flh82f5X9M7OGEZ%2B961jheB0sgL%2Fv0EDIKGpWOt5qKF5uurldFQzolSM5NtgjIQqtcfMTy%2FKTBJ7x49L2XBdlvH3Ya99ZWTQVFfkV%2Ba12QPRvvhhCP6GhKczvmPqzENBjRwZs9Ivr5GfYPQ0XQ%2FNXOS3ruWcgpSrymgU7OfMNyrLBqaXYEdO02u6bPxUthyp60le8Er8Vta6GvE2jvKKohhckQuJLqxj2SXqB%2Byvt%2BR37bqUvL1MRey%2B7wCr1ItnoivfV%2BTcfbc7o2D3KIBqrH4pDGtiTy4hCzsC26dCpzXTfiAHNFFOj9uaYCSgdBYToyP%2FqVgKeECCvc51FhJZbEV1%2B0b%2FxsSEk87utJvsGr3463JE%2F5gFu21PkLAPdqLqjbFkwoh%2F8DYyAYfzGRmUc6H%2FPmObFi7AxBE22wFZoz%2F%2Fv9fpFSoYZNm7egh5jX5sZ6fIRcPrQoRk3e8nLEzrXYfbUgfj5zq0tCMKTepdAGOqUBCNp%2FZmpfPV1htuUzsW3LeOpcnWxaNcaSFw1dvz3YVSoMTGLBW2tHkX2xGLBqKydxiD%2Fhl6R3bKVMNcOZyHA%2FLFkhq4psHC18p%2F3l0k6SD4PM6LGJfScSq3m0v1bJwzVjW25B8EZJsEqAWQc1E3R7O5Fp38Vmbm608KrOWnWOYb2qrDd42au6un4EKaTxQJcol2gdn44WA0vV2odD1RB8GrYTxTEn&X-Amz-Signature=d7a3574a4eacdeee6de7da8032cb116a442d219e5055f7a5096678c81d6aaae8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
