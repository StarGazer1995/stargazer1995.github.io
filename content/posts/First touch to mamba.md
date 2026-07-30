---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFD3XXBP%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T080416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHa9ZUjPstZoUm8mvjRrYvokoPv92bwnU%2BdaItlFEEq6AiEAvdkghrfYKRVRXZYBlDg54dwZ8BoBL1P8cuJpwyNFjZkqiAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOZxaFi%2FDGrUyyRDkircA2OS55aJ8CMCuMUuLgq3DJGG3p%2FuyzpDkluGcds9XoCm5btmyMqE6iEWR5OXgyNDoU22tdQtelMFOzAWJlqUm4%2BZLfUGdIDt3k21AxMiPcTaPXkL8qi0P6o2hEdDGGwBDl%2BQv3r9uuZHRsNovnHTJoOhvp129jOAh9G6lzzZWHOoXc9JgmvcbdvyvX%2BIchoZ5hIs7uTLrs7D4PxOah9Qw%2FfhfAVVnlgELOOAZJd1Og1%2BSd%2FdUrHsytIT11Mv8%2FuopSyrrTJI4ySqtlKEXna7sEuleC61mJI9si6X5f5QKHCTFN5YfHXOtxyB6NxTXVHEL880xocbO33pLdDug9brr0FiNtEDs8DU8%2FgHRxDtopjGfzuwgEN%2B%2FtSycBT%2B30GM28ATa9duKOh9HevOF6oTn3BXbRC6eapV9d2QFNfG50%2FHv8Sk4wfrW1lREbYYOuuCT3KVmIWRV6NKWPjkRdjsaoydih%2BrT1Gy3eoeg4UUzTmbXW4eC2bD%2FCKanC34AUz%2FabM0QIQpYZ5qV3uhPT%2FzVvyzmWK4Optu49SkhrwcoN9LfliDlR1Yht%2F2oMEeB%2BYpjzJ8JwAA6p0U3mRVqkP9IhBriyeZu9zgryIA1xt5MUGPZckuFNbkDBjLvtldMOuErNMGOqUBHxIPbgqxX8c19%2FlizwNsYsOP%2BO4knvce2DEsQ25pVBNOt2iK48f7%2FCzJ3c%2BVejamtcAG4YoXaRBQAq6fRSckV06DERivqYspUMccDzJf6kEQ0Y7iP8f18vVTHmrfd0hfL8%2FuXdm0egsLkA6u0AAtV7bdUik%2FpWbh4amSHx7Q1Hz0SD3FjxDd1PeIya3D6IOmDVaXjTXSwKj2z7VTqnWN5o%2FQaHUN&X-Amz-Signature=77c58474ba6a42080db461e76e0d7ddd69a03ecabc60bf07bff98a4429a4a833&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
