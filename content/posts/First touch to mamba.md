---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRZLACNQ%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T231421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIDdfvfyAEBh2bR2Ybl632s5%2FS1YyaIPdnJ5LEjPY1Jp9AiEAxrtG%2BZczQkjl%2FIvCf8vXzVeZ2LOCoAGwQ1ibDrTwyPsq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDEysAk6frowFm7zCMircA9yiXCijiZt5twCke1jUMzI%2FT0Qca%2BURXq6l7wNEadxIoMAJ3RJn7DtpS2NJQ041G9ebsU88SqPg4lfTWs6v6eNFzLgRqTPr2TPqxnOvxnp5hUeL%2BRogH3nANdnQKNrOcteczVFxtj39jPfwjL1%2BRcCr1TG%2BBNaHDJqQiNihZm%2BIz6IC2ZqTMDnTWGMJZoiQIRoJerI9es6h%2FmneZVptFXCCo6yioiwkCbscqylVv74J6DIqKhUiai8IAxOZawmFJPZv8paYe8TSbzUOPqwRYMw57MJu4bB%2BEKmFbYSrDNhQoglpdrLyrgkwvnsnzELdo%2FlL3VW3bnnmuP8eIp5DwjMUQkaUwtDHweseU%2FYge3w3EvnUZou6k59ZxTQms%2BjlOuO5OHnpyqi%2BLvm4qfVDmPSEfT%2BtDAadBYo%2BQGt%2FvotBVak5DVLZliVWMBEw1Tk1liQidFjtgz2ocXRgy8XvVrVt92Nv8qnoxTlCou6eQzEnoEgBwZs9x%2BcrEBFMr4bkeuMNQi2B7ocB0%2BMCar6gGpzCvocfnFp%2B0LBRqQy2Vw4k7yJU1YxApPMgrJjjMHwLz%2FhbPNzdzOJUCDQBnX7nBsnouLZGKp5hk3PAJs01wILLOUew5vjvBMalI2a%2FMMnTrNEGOqUBkzz3i7A%2B%2BxBgb9Jv9PSE0UqVBNlMsOj8%2FSs8cpcKfv4k4daaTMxvp8U7PnceayiN%2BdPeZgd%2BmPbOohDjK0yF93bt6PJ5TjUZHbs4E1Txc1aN7Pb7%2F%2F2vwqOmapu9iU5OQU7HxDPRfWNOIDNKQhvyvDsaS4SGyNXYKXRvQW72F7KiZelNmka6lF3RhJeQf4gE3%2F%2BmlU8oEo%2F4AGMM7v6xCUh5EMP3&X-Amz-Signature=fbc0d29c5d74cd154fab534bed81cbb2ef64c85063217984ebbc33e950e4a77a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
