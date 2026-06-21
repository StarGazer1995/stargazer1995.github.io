---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TJVHSYQ%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T154504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAyXUdS5TBqMXsmhe5hONFBS9IhkfR3kVkcBUHijpAipAiAkxOdZoSc5za4s3xCGvDPTm4dl%2BnB91KTEVYnBKTUcPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv4ud%2BOVQgX8CRF0yKtwDdse7ZuXU%2Befp7TcDVKZY%2FeJRMGQeaP%2FhBulQpLzAy5w21fgtL%2FA7PlFAZfjqDBejfWtSMIdcSMwuZmoxCWVoLCXeRVL0z9V1PQWP18le0DTnu%2BWe7Ie8QDHEXD28OCF%2B7iI32Fkyvik%2BGCLOHQpeup0bS6gJLP1TCaReRAzxu0Wzdaj24rnu0Oz3mAs%2FQZ7ruu7o6O06fEwPW3xAR7T5JeEeEkDzGa%2FUsiK8KSvad3lF7fgY3%2BsKvddkt8VQGrq4iqf7Ouw8zwHYFD1Lwz6ehJU02Va%2BVebFVpizpfk%2BD3NEO%2FElCBqmhaj52Y2q8XQbBJryk5YLAlAY43gTfcPB8tsV16ypmm5pIMeaT%2Fjux8x1RYGZk0GnWzq9DeCBu%2F3uBHCnUtHDLAwSM4jDndGpXJ9RZxfmVes4AJxrpPriCCdy1u2x9nGiFmcdeXtQj1jv6IyB4S1r3qq5nO6MGha3lnw7bXCV%2FJG5PbEEtNL%2Fta%2Belcco8cHp9yC2%2FGvBFodocUx3RFENSX%2FloquDMy2qYXDaDayzU1pPjrhFVfhqRxQ1KsuQmFUslELlICg%2BMpUM%2FFcl6D3VpNrn%2BLwkF9HOj2m9KOXxe%2FM2ksZjehQsRmIIOeYETzeRmxcG8MswzqHf0QY6pgFW6GC%2F7%2Bd%2BNEhVctOwsxd1LhEEuKXRizdSfFzEwrJ216D%2BQgq0q%2BQ7yeEzBhHHejIv05sCex3tRgUBFAnmb7DFol%2F3ju9531IADJorXWvgZ2WXYUtXW1hdxXUcXr1nvP18Es%2FGoPsqsNUGOue3ehwwQEb3yU9NdujMv6RTfjMC2mX%2FNqxU3B7AlpH6rYDhbFvRLqyG2lzvZvi6pKfygXP4TFI9kMp6&X-Amz-Signature=566bb202a456953727bc64547b1fb60cd4a9dbfe1dd0d18be91fc64f21d459f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
