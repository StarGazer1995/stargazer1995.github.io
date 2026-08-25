---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WLRUOSR%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T122315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHFqm7hIIAbAOQgoS5%2Fc53haHfuIWAo2UMpAL9MEfSmaAiEAtdcm56xV%2FMyl0gFqkd8WuMVb1eXhVwvwDVxjdBf4HE8q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDLypeqEakCNk%2FsLowCrcA5pCT06l6OutnuP%2BQvSLadxUVLS2yP1437kEyj%2BkH9hSG7HvA5UZ2fdx01tJ1UJzgUvG4gNOqPLoK2IRXhvdaztLhLTdIEcrwEIW0MdB9nZRQ1dD%2BzExvUyroarbrGPPJoSrh0Lb%2BEznMSmEuPjZaVyuUdTSWnKah4nxfN0mJD8XTgFKCoSD8%2FtBn8sh2yTh429o%2FZ8ZPhvssL0QrtjbEhD9lB9njIukfDUjsJxPT8KFsbpXR%2F65qdBBdO2zDZPPkngE6akpXOfG6P4SYWCD1lBp8IyFSg%2FFYfRXBjYHuqMxcq80fF6Psysej5NBk%2F0qp%2BlIFZ98Q8zUWiKLI0S9E8w%2F7%2FDGxITSGOOy3Nyd%2FAIxESMsZgUtQhb77KEN7Oi0IY4vLimtHlcB38jvUkQlBbJ2Y4Hdd3mNpSwA014us1HfbSQ19zBVMC%2FsgtWHBUR8RtMhCwo%2Ff1Z1cLIWsJeiKd9zT3l4%2Fkm8o9C5O%2F%2F7AjSfMwr6Epul8umWrMkYxHmFBPoNG7ivoWSfXzErDySGnnAVTZ9YcmgmE1Lj%2BZqbTXR4NXMbmfwm4eLlEhKWc3hqL8w40vk0VYChqPvfJugFFaQLLHmu%2F5z5lMHXrBrfbTlH3CcRIjQc%2BsfWRnWYML2NttQGOqUBuxeZ24WNU3T7yck3H9YNYRLxh3l%2BLuyVe9jCT8jOmSTLousa%2F2IKgslvnbDzzrDwlm8%2FjPf4ufc2zhsEPoc5SBRdXiSI5ARPYU0Ka36uYOQt3OfWVMu5WXT%2B290uzNVgDVpQWQOjFtixprBqo6SeHeA%2FApnFihTd%2FdN8oj2n2zsdrzQ0uyc7ixLvsGz%2BHf%2BguAcuqFgZ1Lc6t%2FIr7EqIaS0LYQhh&X-Amz-Signature=08966e89cc312f5f25086fa0596a92a24886ed325494f2c224202a1df3987ab6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
