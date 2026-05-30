---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDXYZ7XQ%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T185753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDUqT7XfcN%2BH5ruMY5ZmuqcvPfPKgwkx1gNu7ELEWO0LAIhAI4MRjLObVVFY5dO4bjhYb%2FyGlLLxaHeL7rDNNjFHQm7KogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyySLLU1YaIgLvzTpMq3APSfuOnbB8TvHnXXa77Jtf93zgRaE4ScJlGGcKDXmvEiYjt2w8OHeyEu6CzOEvr2Oa9sd9%2B6Q73bxFX3bAt5H%2Bm%2Bqn%2FRIoutE7KsvrrXIWzhEgL%2FDb6zHdIKXswHY86pAOjwdUn%2BFrHo2evu2aO5AUoV87uAHG1%2B5TeM7a0CiOYfdNIyZO8lH2HHb6PkteBpqkYptopKn6juXIgVjvVw%2BfdLgEtfetkx9efuf663NILCijEplLIwPlBf1oGQmeFGN1dnxmFQbonfm%2BN2GP72sxA2loYPooGjaOsvtah46ggRnYT%2BKs12nOI0Oytwu1Pt9V3Qxh3CGx5gVwSXz2rkExoArsuF2%2BvGEiSHMtu7B3m2cLVyD1yab6nAYIBs6l6jN7YOsrJSDe2CUTM8ELWH1zsC8gaItz7ygrCMk7QTY6gHgjq312H85EGW7aDnplvjsP3PDo3dXK4K6gHazS2K%2B%2BqkPZZMHFx02yFWrZFfu%2FZkK6zzoXFbeCy1ZPGfaPmm155gWTkzb1UFf9O7qm5WOeo%2B1e952%2FX%2F2xzTdmODa6UPMVhIk6YciG4xI9dpAh80tTsAJ8hix%2BDS8%2B4BU1R5sY9p4QGhSaK495flu9IWGhZBDKNCHqvwuW58wUj1TDn4ezQBjqkAfL7362lVEThfu4GKUliRdLJnUsCm7OwQ5oTO81AAi67vDNgCbGcfDkaY3wb89G6cx8WoGropXnHNPmTPTxljcfHoK0ho5ZQdhGA6dVMDSdAjkvb21x8qywXQNWX8GXHV5zFJ3l8L3%2B0%2Fm1gSHr860oDWts%2F40I23Jk57M4QRYl8WKClpzwuPJf65zUv6A%2FpwPx7rqWLWcggHHTn0wusSCf5SkTk&X-Amz-Signature=a486b2b4f19f58a8572a4e4d6037ad3b23ea6ed1a654114e8dfb4d050e6558da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
