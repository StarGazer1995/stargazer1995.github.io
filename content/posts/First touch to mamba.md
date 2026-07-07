---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFPYL2XJ%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T122123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt%2BtHbyAKIs9pBCqPpQIQ4qUyJ7e4FjsMXBPy6I%2B6wDgIgTb%2BAK4Zm%2Bp%2BtKXTZsjvzpdEZ112lhqWOqSGHfzf%2BXqAq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDN%2F7YbdizhENJoSBRyrcA1%2FH1mDMljXQTSNFsZvERSmbRIfqp9m1EKF4UdWP5C81KENzyepuWiC4j%2FSzSsYOn1HGUQadaPVKXKxMU0UAdtbfuVaf4QV%2FKjOy0iGUk%2BzFjMx0BP7vIwrRDg5KK%2Bm7FAYNiewWISELr8yUsioXb39VygN6hi1%2FVhtiIC9MFgMUTVP9WWilm59WgwYcY0mc%2F12o51EWON%2FO7XWhlMMoJ3q3qyKdyJwgiDemZoENpNLbZoLYoGMjDT1q%2FPnFTPt%2BS%2FIbHCezN0ZvOteZecuiqHmGxIdC0Nv1hbxQc30zkgKPs34aI9eme3Q%2BcP4SkkZN6JlgvNamx3nvmgekJbm%2F7gOp14i6BDqIbZJAer6eioaWILrx%2FVM3QuGXJNi1wCsP9z0I2c6r5HAjsLTYx9eBRz86UZCIaXVhCJKb8CUk2%2B9TU77PaVszspON7skKOvcL8fiV2xz1CiB%2F923iAPmDuAY287lv2Zi50asVKqnzbBZ7zZIgOemj5jefaqYxSiBdbTHaaBVeaR7FGBLVS3KnV%2F%2Fg%2BMqw8l4WUBV0laBEawXyOC0fBnZWDyb4%2FGyElVBqQQAfDf0TqirhzaPo5K51Q3jACyneyJcrZ5A6l%2BJ%2B%2B4hbFfh5AhuyJ1LJtpmZMMy7s9IGOqUBzQY19oEu%2F920cct6WkYk6XYQFcPZhe355kU5S%2FyLOwlcVHwJMGZKj96PoT%2F5b4qvXEZbeJoTDuwSMxOgsW%2Bt3PJxmwJeTgHBG%2BVRge77psdZ00rJMAHDpwcz%2FsNrp5F%2B0BpfndGw6Po5LOPGdALtfggZogOHtarIKZkKaDefcdQfXXKXZblqUewDkEUByVWyxhjbN0BtvBWBtSP3pZ5838RrN5XH&X-Amz-Signature=2f8966ef5e86dc15039cff8dc8769da411d32487b2075a7b5ebac7e74e73044b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
