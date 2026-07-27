---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDMMNJQN%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T224949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbeYyFdY8kBkXZ2elxC8yH%2FMw8quZd732GguW4Ql8uUgIgHg2zTGVcs2XlP1WxW0K44NMm3iNejpkIB1i101Y6l7Uq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJCwCOkcdGv2WQICfyrcA%2FpJ%2FrXDMnRoyObPxSuCafroizFjzskkPtbT3RcQxz%2BXAF0reVoflZhspmMP0kJRfXxJBZyJW5iv%2Bicbb4v6Eg9YKwkTRDWAf4Ib1msZ0joCrgZTlTzscp7%2FbbtGzwlP4v574%2F8mbuGhmXS%2F306JoaxIsEZ2NG%2Bp908ZJHwkOz3RquJaItms8NxT8q6VYdTPlwLhIEoNr%2BNKLnAV8VxjxGwOZIe9QgWMQBHQjl%2FajoQuBnvTn6G5Gzj7FednSiP0tUrbUie%2BuZO2efWcLqij9f24iFItH8KfoCASQ273Phi9%2BZEhF2Anb7eUAKvbYdHuRlH2vCGIvmHCQ3RbahOMlOL%2BYYuTCnYNBX%2FuJ53V84stpsq3%2BTgCk0XXcoCLMYYLHtZjGUwSb6xHp9S27AeJ47B%2F67xxZUBOBu2GBZREyHHPtYrYcpuhZCF9lgHqjRy1VTZxatUEexjRCNZJ3JtpFUY%2BCCS%2Fv69EfUIUY9WbNknjnc17t56W7CPWL22%2BJqYDQA2f2ZMVWBtq4dgHo8EzZRLOEhPaLv734zdjsAk2wbvQffz6jrtg4VGdkJMwMjt8z%2B0Q1%2Fhp2o4hD5vvteKbV9yDu4N4oLK0a5HS%2BcTFEWhswqFuzTapDzFe81YAMNDrntMGOqUBfNNdVrO%2BdNjs%2BGmqV5UPuz9oNE4yuBAkrguHSaCVpRbVBY04mZMwqkuR9dYtN9xOqtxMJHC1VLZT%2FN7MwNcHQIqX9MfH212RFl5MoMLl2wjpG7kdbzorzg%2FwTjgG2D9hBHFkH3Uunk0%2FBszWMO3J%2FCzHS%2BotPE16rrMsDe3Wav6bAmFaDfvg6h5%2BhJ2b2WEdct4uM82GAd7%2F3DbK9QMTRKmw68oa&X-Amz-Signature=d3ffd2c47b7bb01ff3fad5db1973d9054372df61286ffe6933cfcc2f9b3c6420&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
