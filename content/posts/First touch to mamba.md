---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFDLRLU6%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T092413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAhuzGN0su48%2B96kLizzMDM7vyNh0ShMm7ZFCnvme%2Bq4AiEAmSwap8MET2UMSnWp0RsHq0jTE%2F9lbqIFnSz0ojgdN2Eq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOXizLyZAMG283bDYSrcA63thaztIywysBimIACqHwJP9NvxnrpYnxFaB958lyZX4iHf7iBG%2FQq1RuiVJfaDDd4iqQIkIJsu%2BLsUgYjDYU5o3OT0mk5tRGMhcWUEjjqrRIvVKtLTkOVwi1dJfRDXicljMaOOXwfCSrKVaRY00Kloc25yAwuqO9SQj9Jyd%2Fau%2BUP%2BP4%2BTU86oQxAMYP9Dm9UhxmNtiWraixiLZDes37pKTN1vcQ9IoaH3uzGktkeQTW2lj1QIknE3uSTUbPrkSj%2F3cFXY1ppEifmLdf28qU8kfooDHG6UQocV5zIVACk1T4JssOym26B%2FGvXWHIsZzovV4IlxS9o0IM0%2ByA6TVER9yYF7N6nvmOwngLaTX3Ev7vr%2FDjo0X9B8asTaiMGVGwTCaai%2BNaPt8TE99uyLBqV%2FEgbM2eeRMbS1awOABZpNenpCRWfzZujD6YerJOO6BDELz1nA5K2xGJfZvBHP7uqelp0QOA1WSd6LlgED2RMJjFL7XBnki482JQOV84p6G3yCC8kAgbhOetUokhaOYlSCKaWo5Bn0TGlHq9pDn3pZlvSpCPoXpsNRT0M0Cp%2FiprcvFaQg4fHAMklxicB8YIbHh7i39LG2s%2FlDmQ9CYSLZngvXqUZEIHPoMoOZML%2BznNMGOqUBrn6jDyn7G1eEVt7GqqzWBIK6HuQMmUecJy2PLMINCaqGQd33GbS967sc%2Brx8CgOlTPBm4mNx5gmE6OW4ArT0QrhQyQTx3cNeWEx4I3%2FVTszFv0Lv%2BXT%2FB8N92trVDL2tkF6Vmbr1XuD6DDF0YlG0%2ByLcHcz%2BJXJHRChY%2FOMgDCM2Nlz7og9oPFHAhKUkCnnvoimRnK3UBy2kOdl0HrtlT46%2FZzAg&X-Amz-Signature=29015c790a550ed7e60b58865ff9554bfd72ce59371a7fca4a668ae194cd3893&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
