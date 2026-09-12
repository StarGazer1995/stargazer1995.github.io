---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VU34TPCC%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T114647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH5T1go5YgHSI9wi5I%2FysgyB40BehR%2BN0HXodyNnP5pXAiBP08%2FlSUI%2BOYuoUTP4YwG%2BYZpH2Z%2BImkzkax4d1od%2B8CqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbBnfBucjyXaUenFSKtwDK15pPJOu%2Fp5zln8XoaG56ju%2BqBpAscp3BNwCrVR%2FmCcY4JQCH%2BG72mocI06J2dgArXGFz7t916PnENaXA7EtkSWTBQLpY86dZVrjBToqZXZJczi0yOha8i6%2F%2B1EAa7VcCIf4hKnc3n4JIlFNz%2FxIJwquatVYwd0IhdmivCHjVVUYt0q2I2COJiiOhv9RuXx0qs9mZMGaIs9luOVZSLg6WqSbxFAPzQ25faqd8wYAJ9dXh043jRmqFe2sHLyVg%2FNeTB0e3eqouvih3tNtsHOrrnKETyC%2FupKg0ERVYmkv6km7BiCTewOFqROKF04NtNOcltGnaBJq%2FgE05k9cQ7%2BaiX%2BzOGp83lb3PtyRutz4bPbOV0yYfdibsMijR5GLWAlQWHRpp1z%2BhM0OGb8fQIAkqkosEZqPolmL3cFXZ7nT39wUN360j0f4KV4MbURAmvc9yjkjpZX4S2YelG%2BpGqYyfAv%2FFtWeM0TkZgpMt6zpr6jYzQcf2b4B3p%2BIF0TrhIFgsOPAbyJQYxGO7VCKRcWmPz1Q6jmv8kQzss1ehgLeCsxYdtZeKvESNbsZDM2jKGiXPg6fIs0NnB%2B%2Bco2kjQ8%2BNRo7Yk5IKg85ZX1fB4OZkiNTyiwc636inh8oK7kwqdCU1QY6pgGdFqfccqpZc7DVxzR3tdBHPKm8wI8foHVxVvrldnjmN%2B16kFsq78Wr7abImJ3g6WkF1AF8IjpmZP06Q9b4WZW8h%2B15T1bSgQzsPWi%2FHD69EYovc%2BCnT6WSFhZ9itHR8Ct5kEBb%2BrwZ%2FB4hJiOFIeH0Gk9l01zpTAtWyirVHMwpxIhGYazYl087rYYIV3PSQ%2BdbtP5KNfnRSpbmVvrtBVODGFOePlX1&X-Amz-Signature=096c82b428810061747e17e74b830fd2cee911cea6fa81ec6a4dfafa716b87d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
