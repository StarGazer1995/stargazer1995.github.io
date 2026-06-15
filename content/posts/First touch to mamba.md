---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676WZECU5%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T153658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFl%2Bz4Dhw3cF5uHgrk4Qu9iqxuyC%2FXSnQgCKZwJ%2BCc8gIgHgjml2D6sqTpXAT8etKr%2FTgVSup9nU3OjrpCrT3mnlQq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDCfxr2Yvd8PBqs%2BoMSrcAwB05g074JPUOQgHhAELOJoWbWTbGK5BhuMVlCOOH3%2F9CwAjbem5q3Xa34D8m%2BC2Wzvqj7I%2FRKol3M2JmsAY6twJfyOTrIM1ueTOWHQc2jbNcQWECByNO%2F2iD1Ams9ydnTMkqLzdsjxoCjgouLB7xx2xhv5EJTkXXNm5vN9L1srgjiD2HCwq0vjjWFRaPYFe39SoZ54hX1ckUMOHEoDl77S6%2BetSiv7TjyuX7ErrUcoM6kXjdwnhLZy7c6sIEvkDxM8U5L%2FtzkdNAXGu%2BBROU1WHFIASKDEM60jfHjYlzDnHtqywLKXBGpf9hVn3kdwUzXhLxV0d2NeYlzO5zIsS2%2FX0UvTR5oF%2Fmc3cRi9W7GmxtztfQnRDy9fpcFc2HFaLHcMkN1tgI96R%2BWbJ1Pk2VQHx%2B%2FVx5ZmXYvxfmAjbUiKEtWwSydeEFgwj418z1dPYD9sm9TDoGlu84bb%2FHO7ojxlTPdPphxYZfn9%2FnJj5dwxgjIvavceD9WIzYWwOIqxq6unX2eZnsBQLZixbjrLtaYSynzMWE5cIOzCYglHuFcXNibaNx1mPtl3Ki382eLNB3Idn7Y1xaOuPXUvrvy0ubXxpgNJ4sKFT1%2BX4L6fDVpOBbckyCT4nPMJpjX%2F3MNGrwNEGOqUBbbn0fH8sGBBKElfLlZ%2BbtwXMt6tXTVSAUVBLWdSzuyFEpyhIs4IHZa%2F2oIrsP2HuqC2%2B4ZKyrdqxt1epWRxakPokv3w1olEjbXcb2GHrzkWiqyYXpnSOJogiGsWRB2nVX5iZD7I2dLdAWMHZL9GdKRtk%2Futgfp6%2Bqj4bnHubpmpDoJCH7mflmefXOWzM8Y4LRDPhPY9gZZNEvsbeW5UusSqpYyCp&X-Amz-Signature=1d030cb5942ce5a17769c64163b6fd72e9321d0537caf2c6c78f511b68f4de52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
