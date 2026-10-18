---
date: 2024-07-04T01:57:00+00:00
series: 工程实践
updated: 2026-10-18T01:07:00+00:00
description: A first look at Mamba's selective state-space model and how it
  differs from attention.
created: 2026-10-17T16:08:00+00:00
title: First touch to mamba
id: 3fcb3b02-81c4-8172-be4f-e871d7f0beef
---

![](/images/notion/09777f15e3bb6261.jpg)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

{{< math >}}
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
{{< /math >}}

{{< math >}}
y = C*h(t)
{{< /math >}}

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

{{< math >}}
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
{{< /math >}}

By doing this, we can use SVD partition for reducing the computing demand.

{{< math >}}
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
{{< /math >}}

This can be done
