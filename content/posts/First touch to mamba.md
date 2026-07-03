---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CGC7SPU%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T054216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIDgLnnlePxu%2B9ZJkwrEnGjFjTlrkxkYr%2FQ%2F17DwBHLYvAiEAtRlNehsJ3aIJGPJkrX48jp2YeNukI4QlvX%2FyRs0Jk20q%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDEYsmp9PA2NzR2o0ZircA26%2BdZKYAmEsvarDFCBwgdOzkUMy5grXIthJEeuu2xsz6n62EWaHpoukGtH%2F%2BztEuExQQQH4Z%2BKnDlaP9llLP4QG%2FkaP529rU7EHk5lDl1GPaidtxh8Wb0V1r2dqFilwjTZFxIP3gYPeY78rZEeW1BEQZlBdO%2BJRLZkbQQaz6vhzrDszMXr4a8R1QYLXlMjfWUHpGyMZxBEVMcXnkkPxAt9aTOqf%2BBNqIs8tcXFvGXmgbswPl0FN%2FBOQTkeKagFZ86YOuELbkc%2BRWGaUItH5S8Ja%2FadKUGAE%2FFHCCmILijMXpI3TcQQqsQJWAi%2FE3RnzT29qbOPBn33U%2B6jF%2Fq8ydh5Xcv59byJQG%2FE7pwhOokmD0QC2LeebwLjze%2FJjjqdFaDCM7aEjDA%2F3vpdokuvrKPjGWdvrpqkR19dT8J3uj4iJ3e6LN3RLgG1CvNDIXsYK6GU%2F1YYE5h5lNj%2Fq4VALs6y9d7gkKVnKDb1kiz7i142CmWcr6Ehxf0JknMOabGYwmsCBg5AYXhna1J7QjScdmqfC8jWl6c2p7Gjbk5Wi8DfeDdl9TZwv%2BlfOakGNvYpBnV1dgUWoqq3WaymCeICiEt245vAo5IDxJqLAcjNQ2DXofclHxJ0qZZYtditEMJCSndIGOqUByXI6NStoSCHOyipntDLoeXnEk11Qk8ta70cVFf7Ya9dIHSSH4FvMdtCMB9K8QtIfk7TydhzRH6L8dv6%2BZCDu6LAWhJXsNTwS04iibMzShDRaADVQGUj7tjnvL7BYmOYwDdrAGdIX7jA1Q45vzJpfyxYKb9HeGL3Un4DBaM3PFTZw7%2BVeTmHOUal%2BrO2liLawFzUld74SOMeVhT3FwU7Joh0k8fW%2F&X-Amz-Signature=7f8364570ded66ff10b5d89079246aeb6d01f6535b27b9429b0ab3bd920a0ec9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
