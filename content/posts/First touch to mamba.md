---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLWT2KJS%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T104817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHTrZHts8rTHLg10wvNhal%2BlMzYY2McdsrYNiX%2BlR3QdAiEA%2FhOnZjAoZBVNR5s5Z7uFF7lJX8e8VTLfDOUImxQES7QqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOH3YLxId2O%2FBgAZJCrcA8SKyx%2B76G3JVmVcJn7rBFKuFm0hIQna4foIaD17L2Yumosq7Ls538qV1tkPl5Qg9YWVN77W%2BOYsoj8dP8fwSN%2FibXYZwuCq2ZjTHcY46Rxskg3i%2BsVmyCKj88kEjmaAvkt6x3bpFA8TNDncrfw7Zq%2BygUKT1DFgUTLTzL7t48oRx9NXw984gFPM%2Fx5s4TvpLvESFBLVaRZz3SiTok71G20qi%2Fv9hHSt%2BSpausVXdM9TccThla27Xs%2BbSN75bPTbEOmFN1ONuc87kpM7Q0SWhhj2XgnawYEInDZ%2FmrtEe%2FOoz6Z4rNZiSdsYPYLgDgwDgn9mN1RqCXeQBG7%2B8LMcvrzB2qifDJeP%2FVBdMe5cs39c5Qx%2BiIABGPQ1X4SRfEjYp8UCZJLJkcqTUuftZf7uVnhkLMniRO2y%2BXOHwN5RtD9ZxauXGNIh%2FwVFwa1oI9wD%2BsSf5hhzhBpeZDwEw6oB%2BlLD2SEhTGJfEZkt3pK8508Pk4R8PPpPeqR6CPLGDaF2mJobdg%2BAmR%2B3%2Bp%2FPAmoIE1JIu9Rr2l1%2FYx28ivZg8qV3ooUthGByIviv815G0lL9VOo%2F2fpbas4OLywtP8fnQ7FLobeOFhA%2Fs%2BKVyc3pSfz5BJ0CGWnRfFA9HBXhMOa1jtIGOqUB1VbjwOGb1SxvyDCCixeTjfkMgpMXd7GWsUAb31LfSsBvtJlWDj73kmEHlDjlh3y2g0sHPFhBMqpn2hTEbPoTIwOOJPxOi27T3GvQ9imKO%2Fm60AZoqe9Rjee3UkJsaKu58SMWvVkUfoCflMpWLTLlqw9j%2BwnY4WfEep4Cq1By52lSjOrLjEWwbzN64uMzcCiZQ6%2FGK4aZHI67%2BEIjWAXFnaaqpgfb&X-Amz-Signature=c48edab05c49be5766baf578d462a2c84fb0435eff7bcb2219da226dd217c6ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
