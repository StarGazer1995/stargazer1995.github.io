---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTKCRPKZ%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T185142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQD3Kmj4cdu8%2BLC1gfLinTEv%2BLouOJPxPy8ed4Ty26qtywIgd0W7kekd3CoViqr4wWOMvHtqUnlowRg5mxhDsnw%2F%2BTgqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNOjBbIYURjXNJ0HvircA9mW5PNFDFqCTlVjFTg2XRDd2mL7V2%2FTiVuydCx%2FIBWjK86dL4TT%2FkcjcdwK8J9Gy6nZno2GJxjz4O%2Bpsv%2BKlYvIq0zZAu6rDurbgWJRg0sZnBktdqX7QW%2FXQ%2FsQrox7g8y4VVgZr2ur72onokZWKashJIt9EduFslpaHl7M7888dLeOQXSOLf0k4R2NMP19eusQlkS0rEUNpS1vEOnmH97LyUaI01UfSYjfm55rREU6AWJDTVe%2BCGyF9dxm5Ha2fyHdOadnOjYQT9KmiY3G%2BjCaHgScYN83qiJwCo9qG%2Ftw5vc2JRBhqOv%2F%2BzBqEH8tW%2F0VdiyGSYisqqkkbeNw3J02EcpgnH2q%2BuO6tGK9d9lSksZPspzXpQua3SX5jqNBg0F2VJaJ6T%2BvYiTC7kr1mc7OPSvXpI138eRSTb6XK%2B0CPJux8%2BqtamUlNXEp5GhPZ18zHKp%2FHphUbWmgiXpRvY8yF8W2mKFhAZf%2B2MkYZIQJl3RKED6YpIpUdWgGCbb29neDgMddN3WpvtkzUBOct72Gbf3X2I9l1ywEFKvMUXtx6S7dfkOqfQ%2F2MnBymAYlVwsDvPg7yADu3NCRXkVqbAGuPkRTDwBvz8ksG8%2FJxt9lTH%2BPdjw1ksCQ92ysMJeOvtMGOqUBbkkPxtieK6Lj6N%2FnhbIQwCI6pmepRujt8buWmy4zeBMeTP%2FxLKwCfHvgWrx17XR%2FvQnbvRYoI1%2BN5BDCMdM0C4MDVN6E0fufN2mS8HVY7RIFSmcRsy3uj5CR4YskaAaoa14uQEm80puIvY9%2FK9o5Qp7IxGoVGKE66bRS129VlmF9jB%2FSnAqHWyB%2FdPC6o9J7j9EOayU2KktwFYQYKuR%2B%2BsWWQtgL&X-Amz-Signature=ada0746d675b66bf5dea414f11314315368a6a11ecc85739409f8494cab321d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
