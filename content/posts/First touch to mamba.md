---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TK4KGWM%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T181233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIGzkfHtbG3tZnEwaqxA3pDmed%2F%2Bgrd%2Fmyv2PwprJlMP1AiBFuxeUn7VD78XlE7E4h%2FsxvA0vNFgBZjZphAi5Nmo3Kyr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMWxu0nYkt1ZKXmwEQKtwDVCxaLjfcHibtoiHojNGr7Go3qy7hdk4AWLpyizJxJrzPGlII1mDZKGDSWUqg%2FDNb%2BYBgeCyJ6vKjqW8kHThVjvLMhS8zRLUKCKonPqVj96NO6xWsrGd7Dk0YjyZNfdbTkax%2B36%2BBywPOZ0Co0grbumYnEuCrqDz8qrbf2dai9FaqcIr17JinDV1nqOlCdXf9r390HAGsGHnnJFiir%2Fvx6TpIVD0tQEKB9M3H8Tr600DMcrqdffidodb5Tr0ovvo9SOr8XubW20VJunmQ8bSC7gIbjODulsnECCrtJJxIkZciYvfwjLGskPS2ca3CsDlbMWRjy%2F9TJPiC%2FI0ZuElHBkpHI0jIue4P85TwCN4mtRiUNiJeYSjR3PMlO%2BCu4srbyNvqFA0w3b%2BcHNVwIQX1IdfgaXWvFh4W%2B2tFkgxdjLmiVB9FCnSvgv3XmXpILsFbXcR7kMwLTcJvv0IERPOwtJ8LZTCjXObxtiFqj%2Ba6Vjkay0GTsOeaZLOjKfkO4gOjcSnOF5rpstDJS1BjBt6CQIMn0M8cLNfC%2FwH7dbnnNh2fy4%2FyTcEP3SJ4ypxcRTwij2uOLRAuQCnF%2By2FBljYqgG0UGC2psgjUuH9NGSpgyc6hYGxIeRYjx%2BUqX4wls6H1AY6pgEcztwvSmFe5Hw%2BdL%2FJu6Q9rjJWe%2BGBcYPjSdBp5CoFtMiEgHTui2%2BZA%2FKWT26rR2sKGeVA8BIhgUsjA%2BDcT8bwadMEgrufICAOch3j1oocb7inkhBNffyY2Sp1nfh487Na7KnKqzF383BpNV54YKa3%2FVaRxDnZ9AJeWusmQGCEEaakolZK%2BAnv2Kc583tXQ37%2BlYx%2BTk0J%2FiT2bUXA5zVrjsO6eHul&X-Amz-Signature=02fd10fc022a33068d1da606270a13d801341b08679da434a391dc2bf5aa23eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
