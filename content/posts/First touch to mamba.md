---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUATDIG6%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T020954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBxtj938whh21HnJXRwlXD2LEFGHFfiOsuWjXvOINibQAiB52V1PdF4jTADJnXaHu6puAQm7q1LclHNjJNbzUVsaoCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCn9IfF542%2B5SGTEeKtwDXHZbdiNe8lAsy28daBPjOhrG3VnSFSLmQBaT7wY4RvIt0uV2PfNDyT%2F5TUYqAY%2BuyCb5xzNPyLA77h%2FSjIDfsLlHMJIODrCTf47SPtfbTg0tQBwZ5K7o9BTK4KJW22q2TgxyjxCGsLeXBTjQvtfRslh%2BM%2BZVGQoMK8ulC5oDMfGPNGTN3rAF4G4FqnGvCYcbsvBGyHwhVFPVjlVnu0G1G4aLBXeeUfZ1pdbRiacGHndUJxTMDOXzucAeXImrZb1hMaruL4SSfKSWn5Jhg4S181j4m4kV50FVi30hw0zpLfUtG1ayDrm5z6w4FALdjO3Pjx9UkaS68PjA0eOcxu7yxYgp6NzWCgVHrRzBD5ahb6zcf1jUbj4L5Nh%2BjoUZ0pKULREdqarDfHXAKT9aDlBP62M0FE3UDLMXzdm7FAAKm3GN3CAbeJwpf%2Bxp0U2V0rHEoe315KIzBB8Le1KI3ieaQ1KSAOfHJgkdyUOIG%2BNpt%2FzJpwddSzAqlxNBMer7G2QpLfxnyk4jzkFr%2FR1mZ13eB9JfYtE8arN3YrSzrMlqlxJQOUrGcuMzH2ua90F4A9dPg2m5FBSCJDFljN2mK%2B9SxTbwwtY5VbOAjS%2BzvKbb2iepDSJr2X%2ByP8Od4xswr5GH0gY6pgH6IC3sqIazdOGFZqHtzzO3EukDNeKrST1l7%2FtfFUV8Iv9Xmi8fkynsrRIZBQTNAdJAb0b3IxXrPO3im%2FvfcRc49DC9AtFKS0OBJfEdc3H3DM%2FCeX8m2Q8aaieu0txb18Yng9JTZHyLLtQkDH8WM39lncOHgs6Jtti3Wh0ySmstzDxE3wYFu9TaRBhNW4nv8b7TR2JPYJX984ohgD8TsDRv9mcjLhV%2F&X-Amz-Signature=a8cd775d4bf84dc766c5c11199c9c38beab1403e7d6e5a39ce420771b04008b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
