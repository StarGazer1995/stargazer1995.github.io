---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLKTENSB%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T235955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCmH%2Bsp1a4qBWHo8tbEhzeqlEzcsbE5PYATKUSUjo9TGwIgZJXcdglNgR2jsxV42PjZaqY22J0l0OkNk2R%2FVTdfgwkq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDDOLDQ%2BUZM8znFQiHCrcA3aZPCUrtvZU4%2BsP%2BofrbL1bsmm8rSctUoU34P4cbMzvbL6U1CZCAj8K8EYmcZHvdNq9qezz6HGaPLqh2T8cazJ20Y5kulfKcbBzLtGWNp96tXvG2LuVeghsZoGyoVYVN4XKaU9Jxj9UAZLuD914ItaCqD5c5z4ODHP0GxRD2hhPW4HNygsmxDIHXrDvBCluPjkBjshQulNmNN9VmfGHCxBgYIaysZPH4rgpFmio4u3it0w65Q03jm9fbU6msjwPh96JtOM6fpOryjAlX%2BSWOuUdylqtjGjtJtqBYuVtN2U%2FMLIH7yQ6dkVK1rW6mqPJpO0gRdMw0T7G%2FkyyRrk%2F%2B3%2BUyNBED3yR7MfVE0r5yF2jwa5T08V5S7702ckf%2BSSej8CXecipILNaUmKlr0rL9i1LtaJEWqMxF6ENx6WMoMd1lZhQOS%2BdO1DsCz%2F%2F7b%2FrSVB%2FCHkFx59oyuITXyeTGpJ2P%2FxbPuoyXT%2FHHhTCbP2gag57Dh4udP2CHbCG6I8MSll%2FWhp63%2Btw0mxCv3cstCpRy4bvfTxWdgToeiSlqCTCIZAcUASP8xLxAOk0IkOTiAF8KccilhrXkPQwgbPi7rcc%2BL6eNAEZXpsW9%2FYPKy8fjINfBqOyAC76%2B4AyML6j4dUGOqUB%2FOCPCgA6MIPexadi1MIPTeoV7348tVT%2BIEFMI2bjdki5v6Z9bh8p3mNWrILGRzR1u0BwNDfH6F3KqMHeB50ch9F2zb4kk%2FJ94VMTIVTORkVJEBZ9pqagZesDkr4m%2Fz2aRSmCO41txLwB51CpM6WoIDW%2BHYIm3mJhuIrq1MQTASOOOgtDVC2rnDB%2BjBr6JqxaBA8V1oIv1cC0npYEKxtmaZ%2F9HdEy&X-Amz-Signature=5a189f21babbaf7ef7ec2603077e8ce484f74383516fd86c1e039c4da833cf7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
