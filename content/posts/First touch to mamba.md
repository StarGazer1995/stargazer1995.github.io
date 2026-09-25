---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJTU3HD%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T091041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIHUb7VJ24fC6XcOJkaR5gFrSQSCD7EppiDNBCUQoZMOuAiEA3hjKrBKNWu7Xt8Hn597ToD2POBTYp4a0lTjAFOWDcMEqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP6nND2QhpR910CkICrcA0q7qUW%2Fugz%2BPe3W5YKElY44raxL%2BnxCHo4chRunq6ycQvOMdECqa3VPFxMgtmlGEHARd2UCvn0kd4dOUu6HEBXV3PGa68wKQc8HriZ8VrAY7Rd59r74MyoWEx0ciX%2BUE9biVjvlxcbDxXSZ7qFn97IzEYH7uUL4xa07qPHjYutkicAP2tFevmAPT558268eUv7cIRZ5mn%2BhtDOtEOoa789QklXcyB5oq5Ghs0etl5ITrwljAlfte61dbkvORk%2Bce2GBSsxuw%2F0rrI5pI06ORxmBBtk9JmiNxc7nOQbVYzm51E1ODT3tfoj%2Be9zbR9sUPBV5v00hz1b54F52QuN0ALzJyvagKw49rKz0e1dc1zPsyVF64iP97Mf7%2BkcOQW5lpArMVSfK4wiiLt02JCrd00wLYkWrkP46bXZRUUFAqlWarV0ZM9l8by6xp7b3M7e3tlPL%2ByzB8BW6M54Lrm3G0D5joOCSL6a%2FKxsPU%2Bx7DoKn3d5DxwSdEVTepW9D9qk35hvJcqc8l%2FxbyBJB92sWjukhtCCDJJ%2BFYbhfBvTaDnlmmtvNDz35fpuSc1J9NBJGW3miLB3amPK7CI%2FoMakpMDw4vTbcrF4b7drbCwoT%2BPblyGk%2FF0KOG2aCDUUFMPvv2NUGOqUBAFFHJfs%2FqsQemgziIZp3mqFDh7QGeDQKc5SqgF9lW7lie9WOOCQ2DpBw6JSOLM6%2BDWeO65Opr2Wn2Z51Rj0nLcq5uGaEhq3VEopd28pOhlqS3OrEEYWsFWok5zGlJ%2BxKmxmSu5B4XdqDzFLo6fAakc4h1nhnb9WOFlCmHNDg08dz4ZLKbSpxn61vIrYCfw7AbTdJORfoqMYLLTGuhBSoAHeIL19D&X-Amz-Signature=cc958f843e2e36ab7ec222e1ef5d7facda0fa83261f2cc1be08c649881ff952c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
