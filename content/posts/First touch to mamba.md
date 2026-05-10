---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVCPEMDC%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T014800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBv68CqUlqYMZ2qztgmJUpYc0nj9hkgzN6pQ%2BO5hm2%2BcAiEAiAqqSH%2F7O5Sm1Si1VdPpGSOxRHpKvNLOHC8icAErJ%2FgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM3fMxhTn28ILF4pjircA4tXCVGllRSsF0Kpbo9q6IuE4zu2igkfP33B0kY%2B9ysSmLwgaMzJIjFF5dIA7yh5ArcveyAkiilb3rOrv8j%2FfpZXWQZ87hM4UVHhuBo12rybu%2FR9w3Sm8%2FzSI9%2FlcaDu8cgwL2leZc04mahWPLamVk1RBzvBAXzx3pliq7euDAmjRYN5v1YksJrpN1dx79V%2Bb7snEEXFsgnFpXuJx58xv1Aj8MhUDUpNzuOn4ZY%2BI9RaiEv7ou7zTWIpWpm4Av%2FVAyRlAIbo0%2BAo5Q3BQWc6%2F00h4C9dZ4OLOVXE4YjwX5qM7FrwWdDA8%2BmEFLRK6WDdc0CUsTB%2FGnXiDXtis6ItS2SmybhRteaAuqi9bdoXkVpo0%2F%2F%2BktwCoqxZEtzYyWmQ%2B8XJ%2FcNQck3ZFQXvBCYMZZ7q%2FbOxv5P7%2FsExEpRwkPoB%2Fe0%2BgjAoIYOqwz%2BoSB7eZP1yV3%2FyLRFyOZZUuHkRq9iuvKWJFdrMnR816JFL3LOCjfN8Rzrdgd5uC%2FImch%2FCgHuO%2BoHIlZrQWCX7gZdzHc0pGi3zICzIkqOIYvYNQ5AiKfrMw2vgAc%2FcPYYh4mJ8%2FBajbEt8vcjEsTxjqGZaB9EQ3lqjZKJmfKb3BmYsWeN4p7dW5wkYx0%2B1zKNUMIe%2F%2F88GOqUBPC%2B2arg%2BTyZ0vwlvfh%2BB6rgrL0bSZq7qkRG8fxKQqrOAox5JQxcqiT4bKfDE28wK%2Ben5HaZRaePIvdTTld8bDNG7sul74sneNfxwX3cKsbaK5BpTL2jVx%2FY8WNCbJWMODS7wIpGQJOJ1kNYA%2FD2VROGQD0SW5O6imMM4NPzlEVzw00p25itkPUnOfuyRBKGw3ayZH4bl5MPViiE9ObZMo9Pp8gqx&X-Amz-Signature=951f2b5cd5448e751d2272df100174275c8d618bf95dfcf45cefc7a5e3df3445&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
