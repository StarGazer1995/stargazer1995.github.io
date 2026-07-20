---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656OTHBAU%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T083512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICLHhGWDqmINzak3A5es6g%2Bcl1HCFrNcHU%2F15estYgrYAiAXO5EqKBdUhl3h0XMX9CekRCNlTvo%2BEZHTYr5gKv5FuiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRKP9u4e7StTjwwDIKtwD0wD4RH6ByWa9FokIzIRtMKexlr%2FfDDemukCXAKu93Kb35lOAmKGmVXucGvCyAaz%2Beex4ETdx6Xvc6YcpZ3hRsbI2MbHBZv4P0ueTdyw%2FqEE3WCz8ZNXEm31ckEZUtkiYJq%2BSXpMhnc8A8lyKkYO%2FB2aB6PHBfhb%2FYmnfn5KAG%2BcWoUUI%2FazIFrIA3kxhrQjkbsukyI41THCmJ2uOWZFJx8lPrFdN4KDBmJqTjS4vrcXtl5HRtEOuSEtOSKO6TmI26MXWQdUimMLLuv9QEOmU6XYWce9IJTy1DKcPLyeY1FgevXz85k%2BW3XuATr9xfxzIGflUZ3umCov2ldlJwgoSnO%2FZwV8YbyoTrz7iPiwlBM9btLmTxhANPGOE6R8ecDPYRr%2B7D5xyM1KXAmevVKxSKhOJJQ55dcVjeH8pl%2BYg03fvj75CIKpbXskbbvDiNSmuOWXvOdVpGAlQrp8%2BwVPxBDFgeWsWx3fBPcwBVtqIQhdJTY%2BlrOnFRpNn7d7GPfThk4xxu%2FuwtFNNs3aFrlDgA3zLEm5%2BdkaTYVuIL0xF2F3HaKrsdRS8CPC6YENzkOlEcb0Ix8cg7oZKP5Aa41rOV4711Ho%2B6Vki8cIu0xRzvLsgAvO6TEBiJKR3eRYwgZ730gY6pgGzraUkKy8zIrX16BsLX8sPgdWu8Cwq2IVIJ84g8iEQwZPDmsABOXR8Y9n7YvdbrXBzkYbfATNE0efEUW8dZZfXgH53nTR7E7ew2pU2iHgEg10PJibj6hzrxEN7aBd4B2MXglospXpT5P5QbpAsOwb3uE6bfMKbPUZ2eAq0%2Bcm2ePIv8a9m9pkKD68OGCTYlNccHvB6%2BubGJTy3RSySSrZPqSUbXGBf&X-Amz-Signature=c39cd397226c2e762b123ef80a1613c7384a3866516f2d155355483dcd2ca3a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
