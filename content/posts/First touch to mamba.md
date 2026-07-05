---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C2YQKHU%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T150538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIH4TSIiFSRycyWgCw5z4hcRXk%2BZBbg7uZ1tsZ10%2B5D5iAiAjJXKnTtCTgh4hrqGF3o3d8GFEHV20CRMoLb9XAemQyCr%2FAwg9EAAaDDYzNzQyMzE4MzgwNSIMFCBtX5JIwJhbX3MvKtwDcD6KnK6i3XaSB7awby%2F5Oy87DXJl%2FL7t%2BLoisYAhFJspRjhIvRFAIG9VqkB%2FZaoQXjm41EzYrsMqWq%2FcH7wEoA2AC7EBdjgn6jTBSAVCGE7EOCdpu6d%2FHeiMXZiZFGznq6Gmaa2jc2tDLnXiDuROdXg%2FMXY1dNidLfQhfPmQvkirWmuTG%2BXqEWU1EHSp%2B1CRXhV7MamotVZKzZA%2FDXIWHst5ARv0bHiKX3PZsYZSni41ZTm5%2FTLcOF1u8eFKo5Z0esIifUhIg5bdkNlIM0T24b55jUkGjaeSevOe66OgdaEP0o%2B1st0XVj1boCk3UfRKebaZLLunhSjptWZweFKj7jAlAAosHtc2ORohgwIeurhnySJL46U38pAhkJS2bPBH5mnO3sQHMFjFoJ368Urts87cbq9pGtcrnWe5Aosvq4bQt7zxA53F6JrRXLoB06jG8OoqFL4D%2BBgeGbDDyWKFKMxhZqlle581fPwU4IObNnAEkGanbAlq0FDisFCzdC2%2F%2FWA2U8B9XZRev%2BI9dFoEWT%2BQsttKW4jLw4%2BOgr2hQIoPUMRBB9vxO4a8icQg0Sj%2BQS1RTdR06oQVyHIW8BMB6gLNMSXnt02zGhgWhg5x4zh568MlKm53SQS%2FYK0wrJep0gY6pgHndacY8dyX%2Bu1xHZoOXy4Bwr4wYxnd2CGPc6mXGXVMCj3osqbidXMnJJKLjcspll4u9ln1WlGR5LgXBZOlXm63B6FsJ2Ne%2FbjRUfsK3q3F%2BvPubdxlI4qaD%2BWTj%2BzHB%2FhKgdSuDHKUWMV%2Fs9COo9X7Au7yve6ADP12WRRAw8clToNVWBzR6Wh06dK1YQE5%2BuGBqVuYOP0N5%2BoRpMT8SnHb6COiwH5Z&X-Amz-Signature=167954d477dca0839293917f7f8db2726ee49c1810a21f416bc9825935e4aa04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
