---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTV4A4M%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T124038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDa5wFTlMFx3i357R7UZ232nZB4JF1MVpCcJW8bSElAaAiAWxO4PZssr9IJTkCG6NEmJ5mMmNHqlJ1qox1sN5MGyyCqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqoYEAvz4TPqBexfoKtwDU%2Fuc51ixZ6qhS9fnNL%2F%2FOLxlUH6mfDDP66v7L6JxxmGOf8DBP4oHPHdkcYVG%2FmUBP21jXuVBT38kcEGPS%2BSy4sA9g%2FDMRaSCA2cyUDOwK71Bn6YeWcfdWaEjSfGnQTor6bGjv7W0EY7mwo6cDErkMPKM81sygZ%2Fc4xokGmYePXlJcAEVP0p%2FNMAcy5W%2FjMkEEpxtIiLtnfMKd18WD3JiY6VmZqZi6%2FUDjOa%2B77K0wmOdVBrllagmcAneuoHNGsh5VGs9Fi7SdcVwHqO6cz8huCJlJUXWyuB8Kmbk%2FW3FfHxuydndMIV%2BveUuJK7UomfmWkTv%2B1kyKcw2r5nqxPgNL7E37aDNoL43rVe749b45JuHxV5Bi74Ccgq2EDXqSmQLnxifuiXLxkZ5JTUFhCubDzd%2BqxKVIoudl2VuVPJzT09ydg21GoW%2FtBu%2BAKyQDIM8Ql00CiMWIqiaBgLeggNf3f6WRha6lSAPiaDA%2F8VBQrr5DXcDlqpuCbMRJWxj6tdHRJ1WEZwvKAuJM%2B0dC9Hy1mR5O9AVIPRlv69TWsFqNukVme0eVdb7JQg%2BO8wTovhPYYwATI7p9TIsLRuYvu3T2fum6NWE8dkwWVLkPyX6nCz%2BHcZZ9qx%2FiLpAV1ow2%2B7m0wY6pgELinTc1rLZOlT3Swg0tjNQGUkNRFEQKhyZNf%2BQbCXpNGBA0V3B9SNY3IuBT6bTmJHX7t4AeHYUkJa7w54D0JhYYHbiM4QVOStLMRD0jZMKTA3prATkF727ZAAKSwHBZtBZIrdfcxCYj7kSDMOEek7Xgy%2FHyh4BaPXo91JReyHvg%2FJnEYYg6%2BFX6UWKdz%2BZjohKTScdCc1WMiTfG0dY%2BxwuucDFoM%2FD&X-Amz-Signature=a2c809b74d29edf6dbc9ec57ed5cdb1823d2c30575ec07aee2f897793e7f5bec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
