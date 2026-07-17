---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLHLVAES%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T075031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG28LOe4xa1IApyHp4uNxO87pFHr8j%2BehvdD%2FCMo8K0%2BAiEAnfwZQJg5NXUBUN%2FTLQqknZUTTHvc87cfPS3OcfgLf8gq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJHV%2FR5RM1VL1dlABCrcAz7qQcvaoK05ZrYRv8nUDe%2FDNUfFsRfV914I3JEh49yiYoPzdnIPAPmRFMIEbVO3xCKf0mo9u7N07Bz3YM7Mp4vEU8EBnQvG2i0S8Sfw2DbJuXi67TWIoTL3Y%2Fvu2SSHAuk9C2enb5yJfYf7C2KvEWtT3DiCiXZfmaUcf5vTPVJbDW4YsAx2G0HJg2I08cysSuod4a0QwAddhKIpnOFlsgRbrjzLdemiFKdT22ShkOfJWRZnQFtRUbdZTjYbqtiBlZsRvHcdkxX3KkunKgezS81b8u1Hz%2B9wlgscHWS8KmJFsWywFS70aMgfqsp2c0nAe2VuyzusK8NE67I2ymIVr6YDbfR4h9LagGAGQphGiGdT7KGTRov4v5u8WDvMtl7FO1qtoHX4cQmkhuWEe4HNsiOakAtEfOcQFZch3R6dMzPOxUeuPLCefzuTkHM9c%2BupaJWpE6n39wyXAyxDRgVkYSNdGcQdqryk9k7HcsSew282DoPwrGHBkXiLs0PYLufmPKHP8Rzeo83%2FAMNtY%2FxNFrOOfdhkggDDBySIerialeO3oLFVCdsPmPjomheapzFiCeDCTMGgkN5bTO%2FP4m9SKZVFpA1ugtWysYJlJpwqlabsLDKIsMJDWcXfCrVrMNCt59IGOqUBHJYQZYopisHdKzk%2B9dr77Pt2BHN1IfMVcNfpCN3F86vtyShNu9wh0cY%2B%2F1WKS01YupBu6%2FtX5kwIqUhPsyz3iAbv8E6XHbPC4XzORkCu6vRKdc8ULg34ryQqgeqEsCxnXvrqLh16Rv1J4U3LdQDbCz1VIbjWptYyLyOHzhjQ5%2Bv6L5f357KrvXkTffhZaaiENK%2BAOTUtOEgmxCduG%2FA7baxHlGRG&X-Amz-Signature=ef1122786a8f2320d9e471273bb218b6376903569ca4dd46d884ae7c4f241266&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
