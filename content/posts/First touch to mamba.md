---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVEADPDN%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T100154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDbi3miWi3DZ3Ww4mSyNg635IO3jtvXdyIyoYXdciMp4AiAg6NIPBG%2F%2BdGXPB15TnKbTEmDEbFmrfnQ9QGkZYO%2B46yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi6VXGymDc8Hx22CpKtwDRAvA%2Fh15vWRsrTWnZ7an8DMei7BYgSuuo3pUC%2BIBr6NZEFWbcVez6ev89%2B2a7OvRNOGOy8Vkh2jCUVI4lmlJM7W3eVnW7YblUWa2JtAWrQOYe6E%2FoTYZOL%2FSu3JJepx4ai7UR%2BiGVyUAeuXDjt%2F3BnrKtq%2BYCJRC%2F4HC9S%2Fnzk4MGxTXFrLRI3SFwTf2uCWq3cZjgVqrlBK%2BC10nhbjkUDCUOV6r%2B4aKfEb%2Fm%2FowELaORa8n%2BFZKrT4TbViy%2B0fFqgPrhJwedKGeHdCfnkHIrCevnfc6%2BSwdBmpnhz1zgXLMkjQSeP4H5C47z2fEHjO5qbTWbSoEXwRC8IO%2Bf8cyN1mVryLAGc1ttIv2Vjk0Ds0ohLRD8m1uhUq8Vpg4noVFoNgPkPFktIUdJ%2FwK1s3JzNybq9EE9u1HZDllYW8FbFHJlAZi63BMB4b3qwHC%2Be5LanJKbajFVXrIC2E%2BAYxu0Uw%2FMCQzw3Q16%2BikNm0PpAuFxpeVJXaBLEZoeSVBZQDY%2FzU5kiDpm%2Bzvn0FZknOx04ApWWlmKWp6G1TURVfOw6zMWLtVmoun3sPpMsiATFjVPf4wsV61OiiRovrYg5zaBF%2F219P5l2ui5IvgAITW7AHcFYFSVbu85AZglPkwx5Hg0AY6pgFSwNpLAHWSeCDVT0sc2SNrD8kaXm81ZEbdURPH1ABLi0YzGRDrYrYgvIbfWSP29OiGIar1l169W%2Bb2iJ0Fws9YScjaYwtDDKq6tj7w9Q1DWq817I4Zw7Ebhgc8COVA9BQ9yrGO%2BnpvNU6fXKryLx1cKTNEtVhYaU8OlVljKabtmNsLJRlUlfo3oRbTWhdH8pH3zZMEm0BpZ9PZUXAVpgEXVOdm8rCM&X-Amz-Signature=9d7c979fcd6b6239e6d2089e322e88530ac32da803ca7a872afce575c9ae6407&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
