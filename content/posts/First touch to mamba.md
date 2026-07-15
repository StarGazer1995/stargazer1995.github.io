---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3CJOCKB%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T224655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQDabhl5h6LyCg0oL6j%2Bfhq4FYlDQNvuDC4H9v06S3jUTQIgZnlFGQMc6KdwEHbvUhIaV4%2BYJFeWcnDEHceDjv%2B15jcq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDGK4d0Ssk2eIsIyc5ircA8kXPCesvYbEEbK2ClXi9dn1xaDXl3%2BYJBxUSISzYrlRhc9j7%2BpBOmTDX%2BVI7HDzccz3BF2m%2FG2a9qV6IV9iJNyJQNGYDbZruampQ0uobQ8Od2jJulHuxCIrgK9kiCECgISMl%2Bqcce%2BXstnAyPj2MfMKfI1r0G9FVuO%2BDr5lVuNzalV3DeRzSfA87GjV%2F3PlsCGXbo%2FGrpVI4etLo0KSfKK7KfifqFWG%2BkP8UjPFKXHBa7hjhqWV6m1GFaHidXMeTyY7o2B5KVDd7%2BC0CsPQvLtnV8tNbt8SuGRTezXdjstNLbY6Kso7FM97db64kJDa5NvH1t5f%2F46ljalrXW4NHs8RuAuizrauREFvJTNeTgmixHRA9nivdaRPeY0tKjdOOQdlTCp6VvmvcQVEiMBM%2F%2BS1SiDt5Eeb7gWqSQ8SdRQsoGK7rSIO5pWwMiz2cPiIpNs9WJKQLwX1J7Ig8qZExraQTE1i0vfh%2Bo2TICpJgNITCHC3AoIfIMENJhcxmVVftCPLznGqyz4pwA2oykbScjTSa8jHEihX6gjNM1LLm%2BoxMQnROcKWJcAWnT1isQTXwGY0Ej%2BOyCyfNywcUsqAbXbQO8V0t%2Fxs9mvPw149tpvCMCZnK4OGJDNPl6f%2FMO6F4NIGOqUBM9lawYgCQnVJRxINCRaf7e9FnkIm%2B7rRKzCGhIrdiOPFxyckyr3wkYlJX0LHsx0pTmVTIDol8zEn1cM6nWHTfwEdLoYGIZ3fgWvhHtAMPzzKL84f2XjEAQ5ai3Om87nMNK5vgsCFRWieRf3rXEDCSUkfrxPhB61omGH2mH%2FrBibbzmfqAEky767tetOv3wTI%2Bv24ptprbrk8T%2FelGHmWtrokrTVw&X-Amz-Signature=52751d6dfd66c83453424b1ed84af2f1d074604a3a3c4f72e85929a3593a4750&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
