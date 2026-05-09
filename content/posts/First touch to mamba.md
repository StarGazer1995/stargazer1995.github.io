---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HBZWKPN%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T090736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIBlN4Y3pZmHM37cz1aOn2pdWQsz4spJqgEzVIp%2BgU298AiEAxQ%2BcB5xbTjfNJMdHv5Im1W2i4xSwwZdmAd0cFlrkesMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPNzfp3cLNA0nU6ksSrcA%2BT%2BVuZDSqnvgeAi71WHv9skWVXRoTbQz3T1LULss30MnYxaKqIjrnkXRylFAphRSKI2rvepjaw3TXfzjSNTB0G2KaE03eAk%2FeLZNbY6F4RfSr6auAl0vXlZjJMiyseipVK3GMOFJdyAeH8z5b4b56yD3RbXX3gOfa%2B5AMCiZMHhES1Hemwn9zmmhDOd%2B8xLtPaU2eCJkQKwCQRLR%2FwEOIDnBT8DEDI%2FUEh46CQozBRFHgu3mK%2BW33MPnpEiBw3vgPKSy3nUH6Z%2Fa4eXTZ1RiNc%2FHbD%2Bz5Ha05bAEPyADOhiF6ZtMb0IU5SIrXWTheqqKWigjQ09sMJgJLYjfABU0zVeAUamXyUCOodRKhWwc3PiK%2FXswjYO3i8%2F2m2YUOjA3R7Mx5kQaaJtt9giEyFAtgKHDuaTSWPWGGwGvH6Zq3z13kY3YrDnkyd6LA8y9r%2BpkAy7MCbnqlXD37hrL99r8Mprw%2BGc%2FBwpe2AYeLTeVmX7nuNtRXttIxhq%2FTkyLNxC%2FdOKDEbHgS%2BdQ385Iz20oug4HC6vMjf3qDITeMdd2sa9Vud164ZiXTKOwg959Z5o2EJ3BDO6rPjiqrZvwJd3Zw5ladRsM937ob0YwIAHYTyLC7QIyIqG9qjRaXffMKLX%2B88GOqUBKk8bWouDpXtBHOyQw3yv0ixCPDNs8Odhvq1lOeUywPULE2UKPwGyx816oYQ8l6kENn%2B8X51ITcr2idaiRmWl7VpY5eWGyQepk%2FVrFaSZgrSkOosNplAc9uqXO67j0LEZ7t%2B23mrJW819cDCfprqCegBHEBsLNaR2biS%2FCl8fvMdPbRFCvoqAcOiQ8NpFdv65ZgP6AXlcpJIsUWwhmxlKxG9HPVpX&X-Amz-Signature=f62c2052dbac0b431165841bf1f951d413741e33effd0b2720fd03462bb1d773&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
