---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7UDAT56%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T225140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrUngHARgv6scnSeLnV3O3qAtKWx%2FRXFtylnt15nLCsQIhAKMYIaq7R9KIvDId1ReqcXYfg64Zx7fgB%2BdnUCBnIBdVKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXiiDa2eo94ae42y0q3ANFUNzjiy1qA7aZEQi45un5tOCTIDoXCwjLbSj3DyOWPeahzFeRjJiSYmJotIVDnIzpSQKA26FXSwXtYOCjzkSWwjLCfSdkgiLhQMxWe%2BbnQ2lBlBzuNZxa0euw1lu7GmCbACrBscscqA5c3kRsYWXcJvC0KgejTmGnUouR9n5mOfeZrTP6TxRMOwW4HdSyuECudl%2Fgnw8kMB2lJ%2FIlqb0H8fFwzYNHLRACzi%2FzR2QrD2LnDz%2Bgg2lrnHyy2tf1trP%2FJwvl7K%2FUqnJH%2B9LSxj6YON2NFsH8sbg%2BEFzmBbr2nI0MiQgPZnA0Ve7DMK0CQdXSj8ckSkT4YZVAuXK7viforwmM3jJrGbwKonv73aVnPx39MnixNlpph1BV7oRa2slG2dLNQCvL8EzgHTXqLNYykkVYmUR4FpWzcHNs2NK9eerUnVhGRLM02AWhds34TcJbi3THknyNKWbK0TKYSkpYCYQ5DIQxyvXnF53%2F%2Bi3LfRWMwYvhtZB3%2BAbxkPmLXX13bxL1lWGt%2B1rogmy4q%2BAPDzu5yzmO4i7s0AuGPLOue%2BTqAcvMhKhnuSNb%2BHnTt8xsc0GRhqR%2B4EbJqbWruzMmMRbbDW9kSUWWcRu6F%2F%2B33lDxUk9iH%2B%2BP5hP3AzCajfTPBjqkAfvAqURGt4vNx5Brl%2BH90x5BeUI9UXqHEVzT5EbXyzCOhL%2BR9GT2cup11m71Ko3zk4aZMo%2FWjjr9f5DCJwOSRJp%2BiPnmo7dQj409k7ah%2BOUuA9EOl759McRxtMCN043t7syZ0kpm4Ahngv7%2BZtsWdtmCayppu0zHzFEOPvZTrtDHrMAS8DTchsD04bluc7dCHwHlezibEibCd6aCeEgiLfhwPI3V&X-Amz-Signature=d900e1d7fc9bd8f496fbb473398073716d8ccbc3cbe17d2729ceb31a35c225df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
