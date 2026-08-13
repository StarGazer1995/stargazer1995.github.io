---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SZ33OFX%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T164345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIHU0Kq7O%2BWSili2w%2BjB%2BfOYZjf7sjL61boE%2B%2FjtBty4cAiA4HpwZZBq04ltLlYLqO69GWxS%2Fsy1fHCwu0K6kjNrrziqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsZEH%2FKfP5Fz%2F8e%2FBKtwDB%2Bg5s0S2WEsPO6oHn0edpBtwZHP4ORBZeJeY3XOknBjJAP%2BZBEwSvBb5VzAnNi07JoGB4omEw3kSAli1E3OWolsV79mRIhbBZGMwozhSeV7KmZTyjz5VCXV3S0%2FReaxSJnIUPG7qGXO27ltHu5Mxa4OE3VCHHVylR4R7RjvyQlpbQWNovezVVsEvtdz256zn69iLU0X4%2F7RLxZDeJvvlfXNcRuwQVhjCAlwHNwLWhzwbgXf1zOgL0nvYkpGr7rmlH3hj5H57LEOmEVj%2FqQV%2FoyyQcgFtLvaRwujgdJMFQIoiA4mBChWxADU0SXNfQcxnbYk%2BjduDVnlLhn6d6zLsQyHrYqUongTApbL7e%2BHIzsBZkzas%2BWwIDRDU8Q9LJVr47WfsMooR7mtsC2JwrCF1TtFCMRiviP9MeCxkhy4X6wHqV8qLIHl6XYpwVwYcIfkezrmQhCaVLrl5PoNEdaPjzPDZFqUix%2FlgyDvCGDpDx441x%2B4Uu6NgWoZDOfZxVtXuIV2yAivpOsminKuEa3YpW8nSpCxM5ugspGk6L8hMu6oqjDIwe9R98OIWg5KPXnAsq5dVOYYDvJsRxlvDJDPNc3Vv0dplPtPkRfOdpLb9WbPYztyb31G6%2Fq7TQFUwrNv30wY6pgGIvlkV%2F2vE4G6QGXGZcFk2pHYBe7vxTopdHvly6TAUkK2xH2RAMOKfDEvsfmeQ8Spkc5EHGu1ioG%2FLNIc5%2FqLvoNPF023OTLLP7tLR0Y%2FH24PDTxUDdaKQ3PaO2cUAygzoiV0d3UNh%2FlfvcfADMNGx05SmvDVHfMD4lIVg3PFF1OUfCUPowYTdRVNdfAkotBr7t%2FICletGhXeDgdbisXqFqaXh1tXV&X-Amz-Signature=d21117d4fd2fdfd136177f6112fa3c585ede5c6daa3c082763d92509c0769ebc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
