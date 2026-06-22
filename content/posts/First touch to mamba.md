---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OHLTDRT%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQCVkeOsJxws9IrA1GmiyWoYr7i5cqmFc6gU%2Bl97kUP02AIgIvehzVq%2BoiCN%2FBjoKmmAsW%2FMYdLLmhrn7%2BbJGXWNJ0Iq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDEBF2GYJCXNd2FgkaircA8NlAS4b0wI%2BKlSz5dR0LbyNXY08ITQqZWvqecmGLq5kJQTFPhFsvYS4APqTEoJ%2BuAAOdwz38mtJFO7BDCr7o1lGoTXueHsuQDxvk3DRfSP%2FTOpX5PnpTu07gb1E4VMzWNMkENBIAQUUYrWEVCvLGOF39Ri7RkYfptFjphAxdwhFSllhQDHRVrgpCHBkyhlv68Sd6ZJ2Or9M9zwBXIZ%2BjmbhWGhmWMOi3ogNgE10pF5TbkVOFZ%2Bj%2FNGaE0A8PvFFrLtS%2FDjLmy4oOINa5f8P%2Fr86HxX3P%2BOCPe56Lht5BqCf04UGrCM%2FI3SjzVxW%2FjT0Xc55uV%2FjxdZpgWvu4IfbPkMxopq2%2FwYGDwxU7zzQR1xuCSlTihImoQ0TFSHM2egKb%2B3o48RiVnAKUFMaWbqNX9QyNVE6DQdmmmLe2qanHOWv6F%2BCkM2rWlkM1axOaydOGk8zQzTlcX0MD%2FjqVxZxZ%2BcgpbEpJNhdne2Ra7Mhu2ca8jjRvI%2BOQkjeHdvPLwjw86meI7mX%2FRu9do33sJouiIPALr%2BRFRVB0EYFKUcyl1ip7cTQ26%2FCHCiz23hhAz1zl%2BkQHwfcKCD1I%2BG5CZt2EUKg%2BaeK7HoOSF%2BfrGZbs5W7tkXkszURXVe%2FOmIvMIX349EGOqUBDKrM9GRoB3aanZ02IY2oxpnpXSDjllLw6NoPceD0lcqWlxKOo8tPQIJUnEv5jRIUUiupTQXKSpZfqMexttbfDf1kyYi%2FT51YjaJMblTN0TcDN4TUNRrGsscWczdAfxyYtR%2FsUyuMs3aF7RRTg6UBlhnkOuPBD3WHJs%2F6K4tY%2F5lD%2BVdXZ%2Fa9pXeNQMA0yG2onXvn22hQlOxH4sEQlAG7Sztmeoy6&X-Amz-Signature=8300a014bc1548f92b9741f59b3cfecde0a17c6d1a32534befb7c7b4c22e72ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
