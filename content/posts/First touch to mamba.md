---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXBJZYT3%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T021706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQC7JF0xw9xFrNrXVbuEfSIkO%2FubGDlz%2FTUrD4NkWznQ3QIgLa%2BHX94oyTw1lGVIBk5suAuxDzUw88yIAg0ZDYCIbAQq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDIxp%2FAeHzr7uPCAPjircA8%2BbJnUjS0PzUztY%2B96APM3BSE%2BGO8pNCyLT9auXiIOuaSbfWEPKO%2Bbu5ixRFBTBOTLC3IXAxvTZXD8H2VioGf0n01Tj%2Fo7kezXOebXf1nPoWpIf%2FHdPZyzLO4evPsvTS%2FX%2FsexKCWW6kEkVLXlTbGOf8uh%2Fu0KGeMgxA7CieF7qupEzq7OzrR4aqcp1Vnwc3XGKz7niEEJ11f5U7L%2BDinV87W29MaWDribgE3XBOlibukBLXmDuYrFVYYREn6MaUPWQmy5WGdN0g2pL1KATyeCTtErKOERbK89v6hXFAF7kRcNO3cSv0PvWxzre8mCIQI2Ada4kSeItskvAUOftv5ykH9QZ6vzHbFyHbDmS5tskQ38t%2BB66E9GjXg%2FkGbekwhH0v9o%2FPx6Sh%2FNXqBfkSSDbl8pd4fh6h2PYRsfZKsD5rbw%2FUU%2Bou0pgZUlZsQjWfreIPtQbj2rGPEwIHmLCUQciMEWPZshOh97s9EpGe%2FZaGBVnrh2VEzVq4KAzQWoBoVWbbMIcURcuuumbUNvRflMwLS9RkCWesbcxC59GlNx6Uvp2wiJ5fkw8OiuNiiNXe31zLAjEweyE88cDmcPYI4exeh141Vljs5jeJnsuxmFDnOjxD%2FunL9kBITN6MNSm89AGOqUBqwXHjj8bctQzNmcGLorZPM%2B5ZLoREXJ7tJF8jHSQwQmZuck5UXa9H0YVB2RR%2F7aWP2i0RSNbucLjVcqQJFQqCoFwMOdMHMBAmkUDcfWWyF1%2BOYezmQmIRAPTR%2FFllcuoOO6mqM9LI3Or1NSP6hqMv4cvCSKJcDMAEaP9C6xmnSFmQHFsFOvSLXc8fPZ0up0LobQBCJmM9kk5xukQ3aJpGpx7hDmq&X-Amz-Signature=5d8b6cfdf92b0d5c2b29403df0318674878aaebe65e7310f8419d136156d7a49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
