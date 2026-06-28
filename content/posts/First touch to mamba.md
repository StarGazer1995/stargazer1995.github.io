---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466356K6QZJ%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T165708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf7cuf4lIl1d7M9Pj2vNMV03yczEl9tNyDwz8dKtFkoAiEApg4D%2B67gZs6Vw%2BK9YY8%2FQO009uoa4bmejmLqBjivVxoqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAl34PtS3iPTdi4VYSrcAxtgSOTvFONd2KnxeXZc0umIZhS7pyrMhO3cLhpdcAPxAwrlBpHwnDgTNbO0jeHCEZkrN4ypmzVW9Nj%2F1sU%2FzqnJFtE%2BZ2p5xUjXEza9bP%2FesGhkz8gUog%2BDXP4GPXmM6CCyJwhV5jc6Nqj%2FKM3PCGxvzd97vCGHzNtx7KhUaVRnlWN3sDagChJw%2B2f0cKkoYDDoHKvKct5jDek1JAQ8yOwsDwM5OWGv63Cnp1qxhG5ayVlie5wj%2BYRr0hTT8yQTN0Z41J6hr0SmjY0C5nbx%2BkUvP4PwA9GMyKaICe1XtRGd1b1l2VHhUD%2FN2g3eDdxpyfsk6T4U5TMBpRvv5v3SzH7aXR0VOypUFYY%2FSxI3FHC0FIPjiEc4e8akUqKefg69tV%2FJKtH1Nnioduj0%2Fy1hgWma7R2hO%2FwZMhwMZ3vvQM4ydIZNIuLW8kWtWcrLmgAdYRF8zkPKhXsYoGEm1SB8rK6STGPuh%2Ft%2BAwl%2FxUc4RMoRU3XPxKb7tOu4jTR9TTNiF1sV4ytsu%2Fs9NphlWHZ7opPMUlX9hvDqbXJmRwjNZb9%2FErII4QQbsiqK6eqc1cyuyKC34je7OpJUG8gkofLyLOQF3w2GkOmRqGPilsNpeaepV1tBlaCOMEf3GFArMK73hNIGOqUBh6fjuGna4IpBlvLopVj2EaniEhWU%2FodG4A3bilmjoKUMsnlbhI8THxN1qag35JWwcSszABgnQFp%2B0TnfQBr2lF1%2BRqAHJP5J3y0lPnfZYr6CQYL%2BZOmr9tnrJ15YVRCktOC6ZPiEcQcQ5uXbqqkMv2HTvvxO%2FYiit%2F9mrCaSa7EkMkOY3WeEmtgMVsGBm35USF5ncafNM8S%2BcX1JxJl3XyZ4G5TR&X-Amz-Signature=0a03c5f4ba196d57388d40a7ee833233963a28b5aacfce47637ca16fe40de199&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
