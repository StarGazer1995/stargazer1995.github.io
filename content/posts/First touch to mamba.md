---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YX64P2KJ%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T080817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClvDpKAmMALuj2RSEV4%2FbYHRgpgf%2Fs07DzHMZKs5m8zQIgflDbh5aB3se1WvucO2Xymyp2VhoTTqZXKg5DBcnKn3kqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2BDNzOuwuyc4x8BuyrcA5GXdO6XAbsMZrnWPJgJL0gTNFN7veuwC5zwgbwVTSoQWzU6fukZCA8EfYZT4iQzN%2BbZyEKtPBwVdUTwjx9W50qukW%2BDJmfTGe%2BMpCASG%2F5Y35V7j9SW6Bv7bAZ%2F%2BP3lymABx3lULgyd69azuGwi2tSqvNNDl%2FvpNbLZLKw23eliWmvEUHDE%2F5R%2FhgGjEiumgV2uZKQBvu%2Bz8tSg8q0v0mHshjks6ne3G7XdX6bHA2k6%2F%2BlCeSS18oHmxyRmPcUOJTYrvSVS8P98gv0DClNWv2xswfag5tDjjY4eiKsE58l4zb6gE1oOq%2FhspEejRukmdeqfYPs%2F1%2FPZlhipp2vknA9wLPJLZrd6S91UgVssR0C4nDvNzKuwENlPe1FC9oZQ9Iqx2aZd8K%2FPSEE6BHzHKRnGrfPM1QjhT2R2dl8gz5w7GKwNLdQ63aIU3Id2hny%2BtpZJDR5gL8PWkJFmZUQz7YBBBELu%2FxUzAXS2Sank4tYjmxP%2FvzNttSIaB%2B%2B%2FTgKkM3xK3BE3iFBY4c%2BQwpPvr7tK2Ll%2F6LunzaUj3M2rJyhYJmIKxzKVKHWh7MWdcglv5ZTUtSQEiu8e%2Fh3801gMlaUFw9rASsLXB8P8MzPxIRELb4wd0Wf%2Fag26sJFSMJ%2FgpdAGOqUBWyfjqZeMPdYd3DJGUNHlCJUAk0O7Sbx3Q40AfQmVSup7IAWRW0MITuLd%2BpbFbOF3vbSUraW2FLHwkpjAu0gJWnbUB5Maeo%2FD%2B7aBxiw5Ji%2B5QwuYocunGNuWfonwg9jMHgi0MwqQHAQJazArTKYBnaZDip8pLBEWrA0T9%2BoQcBqrwzuGC9UmHwf9HGLGQd%2FDHCLCMVpnAj0Dqjqt25Cfr4F030My&X-Amz-Signature=0ea5d3763eda036fec5e2611172e6ac7ec0c2263da27993f28bd4c7f7e02b160&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
