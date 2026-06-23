---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZJWZQ2R%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T105336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQCwJuAP8lAc55mmuAF4vhkcvHy1pQUzY%2Bdx2Su6H3MWrAIgScCPZaw5%2FxVGMnTg2D0A28HevWjWpjXvGPRuErj%2B9f8q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDGAETTuL4sn8mbDX%2FyrcA0KZHa4oMnHZP2tFSaQjNMmU36xC3egAkr1H0lLe34rdg0%2BNArj9Y%2B75KfVtQAUtDKamNQv0C6jq2tN6WTbqLDVTAQ2XC0a9CpgbLt9gf9ixJdztzQ3PM3PkJrX3BEWt%2B5IdlUe8Vy5Z2HKqmPWEaJig3NLWhwOP89LMYRWHehZTSnB8x0J5F1mk6TXCVqxxXb92ftkKT0Jz%2Fg9it5FUnanm%2BNaMmxIsAKF4PzLUcWIYyHJdoqbJ775OVtYwkPBHq8mg4KIA%2FdMMezndKp1vAg53gfYicYQxUJTMZ1TYQJ6vH17OGub%2FrSY%2FhSqCQ9i%2BtsALvLEZdS0AT4JLqCHXnrARIj%2BJ0CkEAhhhTv8loWQk1URqs8lOy1ljHHl%2BpqPdpssqa2NCc4PKjgSnYlvOjzm5YdRj8lgfNciSW43mgGjPre%2BJFcrsgidgGKMDRLXUoRACAEIfGmoA%2F%2B%2BqV53cZ8POL4HFSRMqlrM3gcCSLTFjnUcbtokpP8q63OqSVfBweH83scc9MZSnzHVPQnx9CkpZl1MwOoAi3wj%2BQXC66BLe%2B1%2BsMeeFFEzEsriGaIpSg8Ri1%2F9ETvLBrYcjxSKpN9XjKobcSQEVSO9nrJeVHAYmtHHSrFdHRty9I3sPMLmf6dEGOqUB6NLadB5R%2FKks2OrpIYjNCAY1ewFoCIao4IYrVO6nKALlcPT1VU92Oiudh5kaQfsYdMnsq8MkH8CQ2HLG3B7rNAEaZPrMgu24oiSFboDhNlUd2DSOa%2FSPrkSisUQEJMDWg0pM%2BFzlNCTzc76BlneOhenI9nvepa%2Bk8NbXSx5ifJJAT6GatQKcN7h4yYhAsdOU02OzSHnspySebTyza8wWpiWgx1Je&X-Amz-Signature=94accdd37b1eb8f55a2642f6791cf4530e73568cb13c335bc39fa61695b4fbeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
