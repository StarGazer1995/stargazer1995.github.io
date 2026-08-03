---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ4FD43D%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T225006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJHMEUCIBjuC%2B7K5NEM%2FV2iDxJlUQhqloRo%2FlBk3rjhlLueCKALAiEAxyrr8OmLWTU%2F2Nm0GRRB%2FfzCx782sB8AzkPqxSgcYssqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTQp6eIli1Aggw0qircA27dGS%2FG1a8xOS%2BDt%2FTgJ%2BXi5t4NK1RUJDwSF2NlWtGog4uJYaZGW7s3BJx0Ur6hUdtA5ZocBfvp92QMKMH5TMsmOZL6XfHSW1Ame%2FGGkpXxP6spUg4rf3j5J11xA8HFRlKYqE7GzTOJDanSzRrUyXO6dLN%2Bidq2x9lwGKvoDPrTj1lVB7jyZEySdO9U9Cn1Z4NRgH%2Bt4oSEuDJuqamE9qXkYeFfFYipOXdIK7u8Px%2BNVfwQqGdx%2BAs1NMRDWujtft9EsAPILTyPyT1rgsfRgFRZ%2FDZ7Za6Ya1%2FYjY8BTt7za9A4Zk3xGC2j7WHJ%2BEtHVvCIjddGnhNUas8wjMlvspt8nhsjxz5HaRqEZWND2BLdRHu36EHa%2FJqRIgUvlWhLQupH7OysUcIEymk9zScFHPAZlhWO068S3ZkXqxrwGUqWRyAM8fNBIfq4esoBbZ2ncGbyHkkPFoGL5MbnSpuEsubT68utHd5i6WuwyWyPzKLd7Kaj8BFFo03UR6zLeqi23ixzUfuBKDVM8cyWcMhhbUv4EhWXUgyfvTZ%2BVPOvdvpf%2FnpC2CmpBQDOCJrnDsk1uoKbsqvcy7uWdbhQ3Y3lnQEDr2fcNz03xbDMxiq7%2FZMrZLRS2JfO3GL3%2BMF3MKSPxNMGOqUB1OdoDmFM7Cx2wv08WuWeFtuxy9Ov2dxpF33xsh%2BOESG%2F6CuHFtR7sGv0fJFCqIyjJz%2FQmKX9i6cGipL2r%2FNSUJBrgXnb7hgtymXHjNX%2FqlcEXSFrfC5VZ3DhBH1amM8LRxnSAAMEjOWrzjfc29FaYZ%2F6jjJSyhRo8x59rtwDvt%2FwmfZ%2B9%2Fddv%2B8Zm88Cus0nqBKFOW6%2Bf4nVIViHPFAd%2Bz3Osgyu&X-Amz-Signature=bb494709bc5f1651348071abb48831e416c6d5ad0e1f34d2903fd301444863f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
