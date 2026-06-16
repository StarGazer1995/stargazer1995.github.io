---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDHH3Y52%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T220603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKUeVX4hL9WFJccPSFBxGN3ehjTKoqR%2BDrEBo1P1vtZwIhAPEf7pUArsHx9XqfQgxx6cUQ03aQ%2Fv1P1D7vIhRi7JnLKv8DCH8QABoMNjM3NDIzMTgzODA1IgzJ%2Bf9MHja81L7WXN4q3AO28T5TwguC%2FJwQOeSJw8Hydgaiq16cArzxX6sW4EynDQ0TzKZd%2BGXnnTo1HCRiaLHCgzgmWJvYXZ8c%2FrXfl7hTuRwjlcXZ5HjReQFoeZ4MD67eXO4%2FaJZLa4YSZmNz2wXTqoONRJkt3LjNEH%2Fg67YkN5dd7blPm1pKgBahJ%2Fic4H8ZJsNApF6FMr27tcBTaLtTEw7LTEGgAvCPfQByQfdTFEqeKMPltcs6%2Fk0Uxi296mp%2F0ijBW22NChoBAudYhYvIuNi9GNpseEolcgn7rlU2gGnajcL2VEqO8mAY5R5vN2XEmOfJH0wNEC6xB2MwgLuhewpx1cyWdFZgkfi7hqYL7nQv6zTGhTN3Co88dNiIIOX9zWlvreNUdpR7WVkbFxps57GzjMB1HUT%2BRcQV9LWhIZwjgXwrTxVklWiFBelu4yj52P%2BZwPdRY8WszGqxfy0OQD%2BfzIhM6Wvqnbg8Von9kw9xdLmbTF%2BjDOEAcRRY06kex9J0YilluGqOA9NMGPWrUqPtuWkZ1aK9b2pUuMGVVtqZu87RiawlxrM9TzvuHXbz6D51WZsm6qMdRs0RVqoyRtWxxWVIrYOuQ81SDCaONx7JXlmbgsyh8SzaLXI9rBFD3OPo5K7jow%2FrizCugcfRBjqkAZpSvOXLNq2Uwnr6mt1LOXhnZzVW9ALLd9gjwaloZChXpsV1BuhX6r7P2DejvTjbbBkK15pZIzS%2BC7yFFt7f4nfatUE9IuSKJkUBEDEKzqaypZCPvtEPcjBH54tFCjsnzYmtsdWJaKl15Xeb9u2vlXMn7Z385ccHBP2udpJwA95rzv3IHui%2Bfbda9MHPGGaHsV%2BoJ6D%2Fv8EQ7DYnCPIYavI2SYQG&X-Amz-Signature=1023974144db9eefd7b10dc75f72865f77c715eda5db249e0f2a559ab969c3e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
